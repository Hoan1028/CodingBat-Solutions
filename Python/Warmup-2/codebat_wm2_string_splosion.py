#CodingBat Python Warmup-2>string_splosion:
def main():
  #unit test
  print('Expected Values: \nCCoCodCode, aababc, aab, x, ffafadfade, TThTheTherThere, KKiKitKittKitteKitten, BByBye, GGoGooGood, BBaBad \nActual:')
  print(string_splosion('Code'),string_splosion('abc'),string_splosion('ab'),string_splosion('x'),string_splosion('fade'),string_splosion('There'),string_splosion('Kitten'),string_splosion('Bye'),string_splosion('Good'),string_splosion('Bad'))

#Problem:
#Given a non-empty string like "Code" return a string like "CCoCodCode".

#Solution:
def string_splosion(str):
    newStr = ''
    for index, char in enumerate(str):
       newStr += str[:index+1]
    return newStr
main()