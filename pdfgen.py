"""Minimal pure-Python PDF generator (no external dependencies).

Supports multiple pages, Helvetica / Helvetica-Bold standard fonts,
word wrapping and automatic pagination. Content is supplied as a list
of (style, text) blocks.

Styles: 'title', 'h1', 'h2', 'h3', 'body', 'bullet', 'spacer'
"""

# Adobe Helvetica character widths (units per 1000 em) for printable ASCII.
HELV = {
    ' ': 278, '!': 278, '"': 355, '#': 556, '$': 556, '%': 889, '&': 667,
    "'": 191, '(': 333, ')': 333, '*': 389, '+': 584, ',': 278, '-': 333,
    '.': 278, '/': 278, '0': 556, '1': 556, '2': 556, '3': 556, '4': 556,
    '5': 556, '6': 556, '7': 556, '8': 556, '9': 556, ':': 278, ';': 278,
    '<': 584, '=': 584, '>': 584, '?': 556, '@': 1015, 'A': 667, 'B': 667,
    'C': 722, 'D': 722, 'E': 667, 'F': 611, 'G': 778, 'H': 722, 'I': 278,
    'J': 500, 'K': 667, 'L': 556, 'M': 833, 'N': 722, 'O': 778, 'P': 667,
    'Q': 778, 'R': 722, 'S': 667, 'T': 611, 'U': 722, 'V': 667, 'W': 944,
    'X': 667, 'Y': 667, 'Z': 611, '[': 278, '\\': 278, ']': 278, '^': 469,
    '_': 556, '`': 333, 'a': 556, 'b': 556, 'c': 500, 'd': 556, 'e': 556,
    'f': 278, 'g': 556, 'h': 556, 'i': 222, 'j': 222, 'k': 500, 'l': 222,
    'm': 833, 'n': 556, 'o': 556, 'p': 556, 'q': 556, 'r': 333, 's': 500,
    't': 278, 'u': 556, 'v': 500, 'w': 722, 'x': 500, 'y': 500, 'z': 500,
    '{': 334, '|': 260, '}': 334, '~': 584,
}

# Page geometry (A4, points).
PAGE_W = 595.0
PAGE_H = 842.0
MARGIN_L = 55.0
MARGIN_R = 55.0
MARGIN_T = 55.0
MARGIN_B = 55.0
USABLE_W = PAGE_W - MARGIN_L - MARGIN_R

# Style config: (fontsize, bold, space_before, space_after, leading)
STYLES = {
    'title':  (22, True,  0,  16, 26),
    'h1':     (15, True,  14, 6,  19),
    'h2':     (12.5, True, 10, 4,  16),
    'h3':     (11, True,  7,  3,  14),
    'body':   (10.5, False, 0, 4,  14),
    'bullet': (10.5, False, 0, 3,  14),
    'spacer': (10.5, False, 0, 0,  8),
}


def _char_w(ch, size, bold):
    w = HELV.get(ch, 556) / 1000.0 * size
    if bold:
        w *= 1.09  # buffer so bold text never overflows
    return w


def _text_w(s, size, bold):
    return sum(_char_w(c, size, bold) for c in s)


def _wrap(text, size, bold, max_w, indent=0.0):
    avail = max_w - indent
    words = text.split(' ')
    lines = []
    cur = ''
    for word in words:
        trial = word if cur == '' else cur + ' ' + word
        if _text_w(trial, size, bold) <= avail or cur == '':
            # if single word too long, hard-break it
            if cur == '' and _text_w(word, size, bold) > avail:
                piece = ''
                for ch in word:
                    if _text_w(piece + ch, size, bold) <= avail or piece == '':
                        piece += ch
                    else:
                        lines.append(piece)
                        piece = ch
                cur = piece
            else:
                cur = trial
        else:
            lines.append(cur)
            cur = word
    if cur:
        lines.append(cur)
    return lines


def _esc(s):
    return s.replace('\\', r'\\').replace('(', r'\(').replace(')', r'\)')


