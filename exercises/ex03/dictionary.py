"""Different type of dictionaries for each function"""

__author__ = "730751590"


def invert(input: dict[str, str]) -> dict[str, str]:
    # Creating an empty dict for the inverted keys and values
    inverted_dict: dict[str, str] = {}

    # Iterates over keys in the input dict
    for key in input:
        # Returns the key's value
        value = input[key]
        # If key is duplicated in the dictionary/ check if key in dict
        if value in inverted_dict:
            raise KeyError("Duplicate key found when inverting")
        # Inverts the key's value to a key in the dictionary
        inverted_dict[value] = key
    # returns the inverted dictionary of inverted keys and values
    return inverted_dict


def count(values: list[str]) -> dict[str, int]:
    # Create an empty dictionary to store the values
    result: dict[str, int] = {}
    # Set the index to initialize at 0
    i: int = 0
    # If the index is less than the length of the values list
    while i < len(values):
        # If the values at that index is already stored in the result
        # Increment the value by 1 at that index
        if values[i] in result:
            result[values[i]] += 1
        # If the value is not stored already at the index, start the count at 1
        else:
            result[values[i]] = 1
        # Reiterate through each index in the values list
        i += 1
    # Return the dictionary of keys and values
    return result


def favorite_color(colors: dict[str, str]) -> str:
    """Returns the most frequent color in the dictionary"""
    # The key is a string because its the favorite color
    # The value returns the count of the favorite color
    color_count: dict[str, int] = {}
    # Tracks most popular color
    most_popular_color = ""
    # Tracks max color count
    max_count = 0
    # Iterates through the color dictionary for each color
    for color in colors:
        # Returns the value of  the favorite color at the key
        favorite_color = colors[color]
        # If the color is in the count dictionary
        # Increase the favorite color by 1
        if favorite_color in color_count:
            color_count[favorite_color] += 1
        # If the color is not in the count dictionary
        # Initialize it at 1
        else:
            color_count[favorite_color] = 1
        # If the favorite color count is higher than the max
        # Update the favorite color to the most popular color
        # Update the max count
        if color_count[favorite_color] > max_count:
            most_popular_color = favorite_color
            max_count = color_count[favorite_color]
        # Return the most popular color
    return most_popular_color


def bin_len(strings: list[str]) -> dict[int, set[str]]:
    # A dictionary to store strings by their lengths with the values as sets.
    result: dict[int, set[str]] = {}
    # Iterates through the strings dictionary for each string
    for string in strings:
        # Length of given string
        length = len(string)
        # Checks whether the key "length" is present in the dictionary
        if length in result:
            result[length].add(string)
        else:
            # If length is not present, create a new set in the dictionary
            result[length] = set([string])
    return result
