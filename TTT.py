isEnd = False


def one(num):
    if num < 5:
        pass
    else:
        global isEnd
        isEnd = True

if __name__ == "__main__":
    for i in range(6):
        one(i)
        print(isEnd)