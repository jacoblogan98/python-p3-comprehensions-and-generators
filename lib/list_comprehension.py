#!/usr/bin/env python3

def return_evens(num_list):
    # evens = [n for n in num_list if n % 2 == 0]
    # return evens

    return [n for n in num_list if n % 2 == 0]


def make_exclamation(sentence_list):
    # exclamations = [s + "!" for s in sentence_list]
    # return exclamations

    return [s + "!" for s in sentence_list]
