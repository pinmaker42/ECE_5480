# James Smith
# Jfs8888@vt.edu
# ECE 5480, Homework 1

import datetime
#https://docs.python.org/3/library/datetime.html

def numberPossiblePasswords(numDigits, numPossiblePerDigit):
    numPasswords = numPossiblePerDigit**numDigits
    return numPasswords

def maxSecondsToCrack(numPossiblePasswords, secPerAttempt):
    time = numPossiblePasswords*secPerAttempt
    return time

nd = int(input("How many digits long is the passcode? "))
nc = int(input("How many possible characters are there per digit? "))
secondsPerAttempt = .00001
npp = numberPossiblePasswords(nd, nc)
totalSeconds = maxSecondsToCrack(npp, secondsPerAttempt)
print("It will take you " + datetime.datetime.fromtimestamp(totalSeconds).strftime('%M:%S') + "(MM:SS) minutes maximum to crack the password.")
