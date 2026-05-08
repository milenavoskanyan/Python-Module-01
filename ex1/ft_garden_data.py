
# methods: static(no self info), class method(receives cls as argument), instance(has self)

class Plant:
    name: str
    height: int
    age: int

    def show(self) -> None:
        print(f"{self.name}: {self.height}cm, {self.age} days old")

def main() -> None:
    print("=== Garden Plant Registry ===")
    rose: Plant = Plant()
    sunflower: Plant = Plant()
    cactus: Plant = Plant()
    
    rose.name = "Rose"
    rose.height = 25
    rose.age = 30
    sunflower.name = "Sunflower"
    sunflower.height = 80
    sunflower.age = 45
    cactus.name = "Cactus"
    cactus.height = 15
    cactus.age = 120

    rose.show()
    sunflower.show()
    cactus.show()

if __name__ == "__main__":
    main()