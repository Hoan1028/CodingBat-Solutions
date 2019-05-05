#CodingBat Python Warmup-2>string_times:
def main():
  #unit test
  print('Expected Values: \nHiHi, HiHiHi, Hi, \'\', HiHiHiHiHi, Oh Boy!Oh Boy!, xxxx, \'\', codecode, codecodecode \nActual:')
  print(string_times('Hi', 2),string_times('Hi', 3),string_times('Hi', 1),string_times('Hi', 0),string_times('Hi', 5),string_times('Oh Boy!', 2),string_times('x', 4),string_times('', 4),string_times('code', 2),string_times('code', 3))

#Problem:
#Given a string and a non-negative int n, return a larger string that is n copies of the original string.

#Solution:
def string_times(str, n):
  return str*n
main()