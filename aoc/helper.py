import requests
from pathlib import Path
from bs4 import BeautifulSoup

AOC_BASE_URL = "https://adventofcode.com"


def _get_session_cookie() -> str:
    session_cookie_file = Path(__file__).parent / ".." / ".session-cookie"

    if not session_cookie_file.exists():
        raise Exception("session cookie file does not exist")

    with open(session_cookie_file) as f:
        session_cookie = f.read()

    return session_cookie


def download_input(year: int, day: int):
    target_filepath = Path(f"../{year}/{year}_d{day:02d}.txt")

    if not target_filepath.is_file():
        response = requests.get(
            f"{AOC_BASE_URL}/{year}/day/{day}/input",
            headers={"Cookie": f"session={_get_session_cookie()}"},
        )

        if response.status_code >= 400:
            raise Exception("Cannot download input")

        with open(target_filepath, mode="wb") as f:
            f.write(response.content)


def submit_answer(year: int, day: int, part: int, answer: int | str) -> bool:
    response = requests.post(
        f"{AOC_BASE_URL}/{year}/day/{day}/answer",
        headers={"Cookie": f"session={_get_session_cookie()}"},
        data={"level": part, "answer": answer},
    )

    if response.status_code >= 400:
        raise Exception("Cannot submit answer")

    soup = BeautifulSoup(response.content, "html.parser")
    text = soup.body.article.p.text
    print(text)

    is_correct_answer = "that's the right answer" in text.lower()
    return is_correct_answer
