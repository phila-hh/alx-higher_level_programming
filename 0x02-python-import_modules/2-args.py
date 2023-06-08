#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    argLength = len(argv) - 1

    print(f"{argLength} arguments" + ("." if argLength == 0 else ":"))
    for i in range(1, len(argv)):
        print(f"{i}: {argv[i]}")
