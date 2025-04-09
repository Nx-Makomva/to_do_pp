from lib.to_do import *
import pytest

def test_returns_false_no_todo():
    assert includes_todo('drink water') == False

def  test_returns_true_contains_todo():
    assert includes_todo('#TODO drink water') == True
    assert includes_todo('drink water #TODO') == True
    assert includes_todo('drink#TODOwater') == True


def test_returns_false_lowercase_todo():
    assert includes_todo('#todo drink water') == False
    
def test_returns_false_whitespace_between_hash_todo():
    assert includes_todo('# todo drink water') == False
    assert includes_todo('# TODO drink water') == False

def test_returns_false_todo_no_hash():
    assert includes_todo('TODO drink water') == False

def test_returns_false_empty_string():
    with pytest.raises(Exception) as e:
        includes_todo('')
    assert str(e.value) == 'Input is empty, please write a task'

def test_returns_false_when_input_not_string():
    assert includes_todo(2163) == False
    assert includes_todo(None) == False
