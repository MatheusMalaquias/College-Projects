from Receipt import read_dictionary
from os import path
from tempfile import mktemp
from pytest import approx
import pytest


def test_read_dictionary():
    PRODUCT_NUM_INDEX = 0
    filename = path.join(path.dirname(__file__), "Products.csv")
    products_dict = read_dictionary(filename, PRODUCT_NUM_INDEX)
    assert isinstance(products_dict, dict), \
        "read_dictionary function must return a dictionary:" \
        f" expected a dictionary but found a {type(products_dict)}"
    length = len(products_dict)
    exp_len = 16
    assert length == exp_len, \
        "products dictionary has too" \
        f" {'few' if length < exp_len else 'many'} items:" \
        f" expected {exp_len} but found {length}"
    check_product(products_dict, "D150", ["1 gallon milk", 2.85])
    check_product(products_dict, "D083", ["1 cup yogurt", 0.75])
    check_product(products_dict, "D215", ["1 lb cheddar cheese", 3.35])
    check_product(products_dict, "P019", ["iceberg lettuce", 1.15])
    check_product(products_dict, "P020", ["green leaf lettuce", 1.79])
    check_product(products_dict, "P021", ["butterhead lettuce", 1.83])
    check_product(products_dict, "P025", ["8 oz arugula", 2.19])
    check_product(products_dict, "P143", ["1 lb baby carrots", 1.39])
    check_product(products_dict, "W231", ["32 oz granola", 3.21])
    check_product(products_dict, "W112", ["wheat bread", 2.55])
    check_product(products_dict, "C013", ["twix candy bar", 0.85])
    check_product(products_dict, "H001", ["8 rolls toilet tissue", 6.45])
    check_product(products_dict, "H014", ["facial tissue", 2.49])
    check_product(products_dict, "H020", ["aluminum foil", 2.39])
    check_product(products_dict, "H021", ["12 oz dish soap", 3.19])
    check_product(products_dict, "H025", ["toilet cleaner", 4.50])


def check_product(products_dict, product_number, expected_value):
    assert product_number in products_dict
    actual_value = products_dict[product_number]
    length = len(actual_value)
    min_len = 2
    max_len = 3
    assert min_len <= length and length <= max_len, \
        f"value list for product {product_number} contains too" \
        f" {'few' if length < min_len else 'many'} elements:" \
        f" expected {min_len} or {max_len} elements but found {length}"

    if length == min_len:
        NAME_INDEX = 0
        PRICE_INDEX = 1
    else:
        NAME_INDEX = 1
        PRICE_INDEX = 2

    act_name = actual_value[NAME_INDEX]
    exp_name = expected_value[0]
    assert act_name == exp_name, \
        f"wrong name for product {product_number}: " \
        f"expected {exp_name} but found {act_name}"

    act_price = actual_value[PRICE_INDEX]
    if isinstance(act_price, str):
        act_price = float(act_price)
    exp_price = expected_value[1]
    assert act_price == approx(exp_price), \
        f"wrong price for product {product_number}: " \
        f"expected {exp_price} but found {act_price}"

pytest.main(["-v", "--tb=line", "-rN", __file__])