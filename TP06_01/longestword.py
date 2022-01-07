#!/bin/python

user_input = input("Entrez plusieurs mots : ")

strings = user_input.split(" ")
lengths = [len(string) for string in strings]

print("Le mot le plus long fait {} caractères.".format(max(lengths)))