
# imports random module
import random

def printMainMenu():
    optionSelected = ""
    options = ["i", "p", "q"]
    while True:
        menu = "Golf!\n(I)nstructions\n(P)lay round\n(Q)uit"
        print(menu)
        optionSelected = input().lower()
        if optionSelected == "i":
            return optionSelected
        elif optionSelected == "p":
            return optionSelected
        elif optionSelected == "q":
            return optionSelected
        else:
            print("Invalid menu choice.")
            print("Let's play golf, CP1401 style!")
    return optionSelected

def inputPar():
    while True:
        par = int(input("Choose a par for this course (between 3-5 inclusive) "))
        if (3 <= par) and (par <= 5):
            return par
        else:
            print(
                "I’m sorry, you must choose a number between 3-5 inclusive. Please enter again.")
    return par

def inputMetersToHole():
    while True:
        # validation Required
        metersToHole = int(
            input("How many meters to the hole (between 195 – 250 inclusive) "))
        if (195 <= metersToHole) and (metersToHole <= 250):
            return metersToHole
        else:
            print(
                "I’m sorry, you must choose a number between 195-250 inclusive. Please enter again.")

    return metersToHole

def printInstructions(metersToHole, par):
	
    print("This is a simple golf game in which each hole is {}m ".format(metersToHole), end="")
    print("game away with par {}. You are able to choose from 3 clubs, the Driver, Iron or Putter.".format(par), end=" ")
    print("The Driver will hit around 100m, the Iron around 30m and the Putter around 10m. The putter is best used very close to the hole.", end=" ")

    print("For each shot, you may use a driver, iron or a putter – each shot will vary in distance.")
    print("The average distance each club can hit is")
    print("Driver = 100m\nIron = 30m\nPutter = 10m")

def playGolf(metersToHole, par):
    distance = metersToHole
    hits = 0
    travelDistance = 0
    print("This hole is a " + str(metersToHole)+"m par " + str(par) + ".")

    while distance > 0:
        checkForBreak = True
        while checkForBreak:
            club = input("You are " + str(distance) + "m from the hole, after " +
                         str(hits) + " shot/s.\n" +
                         "Club selection: press D for Driver, I for Iron, P for Putter.\n" +
                         "Choose club:")
            print()
            club = club.upper()
            club in ["I", "P", "D"]
            checkForBreak = False
        if distance >= 100 and club in ["I", "P"]:
            travelDistance = -1
        if 20 < distance < 100 and club in ["D", "P"]:
            travelDistance = -1
        if distance < 21 and club in ["D", "I"]:
            travelDistance = -1

        if travelDistance < 0:
            hits += 1
            print("Invalid club selection = air swing :(\n" +
                  "Your shot went 0m. You are " + str(distance) +
                  "m from the hole, after " + str(hits) + " shot/s\n")
            travelDistance = 0
        else:
            travelDistance = getShot(distance, club)
            hits += 1
        distance = abs(distance - travelDistance)
        if hits >= 10:
            print("Disappointing. You are" +
                  str(par) + " over par for this hole.")
            return 10
        if distance == 0:
            print("Clunk…After " + str(hits) +
                  " hits your ball is in the hole!")
            if hits == par:
                print("And that's par.")
            elif hits < par:
                print("Congratulations. You are " + str(par - hits) +
                      " under par for this hole.")
            else:
                print("Disappointing. You are " + str(hits - par) +
                      " over par for this hole.")
            return hits

def getShot(holeDistance, cl):
    if cl == "D":
        holeDistance = random.randint(80, 120)
    elif cl == "I":
        holeDistance = random.randint(24, 36)
    elif cl == "P" and holeDistance <= 10:
        holeDistance = random.randint(
            round(0.8 * holeDistance), round(1.2 * holeDistance))
    else:
        holeDistance = random.randint(8, 12)
    print("\nYour ball went " + str(holeDistance) + "m.")
    return holeDistance

def main():
    score = []
    name = input("What is your name? ")
    print("Welcome ", name, ".")
    print("Let's play golf, CP1401 style!")
    par = inputPar()
    metersToHole = inputMetersToHole()
    checkForBreakMain = True
    while checkForBreakMain:
        optionSelected = printMainMenu()
        if optionSelected == "i":
            printInstructions(metersToHole, par)
        elif optionSelected == "p":
            score.append(playGolf(metersToHole, par))
            par_score = sum(score) - 5 * len(score)
            par_abs = abs(par_score)
            if par_score == 0:
                over_und = "on par"
            elif par_score > 0:
                over_und = str(par_abs) + " over par"
            else:
                over_und = str(par_abs) + " under par"
            print("Your overall score is " + str(sum(score)) +
                  " and you are " + over_und + " after " + str(len(score)) +
                  " rounds.")

        elif optionSelected == "q":
            checkForBreakMain = False

    print("Fairwell and thanks for playing " + name + ".", sep="")
    for i in range(len(score)):
        par_score = score[i] - 5
        par_abs = abs(par_score)
        if par_score == 0:
            over_und = "On par."
        elif par_score > 0:
            over_und = str(par_abs) + " over par."
        else:
            over_und = str(par_abs) + " under par"
        print("Round " + str(i + 1) + " : " + str(score[i]) + ". " + over_und)

if __name__ == '__main__':
    main()
