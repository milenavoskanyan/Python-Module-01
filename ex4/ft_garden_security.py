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


if __name__ == "__main__":
    print("=== Garden Security System ===")
    rose = Plant("Rose", 15.0, 10)
    print("Plant created: ", end="")
    rose.show()

    rose.set_height(25.0)
    print("Height updated: 25cm")

    rose.set_age(30)
    print("Age updated: 30 days")

    rose.set_height(-5.0)
    rose.set_age(-10)

    print("Current state: ", end="")
    rose.show()
