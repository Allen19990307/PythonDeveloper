if __name__ == '__main__':
    with open("text.txt") as file:
        for item in file:
            # print(item)
            print(item.split("//")[1])