import sys

text = sys.argv[1]
text = text.upper()

key_type = sys.argv[2] # f for file, o for order, w for keyword

key_inp = sys.argv[3]

# take initial ordering in the form of a file, a string, or a keyword and turn into [1,2,3,...]
def getKey(key_type, key_inp): 
    if key_type == 'f':
        key_file = open(key_inp)
        key = key_file.readlines()
        key = [int(i) for i in key]
    elif key_type == 'o':
        key = key_inp.split()
        key = [int(i) for i in key]
    elif key_type == 'w':
        print() # PLACEHOLDER -- CHANGE THIS
    else:
        print('no') # change this lol
        sys.exit()
    return key

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

deck = []
key = getKey(key_type, key_inp)
#print(key)
numCards = len(key)
for i in range(numCards):
    deck.append(Card(key[i]))
    
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
