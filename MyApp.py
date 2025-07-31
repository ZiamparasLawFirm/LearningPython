new_member = input("Enter new member name: ")

file = open("members.txt", "r")
members = file.readlines()
file.close()

members.append("\n" + new_member)

file = open("members.txt", "w")
file.writelines(members)
file.close()

print(members)
