import csv

print("Welcome to the Citizen Kiosk")
def citizenDetails():
    citizen = input('What is your name?')
    print('Your name is: ' +citizen)
    age = int(input('What is your age?'))
    print(f'You are {age} years old')
    city = input('Which city are you from? ')
    print('You live in ' +city)
    citizen_dict = {'name': citizen, 'age': age, 'city':city}
    with open('data/citizens.csv','a',newline='') as f:
        fieldNames = ['name','age','city']
        writer = csv.DictWriter(f,fieldnames=fieldNames)
        writer.writeheader()
        writer.writerow(citizen_dict)
    return citizen_dict
print(citizenDetails())
answer = input('Do you want to add a new citizen? Y/N:')
if (answer.upper() == 'Y'):
    citizenDetails()
    # print(citizenDetails)
elif (answer.upper()!= 'N'):
    print("incorrect option")
else:
    print('Thank you!')

# my_file = open('greeting.txt','r') #w, a
# print(my_file.read(10))
# print(my_file.readline())
# print(my_file.readline())

# line_by_line = my_file.readlines()
# line_by_line1 = my_file.read().splitlines()
# print('readlines: ',line_by_line)
# print('splitlines: ',line_by_line1)
# my_file.close()


#without closing file(context manager)
# with open('friends.csv','r') as f:
#     print(f.read())
#     friends = f.read().splitlines()
#     print(friends)
#     for friend in friends:
#         friend = friend.split(',')
#         name = friend[0]
#         year = int(friend[1].strip())
#         print(f'In 2030 {name} will be {2030 -year} years old')