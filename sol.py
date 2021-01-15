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

deck = getKey(key_type, key_inp)

keystream = []

def get_keystream_val(deck):
    done = False
    while not done:
        # move card 53 down by one place
        pos1 = deck.index(53)
        if pos1 != 53:
            pos2 = pos1 + 1
        else:
            pos2 = 1 # last card becomes second card
        deck[pos1], deck[pos2] = deck[pos2], deck[pos1]

        # move card 54 down by two places
        pos1 = deck.index(54)
        if pos1 != 52:
            pos2 = (pos1 + 2) % 54
        else:
            pos2 = 2 # last card becomes third card
        deck[pos1], deck[pos2] = deck[pos2], deck[pos1]

        # triple cut

        # count cut

        # return keystream value
        topcard = deck[0]
        if topcard == 54:
            topcard = 53
        if deck[topcard] != 53 and deck[topcard] != 54:
            keystream_val = topcard
            done = True
    return keystream_val

for i in range(len(text)):
    keystream.append(get_keystream_val(deck))

nums = []
for i in range(len(text)):
    nums.append((toNum(text)[i] + keystream[i]) % 26)

def toAlpha(num):
    result = ''
    for i in num:
        result += chr(i + 64)
    return result

print(toAlpha(nums))
