
birthdays = {
"22 nov": ["Bob Bernt", "Mathias"],
"10 des": "Elle",
"31 okt": ["Aragusta", "Carina"],
"12 jan": "Silje",
"23 okt": "Willy",
"5 jul": ["Martin", "Øystein"],
"11 mar": "Miriam"
}
def add_birthday_to_date(date, name):
    try:
        birthdays[date].append(name)
    except AttributeError:
        listkey = []
        listkey.append(birthdays[date]), listkey.append(name)
        birthdays.pop(date)
        birthdays[date] = listkey
    except KeyError:
        birthdays[date] = name


add_birthday_to_date("12 jan", "Sindre")
add_birthday_to_date("9 feb", "Lillian")
print(birthdays)
