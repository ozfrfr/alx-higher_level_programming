#!/usr/bin/python3
''' module: 4-inherits_from
'''


def inherits_from(obj, a_class):
    '''the object is an instnc of a cls that inherited (Dir or inDir)
    obj: an object
    a_class: a class
    returns None
    '''
    return type(obj) != a_class and isinstance(obj, a_class)
