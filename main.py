import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''



get_images = [rock, paper, scissors]


User_input = int(input('what do you choose? Type 0 for Rock, 1 for paper, 2 for scissors '))

User_choice = get_images[User_input]

print(f'You chose: ')
print(get_images[User_input])


Computer_choice = random.randint(0,2)
print('Computer chose:')
print(get_images[Computer_choice])

if User_choice >= 3:
    print('You have typed and invalid Option')
elif User_choice == 0 and Computer_choice == 2:
    print('You won')
elif User_choice == 2 and Computer_choice == 1:
    print('You Won')
else:
    print('you lose')














