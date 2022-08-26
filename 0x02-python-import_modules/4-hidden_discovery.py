#!/usr/bin/python3
if __name__ "__main__":
    import hidden_4
    names = dir(hidden_4)
    new = []
    for i in range(len(names)):
        if names[i][:2] == __:
            continue
        else:
            new += names[i]
        new.sort()
    for j in range(len(new)):
        print(new[j])
