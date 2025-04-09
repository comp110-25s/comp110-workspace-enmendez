"""File to define Bear class."""


class Bear:
    """A Bear that lives in the river and eats fish."""

    age: int
    hunger_score: int

    def __init__(self):
        """Initialize a Bear with age 0 and hunger_score 0."""
        self.age = 0
        self.hunger_score = 0

    def one_day(self):
        """Increments age by 1 and decreases hunger score as 1 day passes."""
        self.age += 1
        self.hunger_score -= 1

    def eat(self, num_fish: int) -> None:
        """Increase hunger_score based on the number of fish eaten."""
        self.hunger_score += num_fish
