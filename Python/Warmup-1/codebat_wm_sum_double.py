#CodingBat Python Warmup-1>sum_double:
def main():
  #unit test
  print('Expected Values: \n3, 5, 8, -1, 12, 0, 1, 7 \nActual:')
  print(sum_double(1, 2), sum_double(3, 2), sum_double(2, 2), sum_double(-1, 0), sum_double(3, 3), sum_double(0, 0), sum_double(0, 1), sum_double(3, 4))

#Problem:
#Given two int values, return their sum.
#Unless the two values are the same, then return double their sum.

#Solution:
def sum_double(a, b):
    if a == b:
        return 2*(a + b)
    else:
        return a + b
  
main()
