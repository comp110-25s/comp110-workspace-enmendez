"""Conducting Unit Tests on the Dictionaries (Functions)"""

__author__ = "730751590"


from exercises.ex03.dictionary import invert, count, bin_len, favorite_color


def test_invert_use() -> None:
    """Test the use case of the invert function"""
    assert invert({"a": "z", "b": "y", "c": "x"}) == ({"z": "a", "y": "b", "x": "c"})


def test_invert_use2() -> None:
    """Test the second use case of the invert function"""
    assert invert({"x": "y"}) == ({"y": "x"})


def test_invert_edge() -> None:
    """Test the edge case of the invert function"""
    assert invert({}) == ({})


def test_count_use() -> None:
    """Test the use case of count"""
    assert count(["apple", "banana", "banana", "cherry"]) == {
        "apple": 1,
        "banana": 2,
        "cherry": 1,
    }


def test_count_use2() -> None:
    """Test the second use case of count"""
    assert count(["x", "y", "z", "z", "x", "z"]) == {"x": 2, "y": 1, "z": 3}


def test_count_edge() -> None:
    assert count([]) == {}


def test_favorite_color_use() -> None:
    """Test the use case of favorite_color"""
    assert (
        favorite_color(
            {
                "Eva": "blue",
                "Bailey": "pink",
                "Bella": "brown",
                "Gabriel": "blue",
                "Hillary": "green",
                "Austin": "blue",
            }
        )
        == "blue"
    )


def test_favorite_color_use2() -> None:
    """Test the second use case of favorite color"""
    assert favorite_color({"Hillary": "green"}) == "green"


def test_favorite_color_edge() -> None:
    """Test the edge case of favorite clor"""
    assert favorite_color({}) == ""


def test_bin_len_use() -> None:
    "Test the use case of bin_len"
    assert bin_len(["the", "quick", "fox"]) == {3: {"the", "fox"}, 5: {"quick"}}


def test_bin_len_use2() -> None:
    "Test the second use case of bin_len"
    assert bin_len(["the", "the", "fox"]) == {3: {"the", "fox"}}


def test_bin_len_edge() -> None:
    "Test the edge case of bin_len"
    assert bin_len([]) == {}
