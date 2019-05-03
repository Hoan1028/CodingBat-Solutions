#CodingBat Python Warmup-1>near_hundred:
def main():
  #unit test
  print('Expected Values: \nTrue, True, False, True, False, False, False, False, True, True, False, False, False, True, False, True, True, False, False \nActual:')
  print(near_hundred(93),near_hundred(90),near_hundred(89),near_hundred(110),near_hundred(111),near_hundred(121),near_hundred(-101),near_hundred(-209),near_hundred(190),near_hundred(209),near_hundred(0),near_hundred(5),near_hundred(-50),near_hundred(191),near_hundred(189),near_hundred(200),near_hundred(210),near_hundred(211),near_hundred(290))

#Problem:
#Given an int n, return True if it is within 10 of 100 or 200. 
#Note: abs(num) computes the absolute value of a number.

#Solution:
def near_hundred(n):
    if (abs(n-100) <= 10 or abs(n-200) <= 10):
        return True
    else:
        return False
main()
