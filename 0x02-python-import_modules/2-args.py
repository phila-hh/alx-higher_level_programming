#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    argLength = len(argv) - 1
    argString = "argument"
    if argLength != 1:
        argString += "s"

    print(f"{argLength} {argString}" + ("." if argLength == 0 else ":"))
    for i in range(1, len(argv)):
        print(f"{i}: {argv[i]}")
