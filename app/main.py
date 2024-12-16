class Animal:
    alive = []

    def __init__(
            self,
            name: str,
            health: int = 100,
            hidden: bool = False
    ) -> None:
        self.name = name
        self.health = health
        self.hidden = hidden
        Animal.alive.append(self)

    def __del__(self) -> None:
        if self.hidden and self in Animal.alive:
            Animal.alive.remove(self)

    def hide(self) -> None:
        self.hidden = not self.hidden

    def __str__(self) -> None:
        return f"{{Name: {self.name}, Health: {self.health}, Hidden: {self.hidden}}}"

    def __repr__(self) -> None:
        return str(self)


class Herbivore(Animal):

    def hide(self) -> None:
        super().hide()


class Carnivore(Animal):

    def bite(self, herbivore: Herbivore) -> None:
        if isinstance(herbivore, Herbivore) and not herbivore.hidden:
            herbivore.health -= 50
            if herbivore.health <= 0:
                herbivore.hidden = True
                if herbivore in Animal.alive:
                    Animal.alive.remove(herbivore)
