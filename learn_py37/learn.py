""" dataclass """
from dataclasses import dataclass, field


@dataclass(order=True)
class Country:
    name: str
    population: int
    area: float = field(repr=False, compare=False)
    coastline: float = 0

    def beach_per_person(self):
        """Meters of coastline per person"""
        return (self.coastline * 1000) / self.population


if __name__ == '__main__':
    norway1 = Country("Norway", 5320045, 323802, 58133)
    norway2 = Country("Norway", 5320045, 0, 58133)
    usa = Country("United States", 326625791, 9833517, 19924)
    nepal = Country("Nepal", 29384297, 147181)
    print(norway1 == norway2)  # compare between each attribute
