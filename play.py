#!/usr/bin/env python3
"""Download the pinned upstream HTML, verify it, and optionally serve on loopback."""
import argparse
import functools
import hashlib
import http.server
from pathlib import Path
import tempfile
import urllib.request
import webbrowser

ROOT = Path(__file__).resolve().parent
GAME = ROOT / ".private" / "index.html"
URL = "https://github.com/joeymavv/26.3-JM/releases/download/v26.3-jm.1/26.3-fixed.html"
SHA256 = "1716c4673de4ab5b03ac9ac6ebe8d4db1358f6008825b84fcb4bb05c7228a610"


def digest(path):
    with path.open("rb") as source:
        return hashlib.file_digest(source, "sha256").hexdigest()


def prepare():
    if GAME.exists():
        if digest(GAME) != SHA256:
            raise RuntimeError("Existing game differs from the pinned release. Preserve it elsewhere before retrying.")
        print("Verified existing game:", GAME)
        return
    GAME.parent.mkdir(parents=True, exist_ok=True)
    temporary = None
    try:
        with tempfile.NamedTemporaryFile(dir=GAME.parent, suffix=".download", delete=False) as target:
            temporary = Path(target.name)
            print("Downloading upstream release (about 82 MB)...", flush=True)
            with urllib.request.urlopen(URL, timeout=60) as response:
                while chunk := response.read(1024 * 1024):
                    target.write(chunk)
        if digest(temporary) != SHA256:
            raise RuntimeError("SHA-256 mismatch; refusing to use the download.")
        temporary.replace(GAME)
        print("Downloaded and SHA-256 verified:", GAME)
    finally:
        if temporary is not None:
            temporary.unlink(missing_ok=True)


class Handler(http.server.SimpleHTTPRequestHandler):
    def list_directory(self, path):
        self.send_error(403, "Directory listing disabled")

    def do_GET(self):
        # Only the self-contained HTML is served, never repository files.
        if self.path.split("?", 1)[0] not in ("/", "/index.html"):
            self.send_error(404)
            return
        super().do_GET()

    def do_HEAD(self):
        if self.path.split("?", 1)[0] not in ("/", "/index.html"):
            self.send_error(404)
            return
        super().do_HEAD()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--download-only", action="store_true")
    parser.add_argument("--no-browser", action="store_true")
    args = parser.parse_args()
    prepare()
    if args.download_only:
        return
    handler = functools.partial(Handler, directory=str(GAME.parent))
    with http.server.ThreadingHTTPServer(("127.0.0.1", 8765), handler) as server:
        url = "http://127.0.0.1:8765/"
        print("Open", url, "on this computer. Press Ctrl+C to stop.", flush=True)
        if not args.no_browser:
            webbrowser.open(url)
        try:
            server.serve_forever()
        except KeyboardInterrupt:
            pass


if __name__ == "__main__":
    try:
        main()
    except (OSError, RuntimeError) as error:
        raise SystemExit(str(error))
