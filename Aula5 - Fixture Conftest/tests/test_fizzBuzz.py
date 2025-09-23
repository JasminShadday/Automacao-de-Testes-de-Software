import pytest
from src.fizzBuzz import fizBuzz

@pytest.fixture
def fizzbuzz_values():
    return( {i:fizBuzz(i) for i in range(1, 21)})

@pytest.mark.parametrize("num, expected", [
    (1, 1), (2, 2), (3, 'Fizz'),(4, 4),
    (5, 'Buzz'),(6, 'Fizz'),
    (7, 7),(8, 8),
    (9, 'Fizz'),(10, 'Buzz'),
    (11, 11),(12, 'Fizz'),
    (13, 13), (14, 14),
    (15, 'FizzBuzz'), (16, 16),
    (17, 17),  (18, 'Fizz'),
    (19, 19),
    (20, 'Buzz'),
])
def test_fizzbuzz(fizzbuzz_values, num, expected):
    assert fizzbuzz_values[num] == expected
