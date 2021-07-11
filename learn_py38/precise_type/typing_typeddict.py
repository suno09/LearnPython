from typing import TypedDict


class PythonVersion(TypedDict):
    version: str
    release_year: int


py38 = PythonVersion(version="3.8", release_year=2019)
py37 = PythonVersion(version="3.7")  # Error release_year unfilled
