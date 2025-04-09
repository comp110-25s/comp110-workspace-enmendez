"""File to define Fish class."""


class Fish:
    """A fish that lives in the river and ages over time."""

    age: int

    def __init__(self):
        """Initialize a Fish with age 0."""
        self.age = 0

    def one_day(self):
        """Increments age by 1 to simulate one day passing."""
        self.age += 1
