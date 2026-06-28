# child(parent)
class Plant:
    def __init__(self, name: str = "", height: float = 0,
                 age_days: int = 0) -> None:
        self._name = name

        self._age_days = 0
        self._height = 0.0
        self.set_age(age_days)
        self.set_height(height)

    def set_height(self, new_height: float) -> None:
        if new_height >= 0:
            self._height = new_height
        else:
            print(f"{self._name}: Error, height can't be negative")
            print("Height update rejected")

    def get_height(self) -> float:
        return self._height

    def set_age(self, new_age: int) -> None:
        if new_age >= 0:
            self._age_days = new_age
        else:
            print(f"{self._name}: Error, age can't be negative")
            print("Age update rejected")

    def get_age(self) -> int:
        return self._age_days

    def grow(self) -> None:
        self._height += 0.8

    def age(self) -> None:
        self._age_days += 1

    def show(self) -> None:
        print(f"{self._name}: {self._height:.1f}cm, {self._age_days} days old")


class Flower(Plant):
    def __init__(self, name: str = "", height: float = 0,
                 age_days: int = 0, color: str = "") -> None:
        super().__init__(name, height, age_days)
        self._color: str = color
        self._has_bloomed: bool = False

    def bloom(self) -> None:
        self._has_bloomed = True

    def show(self) -> None:
        super().show()
        print(f"Color: {self._color}")
        if self._has_bloomed:
            print(f"{self._name} is blooming beautifully!")
        else:
            print(f"{self._name} has not bloomed yet")


class Tree(Plant):
    def __init__(self, name: str = "", height: float = 0,
                 age_days: int = 0, trunk_diameter: float = 0) -> None:
        super().__init__(name, height, age_days)
        self._trunk_diameter = trunk_diameter

    def show(self) -> None:
        super().show()
        print(f"Trunk diameter: {self._trunk_diameter:.1f}cm")

    def produce_shade(self) -> None:
        print(f"Tree {self._name} now produces a shade of ", end="")
        print(f"{self._height:.1f}cm long and ", end="")
        print(f"{self._trunk_diameter:.1f}cm wide.")


class Vegetable(Plant):
    def __init__(self, name: str = "", height: float = 0,
                 age_days: int = 0, harvest_season: str = "") -> None:
        super().__init__(name, height, age_days)
        self._harvest_season = harvest_season
        self._nutritional_value: float = 0

    def show(self) -> None:
        super().show()
        print(f"Harvest season: {self._harvest_season}")
        print(f"Nutritional value: {round(self._nutritional_value)}")

    def age(self) -> None:
        super().age()
        self._nutritional_value += 0.5

    def grow(self) -> None:
        self._height += 2.1
        self._nutritional_value += 0.5


if __name__ == "__main__":
    print("=== Garden Plant Types ===")
    print("=== Flower")
    rose = Flower("Rose", 15, 10, "red")
    rose.show()
    print("[asking the rose to bloom]")
    rose.bloom()
    rose.show()
    print()

    print("=== Tree")
    tree = Tree("Oak", 200, 365, 5)
    tree.show()
    print("[asking the oak to produce shade]")
    tree.produce_shade()
    print()

    print("=== Vegetable")
    tomato = Vegetable("Tomato", 5, 10, "April")
    tomato.show()
    print("[make tomato grow and age for 20 days]")
    for _ in range(20):
        tomato.age()
        tomato.grow()
    tomato.show()
