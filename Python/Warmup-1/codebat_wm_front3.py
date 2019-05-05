#CodingBat Python Warmup-1>front3:
def main():
  #unit test
  print('Expected Values: \nJavJavJav, ChoChoCho, abcabcabc, abcabcabc, ababab, aaa, \'\' \nActual:')
  print(front3('Java'), front3('Chocolate'), front3('abc'), front3('abcXYZ'), front3('ab'), front3('a'), front3(''))

#Problem:
#Given a string, we'll say that the front is the first 3 chars of the string.
#If the string length is less than 3, the front is whatever is there.
#Return a new string which is 3 copies of the front.

#Solution:
def front3(str):
  if len(str) < 3:
    return str*3
  else:
    return str[:3]*3
main()