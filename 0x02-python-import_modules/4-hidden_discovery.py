#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    names = dir(hidden_4)

    names.sort()
    for n in names:
        startsWith = n[:2]
        if startsWith != "__":
            print(f"{n}")
