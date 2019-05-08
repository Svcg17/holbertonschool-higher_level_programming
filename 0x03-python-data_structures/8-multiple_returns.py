#!/usr/bin/python3
def multiple_returns(sentence):
        leni = len(sentence)
        if sentence:
            first = sentence[0:1]
            toup = leni, first
            return toup
        else:
            first = None
            toup = leni, first
            return toup
