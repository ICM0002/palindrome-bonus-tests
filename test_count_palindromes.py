from count_palindromes import count_palindromes

def test_count_palindromes():
    assert count_palindromes("madam racecar level") == 3
    assert count_palindromes("hello world") == 0
    assert count_palindromes("wow is this a test") == 1

def test_case_insensitivity():
    assert count_palindromes("Madam Racecar Level") == 3
    assert count_palindromes("MadAm") == 1

def test_empty_string():
    assert count_palindromes("") == 0