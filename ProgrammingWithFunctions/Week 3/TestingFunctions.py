# def deposit(amount):
#    assert amount > 0

# def test_min():
#    assert min(7, -3, 0, 2) == -3

#e = 7.135
#f = 7.128
#if abs(e - f) < 0.01:
#    print(f'{e} and {f} are close enough so')
#    print("We'll consider them to be equal")
#else:
#   print(f'{e} and {f} are not close and')
#    print('therefor not equal')

# def test_sqrt():
#   assert math.sqrt(5) == approx(2.24, rel = 0.01)

# def test_sqrt():
#    assert math.sqrt(5) == approx(2.24, abs=0.01)

#tolerance = expected_value * rel
#if abs(actual_value - expected_value) < tolerance:
#    return True
#else:
#    return False


#Weather

#from weather import cels_from_fahr
#from pytest import approx
#import pytest

# def test_cels_from_fahr():
#   assert cels_from_fahr(-25) == approx(-31.66667)
#   assert cels_from_fahr(0) == approx(-17.77778)
#   assert cels_from_fahr(32) == approx(0)
#   assert cels_from_fahr(70) == approx(21.1111)
#pytest.main(["-v", "--tb=line", "-rN", __file__])

# def wind_chill(temperature, wind_speed):
#    chill_factor = 35.74 \
#        + 0.6215 * temperature \
#        - 35.75 * wind_speed ** 0.16 \
#        + 0.4275 * temperature * wind_speed ** 0.16
#rounded = round (chill_factor, 1)
#return rounded


#index = - 42.379 \
#    + 2.04901523 * temperature \
#    + 10.14333127 + humidity \
#    - 0.22475541 + temperature * humidity \
#    - 0.00683783 * temperature ** 2 \
#    - 0.05481717 * humidity ** 2 \
#    - 0.00122874 * temperature ** 2 * humidity \
#    + 0.00085282 * temperature * humidity ** 2 \
#    - 0.00000199 * temperature * 2 * humidity * 2
#rounded = round (index, 1)
#return rounded