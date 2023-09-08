names = ['Jenny', 'Adam', 'Cristina', 'Arturo', 'Izabelle']
numbers = [
  '857-531-7893', '617-258-2462', '502-789-5783', '901-789-7894',
  '278-389-6892'
]
print("press 1 to search by name")
print("press 2 to search by phone number")

search_type = input("Enter 1 or 2: ")

if search_type == '1':
  name_search = input("Search by name: ")
  #checks index of name and prints number from number list with that same index.
  if names.count(name_search):
    index = names.index(name_search)
    print(numbers[index])
# adds new contact + phone number
  else:
    print("contact not found")
    add_name = input("Enter new contact name: ")
    add_number = input("Enter new contact number: ")

    names.append(add_name)
    numbers.append(add_number)
    print(names)
    print(numbers)
#search by phone number
elif search_type == '2':
  number_search = input("Search by phone number: ")
  if numbers.count(number_search):
    number_index = numbers.index(number_search)
    print(names[number_index])
    
  elif numbers.count(number_search) == 0:
    print("phone number not found, please search by name instead.")

else:
  str(search_type)
  print("sorry, I do not understand, please try again.")
