import json
import logging
from pathlib import Path

try:
    import requests  # type: ignore[import-not-found]
except ModuleNotFoundError:
    requests = None  # type: ignore[assignment]


ROOT = Path(__file__).resolve().parent.parent
DATA_DIR = ROOT / "data"
LOG_DIR = ROOT / "logs"

DATA_DIR.mkdir(parents=True, exist_ok=True)
LOG_DIR.mkdir(parents=True, exist_ok=True)

logging.basicConfig(
    filename=LOG_DIR / "lab4.log",
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(message)s",
)


def main():
    try:
        response = requests.get(
            "https://icanhazdadjoke.com/",
            headers={"Accept": "application/json"},
            timeout=10,
        )

        if response.status_code != 200:
            logging.error("[LAB4_ERR] HTTP status %s", response.status_code)
            return 1

        logging.info("[LAB4_JOKE_HTTP_OK]")

        payload = response.json()
        if not isinstance(payload, dict):
            logging.error("[LAB4_ERR] Expected a JSON object")
            return 1

        joke = payload.get("joke")
        if not isinstance(joke, str) or not joke.strip():
            logging.error("[LAB4_ERR] Missing or empty joke field")
            return 1

        logging.info("[LAB4_JOKE_JSON_OK]")

        joke_line = " ".join(joke.splitlines()).strip()

        (DATA_DIR / "joke.json").write_text(
            json.dumps(payload, indent=2) + "\n",
            encoding="utf-8",
        )
        (DATA_DIR / "joke.txt").write_text(
            joke_line + "\n",
            encoding="utf-8",
        )

        print(joke_line)
        logging.info("[LAB4_JOKE_PRINTED]")
        return 0

    except (requests.RequestException, ValueError,OSError) as error:
        logging.error("[LAB4_ERR] %s", error)
        return 1

if __name__ == "__main__":
    raise SystemExit(main())
