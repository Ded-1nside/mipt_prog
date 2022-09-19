with open("text1.txt", "r+") as txt:
    for i in range(10):
        txt.write("Я строка текста\n")
    for line in txt:
        print(line)
