from Words import prefix, suffix
import pytest

def test_prefix():
    pre = prefix('upbeat', 'upgrade')
    assert isinstance(pre, str), 'prefix function must return a string'
    assert prefix('', '') == ''
    assert prefix('', 'correct') == ''
    assert prefix('clear', '') == ''
    assert prefix('happy', 'funny') == ''
    assert prefix('cat', 'catalog') == 'cat'
    assert prefix('dogmatic', 'dog') == 'dog'
    assert prefix('jump', 'joyous') == 'j'
    assert prefix('upbeat', 'upgrade') == 'up'
    assert prefix('Disable', 'dIstasteful') == 'dis'

def test_suffix():
    assert suffix('', '') == ''
    assert suffix('', 'correct') == ''
    assert suffix('clear', '') == ''
    assert suffix('angelic', 'awesome') == ''
    assert suffix('found', 'profound') == 'found'
    assert suffix('ditch', 'itch') == 'itch'
    assert suffix('happy', 'funny') == 'y'
    assert suffix('tired', 'fatigued') == 'ed'
    assert suffix('swimming', 'FLYING') == 'ing'

pytest.main(["-v", "--tb=line", "-rN", __file__])
