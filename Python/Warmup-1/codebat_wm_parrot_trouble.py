#CodingBat Python Warmup-1>parrot_trouble:
def main():
  #unit test
  print('Expected Values: \nTrue, False, False, True, False, False, True, False, False, False \nActual:')
  print(parrot_trouble(True, 6), parrot_trouble(True, 7), parrot_trouble(False, 6), parrot_trouble(True, 21), parrot_trouble(False, 21), parrot_trouble(False, 20), parrot_trouble(True, 23), parrot_trouble(False, 23), parrot_trouble(True, 20), parrot_trouble(False, 12))

#Problem:
#We have a loud talking parrot. The "hour" parameter is the current hour time in the range 0..23.
#We are in trouble if the parrot is talking and the hour is before 7 or after 20. Return True if we are in trouble.

#Solution:
def parrot_trouble(talking, hour):
    if ((hour < 7) or ( hour > 20)) and talking:
        return True
    else:
        return False
main()
