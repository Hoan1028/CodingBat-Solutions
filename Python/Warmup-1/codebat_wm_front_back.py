#CodingBat Python Warmup-1>front_back:
def main():
  #unit test
  print('Expected Values: \neodc, a, ba, cba, \'\', ehocolatC, Java, oellh \nActual:')
  print(front_back('code'), front_back('a'), front_back('ab'), front_back('abc'), front_back(''), front_back('Chocolate'), front_back('aavJ'), front_back('hello'))

#Problem:
#Given a string, return a new string where the first and last chars have been exchanged.

#Solution:
def front_back(str):
    if len(str) <= 1:
        return str
    else:
      return str[-1]+str[1:-1]+str[0]
main()
