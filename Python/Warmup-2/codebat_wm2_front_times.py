#CodingBat Python Warmup-2>front_times:
def main():
  #unit test
  print('Expected Values: \nChoCho, ChoChoCho, AbcAbcAbc, AbAbAbAb, AAAA, \'\', \'\' \nActual:')
  print(front_times('Chocolate', 2), front_times('Chocolate', 3), front_times('Abc', 3), front_times('Ab', 4), front_times('A', 4), front_times('', 4),front_times('Abc', 0))

#Problem:
#Given a string and a non-negative int n, we'll say that the front of the string is the first 3 chars,
#or whatever is there if the string is less than length 3.
#Return n copies of the front.

#Solution:
def front_times(str, n):
  if len(str) < 3:
    return str*n
  else:
    return str[:3]*n
main()