import pytest
from string_utils import reverse_string, is_palindrome, count_vowels, truncate

class TestReverseString:
    def test_reverse_string_with_valid_input(self):
        s = 'hello'
        expected = 'olleh'
        result = reverse_string(s)
        assert result == expected

    def test_reverse_string_with_empty_string(self):
        s = ''
        expected = ''
        result = reverse_string(s)
        assert result == expected

    def test_reverse_string_with_palindrome(self):
        s = 'madam'
        expected = 'madam'
        result = reverse_string(s)
        assert result == expected

class TestIsPalindrome:
    def test_is_palindrome_with_valid_input(self):
        s = 'Racecar'
        expected = True
        result = is_palindrome(s)
        assert result == expected

    def test_is_palindrome_with_non_palindrome(self):
        s = 'hello'
        expected = False
        result = is_palindrome(s)
        assert result == expected

    def test_is_palindrome_with_empty_string(self):
        s = ''
        expected = True
        result = is_palindrome(s)
        assert result == expected

class TestCountVowels:
    def test_count_vowels_with_vowels(self):
        s = 'hello'
        expected = 2
        result = count_vowels(s)
        assert result == expected

    def test_count_vowels_with_no_vowels(self):
        s = 'bcdfg'
        expected = 0
        result = count_vowels(s)
        assert result == expected

    def test_count_vowels_with_empty_string(self):
        s = ''
        expected = 0
        result = count_vowels(s)
        assert result == expected

class TestTruncate:
    def test_truncate_with_valid_input(self):
        s = 'hello world'
        max_length = 8
        suffix = '...'
        expected = 'hello...'
        result = truncate(s, max_length, suffix)
        assert result == expected

    def test_truncate_without_truncation(self):
        s = 'hello'
        max_length = 10
        suffix = '...'
        expected = 'hello'
        result = truncate(s, max_length, suffix)
        assert result == expected

    def test_truncate_with_suffix_exceeding_max_length(self):
        s = 'world'
        max_length = 2
        suffix = '...'
        with pytest.raises(ValueError):
            truncate(s, max_length, suffix)
