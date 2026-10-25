"""Generate a Daybreak (light) layer for a stylesheet set written for the night sky.

For every rule whose declarations use a night colour in a text or surface role, emit the same
selector under html[data-theme="light"] with that colour mapped to its Daybreak partner.
Rules over photographs (lightbox, captions on images, the polaroid wall) are left alone: they
sit on their own dark ground in either light.

usage: python3 daybreak.py out.css in1.css [in2.css ...]
"""
import re, sys

SKIP_SELECTOR = re.compile(r"\.conv-lb|figcaption|\.hero-gallery|::?selection")
TEXT_PROPS = {"color", "-webkit-text-fill-color", "caret-color", "fill", "stroke"}
SURFACE_PROPS = {"background", "background-color", "border", "border-color", "border-top", "border-bottom",
                 "border-left", "border-right", "border-block", "border-inline", "outline", "border-top-color",
                 "border-bottom-color"}

def rgba(m):
    return [float(x) for x in m.group(1).split(",")]

def map_text(v):
    # A kit variable with a night fallback (var(--gold, #e8b45a)): the kit's own Daybreak value can be too
    # pale for text here, so the mapped fallback replaces the whole expression.
    v = re.sub(r"var\(--[a-z-]+,\s*(#[0-9a-fA-F]{3,8}|rgba?\([^)]*\))\s*\)",
               lambda m: m.group(1) if map_text_plain(m.group(1)) != m.group(1) else m.group(0), v)
    return map_text_plain(v)

def map_text_plain(v):
    v2 = v
    v2 = re.sub(r"#f3eee4\b", "#1c1530", v2, flags=re.I)
    v2 = re.sub(r"rgba\(\s*243\s*,\s*238\s*,\s*228\s*,\s*([0-9.]+)\s*\)",
                lambda m: f"rgba(28, 21, 48, {min(1, float(m.group(1)) + 0.12):.2f})", v2)
    v2 = re.sub(r"#e8b45a\b", "#85560c", v2, flags=re.I)
    v2 = re.sub(r"#a78bfa\b", "#5b33b8", v2, flags=re.I)
    v2 = re.sub(r"#ff6e3c\b", "#b23c0f", v2, flags=re.I)
    v2 = v2.replace("var(--cv-gold)", "#85560c").replace("var(--cv-violet)", "#5b33b8")
    v2 = v2.replace("var(--gal-gold)", "#85560c").replace("var(--gal-violet)", "#5b33b8")
    return v2

def map_surface(v):
    if "gradient" in v:
        return v  # decorative washes and gradient buttons (dark text on them) read in both lights
    v2 = re.sub(r"rgba\(\s*255\s*,\s*255\s*,\s*255\s*,\s*([0-9.]+)\s*\)",
                lambda m: f"rgba(40, 20, 80, {float(m.group(1)):.2f})", v)
    v2 = re.sub(r"rgba\(\s*(6\s*,\s*5\s*,\s*14|11\s*,\s*9\s*,\s*24)\s*,\s*([0-9.]+)\s*\)",
                lambda m: f"rgba(247, 244, 253, {max(0.85, float(m.group(2))):.2f})", v2)
    v2 = re.sub(r"#f3eee4\b", "#1c1530", v2, flags=re.I)
    return v2

def rules(css):
    """Yield (prelude_stack, selector, body) for every style rule, descending into @media/@supports."""
    css = re.sub(r"/\*.*?\*/", "", css, flags=re.S)
    i, n = 0, len(css)
    def parse(i, stack):
        start = i
        while i < n:
            c = css[i]
            if c == "{":
                prelude = css[start:i].strip()
                depth, j = 1, i + 1
                while j < n and depth:
                    depth += {"{": 1, "}": -1}.get(css[j], 0)
                    j += 1
                body = css[i + 1:j - 1]
                if prelude.startswith("@media") or prelude.startswith("@supports"):
                    yield from parse_block(body, stack + [prelude])
                elif not prelude.startswith("@"):
                    yield stack, prelude, body
                i = j
                start = i
            elif c == "}":
                return
            else:
                i += 1
    def parse_block(text, stack):
        nonlocal css, n
        saved_css, saved_n = css, n
        css, n = text, len(text)
        yield from parse(0, stack)
        css, n = saved_css, saved_n
    yield from parse(0, [])

out_lines = ["/* Daybreak: the light layer, generated from the night stylesheets. Loads last.",
             "   Regenerate with daybreak.py after changing colours in the night styles. */", ""]
for path in sys.argv[2:]:
    css = open(path).read()
    for stack, selector, body in rules(css):
        if SKIP_SELECTOR.search(selector):
            continue
        decls = []
        for d in body.split(";"):
            if ":" not in d:
                continue
            prop, val = d.split(":", 1)
            prop, val = prop.strip().lower(), val.strip()
            if prop.startswith("--"):
                continue
            if prop in TEXT_PROPS:
                new = map_text(val)
            elif prop in SURFACE_PROPS:
                new = map_surface(val)
            else:
                continue
            if new != val:
                decls.append(f"{prop}: {new}")
        if not decls:
            continue
        sels = ", ".join(f'html[data-theme="light"] {s.strip()}' for s in selector.split(","))
        rule = f"{sels} {{ {'; '.join(decls)}; }}"
        for p in reversed(stack):
            rule = f"{p} {{ {rule} }}"
        out_lines.append(rule)
open(sys.argv[1], "w").write("\n".join(out_lines) + "\n")
print(len(out_lines) - 3, "rules")
