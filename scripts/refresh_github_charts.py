"""Refresh repository-hosted GitHub cards, preserving the last valid copy."""

from concurrent.futures import ThreadPoolExecutor
import json
from pathlib import Path
import re
from urllib.request import Request, urlopen
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]
LIMIT = 2 * 1024 * 1024
SVG = "{http://www.w3.org/2000/svg}"
ERROR = re.compile(
    r"something went wrong|could not fetch|failed to fetch|rate limit|"
    r"maximum retries|service unavailable|user not found|invalid token|"
    r"bad credentials|no stats found|deployment_not_found",
    re.IGNORECASE,
)


def download_chart(url):
    request = Request(url, headers={"User-Agent": "ankush-48-profile-charts/1.0"})
    with urlopen(request, timeout=30) as response:
        if response.headers.get_content_type() != "image/svg+xml":
            raise ValueError("provider did not return an SVG image")
        data = response.read(LIMIT + 1)
    if len(data) > LIMIT or b"<!doctype" in data.lower():
        raise ValueError("unexpected SVG size or document type")
    root = ET.fromstring(data)
    if root.tag != SVG + "svg":
        raise ValueError("unexpected document type")
    text = " ".join("".join(node.itertext()).strip() for node in root.iter()
                    if node.tag in {SVG + "text", SVG + "title", SVG + "desc"})
    if ERROR.search(text):
        raise ValueError("provider returned an error card")
    if any(node.tag in {SVG + "script", SVG + "foreignObject"} for node in root.iter()):
        raise ValueError("unexpected active SVG content")
    return data


def refresh(entry):
    name, url = entry
    path = ROOT / "assets/github" / name
    try:
        data = download_chart(url)
    except (OSError, ValueError, ET.ParseError) as exc:
        print(f"::warning title={name}::Kept previous card ({exc})")
        return False
    if not path.exists() or data != path.read_bytes():
        temp = path.with_suffix(".tmp")
        temp.write_bytes(data)
        temp.replace(path)
    print(f"Refreshed {name}")
    return True


if __name__ == "__main__":
    manifest = json.loads(Path(__file__).with_name("github-charts.json").read_text())
    with ThreadPoolExecutor(max_workers=4) as executor:
        results = list(executor.map(refresh, manifest.items()))
    print(f"{sum(results)} of {len(results)} chart providers returned valid images.")
