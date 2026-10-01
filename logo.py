from pathlib import Path
import re

SOURCE = Path('/mnt/data/vectorizer-io_freesample.svg')
OUTPUT = Path('/mnt/data/urro_logo_refined.svg')

src = SOURCE.read_text(encoding='utf-8')
main_path = re.search(r'<path id="plU2C59Ua" d="([^"]+)"', src).group(1)

svg = f'''<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg"
     viewBox="0 0 12540 12540"
     width="1254" height="1254"
     role="img" aria-labelledby="title desc">
  <title id="title">Urro logo</title>
  <desc id="desc">A symmetric black glyph combining a four-lobed form, a central delta, and a macron.</desc>

  <defs>
    <!-- Preserve the stronger left-side geometry and mirror it for exact symmetry.
         The 10-unit overlap prevents a raster seam at the centerline. -->
    <clipPath id="left-half" clipPathUnits="userSpaceOnUse">
      <rect x="0" y="0" width="6280" height="12540"/>
    </clipPath>
    <g id="source-half" clip-path="url(#left-half)">
      <path d="{main_path}"/>
    </g>
  </defs>

  <g fill="#000000">
    <use href="#source-half"/>
    <use href="#source-half" transform="translate(12540 0) scale(-1 1)"/>

    <!-- Replace the traced bar with exact geometry: centered, slightly shorter,
         and thinner so the diacritic supports rather than dominates the glyph. -->
    <rect x="5130" y="2365" width="2280" height="430"/>
  </g>
</svg>
'''

OUTPUT.write_text(svg, encoding='utf-8')
print(OUTPUT)
