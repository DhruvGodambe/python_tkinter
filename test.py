def file_to_list():
    file = open('names.txt')
    data = file.read().split()
    return data

def update_file(name_list):
    file = open('names.txt', 'w')
    string = ''
    for l in name_list:
        string += l + " "
    file.write(string)

guests = file_to_list()

inputName = input("Enter guest name: ")

found = False

for name in guests:
    if name == inputName:
        found = True
        break
    
if found:
    print("guest already invited")
    y = input("do you want to remove this guest? (y/n):")
    if y == "y":
        guests.remove(inputName)
        update_file(guests)
else:
    print("guest not invited")
    y = input("do you want to invite this guest? (y/n):")
    if y == "y":
        guests.append(inputName)
        update_file(guests)
