print("Welcome to the Citizen Kiosk")
def citizenDetails():
    citizen = input('What is your name?')
    print('Your name is: ' +citizen)
    age = int(input('What is your age?'))
    print(f'You are {age} years old')
    city = input('Which city are you from? ')
    print('You live in ' +city)
    return 
answer = input('Do you want to add a new citizen? Y/N:')
if (answer.upper() == 'Y'):
    citizenDetails()
elif (answer.upper()!= 'N'):
    print("incorrect option")
else:
    print('Thank you!')

