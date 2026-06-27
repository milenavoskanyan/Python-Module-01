class Plant:
    def __init__(self, name: str = "", height: float = 0,
                 age_days: int = 0) -> None:
        self.age_days = age_days
        self.height = height
        self.name = name

    def grow(self) -> None:
        self.height += 0.8

    def age(self) -> None:
        self.age_days += 1

    def show(self) -> None:
        print(f"{self.name}: {self.height:.1f}cm, {self.age_days} days old")


if __name__ == "__main__":
    print("=== Plant Factory Output ===")

    print("Created: ", end="")
    Plant("Rose", 25.0, 30).show()

    print("Created: ", end="")
    Plant("Oak", 200.0, 365).show()

    print("Created: ", end="")
    Plant("Cactus", 5.0, 90).show()

    print("Created: ", end="")
    Plant("Sunflower", 80.0, 45).show()

    print("Created: ", end="")
    Plant("Fern", 15.0, 120).show()
