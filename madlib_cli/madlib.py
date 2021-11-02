import re

print("""
***************************************************************************************************
*** this is game for fun will ask you to enter some words and will give back to you a paragraph ***
***************************************************************************************************
""")


def read_template(p):
    with open(p) as f:
        d = f.read()
        return d


def inputs(d):
    inputList = []
    print("   enter this list and dont miss it :   ")
    for x in range(21):
        inputList += [input(f'{d[x]} :')]
    return tuple(inputList)


def parse_template(t):
    d = re.findall(r"\{(.*?)\}", t)
    t = re.sub(r"\{(.*?)\}", '{}', t)
    return [t, tuple(d)]


def merge(a, b):
    return(a.format(*b))


def copyFile(t):
    f = open('assets/result.txt', 'w')
    f.write(t)
    print(t)


if __name__ == "__main__":
    p = 'assets/tamplate.txt'
    a = parse_template(read_template(p))[0]
    b = inputs(parse_template(read_template(p))[1])
    copyFile(merge(a, b))
