"""String utility functions."""


def reverse_string(s: str) -> str:
    """Reverse a string."""
    return s[::-1]


def is_palindrome(s: str) -> bool:
    """Check if a string is a palindrome (case-insensitive)."""
    cleaned = s.lower().replace(" ", "")
    return cleaned == cleaned[::-1]


def count_vowels(s: str) -> int:
    """Count the number of vowels in a string."""
    return sum(1 for char in s.lower() if char in "aeiou")


def truncate(s: str, max_length: int, suffix: str = "...") -> str:
    """Truncate a string to a maximum length, adding a suffix if truncated.

    Args:
        s: The string to truncate.
        max_length: Maximum allowed length (must be > len(suffix)).
        suffix: String to append when truncated.

    Returns:
        The truncated string.

    Raises:
        ValueError: If max_length is less than or equal to len(suffix).
    """
    if max_length <= len(suffix):
        raise ValueError(f"max_length must be greater than {len(suffix)}")
    if len(s) <= max_length:
        return s
    return s[: max_length - len(suffix)] + suffix
