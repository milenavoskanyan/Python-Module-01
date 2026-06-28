# child(parent)
class Plant:
    class Stats:
        def __init__(self) -> None:
            self._grow_calls: int = 0
            self._age_calls: int = 0
            self._show_calls: int = 0

        def display(self) -> None:
            print(f"Stats: {self._grow_calls} grow, ", end="")
            print(f"{self._age_calls} age, {self._show_calls} show")

    def display_stats(self) -> None:
        print(f"[statistics for {self._name}]")
        self._stats.display()

    def __init__(self, name: str = "", height: float = 0,
                 age_days: int = 0) -> None:
        self._name = name
        self._age_days = 0
        self._height = 0.0
        self.set_age(age_days)
        self.set_height(height)
        self._stats: Plant.Stats = Plant.Stats()
        # self.Inner() = Outer.Inner() inside
        # Outer_instance.Inner() = Outer.Inner() outside

    @classmethod
    def create_anonymous(cls) -> "Plant":  # forward ref, cls non-exist
        return cls("Unknown")

    @staticmethod
    def is_older_than_year(age: int) -> bool:
        return age > 365

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
        self._stats._grow_calls += 1

    def age(self) -> None:
        self._age_days += 1
        self._stats._age_calls += 1

    def get_name(self) -> str:
        return self._name

    def show(self) -> None:
        print(f"{self._name}: {self._height:.1f}cm, {self._age_days} days old")
        self._stats._show_calls += 1


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


class Seed(Flower):
    def __init__(self, name: str = "", height: float = 0,
                 age_days: int = 0, color: str = "") -> None:
        super().__init__(name, height, age_days, color)
        self._seed_count: int = 0

    def show(self) -> None:
        super().show()
        print(f"Seeds: {self._seed_count}")

    def bloom(self) -> None:
        super().bloom()
        self._seed_count = 42


class Tree(Plant):
    def __init__(self, name: str = "", height: float = 0,
                 age_days: int = 0, trunk_diameter: float = 0) -> None:
        super().__init__(name, height, age_days)
        self._trunk_diameter = trunk_diameter
        self._shade_calls: int = 0

    def show(self) -> None:
        super().show()
        print(f"Trunk diameter: {self._trunk_diameter:.1f}cm")

    def produce_shade(self) -> None:
        print(f"Tree {self._name} now produces a shade of ", end="")
        print(f"{self._height:.1f}cm long and ", end="")
        print(f"{self._trunk_diameter:.1f}cm wide.")
        self._shade_calls += 1

    def display_stats(self) -> None:
        super().display_stats()
        print(f"{self._shade_calls} shade")


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
        super().grow()
        self._height += 1.3  # additional
        self._nutritional_value += 0.5


def display_statistics(plant: Plant) -> None:
    print(f"statistics for {plant.get_name()}")
    plant.display_stats()


if __name__ == "__main__":
    print("=== Garden statistics ===")
    print("=== Check year-old")
    print(f"Is 30 days more than a year? -> {Plant.is_older_than_year(30)}")
    print(f"Is 400 days more than a year? -> {Plant.is_older_than_year(400)}")
    print()

    # flower

    print("=== Flower")
    rose = Flower("Rose", 15, 10, "red")
    rose.show()
    rose.display_stats()
    print("[asking the rose to grow and bloom]")
    for _ in range(10):
        rose.grow()
    rose.bloom()
    rose.show()
    rose.display_stats()
    print()

    # tree

    print("=== Tree")
    tree = Tree("Oak", 200, 365, 5)
    tree.show()
    tree.display_stats()
    print("[asking the oak to produce shade]")
    tree.produce_shade()
    tree.display_stats()
    print()

    # seed

    print()
    print("=== Seed")
    seed = Seed("Sunflower", 80, 45, "yellow")
    seed.show()
    print("[make sunflower grow, age and bloom]")
    for _ in range(20):
        seed.grow()
        seed.age()
    seed.bloom()
    seed.show()
    seed.display_stats()

    # anonymous

    print()
    print("=== Anonymous")
    unknown = Plant.create_anonymous()
    unknown.show()
    unknown.display_stats()
