"""Build an animated contribution snake from the cached GitHub heatmap."""

from pathlib import Path
import xml.etree.ElementTree as ET

CHARTS = Path(__file__).resolve().parents[1] / "assets/github"
STEP = 22
LEFT = 45
TOP = 78
DURATION = 32


def render(heatmap):
    days = [
        ((int(node.attrib["x"]) - 45) // STEP, (int(node.attrib["y"]) - 175) // STEP, node.attrib["fill"])
        for node in ET.fromstring(heatmap).findall(".//{*}rect")
        if node.find("{*}title") is not None
    ]
    if len(days) != 365:
        raise ValueError("Expected 365 contribution days in the cached heatmap")
    columns = max(column for column, _, _ in days) + 1
    right = LEFT + (columns - 1) * STEP
    route = f"M{LEFT} {TOP}"
    for row in range(7):
        route += f" H{right if row % 2 == 0 else LEFT}"
        if row < 6:
            route += f" V{TOP + (row + 1) * STEP}"
    route_steps = 7 * (columns - 1) + 6
    tiles = []
    food = []
    for column, row, color in days:
        x, y = LEFT + column * STEP, TOP + row * STEP
        tiles.append(f'<rect x="{x-9}" y="{y-9}" width="18" height="18" rx="4" fill="#21192d"/>')
        if color == "#171717":
            continue
        position = row * columns + (column if row % 2 == 0 else columns - 1 - column)
        hit = min(.994, max(.001, position / route_steps))
        food.append(f'<circle cx="{x}" cy="{y}" r="5" fill="{color}"><animate attributeName="opacity" values="1;1;0;0" keyTimes="0;{hit:.4f};{hit+.003:.4f};1" dur="{DURATION}s" repeatCount="indefinite"/></circle>')

    snake = []
    for index in range(5, 0, -1):
        snake.append(f'<circle r="{5 + (5-index)*.65}" fill="#59e7c5" opacity="{1-index*.1}"><animateMotion path="{route}" begin="{index*.07:.2f}s" dur="{DURATION}s" repeatCount="indefinite"/></circle>')
    snake.append(f'''<g>
<path fill="#bd9cff" d="M0 0L7 -5A8.6 8.6 0 1 0 7 5Z">
<animate attributeName="d" values="M0 0L7 -5A8.6 8.6 0 1 0 7 5Z;M0 0L8.5 -.5A8.6 8.6 0 1 0 8.5 .5Z;M0 0L7 -5A8.6 8.6 0 1 0 7 5Z" dur=".32s" repeatCount="indefinite"/>
</path>
<circle cx="1" cy="-5" r="1" fill="#090b10"/>
<animateMotion path="{route}" rotate="auto" dur="{DURATION}s" repeatCount="indefinite"/>
</g>''')
    width = right + LEFT
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="250" viewBox="0 0 {width} 250" role="img">
<title>Ankush Yadav's animated GitHub contribution snake</title>
<desc>A Pac-Man-style snake travels across the last year of GitHub activity and eats the colored contribution dots.</desc>
<rect x="1" y="1" width="{width-2}" height="248" rx="18" fill="#090b10" stroke="#322840"/>
<text x="36" y="42" fill="#f6f2ff" font-family="system-ui, sans-serif" font-size="26" font-weight="700">GitHub contribution snake</text>
{''.join(tiles)}
{''.join(food)}
{''.join(snake)}
</svg>
'''


if __name__ == "__main__":
    asset = CHARTS / "contribution-snake.svg"
    data = render((CHARTS / "contribution-heatmap.svg").read_text(encoding="utf-8"))
    ET.fromstring(data)
    temp = asset.with_suffix(".tmp")
    temp.write_text(data, encoding="utf-8")
    temp.replace(asset)
