from pytest_example import hehe, count_regs

"""Test functions in c120 module"""


def test_hehe() -> None:
    """Test the hehe function"""
    assert hehe(3) == 0


def test_count_reqs_use() -> None:
    """Test use case of count_regs."""
    assert count_regs("Orange", ["Wake", "Orange", "Orange", "Durham"]) == 2


def test_count_regs_edge() -> None:
    """Test edge case for count_regs."""
    assert count_regs("Orange", []) == 0


def test_count_regs_mutate() -> None:
    """Test whether count_regs mutates list."""
    cs: list[str] = ["Durham", "Wake", "Lee"]  # If list will be altered
    count_regs("Wake", cs)
    assert cs == ["Durham", "Wake", "Lee"]  # Fails if Lee is removed
