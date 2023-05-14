'''
find_user("Colt", "Steele") # 1
find_user("Alan", "Turing") # 3
find_user("Not", "Here") # 'Not Here not found.'
'''
import csv

def find_user(first_name, last_name):
    with open('users.csv') as file:
        csv_reader = list(csv.reader(file))
        user = [first_name, last_name]
        if user not in csv_reader:
            return(f'{first_name} {last_name} not found.')
        else:
            return(csv_reader.index(user))
            

print(find_user("Colt", "Steele"))
print(find_user("Alan", "Turing"))
print(find_user("Not", "Here"))