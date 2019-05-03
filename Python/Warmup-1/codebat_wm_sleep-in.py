#CodingBat Python Warmup-1>sleep_in:
def main():
  #unit test
  print('Expected Values: \nTrue, False, True, True \nActual:')
  print(sleep_in(False, False), sleep_in(True, False), sleep_in(False, True), sleep_in(True, True))

#Problem:
#The parameter weekday is True if it is a weekday, and the parameter vacation is True if we are on vacation.
#We sleep in if it is not a weekday or we're on vacation. Return True if we sleep in.

#Solution:
def sleep_in(weekday, vacation):
  if weekday and not vacation:
    return False
  else:
    return True
main()
