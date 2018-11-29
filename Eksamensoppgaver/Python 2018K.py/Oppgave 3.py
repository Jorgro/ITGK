#3a)

notebook = {'Facebook': ['Urgle',['pwd1']],
 'reddit': ['urgle',['asdf1234','pwd1']],
'Aftenposten': ['ivrig',['pwdold','pwdnew']]}
def addSite(notebook):
    key = input('Site: ')
    if key in notebook: 
        print('Site already in notebook.')
        return notebook
    username = input('Username: ')
    password = input('Password: ')

    notebook[key] = [username, [password]]
    print(f'Account addet for {key}')
    return notebook

#3b) 
def showSites(notebook):

    print('Nettsted:'.ljust(17) + 'Brukernavn:'.ljust(15) + 'Passord:')

    for key, value in notebook.items():
        site = key[:15] + ':'
        print(f'{site.ljust(17)}{value[0].ljust(15)}{value[1][-1]}')


#3c)
def formatList(list):
    streng = ', '.join(list)
    return streng

#3d)
def editSite(notebook, site):
    
    password = input(f'Add new site password for {site}: ')

    site_info = notebook.get(site)

    if password not in site_info[1]:
        site_info[1].append(password)
        notebook[site] = site_info
        print(f'{site} has been updated with a new password.')
        return notebook
    else:
        print(f"'{password} has already been used for {site}'") 
        print(f'The following passwords have been used: {formatList(site_info[1])}')

        return editSite(notebook, site)

#notebook = {'Facebook': ['Urgle',['pwd1','pwd2']]}
#print(editSite(notebook, 'Facebook'))

#3e)
def secureSites(notebook):
    passwords = []
    password_site = []

    for key, value in notebook.items():
        for i in value[1]:
            passwords.append(i)
            password_site.append(key)
    
    dict_pass = {}
    for i in range(len(passwords)):
        if passwords.count(passwords[i]) > 1:
            if passwords[i] not in dict_pass:
                dict_pass[passwords[i]] = [password_site[i]]
            else:
                dict_pass[passwords[i]].append(password_site[i])
    print(dict_pass)
    if dict_pass:
        for key, value in dict_pass.items():
            print(f"You have used the password '{key}' on the following sites: {formatList(dict_pass[key])}")
    else:
        print('GJ')

notebook = {'Facebook': ['Urgle',['oldpwd', 'pwd1']], \
 'reddit': ['Urgle',['pwd1']]}
secureSites(notebook)
        
