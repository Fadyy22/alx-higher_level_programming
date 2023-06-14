#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary:
        best_score = list(a_dictionary.keys())[0]
        for key in a_dictionary:
            if a_dictionary[key] > a_dictionary[best_score]:
                best_score = key
        return best_score
    return None
