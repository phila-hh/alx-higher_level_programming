#!/usr/bin/python3
diff = 32
char_ascii = 122
for i in range(26):
    print("{}".format(chr(char_ascii)), end="")
    diff *= -1
    char_ascii += diff - 1
