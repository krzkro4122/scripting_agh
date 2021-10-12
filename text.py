#!/bin/bash
# -*- coding: utf8 -*-

# --- WORDS REMOVAL --- #

file = open("TEXT.txt", "r")
#file = open("english.txt", "r")
text = file.read()
file.close()

print(text, end="")

words_to_delete = [" się ", " i ", " oraz ", " nigdy ", " dlaczego "]

for word_to_delete in words_to_delete:
	text = text.replace(word_to_delete, " ")
print(text, end="")

# --- WORDS REPLACMEMENT --- #
