from replit import db
import getpass

keys = db.keys()


def clear():
  print("\033c", end="")


def cont():
  input("\n[Enter]\n")
  clear()


def line():
  return '+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+='

def title(name=''):
  clear()
  print(f'STUDENT GRADES PORTAL {name}\n{line()}\n')


def calc_avg(lst: list) -> float:
  k = 0
  for i in lst:
    k += float(i)
  k /= len(lst)

  return round(k, 2)


find_grade = lambda s: {
  96.67 <= s: ('A+', 4.0),
  93.33 <= s < 96.67: ('A', 4.0),
  90 <= s < 93.33: ('A-', 3.7),
  86.67 <= s < 90: ("B+", 3.3),
  83.33 <= s < 86.67: ("B", 3.0),
  80 <= s < 83.33: ("B-", 2.7),
  76.67 <= s < 80: ("C+", 2.3),
  73.33 <= s < 76.67: ("C", 2.0),
  70 <= s < 73.33: ("C-", 1.7),
  66.67 <= s < 70: ("D+", 1.3),
  60 <= s < 66.67: ("D", 1.0),
}.get(True, ("F", 0.0))

# print(db["Joshua"]["subjects"]["Math"][])
# exit(0)
#
# for i in keys:
#   del db[i]

# print(keys)
# exit(0)

log_in_phase = False
while True:
  while log_in_phase != True:
    title()
    print("Type 1 to create an account\nType 2 to get the list of users")
    username = input("Input your username: ")
    if username == '1':
      title()
      username = input("Create a username: ")
      if username in keys:
        print("Username taken.")
        cont()
      else:
        password = getpass.getpass("Enter your password: ")
        conf_password = getpass.getpass("Confirm your password: ")

        if password == conf_password:
          db[username] = {}
          db[username]["password"] = password
          db[username]["subjects"] = {}
          print("User successfully created.")
          exit()
        else:
          print("\nPasswords do not match. Try again.")
          cont()
    elif username in keys:
      password = getpass.getpass("Input your password: ")
      if password == db[username]["password"]:
        print("Successfully logged in.")
        cont()
        log_in_phase = True
      else:
        print("Password does not match.")
        cont()
    elif username == '2':
      title()
      x = 1
      for i in keys:
        print(f"{x}) {i}")
        x += 1
      cont()

    else:
      print("\nUser does not exist.")
      cont()

  # view all subjects page
  title(username)
  if len(db[username]["subjects"]) == 0:
    print("You have not added any subjects.\n")

  else:
    x = 1
    for i in db[username]["subjects"]:
      print(f"{x}) {i}")
      x += 1
      print()

    try:
      lst = []
      # gpa = []
      for i in db[username]["subjects"]:
        for s in db[username]["subjects"][i]:
          lst.append(s)
      #     gpa.append(find_grade(float(s))[1])

      # print("\nOverall average:", calc_avg(lst))
      # print("Overall letter grade:", find_grade(calc_avg(lst))[0])
      # print("Overall GPA:", calc_avg(gpa))
      # print()
    except:
      print("Error in calculating grade info.\n")

  print(line())
  print("Type 1 to add a new subject.\nType 2 to delete an already existing subject.")
  if len(db[username]["subjects"]) == 0:
    sub_name = input("Type 1 or 2: ")
  else:
    sub_name = input("Enter a subject name: ")
  if sub_name == '1':
    title(username)
    sub_name = input("Enter the subject name: ")
    db[username]["subjects"][sub_name] = []

  # individual subjects
  elif sub_name in db[username]["subjects"]:
    title(username)

    if len(db[username]["subjects"][sub_name]) == 0:
      print("Not enough data")

    else:
      print("All Scores:\n\t", list(db[username]["subjects"][sub_name]))
      try:
        print("\nAverage:", calc_avg(list(db[username]["subjects"][sub_name])))
        print(
          "Letter Grade:",
          find_grade(calc_avg(list(db[username]["subjects"][sub_name])))[0])
        print(
          "GPA:",
          find_grade(calc_avg(list(db[username]["subjects"][sub_name])))[1])
      except:
        print(
          "\nError in calculating the grade. Try making sure that your scores only contain integers and floats."
        )

    print()
    print(line())
    print("Type 'remove' to remove a score(s)")
    thing = True
    while thing:
      grade = input("Add Scores. Type 'exit' to exit\n ")
      if grade == 'exit':
        thing = False
      elif grade == 'remove':
        while thing:
          a = input("Remove your existing scores: ")
          if a == 'exit':
            thing = False
          elif a in db[username]["subjects"][sub_name]:
            db[username]['subjects'][sub_name].remove(a)
          else:
            print("Not in Scores List.")
      else:
        db[username]["subjects"][sub_name].append(grade)

  elif sub_name == '2':
    title(username)
    choice = input("Enter a subject name to remove: ")
    if choice in db[username]["subjects"]:
      del db[username]["subjects"][choice]
    else:
      print("Error")
