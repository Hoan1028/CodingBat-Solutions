#CodingBat Python Warmup-1>missing_char:
def main():
  #unit test
  print('Expected Values: \nktten, itten, kittn, i, H, ode, cde, coe, cod, chocolat \nActual:')
  print(missing_char('kitten', 1), missing_char('kitten', 0), missing_char('kitten', 4), missing_char('Hi', 0), missing_char('Hi', 1), missing_char('code', 0), missing_char('code', 1), missing_char('code', 2), missing_char('code', 3), missing_char('chocolate', 8))

#Problem:
#Given a non-empty string and an int n, return a new string where the char at index n has been removed.
#The value of n will be a valid index of a char in the original string (i.e. n will be in the range 0..len(str)-1 inclusive).

#Solution:
def missing_char(str, n):
    return str[:n]+str[n+1:]
main()
