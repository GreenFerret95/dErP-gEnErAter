#!/usr/bin/env python3
import sys

class Generate:
    def __init__(self):
        message = sys.argv[1].lower()
        count = 0
        new_message = []
        for char in message:
            if (count % 2) != 0:
                new_message.append(char.upper())
                print(char.upper())
            else: 
                new_message.append(char)
                print(char)
            count+=1
        s = ""
        new_message = s.join(new_message)
        print(new_message)

g = Generate()
