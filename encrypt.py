import sys
import sol

if len(sys.argv) != 4:
   print("Invalid input. Please try again with a valid input.")
   sys.exit()

text = sys.argv[1].upper()
key_type = sys.argv[2] # f for file, o for order, w for keyword
key_inp = sys.argv[3]

text = sol.makeAlpha(text)

#create the deck based on the key
deck = sol.getKey(key_type, key_inp)
keystream = []

for i in range(len(text)):
    keystream_val, deck = sol.get_keystream_val(deck)
    keystream.append(keystream_val)

#ENCRYPT:
nums = [(sol.toNum(text)[i] + keystream[i]) % 26 for i in range(len(text))]

print(sol.toAlpha(nums))
