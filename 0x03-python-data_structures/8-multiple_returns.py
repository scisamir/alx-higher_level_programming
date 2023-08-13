#!/usr/bin/python3
def multiple_returns(sentence):
    if len(sentence) == 0:
        fchar = "None"
    else:
        fchar = sentence[0]

    tupl = len(sentence), fchar
    return tupl
