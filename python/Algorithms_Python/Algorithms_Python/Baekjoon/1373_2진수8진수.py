import sys
input = sys.stdin.readline

print(oct(int('0b' + input(), 2))[2:])