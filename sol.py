import sys

text = sys.argv[1].upper()
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
    #elif key_type == 'w':
        #print() # PLACEHOLDER -- CHANGE THIS
    else:
        print('Invalid input. Please try again with a valid input.')
        sys.exit()
    return key

# ABC --> [1,2,3]
def toNum(text):
    result = []
    for i in text:
        result.append(ord(i) - 64)
    return result

# [1,2,3] ---> ABC
def toAlpha(num):
    result = ''
    for i in num:
        if i == 0:
            i = 26
        result += chr(i + 64)
    return result

#create the deck based on the key
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
        if pos1 < 52:
            pos2 = pos1 + 2
        elif pos1 == 52:
            pos2 = 1 # second to last card becomes second card
        else:
            pos2 = 2 # last card becomes third card
        deck[pos1], deck[pos2] = deck[pos2], deck[pos1]

        # triple cut
        # find first joker + everything above it, second joker + everything below it
        # exchange last third and first third
        pos1 = min(deck.index(53), deck.index(54))
        pos2 = max(deck.index(54), deck.index(53))
        first_sec = deck[0:pos1]
        middle_sec = deck[pos1:pos2+1]
        last_sec = deck[pos2+1:]
        deck = last_sec + middle_sec + first_sec

        # count cut
        val_last = deck[-1]
        #if either joker, value is 27
        if val_last = 28:
            val_last = 27
        first_sec = deck[0:val_last]
        second_sec = deck[val_last:-1]
        last_num = deck[-1]
        deck = second_sec + first_sec + [last_num]

        # return keystream value
        topcard = deck[0]
        if topcard == 54 or topcard == 53:
            topcard = 27
        if deck[topcard] != 53 and deck[topcard] != 54:
            keystream_val = deck[topcard]
            done = True
    return keystream_val, deck

for i in range(len(text)):
    keystream_val, deck = get_keystream_val(deck)
    keystream.append(keystream_val)

nums = [(toNum(text)[i] + keystream[i]) % 26 for i in range(len(text))]

print(toAlpha(nums))
