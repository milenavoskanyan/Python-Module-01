class Plant:
    def __init__(self, name: str = "", height: float = 0,
                 age: int = 0, growth: float = 0) -> None:
        self.age_days = age
        self.height = height
        self.name = name
        self.growth = growth

    def grow(self) -> None:
        self.height += 0.8
        self.growth += 0.8

    def age(self) -> None:
        self.age_days += 1

    def show(self) -> None:
        print(f"{self.name}: {self.height:.1f}cm, {self.age_days} days old")

    def show_growth(self) -> None:
        print(f"Growth this week: {self.growth}")


if __name__ == "__main__":
    rose: Plant = Plant("Rose", 25, 30)
    print("=== Garden Plant Growth ===")
    for i in range(1, 8):
        print(f"=== Day {i} ===")
        rose.show()
        rose.grow()
        rose.age()
    rose.show_growth()
