from typing import Counter


total = 0
Counter = 1

n = int(input("enter number:"))
while(Counter < n + 1):
    print("count:", Counter)
    total = total + int(input())
    Counter = Counter + 1

average =  total / 5

print("average score:", average)