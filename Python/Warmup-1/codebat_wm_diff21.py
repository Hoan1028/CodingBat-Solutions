#CodingBat Python Warmup-1>diff21:
def main():
  #unit test
  print('Expected Values: \n2, 11, 0, 2, 8, 18, 21, 20, 19, 22, 23, 58 \nActual:')
  print(diff21(19), diff21(10), diff21(21), diff21(22), diff21(25), diff21(30), diff21(0), diff21(1), diff21(2), diff21(-1), diff21(-2), diff21(50))

#Problem:
#Given an int n, return the absolute difference between n and 21, 
#except return double the absolute difference if n is over 21.

#Solution:
def diff21(n):
    if n <= 21:
        return abs(n-21)
    else:
        return 2 * abs(n-21)
main()
