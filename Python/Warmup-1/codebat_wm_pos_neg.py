#CodingBat Python Warmup-1>pos_neg:
def main():
  #unit test
  print('Expected Values: \nTrue, True, True, False, True, False, False, False, False, False, False, True, True, True, False, False, False, False, True \nActual:')
  print(pos_neg(1, -1, False),pos_neg(-1, 1, False),pos_neg(-4, -5, True),pos_neg(-4, -5, False),pos_neg(-4, 5, False),pos_neg(-4, 5, True),pos_neg(1, 1, False),pos_neg(-1, -1, False),pos_neg(1, -1, True),pos_neg(-1, 1, True),pos_neg(1, 1, True),pos_neg(-1, -1, True),pos_neg(5, -5, False),pos_neg(-6, 6, False),pos_neg(-5, -6, False),pos_neg(-2, -1, False),pos_neg(1, 2, False),pos_neg(-5, 6, True),pos_neg(-5, -5, True))

#Problem:
#Given 2 int values, return True if one is negative and one is positive.
#Except if the parameter "negative" is True, then return True only if both are negative.

#Solution:
def pos_neg(a, b, negative):
    if (( a < 0 and b >= 0) or ( a >= 0 and b < 0)) and negative is False:
        return True
    elif negative is True:
        if ( a < 0 and b < 0):
            return True
    return False
main()
