from dataclasses import dataclass
from functools import wraps
from pathlib import Path

import requests
from bs4 import BeautifulSoup


@dataclass(kw_only=True, frozen=True)
class AOCData:
    year: int
    day: int
    part: int


class AOC:
    _base_url = "https://adventofcode.com"

    _instance: AOCData = None

    def _build(self, aoc_data: AOCData):
        self._instance = aoc_data

    @staticmethod
    def _get_session_cookie() -> str:
        session_cookie_file = Path(__file__).parent / ".." / ".." / ".session-cookie"

        if not session_cookie_file.exists():
            raise Exception("session cookie file does not exist")

        with open(session_cookie_file) as f:
            session_cookie = f.read()

        return session_cookie.strip()

    @classmethod
    def puzzle(cls, year, day, part):

        def decorator(func):
            @wraps(func)
            def wrapper(*args, **kwargs):
                cls._build(cls, AOCData(year=year, day=day, part=part))
                return func(*args, **kwargs)

            return wrapper

        return decorator

    @classmethod
    def get_data(cls):
        year = cls._instance.year
        day = cls._instance.day

        target_filepath = Path(f"../{year}/{year}_d{day:02d}.txt")

        if not target_filepath.is_file():
            response = requests.get(
                f"{cls._base_url}/{year}/day/{day}/input",
                headers={"Cookie": f"session={cls._get_session_cookie()}"},
            )

            if response.status_code >= 400:
                raise Exception("Cannot download input")

            with open(target_filepath, mode="wb") as f:
                f.write(response.content)

        with open(target_filepath, mode="r") as f:
            data = f.read()

        return data

    @classmethod
    def submit_answer(cls, answer):
        year = cls._instance.year
        day = cls._instance.day
        part = cls._instance.part

        response = requests.post(
            f"{cls._base_url}/{year}/day/{day}/answer",
            headers={"Cookie": f"session={cls._get_session_cookie()}"},
            data={"level": part, "answer": answer},
        )

        if response.status_code >= 400:
            raise Exception("Cannot submit answer")

        soup = BeautifulSoup(response.content, "html.parser")
        text = soup.body.article.p.text
        print(text)

        is_correct_answer = "that's the right answer" in text.lower()
        return is_correct_answer
