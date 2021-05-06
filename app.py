import random


def test(items, numOfItems):
    randNum = random.randint(0, numOfItems)

    print("*Spining* 🟥🟦🟩")
    print(f"The spinner landed on: '{items[randNum]}'")


def Spinner():
    numOfItems = int(
        input("How many times do you want in your the spinner? >_"))
    items = []

    for i in range(0, numOfItems):
        item = input(f"Enter an item ({i}/{numOfItems}): >_")
        items.append(item)

    print(f"Your items: {items}")

    test(items, numOfItems)

    spinAgain = True

    while (spinAgain == True):
        answer = input("Do you want to spin again[y/n]: ")

        if (answer == "y"):
            spinAgain = True
            test(items, numOfItems)
        else:
            spinAgain = False


Spinner()
