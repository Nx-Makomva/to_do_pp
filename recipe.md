## 1. Describe the Problem

_Put or write the user story here. Add any clarifying notes you might have._

As a user
So that I can find my tasks among all my notes
I want to check if a line from my notes includes the string `#TODO`.


## 2. Design the Function Signature

_Include the name of the function, its parameters, return value, and side effects._

```python

def includes_todo(notes):
  """It filters through 'notes' passed in to find if it is a #TODO task

  Parameters: notes: a string that may contain multiple words e.g. 
    "learn to test-drive my code #TODO" or "drink tea"

  Returns: boolean: True or False if notes contains #TODO

  Side effects: If notes does not contain specific tag of #TODO then func may have incorrect return value

  """
  pass

```

```python
# EXAMPLE

def extract_uppercase(mixed_words):
    """Extracts uppercase words from a string

    Parameters: (list all parameters and their types)
        mixed_words: a string containing words (e.g. "hello WORLD")

    Returns: (state the return value and its type)
        a list of strings, each one a word (e.g. ["WORLD"])

    Side effects: (state any side effects)
        This function doesn't print anything or have any other side-effects
    """
    pass # Test-driving means _not_ writing any code here yet.
```

## 3. Create Examples as Tests

_Make a list of examples of what the function will take and return._





```python

"""
Given a string that doesn't contain #TODO:
"""
includes_todo('drink tea') => False


"""
Given a string that does contain #TODO:
"""
includes_todo('#TODO drink tea') => True


"""
Given a string containing #todo
"""
includes_todo('#todo drink tea') => False


"""
Given a int or float rather than a string
"""
includes_todo(23456789) => False | 'Input must be a string'


"""
Given a string which contains TODO (no #)
"""
includes_todo('TODO drink water') => False


```

_Encode each example as a test. You can add to the above list as you go._

## 4. Implement the Behaviour

_After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour._

Here's an example for you to start with:

```python
# EXAMPLE

from lib.includes_todo import *

"""
Given a string that doesn't contain #TODO:
"""
def test_returns_false_no_todo():
    assert includes_todo('Drink water') == False


"""
Given a string that does contain #TODO:
"""
def test_returns_true_contains_todo():
    assert includes_todo('#TODO drink water') == True


"""
Given a string that does contain #TODO end of input:
"""
def test_returns_true_contains_todo():
    assert includes_todo('drink water #TODO') == True


"""
Given a string containing #todo
"""
def test_returns_false_lowercase_todo():
    assert includes_todo('#todo drink water') == False


# """
# Given a int or float rather than a string
# """
# def test_throws_error_if_input_not string():
#     (948484)

"""
Given an empty string
"""
def test_returns_false_empty_string():
    with pytest.raises(Exception) as e:
        includes_todo('')
    assert str(e.value) == 'Input is empty, please write a task'


"""
Given a sting that contains todo (no #)
"""
def test_returns_false_todo_no_hash():
    assert includes_todo('TODO drink water') => False


```

Ensure all test function names are unique, otherwise pytest will ignore them!