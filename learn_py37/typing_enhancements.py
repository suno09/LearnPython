from __future__ import annotations


class Tree:
    # with __future__ can declere type Tree inside class Tree
    def __init__(self, left: Tree, right: Tree) -> None:
        self.left = left
        self.right = right


def greet(name: print("Now!")):
    print(f"Hello {name}")


print('greet.__annotations__["name"] => ', greet.__annotations__["name"])
print('eval(greet.__annotations__["name"]) => ', eval(greet.__annotations__["name"]))
print('greet.__annotations__ => ', greet.__annotations__)
# print(greet.__annotations__)

import typing

print(typing.get_type_hints(greet))
