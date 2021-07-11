from typing import Literal


def double(number: float) -> float:
    return 2 * number


'''
precise two value for direction: 'horizontal' or 'vertical'
'''


def draw_line(direction: Literal['horizontal', 'vertical']) -> None:
    if direction == "horizontal":
        print("draw H")
    elif direction == "vertical":
        print("draw V")
    else:
        raise ValueError(f"invalid direction {direction!r}")


if __name__ == '__main__':
    # print(double(number=5))
    # print(double(number="i am not double\n"))
    draw_line("h")
