#CodingBat Python Warmup-2>array_count9:
def main():
  #unit test
  print('Expected Values: \n1, 2, 3, 0, 0, 0, 1 \nActual:')
  print(array_count9([1, 2, 9]),array_count9([1, 9, 9]),array_count9([1, 9, 9, 3, 9]),array_count9([1, 2, 3]),array_count9([]),array_count9([4, 2, 4, 3, 1]),array_count9([9, 2, 4, 3, 1]))

#Problem:
#Given an array of ints, return the number of 9's in the array.

#Solution:
def array_count9(nums):
    counter = 0
    for element in nums:
        if element == 9:
            counter = counter + 1
    return counter
main()