#PROMPT: This problem was asked by Apple.
#Implement a job scheduler which takes in a function f and an integer n, and calls f after n milliseconds.

#Using: Python

import time

#Define function: To print the integer given at the start of the program

def job_scheduler(n):
    time.sleep(n/1000)
    print("Time's up!")
    return 0;

n = input("How long would you like to wait? In milliseconds: ")

job_scheduler(int(n))
