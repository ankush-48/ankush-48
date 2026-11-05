"""Render the profile heatmap from GitHub's public contribution calendar."""

from datetime import date
from html.parser import HTMLParser
import json
from pathlib import Path
import re
from urllib.request import Request, urlopen

DEST = Path(__file__).resolve().parents[1] / "assets/github/contribution-heatmap.svg"
COLORS = ("#171717", "#4a200f", "#843013", "#c13e13", "#ff591f")


class Calendar(HTMLParser):
    def __init__(self):
        super().__init__()
        self.cells = {}
        self.counts = {}
        self.tip = None

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if "data-date" in attrs and "data-level" in attrs and attrs.get("id"):
            self.cells[attrs["id"]] = (attrs["data-date"], int(attrs["data-level"]))
        if tag == "tool-tip" and attrs.get("for", "").startswith("contribution-day-component-"):
            self.tip = attrs["for"]

    def handle_data(self, data):
        if self.tip:
            match = re.search(r"(No|[\d,]+) contributions? on", data)
            if match:
                self.counts[self.tip] = int(match[1].replace(",", "")) if match[1] != "No" else 0

    def handle_endtag(self, tag):
        if tag == "tool-tip":
            self.tip = None


def get(url):
    request = Request(url, headers={"User-Agent": "ankush-48-profile-heatmap", "Accept-Language": "en"})
    with urlopen(request, timeout=25) as response:
        return response.read().decode("utf-8"), response.headers.get("Link", "")


def render(days, repos, stars, followers):
    days = sorted((date.fromisoformat(day), level, count) for day, level, count in days)
    if len(days) < 360 or len({day for day, _, _ in days}) != len(days):
        raise ValueError("Incomplete contribution calendar")
    last = days[-1][0]
    days = [entry for entry in days if (last - entry[0]).days < 365]
    first = days[0][0]
    offset = (first.weekday() + 1) % 7
    cells = []
    current = longest = 0
    for day, level, count in days:
        index = (day - first).days + offset
        week, weekday = divmod(index, 7)
        cells.append(f'<rect x="{45 + 22 * week}" y="{175 + 22 * weekday}" width="19" height="19" rx="4" fill="{COLORS[level]}"><title>{day} · {count} contributions</title></rect>')
        current = current + 1 if count else 0
        longest = max(longest, current)
    if not days[-1][2]:
        for _, _, count in reversed(days[:-1]):
            if not count:
                break
            current += 1
    stats = ((current, "Current streak"), (longest, "Longest streak"), (repos, "Public repos"), (stars, "Stars"), (followers, "Followers"))
    metrics = "".join(
        f'<text x="{45 + i * 237}" y="383" fill="#ff591f" font-size="34" font-weight="600">{value:,}</text>'
        f'<text x="{45 + i * 237}" y="409" fill="#9a9896" font-size="17">{label}</text>'
        for i, (value, label) in enumerate(stats)
    )
    total = sum(count for _, _, count in days)
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1265 429" width="1265" height="429" role="img">
<title>Live from GitHub · {total} contributions in the last year</title>
<rect width="1265" height="89" rx="18" fill="#0a0a0a"/>
<rect y="96" width="1265" height="333" rx="18" fill="#0a0a0a"/>
<g font-family="system-ui, sans-serif">
<text x="38" y="48" fill="#9a9896" font-family="monospace" font-size="20">(05)</text>
<text x="126" y="50" fill="#f3efe9" font-size="47" font-weight="700">Live from GitHub</text>
<g stroke="#ff591f" stroke-width="1.6">
<path d="M1206 32h30m-15-17v34m-12-29 24 24m-24 0 24-24"/>
</g>
<g fill="#ff591f"><circle cx="117" cy="20" r="2"/><circle cx="157" cy="13" r="2"/><circle cx="476" cy="61" r="2"/></g>
<text x="45" y="147" fill="#f3efe9" font-size="27" font-weight="600">{total:,} contributions in the last year</text>
{''.join(cells)}
{metrics}
</g>
</svg>
'''


def refresh():
    parser = Calendar()
    parser.feed(get("https://github.com/users/ankush-48/contributions")[0])
    if not parser.cells.keys() <= parser.counts.keys():
        raise ValueError("GitHub contribution counts were incomplete")
    days = [(day, level, parser.counts[key]) for key, (day, level) in parser.cells.items()]
    account = json.loads(get("https://api.github.com/users/ankush-48")[0])
    repos = []
    url = "https://api.github.com/users/ankush-48/repos?type=owner&per_page=100"
    while url:
        body, links = get(url)
        repos.extend(json.loads(body))
        next_page = re.search(r'<(https://api\.github\.com/[^>]+)>; rel="next"', links)
        url = next_page[1] if next_page else None
    svg = render(days, account["public_repos"], sum(repo["stargazers_count"] for repo in repos), account["followers"])
    temp = DEST.with_suffix(".tmp")
    temp.write_text(svg, encoding="utf-8")
    temp.replace(DEST)


if __name__ == "__main__":
    try:
        refresh()
    except (OSError, ValueError, KeyError, IndexError) as exc:
        print(f"::warning title=Contribution heatmap::Kept previous heatmap ({exc})")
