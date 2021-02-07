# fast input/output 

# User enters N numbers, find the sum

# basic implementation
n = int(input())
nums = [int(i) for i in input().split()]
print(sum(nums))

# better
n = int(raw_input())
nums = [int(i) for i in raw_input().split()]
print(sum(nums))

# using stdin, stdout
from sys import stdin, stdout
n = stdin.readline()
nums = [int(i) for i in stdin.readline().split()]
print(str(sum(nums)))

# get a list of ints and assign to variables
# example: 
# input: 
# 1 22 37 48
# output: 
# a = 1
# b = 22
# c = 37
# d = 48

# one line
# a, b, c, d = map(int, input().split())
a, b, c, d = map(int, sys.stdin.readline().strip().split())

# using sys
import sys
def get_int():
  return map(int, sys.stdin.readline().strip().split())
a, b, c, d = get_int()

# input list of ints as a single line

nums = list(map(int, sys.stdin.readline().strip().split()))

import sys
def get_list():
  return list(map(int, sys.stdin.readline().strip().split()))
nums = get_list()

# input string

str = input()
str = raw_input()

import sys
def get_str():
  return sys.stdin.readline().strip()
str = get_str()
