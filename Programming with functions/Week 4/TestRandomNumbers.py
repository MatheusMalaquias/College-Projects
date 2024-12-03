from RandomNumbers import append_random_numbers, append_random_words
import pytest


def test_append_random_numbers():
    numbers_list = []
    assert len(numbers_list) == 0
    append_random_numbers(numbers_list)
    assert len(numbers_list) == 1
    for x in numbers_list:
        assert isinstance(x, float)
    append_random_numbers(numbers_list, 3)
    assert len(numbers_list) == 4
    for x in numbers_list:
        assert isinstance(x, float)


#def test_append_random_words():
#    words_list = []
#    assert len(words_list) == 0

#    append_random_words(words_list)
#    assert len(words_list) == 1
#    for word in words_list:
#        assert isinstance(word, str)
#        assert len(word) >= 1

#    append_random_words(words_list, 3)
#    assert len(words_list) == 4
#    for word in words_list:
#        assert isinstance(word, str)
#        assert len(word) >= 1

pytest.main(["-v", "--tb=line", "-rN", __file__])
