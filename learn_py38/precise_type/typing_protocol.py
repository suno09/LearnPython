from typing import Protocol


class Named(Protocol):
    name: str


def greet(obj: Named) -> None:
    print(f"Hi {obj.name}")
