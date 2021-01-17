import sys
import sol

if len(sys.argv) < 4:
   print("Invalid input. Please try again with a valid input.")
   sys.exit()

verbose = False
text = sys.argv[1].upper()
key_type = sys.argv[2] # f for file, o for order, w for keyword
key_inp = sys.argv[3]
if len(sys.argv) == 5:
    if sys.argv[4] == 'v':
        verbose = True

text = sol.makeAlpha(text)

#create the deck based on the key
deck = sol.getKey(key_type, key_inp, verbose)

keystream = []

if verbose:
    print('NOW GENERATING KEYSTREAM:')

for i in range(len(text)):
    keystream_val, deck = sol.get_keystream_val(deck, verbose)
    keystream.append(keystream_val)

if verbose:
    print('DONE GENERATING KEYSTREAM! \n')
    print('YOUR KEYSTREAM IS: ' + str(keystream))

#DECRYPT:
nums = [(sol.toNum(text)[i] - keystream[i]) % 26 for i in range(len(text))]

if verbose:
    print('YOUR DECRYPTED MESSAGE IS: ' + sol.toAlpha(nums))
else:
    print(sol.toAlpha(nums))
