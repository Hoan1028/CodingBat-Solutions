#CodingBat Python Warmup-2>last2:
def main():
  #unit test
  print('Expected Values: \n1, 1, 2, 3, 0, 2, 1, 1, 0 ,2, 0, 0, 0 \nActual:')
  print(last2('hixxhi'), last2('xaxxaxaxx'), last2('axxxaaxx'), last2('xxaxxaxxaxx'), last2('xaxaxaxx'), last2('xxxx'), last2('13121312'), last2('11212'), last2('13121311'), last2('1717171'), last2('hi'), last2('h'), last2(''))
#Problem:
#Given a string, return the count of the number of times that a substring length 2 appears in the string and also as the last 2 chars of the string,
#so "hixxxhi" yields 1 (we won't count the end substring).

#Solution:
def last2(str):
    substr = str[-2:]
    counter = 0
    for i in range(len(str)-2):
        if ( str[i:i+2]) == substr:
            counter += 1
    return counter
main()