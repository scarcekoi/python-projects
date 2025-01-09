from datetime import datetime

month_map = {
    "January": 1,
    "February": 2,
    "March": 3,
    "April": 4,
    "May": 5,
    "June": 6,
    "July": 7,
    "August": 8,
    "September": 9,
    "October": 10,
    "November": 11,
    "December": 12
}

firstName = input("What is your first name? ").capitalize()
middleName = ""
hasMiddleName = input("Do you have a middle name? Y/N: ").capitalize()

while hasMiddleName not in ['Y', 'N']:
    hasMiddleName = input("Invalid input. Please enter 'Y' for Yes or 'N' for No. "
                          "Do you have a middle name? Y/N: ").capitalize()

if hasMiddleName == "Y":
    middleName = input("What is your middle name: ").capitalize()
    lastName = input("What is your last name: ").capitalize()
else:
    lastName = input("What is your last name: ").capitalize()
name = f"{firstName} {middleName} {lastName}"

birthFormat = input("What time format for your birth date would you prefer? 1. MM/DD/YY, 2. MM/DD/YYYY, 3. DD/MM/YY, or 4. DD/MM/YYYY. (Type 1, 2, 3, or 4): ")

while birthFormat not in ['1', '2', '3', '4']:
    birthFormat = input("Invalid input. Please enter a number between 1 and 4. "
                        "What time format for your birth date would you prefer? 1. MM/DD/YY, 2. MM/DD/YYYY, 3. DD/MM/YY, or 4. DD/MM/YYYY. (Type 1, 2, 3, or 4): ")

birthDay = input("What day were you born: ")
birthMonthNum = 0
birthMonth = input("What month were you born: ").capitalize()

if birthMonth.isdigit():
    birthMonthNum = int(birthMonth)
else:
    while birthMonth not in month_map:
        birthMonth = input("Invalid month. What month were you born in: ").capitalize()
    birthMonthNum = month_map[birthMonth]

birthYear = input("What year were you born: ")
shortBirthYear = str(birthYear)[-2:]
if birthFormat == '1':
    birthDate = f"{birthMonthNum}/{birthDay}/{shortBirthYear}"
elif birthFormat == '2':
    birthDate = f"{birthMonthNum}/{birthDay}/{birthYear}"
elif birthFormat == '3':
    birthDate = f"{birthDay}/{birthMonthNum}/{shortBirthYear}"
elif birthFormat == '4':
    birthDate = f"{birthDay}/{birthMonthNum}/{birthYear}"
else:
    birthDate = f"{birthMonthNum}/{birthDay}/{shortBirthYear}"

while True:
    birthWasCorrect = input(f"Your birthday is {birthDate}, correct? Y/N: ").capitalize()

    if birthWasCorrect == "Y":
        birthDateObj = datetime(int(birthYear), birthMonthNum, int(birthDay))
        today = datetime.now()

        years = today.year - birthDateObj.year
        months = today.month - birthDateObj.month
        days = today.day - birthDateObj.day

        if days < 0:
            months -= 1
            days += (today - datetime(today.year, today.month, 1)).days

        if months < 0:
            years -= 1
            months += 12

        print(f"So you are {name}, born on {birthDate}, aged {years} years, {months} months, and {days} days.")
        break

    elif birthWasCorrect == "N":
        birthDay = input("What day were you born: ")
        birthMonth = input("What month were you born: ").capitalize()
        birthYear = input("What year were you born: ")

        shortBirthYear = str(birthYear)[-2:]
        if birthFormat == '1':
            birthDate = f"{birthMonthNum}/{birthDay}/{shortBirthYear}"
        elif birthFormat == '2':
            birthDate = f"{birthMonthNum}/{birthDay}/{birthYear}"
        elif birthFormat == '3':
            birthDate = f"{birthDay}/{birthMonthNum}/{shortBirthYear}"
        elif birthFormat == '4':
            birthDate = f"{birthDay}/{birthMonthNum}/{birthYear}"

    else:
        print("Invalid input. Please enter 'Y' for Yes or 'N' for No.")