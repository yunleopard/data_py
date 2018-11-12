'''
Created on Nov 12, 2018

@author: yangzh
'''
from . import helpers

def say_hi():
    """Get a thought."""
    return 'Hi,  my friend ...'


def saySomething():
    """Contemplation..."""
    if helpers.get_answer():
        print(say_hi())