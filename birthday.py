firstName = input("What is your first name: ")
hasMiddleName = input("Do you have a middle name? Y/N")
if hasMiddleName == "Y":
    middleName = input("What is your middle name: ")
else:
    lastName = input("What is your last name: ")

birthDay = input("What day where you born: ")
birthMonth = input("What month where you born: ")
birthYear = input("What year where you born: ")

birthWasCorrect = input(f"Your birthday is {birthMonth}/{birthDay}/{birthYear}, correct? Y/N")

if birthWasCorrect == "Y":
    birthFormat = input("What time format would you prefer? 1. MM/DD/YY, 2. MM/DD/YYYY, 3. DD/MM/YY, or 4. DD/MM/YY (Type 1, 2, 3, or 4.)")
else:
    birthDay = input("What day where you born: ")
    birthMonth = input("What month where you born: ")
    birthYear = input("What year where you born: ")