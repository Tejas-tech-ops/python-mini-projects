# Rock Paper Scissors ASCII Art
import random
print("Press 1 for Rock\nPress 2 for Paper\nPress 3 for Scissors")
n = int(input())

if n==1:
    print("Player choses")
    print("""
            _______
        ---'   ____)
              (_____)
              (_____)
              (____)
        ---.__(___)
        """)
elif n==2:
    print("Player choses")
    print("""
             _______
        ---'    ____)____
                   ______)
                  _______)
                 _______)
        ---.__________)
        """)
else:
    print("Player choses")
    print("""
            _______
        ---'   ____)____
                  ______)
               __________)
              (____)
        ---.__(___)
        """)
random_hand_sign = random.randint(1,3)
# Rock
if random_hand_sign == 1:
    print("Computer choses")
    print("""
        _______
    ---'   ____)
          (_____)
          (_____)
          (____)
    ---.__(___)
    """)

# Paper
elif random_hand_sign == 2:
    print("Computer choses")
    print("""
         _______
    ---'    ____)____
               ______)
              _______)
             _______)
    ---.__________)
    """)

# Scissors
else:
    print("Computer choses")
    print("""
        _______
    ---'   ____)____
              ______)
           __________)
          (____)
    ---.__(___)
    """)

if n==random_hand_sign:
    print("Draw")
elif n==1 and random_hand_sign==2:
    print("Computer Wins")
elif n==2 and random_hand_sign==1:
    print("Player Wins")
elif n==1 and random_hand_sign==3:
    print("Player Wins")
elif n==3 and random_hand_sign==1:
    print("Computer Wins")
elif n==2 and random_hand_sign==3:
    print("Computer Wins")
elif n==3 and random_hand_sign==2:
    print("Player wins")
else:
    print("You entered wrong number")
