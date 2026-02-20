import pytest
from string_utils import reverse_string, is_palindrome, count_vowels, truncate

class TestReverseString:
    def test_reverse_string_with_valid_input(self):
        result = reverse_string(s='hello')
        assert result == 'olleh'

    def test_reverse_string_with_empty_input(self):
        result = reverse_string(s='')
        assert result == ''

    def test_reverse_string_with_single_character(self):
        result = reverse_string(s='a')
        assert result == 'a'

class TestIsPalindrome:
    def test_is_palindrome_with_palindrome_input(self):
        result = is_palindrome(s='Madam')
        assert result is True

    def test_is_palindrome_with_non_palindrome_input(self):
        result = is_palindrome(s='Hello')
        assert result is False

    def test_is_palindrome_with_empty_string(self):
        result = is_palindrome(s='')
        assert result is True

    def test_is_palindrome_with_special_characters_and_spaces(self):
        result = is_palindrome(s='A man, a plan, a canal, Panama')
        assert result is True

class TestCountVowels:
    def test_count_vowels_with_valid_input(self):
        result = count_vowels(s='Hello World')
        assert result == 3

    def test_count_vowels_with_empty_string(self):
        result = count_vowels(s='')
        assert result == 0

    def test_count_vowels_with_no_vowels(self):
        result = count_vowels(s='bcdfg')
        assert result == 0

class TestTruncate:
    def test_truncate_with_valid_input(self):
        result = truncate(s='Hello World', max_length=8, suffix='...')
        assert result == 'Hello...'

    def test_truncate_with_string_shorter_than_max_length(self):
        result = truncate(s='Hi', max_length=5)
        assert result == 'Hi'

    def test_truncate_with_empty_string(self):
        result = truncate(s='', max_length=5)
        assert result == ''

    def test_truncate_with_invalid_max_length(self):
        with pytest.raises(ValueError):
            truncate(s='Hello', max_length=-1)
