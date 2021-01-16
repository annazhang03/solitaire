# Solitaire Cipher
#### by Grace Cantarella and Anna Zhang

## Description
This is our repo containing our Python implementation of the Solitaire cipher. This cipher is traditionally carried out through non-electronic means—the message is encrypted and decrypted using a deck of cards.

## Launch

### Encryption:
```
[makefile details to be added]

to encrypt using a key from a file:
make encrypt [text] f [filename]
#example: make encrypt 'hello' f yes.txt

to encrypt using a predetermined order:
make encrypt [text] o [order]
#example: make encrypt 'hello' f '0 54 1 53 2 52 3 51 4 50 5 49 6 48 7 47 8 46 9 45 10 44 11 43 12 42 13 41 14 40 15 39 16 38 17 37 18 36 19 35 20 34 21 33 22 32 23 31 24 30 25 29 26 28 27'

to encrypt using a plaintext keyword:
make encrypt [text] w [keyword]
#example: make encrypt 'hello' w 'yes'
```

### Decryption:
```
to decrypt using a key from a file:
make decrypt [text] f [filename]
#example: make decrypt 'goodbye' f no.txt

to decrypt using a predetermined order:
make decrypt [text] o [order]
#example: make decrypt 'goodbye' f '0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53 54'

to decrypt using a plaintext keyword:
make decrypt [text] w [keyword]
#example: make decrypt 'goodbye' f 'no'

```

 ## Citations
