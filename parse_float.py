'''
Module
'''
from typing import List
NUMBER_LIST = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']


def parse(strng: str) -> bool:
    '''

    :param s:
    :return:
    '''
    if strng == '':
        return False
    list_elem: List = []
    list_elem.extend(strng)
    result_line = ''
    for i in list_elem:
        if i not in NUMBER_LIST:
            result_line += i
    if result_line in ['.', '-.', '-', '']:
        return True
    return False
