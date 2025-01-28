"""Calculates the # of tea bags, treats, and the total anticipated cost"""

__author__: str = "730751590"


def main_planner(guests: int) -> None:
    """Produced printed output and does not return a value"""
    print("A Cozy Tea Party for " + str(guests) + " People!")
    print("Tea Bags: " + str(tea_bags(guests)))
    print("Treats: " + str(treats(guests)))
    print("Cost: $" + str(cost(tea_bags(guests), treats(guests))))


def tea_bags(people: int) -> int:
    """Calculates # of attendees based on # of tea bags"""
    return people * 2


def treats(people: int) -> int:
    """Calculates # of treats based on # of tea guests"""
    return int(tea_bags(people) * 1.5)


def cost(tea_count: int, treat_count: int) -> float:
    """Calculates total cost of tea bags and treats"""
    return tea_count * 0.50 + treat_count * 0.75


if __name__ == "__main__":
    main_planner(guests=int(input("How many guests are attending your tea party?")))
