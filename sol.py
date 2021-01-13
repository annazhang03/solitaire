import sys

text = sys.argv[1]
text = text.upper()

# ABC --> [1,2,3]
def toNum(text):
    result = []
    for i in text:
        result.append(ord(i) - 64)    
    return result

class Card:
    def __init__(self, value):
        self.value = value
    def get_value(self, suit_val):
      return self.val+suit_val

suits = ['spades', 'diamonds', 'clubs', 'hearts', 'jokers']
deck = [Card(value) for value in range(1,55)]

keystream = []

''' KEYSTREAM ALGORITHM:
for i in range(len(text)):
    move card 53 down by one place
    move card 54 down by two places
    triple cut
    count cut
    get keystream value
    keystream.append(value)
'''

nums = []
for i in range(len(text)):
    nums.append((toNum(text)[i] + keystream[i]) % 26)

def toAlpha(num):
    result = ''
    for i in num:
        result += chr(i + 64)
    return result

print(toAlpha(nums))
