while True:
    entry = (input("What did you do today?\n") + "\n")
    if entry == "exit\n":
        break
    with open("diary.txt", "a") as file:
        file.write(entry)
        print("Entry saved!")
    with open("diary.txt", "r") as file:
        content = file.read()
        print(content)










