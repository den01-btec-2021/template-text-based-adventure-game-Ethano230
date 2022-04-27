import time

def main():
    print("Welcome to my game")
    player_name = input ("What is your name? ")
    print ("Hi " + player_name)

    Lives = 3
    print(f"You have {Lives} lives remaining") 
    backpack = [] # initialise empty list for backpack

    while True:
        direction = input("Which direction do you want to go? ")

        if direction == "North":
          puzzle ="What is 4+4 ? "
          puzzle_solution = "8"
          key_number = 1
          in_room(backpack,Lives,direction,puzzle,puzzle_solution,key_number)

        elif direction == "South":
          puzzle ="What is 5*5 ? "
          puzzle_solution = "25"
          key_number = 1
          in_room(backpack,Lives,direction,puzzle,puzzle_solution,key_number)
         
        elif direction == "East":
          puzzle ="What is 60/5 ? "
          puzzle_solution = "12"
          key_number = 1
          in_room(backpack,Lives,direction,puzzle,puzzle_solution,key_number)

        elif direction("West"):
          puzzle ="What is 100-50 ? "
          puzzle_solution = "50"
          key_number = 1
          in_room(backpack,Lives,direction,puzzle,puzzle_solution,key_number)
        else:
         print("Sorry not recognised")

         # if backpack is full open door win game
         if ("Key 1" in backpack) and ("Key 2" in backpack) and ("Key 3" in backpack) and ("Key 4" in backpack):
             print("You have unlocked the door. Victory!")

        if Lives == 0:
            print("Sorry, you have failed!") 
            exit()

def in_room(backpack,Lives,direction,puzzle,puzzle_solution,key_number):
  print(f"You went {direction}, Timer has begun. You have 5 seconds to solve the puzzle! ") 
  # start the timer
  time_elapsed = time.time()
  #if 5 seconds has passed lost life

  puzzle_guess = input(puzzle)
  if puzzle_guess == puzzle_solution:
    print(f"Correct Key {key_number}collected")
    backpack.append(f"Key {key_number}")
  else:
    Lives -= 1
    print(f"Incorrect, You now have {Lives} lives remaining")




main()
