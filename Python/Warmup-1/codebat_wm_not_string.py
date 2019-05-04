#CodingBat Python Warmup-1>not_string:
def main():
  #unit test
  print('Expected Values: \nnot candy, not x, not bad, not bad, not, not is not, not no \nActual:')
  print(not_string('candy'), not_string('x'), not_string('not bad'), not_string('bad'), not_string('not'), not_string('is not'), not_string('no'))

#Problem:
#Given a string, return a new string where "not " has been added to the front.
#However, if the string already begins with "not", return the string unchanged.

#Solution:
def not_string(str):
    if str.startswith('not'):
        return str
    else:
        return "not " + str
main()
