from typing import Annotated, get_type_hints


def speed(distance: Annotated[float, "feet"], time: Annotated[float, "seconds"]) -> Annotated[float, "miles per hour"]:
    """Calculate speed as distance over time"""
    fps2mph = 3600 / 5280  # Feet per second to miles per hour
    return distance / time * fps2mph


print(f'speed.__annotations__ = {speed.__annotations__}')
print(f'get_type_hints(speed) = {get_type_hints(speed)}')
print(f'get_type_hints(speed, include_extras=True) = {get_type_hints(speed, include_extras=True)}')
print(f'speed.__annotations__["distance"].__metadata__ = {speed.__annotations__["distance"].__metadata__}')


class AnnotationFactory:
    def __init__(self, type_hint):
        self.type_hint = type_hint

    def __getitem__(self, key):
        if isinstance(key, tuple):
            return Annotated[(self.type_hint,) + key]
        else:
            return Annotated[self.type_hint, key]

    def __repr__(self):
        return f"{self.__class__.__name__}({self.type_hint})"


Float = AnnotationFactory(float)


def speed2(
    distance: Float["feet"], time: Float["seconds"]
) -> Float["miles per hour"]:
    """Calculate speed as distance over time"""
    fps2mph = 3600 / 5280  # Feet per second to miles per hour
    return distance / time * fps2mph


print(f'speed2.__annotations__ = {speed2.__annotations__}')
print(f'get_type_hints(speed2) = {get_type_hints(speed2)}')
print(f'get_type_hints(speed2, include_extras=True) = {get_type_hints(speed2, include_extras=True)}')
print(f'speed2.__annotations__["distance"].__metadata__ = {speed2.__annotations__["distance"].__metadata__}')
