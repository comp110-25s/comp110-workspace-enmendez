"""File to define River class."""

__author__ = "730751590"

from exercises.EX04.fish import Fish
from exercises.EX04.bear import Bear


class River:
    """A river where bears and fish live."""

    day: int
    bears: list[Bear]
    fish: list[Fish]

    def __init__(self, num_fish: int, num_bears: int):
        """New River with num_fish Fish and num_bears Bears."""
        self.day: int = 0
        self.fish: list[Fish] = []
        self.bears: list[Bear] = []
        # populate the river with fish and bears
        for _ in range(0, num_fish):
            self.fish.append(Fish())
        for _ in range(0, num_bears):
            self.bears.append(Bear())

    def check_ages(self):
        """A bear is removed after a specific age from the river."""
        surviving_fish: list[Fish] = []
        surviving_bears: list[Bear] = []
        for fish in self.fish:
            if fish.age <= 3:
                surviving_fish.append(fish)
            self.fish = surviving_fish
        for bear in self.bears:
            if bear.age <= 5:
                surviving_bears.append(bear)
            self.bears = surviving_bears

    def bears_eating(self):
        """Determines amount of fish for the bear to eat."""
        for bear in self.bears:
            if len(self.fish) >= 5:
                self.remove_fish(3)
                bear.eat(3)

    def check_hunger(self):
        """If the hunger_score = 0, a bear is removed from the population."""
        surviving_bears: list[Bear] = []
        for bear in self.bears:
            if bear.hunger_score >= 0:
                surviving_bears.append(bear)
            self.bears = surviving_bears

    def repopulate_fish(self):
        """Each pair should produce 4 offspring."""
        num_fish = len(self.fish)
        num_new_fish = (num_fish // 2) * 4
        for _ in range(num_new_fish):
            self.fish.append(Fish())

    def repopulate_bears(self):
        """Each pair should produce 1 offspring."""
        num_bears = len(self.bears)
        num_new_bears = num_bears // 2
        for _ in range(num_new_bears):
            self.bears.append(Bear())

    def view_river(self) -> None:
        """Prints the total fish and bear population based on day."""
        print(f"~~~ Day {self.day}: ~~~")
        print(f"Fish population: {len(self.fish)}")
        print(f"Bear population: {len(self.bears)}")

    def one_river_day(self):
        """Simulate one day of life in the river."""
        # Increase day by 1
        self.day += 1
        # Simulate one day for all Bears
        for bear in self.bears:
            bear.one_day()
        # Simulate one day for all Fish
        for fish in self.fish:
            fish.one_day()
        # Simulate Bear's eating
        self.bears_eating()
        # Remove hungry Bear's from River
        self.check_hunger()
        # Remove old Fish and Bear's from River
        self.check_ages()
        # Simulate Fish repopulation
        self.repopulate_fish()
        # Simulate Bear repopulation
        self.repopulate_bears()
        # Visualize River
        self.view_river()

    def one_river_week(self) -> None:
        """Calls the method 7 times."""
        for _ in range(7):
            self.one_river_day()

    def remove_fish(self, amount: int) -> None:
        """Removes the first fish in the list [frontmost fish]."""
        # Iterates through 'amount' of times
        for _ in range(amount):
            # Checks the length of the list and loops through each item
            if len(self.fish) > 0:
                # Removes the first item in the list "fish at the front"
                self.fish.pop(0)