def build_pdf(blocks, out_path, footer_prefix='Page'):
    """blocks: list of (style, text). Writes a PDF to out_path."""
    # Layout into pages -> list of drawing ops per page.
    pages = []
    ops = []
    y = PAGE_H - MARGIN_T

    def new_page():
        nonlocal ops, y
        pages.append(ops)
        ops = []
        y = PAGE_H - MARGIN_T

    for style, text in blocks:
        size, bold, sb, sa, lead = STYLES[style]
        indent = 0.0
        prefix = ''
        if style == 'bullet':
            indent = 16.0
            prefix = '-  '
        y -= sb
        if style == 'spacer':
            y -= lead
            if y < MARGIN_B:
                new_page()
            continue
        wrapped = _wrap(prefix + text if prefix else text, size, bold,
                        USABLE_W, indent)
        first = True
        for ln in wrapped:
            if y - lead < MARGIN_B:
                new_page()
            x = MARGIN_L + (indent if (style == 'bullet' and not first) else 0)
            # For bullets, continuation lines align after the marker.
            if style == 'bullet' and not first:
                x = MARGIN_L + indent
            elif style == 'bullet' and first:
                x = MARGIN_L
            ops.append((x, y, ln, size, bold))
            y -= lead
            first = False
        y -= sa
    pages.append(ops)

    # Build PDF objects.
    objects = []

    def add_obj(s):
        objects.append(s)
        return len(objects)  # 1-based id

    # Reserve: 1=catalog, 2=pages tree, fonts, then page+content objs.
    font_reg = add_obj('<< /Type /Font /Subtype /Type1 /BaseFont /Helvetica '
                        '/Encoding /WinAnsiEncoding >>')
    font_bold = add_obj('<< /Type /Font /Subtype /Type1 /BaseFont '
                        '/Helvetica-Bold /Encoding /WinAnsiEncoding >>')

    page_obj_ids = []
    content_ids = []
    total = len(pages)
    for pnum, page_ops in enumerate(pages, start=1):
        parts = []
        for (x, y, ln, size, bold) in page_ops:
            fnt = '/F2' if bold else '/F1'
            parts.append('BT %s %.2f Tf 1 0 0 1 %.2f %.2f Tm (%s) Tj ET'
                         % (fnt, size, x, y, _esc(ln)))
        # footer
        footer = '%s %d of %d' % (footer_prefix, pnum, total)
        parts.append('BT /F1 9 Tf 1 0 0 1 %.2f %.2f Tm (%s) Tj ET'
                     % (MARGIN_L, 30.0, _esc(footer)))
        stream = '\n'.join(parts)
        cid = add_obj('<< /Length %d >>\nstream\n%s\nendstream'
                     % (len(stream), stream))
        content_ids.append(cid)
        # placeholder page obj, fixed after we know pages-tree id
        page_obj_ids.append(None)

    pages_tree_id = len(objects) + 1 + total  # will compute below properly

    # Create page objects now (need pages tree id). We'll assign ids in order.
    page_ids = []
    for i, cid in enumerate(content_ids):
        pid = add_obj('PLACEHOLDER')  # fill later
        page_ids.append(pid)

    pages_tree_id = add_obj('PLACEHOLDER')
    catalog_id = add_obj('<< /Type /Catalog /Pages %d 0 R >>' % pages_tree_id)

    # Fill page objects.
    for i, pid in enumerate(page_ids):
        objects[pid - 1] = (
            '<< /Type /Page /Parent %d 0 R /MediaBox [0 0 %.0f %.0f] '
            '/Resources << /Font << /F1 %d 0 R /F2 %d 0 R >> >> '
            '/Contents %d 0 R >>'
            % (pages_tree_id, PAGE_W, PAGE_H, font_reg, font_bold,
               content_ids[i]))
    kids = ' '.join('%d 0 R' % pid for pid in page_ids)
    objects[pages_tree_id - 1] = (
        '<< /Type /Pages /Count %d /Kids [%s] >>' % (total, kids))

    # Serialize.
    out = ['%PDF-1.4\n%\xe2\xe3\xcf\xd3\n']
    offsets = []
    pos = len(out[0].encode('latin-1'))
    body = []
    for i, obj in enumerate(objects, start=1):
        offsets.append(pos)
        chunk = '%d 0 obj\n%s\nendobj\n' % (i, obj)
        body.append(chunk)
        pos += len(chunk.encode('latin-1'))
    xref_pos = pos
    n = len(objects)
    xref = ['xref\n0 %d\n' % (n + 1), '0000000000 65535 f \n']
    for off in offsets:
        xref.append('%010d 00000 n \n' % off)
    trailer = ('trailer\n<< /Size %d /Root %d 0 R >>\nstartxref\n%d\n%%%%EOF\n'
               % (n + 1, catalog_id, xref_pos))
    with open(out_path, 'wb') as f:
        f.write(out[0].encode('latin-1'))
        for chunk in body:
            f.write(chunk.encode('latin-1'))
        f.write(''.join(xref).encode('latin-1'))
        f.write(trailer.encode('latin-1'))
    return total
