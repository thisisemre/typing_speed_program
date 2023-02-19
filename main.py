from random import randint
from tkinter import *
root = Tk()
root.title("Typing Speed Test ")
words = []
paragraph = []

with open('words.txt') as f:
    for word in f:
        words.append(word.split("\n")[0])

for _ in range(150):
    paragraph.append(words[randint(0, 2998)])

