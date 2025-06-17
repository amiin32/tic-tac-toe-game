import pvp
import mid_ai
import smart_ai
def main():
    while True:
        print("==== TIC TAC TOE GAME ====")
        print("1. Player Vs Player (PVP)")
        print("2. Player Vs AI (PVAi)")
        print("3. Quit")

        userChoice = input("Enter your choice: ")

        if userChoice == "1":
            pvp.start_game()
        elif userChoice == "2":
            print("1. Medium Ai")
            print("2. Smart Ai")
            aichoice = int(input("Enter your choice: "))
            if aichoice == 1:
                mid_ai.start_game()
            elif aichoice == 2:
                smart_ai.start_game()
        elif userChoice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")
            exit()

main()
