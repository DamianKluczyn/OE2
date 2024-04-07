import numpy as np
from typing import Tuple, List
from math import log2, ceil

#TODO klasa chromosom

def binary_list_to_decimal(binary_list: List) -> int:
    """
    Converts a binary list to a decimal
    :param binary_list: The binary list to convert
    :return: The decimal value of the binary list
    """
    return sum(value * (2 ** index) for index, value in enumerate(reversed(binary_list)))


def generate_binary_chromosome(boundries: Tuple[int, int], accuracy: int) -> List:
    """
    Generates a binary chromosome with the given boundries and accuracy
    :param boundries: the boundries of the solution
    :param accuracy: the accuracy of the solution
    :return: the binary chromosome
    """
    chromosome_length = ceil(log2((boundries[1] - boundries[0]) * 10 ** accuracy))

    return np.random.choice([0, 1], size=chromosome_length, p=[0.5, 0.5])


def decode_binary_chromosome(boundries: Tuple[int, int], binary_chain: List) -> float:
    """
    Decodes the given binary chromosome to a float value
    :param boundries: the boundries of the solution
    :param binary_chain: the binary chain of the chromosome
    :return: the float value of the chromosome
    """
    return (boundries[0] + binary_list_to_decimal(binary_chain) *
            (boundries[1] - boundries[0]) / (2 ** len(binary_chain) - 1))
