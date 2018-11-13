
def main():
    facebook = []
    newuser = ''
    print('Hello, welcome to Facebook. Add a new user by writing "given_name surname age gender relationship_status".')
    while newuser != 'done':
        newuser = input('Add new user: ')
        if newuser == 'done':
            break
        facebook.append(add_data(newuser))
    print('Ok')
    searching = ''
    while searching != 'done':
        searching = input('Search for a user: ')
        if searching == 'done':
            break
        get_person(searching, facebook)


def add_data(string):
    data = string.split()
    data[2] = int(data[2])
    return data



def get_person(given_name, facebook):
    for i in range(len(facebook)):
        if facebook[i][0] == given_name:
            user = facebook[i]
            if user[3].lower() == 'female':
                print(f'{user[0]} {user[1]} is {user[2]} years old, her relationship status is {user[4]}')
            elif user[3].lower() == 'male':
                print(f'{user[0]} {user[1]} is {user[2]} years old, his relationship status is {user[4]}')

main()
