#CodingBat Python Warmup-1>makes10:
def main():
  #unit test
  print('Expected Values: \nTrue, False, True, True, True, True, False, True, True \nActual:')
  print(makes10(9, 10), makes10(9, 9), makes10(1, 9), makes10(10, 1), makes10(10, 10), makes10(8, 2), makes10(8, 3), makes10(10, 42), makes10(12, -2))

#Problem:
#Given 2 ints, a and b, return True if one if them is 10 or if their sum is 10.

#Solution:
def makes10(a, b):
    if (a == 10 or b == 10) or ( a + b == 10):
        return True
    else:
        return False 
main()
