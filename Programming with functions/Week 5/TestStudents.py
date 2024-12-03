from Students import read_dictionary
from inspect import signature
from os import path
from tempfile import mktemp
import pytest

def test_read_dictionary():
    I_NUMBER_INDEX = 0
    filename = mktemp(dir=".", prefix="not", suffix=".csv")
    with pytest.raises(FileNotFoundError):
        call_read_dictionary(filename, I_NUMBER_INDEX)
        pytest.fail("read_dictionary function must use its filename parameter")
    filename = path.join(path.dirname(__file__), 'c:\\Users\\NOTEBOOK\\Desktop\\BYU-I\\Intro to Python Development\\Programming with functions\\Week 5\\Students.csv')
    students_dict = call_read_dictionary(filename, I_NUMBER_INDEX)
    assert isinstance(students_dict, dict), \
        "read_dictionary function must return a dictionary:" \
        f" expected a dictionary but found a {type(students_dict)}"
    length = len(students_dict)
    exp_len = 9
    assert length == exp_len, \
        "students dictionary has too" \
        f" {'few' if length < exp_len else 'many'} items:" \
        f" expected {exp_len} but found {length}"
    check_student(students_dict, "751766201", "James Smith")
    check_student(students_dict, "751762102", "Esther Einboden")
    check_student(students_dict, "052058203", "Cassidy Benavidez")
    check_student(students_dict, "323021604", "Joel Hatch")
    check_student(students_dict, "251041405", "Brianna Ririe")
    check_student(students_dict, "001152306", "Stefano Hisler")
    check_student(students_dict, "182706207", "Hyeonbeom Park")
    check_student(students_dict, "124712708", "Maren Thomas")
    check_student(students_dict, "212505409", "Tyler Clark")


def call_read_dictionary(filename, key_column_index):
    sig = signature(read_dictionary)
    length = len(sig.parameters)
    min_len = 1
    max_len = 2
    assert length == min_len or length == max_len, \
        "The read_dictionary function contains too " \
        f"{'few' if length < min_len else 'many'} parameters; " \
        f"expected {min_len} or {max_len} parameters but found {length}"
    if length == min_len:
        dictionary = read_dictionary(filename)
    else:
        dictionary = read_dictionary(filename, key_column_index)
    return dictionary


def check_student(students_dict, inumber, exp_name):
    assert inumber in students_dict, \
        f'"{inumber}" is missing from the students dictionary.'

    actual = students_dict[inumber]
    assert isinstance(actual, str) or isinstance(actual, list), \
        "Each value in the students dictionary must be either a string " \
        f"or a list. The value for {inumber} is of type {type(actual)} " \
        "which is not a string or a list."

    if isinstance(actual, str):
        assert actual == exp_name, \
                f'Wrong name for "{inumber}"; ' \
                f'expected {exp_name} but found {actual}'
    else:
        length = len(actual)
        min_len = 1
        max_len = 2
        assert length == min_len or length == max_len, \
            f"The value list for student {inumber} contains too " \
            f"{'few' if length < min_len else 'many'} elements; " \
            f"expected {min_len} or {max_len} elements but found {length}"

        if length == min_len:
            NAME_INDEX = 0
            act_name = actual[NAME_INDEX]
            assert act_name == exp_name, \
                    f'Wrong name for "{inumber}"; ' \
                    f'expected {exp_name} but found {act_name}'
        else:
            I_NUMBER_INDEX = 0
            act_inum = actual[I_NUMBER_INDEX]
            assert act_inum == inumber, \
                    'Inconsistent I-Numbers in the key and value. ' \
                    f'The key is {inumber} but {act_inum} is in ' \
                    'the corresponding value.'
            NAME_INDEX = 1
            act_name = actual[NAME_INDEX]
            assert act_name == exp_name, \
                    f'Wrong name for "{inumber}"; ' \
                    f'expected {exp_name} but found {act_name}'

pytest.main(['-v', '--tb=line', '-rN', __file__])