import importlib.util
import json
import logging
import urllib.error
from pathlib import Path
from urllib.parse import urlencode
from urllib.request import Request, urlopen

if importlib.util.find_spec("requests") is not None:
    import requests  # type: ignore[import-not-found]
else:
    class _RequestsTimeout(Exception):
        pass

    class _RequestsRequestException(Exception):
        pass

    class _RequestsCompat:
        Timeout = _RequestsTimeout
        RequestException = _RequestsRequestException

        @staticmethod
        def get(url, params=None, timeout=10):
            query = urlencode(params) if params else ""
            request_url = f"{url}?{query}" if query else url

            try:
                request = Request(request_url, headers={"Accept": "application/json"})
                with urlopen(request, timeout=timeout) as response:
                    payload = response.read()
                    status_code = response.getcode()
            except urllib.error.HTTPError as error:
                payload = error.read()
                status_code = error.code
            except (urllib.error.URLError, TimeoutError) as error:
                raise _RequestsRequestException(str(error)) from error

            class Response:
                def __init__(self, body, code):
                    self._body = body
                    self.status_code = code

                def json(self):
                    if not self._body:
                        return {}
                    return json.loads(self._body.decode("utf-8"))

            return Response(payload, status_code)

    requests = _RequestsCompat()

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

BASE_URL = "https://deckofcardsapi.com/api/deck"

RANK_VALUES = {str(number): number for number in range(2, 11)}
RANK_VALUES.update({
    "J": 11, "JACK": 11,
    "Q": 12, "QUEEN": 12,
    "K": 13, "KING": 13,
    "A": 14, "ACE": 14,
})

def api_get(url, params=None):
    response = requests.get(url, params=params, timeout=10)

    if response.status_code != 200:
        raise ValueError(f"HTTP status {response.status_code}")

    payload = response.json()

    if not isinstance(payload, dict):
        raise ValueError("Expected a JSON object") 

    if payload.get("success") is not True:
        raise ValueError(f"API request failed: {payload.get('error')}")

    return payload 

def get_player_count():
    while True:
        try:
            count = int(input("Number of players (2-52): "))

            if 2 <= count <= 52:
                return count 

            logging.error("[LAB4_ERR] Player count outside 2-52")
            print("Enter a number between 2 and 52.")

        except ValueError:
            logging.error("[LAB4_ERR] Player count must be an integer")
            print("Please enterr a whole number.")

def save_rounds(rounds):
    (DATA_DIR / "high_card_rounds.json").write_text(
        json.dumps(rounds, indent=2) + "\n",
        encoding="utf-8",
    )

def main():
    rounds = []
    summary = []

    def report(message):
        print(message)
        summary.append(message)

    try:
        deck = api_get(
            f"{BASE_URL}/new/shuffle/",
            params={"deck_count": 1},
        )
        deck_id = deck.get("deck_id")

        if not isinstance(deck_id, str) or not deck_id:
            raise ValueError("Missing deck_id")

        remaining = deck.get("remaining")
        if type(remaining) is not int or remaining < 0:
            raise ValueError("Invalid remaining card count")

        logging.info("[LAB4_DECK_CREATE_OK] deck_id=%s", deck_id)

        player_count = get_player_count()
        players = list(range(1, player_count + 1))
        round_number = 1

        while True:

            if remaining < len(players):
                shuffled = api_get(
                    f"{BASE_URL}/{deck_id}/shuffle/",
                    params={"remaining": "false"},
                )
                remaining = shuffled.get("remaining")

                if type(remaining) is not int or remaining < len(players):
                    raise ValueError("Not enough cards after reshuffling")

                report ("Deck reshuffled for the next round.")

            if round_number > 1:
                logging.info(
                    "[LAB4_TIE_ROUND] round=%s players=%s",
                    round_number,
                    players,
                )
            draw = api_get(
                f"{BASE_URL}/{deck_id}/draw/",
                params={"count": len(players)},
            )

            round_data = {
                "round": round_number,
                "players": players.copy(),
                "raw_response": draw,
            }
            rounds.append(round_data)
            save_rounds(rounds)

            cards = draw.get("cards")
            if not isinstance(cards, list) or len(cards) != len(players):
                raise ValueError("API returned an unexpected number of cards")

            remaining = draw.get("remaining")
            if type(remaining) is not int or remaining < 0:
                raise ValueError("Invalid remaining card count")

            results = []

            for player, card in zip(players, cards):
                if not isinstance(card, dict):
                    raise ValueError("Invalid card data")

                rank = str(card.get("value", "")).upper()
                suit = card.get("suit")

                if rank not in RANK_VALUES or not isinstance(suit, str):
                    raise ValueError("Invalid card rank or suit")

                results.append({
                    "player": player,
                    "card": card,
                    "value": RANK_VALUES[rank],
                })

        
            logging.info(
                "[LAB4_DRAW_OK] round=%s cards=%s",
                round_number,
                len(results),
            )

            highest = max(result["value"] for result in results)
            tied_players = [
                result["player"]
                for result in results
                if result["value"] == highest
            ]

            round_data["results"] = results
            round_data["highest_value"] = highest
            round_data["leaders"] = tied_players
            save_rounds(rounds)

            report(f"\nRound {round_number}:")
            for result in results:
                card = result["card"]
                report(
                    f"Player {result['player']}: "
                    f"{card['value']} of {card['suit']} "
                    f"(rank {result['value']})"
                )
            if len(tied_players) == 1:
                winner = tied_players[0]
                report(f"\nFinal winner: Player {winner}!")

                (DATA_DIR / "high_card_result.txt").write_text(
                    "\n".join(summary) + "\n",
                    encoding="utf-8",
                )

                logging.info("[LAB4_GAME_END] winner=Player %s", winner)
                return 0

            report(
                "Tie! Redrawing only for: "
                + ", ".join(f"Player {player}" for player in tied_players)
            )

            players = tied_players
            round_number += 1

    except requests.Timeout as error:
        logging.error("[LAB4_ERR] Request timed out: %s", error)
        print("The API timed out. Check the log and try again")

    except requests.RequestException as error:
        logging.error("[LAB4_ERR] Network error: %s", error)
        print("A network request failed. Check the log.")

    except (ValueError, OSError) as error:
        logging.error("[LAB4_ERR] %s", error)
        print("The game could not finish. Check logs/lab4.log.")

    except (EOFError, KeyboardInterrupt):
        logging.error("[LAB4_ERR] Game input cancelled")
        print("\nGame cancelled.")

    return 1

if __name__ == "__main__":
    raise SystemExit(main())
        