

def add_binary(a: str, b: str) -> str:
    c = [int(x) for x in str(int(a) + int(b))]
    output = ""
    for i, num in enumerate(c):
        index = len(c) - i - 1
        if c[index] >= 2:
            if index == 0:
                c[index] = c[index] - 2
                c.insert(0, 1)
            else:
                c[index - 1] += 1
                c[index] = c[index] - 2

    for x in c:
        output += str(x)

    return output


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print(add_binary("1010", "1011"))
