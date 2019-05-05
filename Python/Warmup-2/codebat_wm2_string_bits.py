#CodingBat Python Warmup-2>string_bits:
def main():
  #unit test
  print('Expected Values: \nHlo, H, Hello, HHH, \'\', Getns, Coot, p, Hlokte, happy \nActual:')
  print(string_bits('Hello'), string_bits('Hi'), string_bits('Heeololeo'), string_bits('HiHiHi'), string_bits(''), string_bits('Greetings'), string_bits('Chocoate'), string_bits('pi'), string_bits('Hello Kitten'), string_bits('hxaxpxpxy'))

#Problem:
#Given a string, return a new string made of every other char starting with the first, so "Hello" yields "Hlo".

#Solution:
def string_bits(str):
    newStr = ''
    for index, char in enumerate(str):
        if index % 2 == 0:
            newStr += char
    return newStr
main()