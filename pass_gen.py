import string
from secrets import choice



a1 = string.ascii_lowercase
a2 = string.ascii_uppercase
a3 = string.digits
a4 = string.punctuation

defense = ['Bad', 'Normal', 'Good', 'Perfect']

def generate(activity, password= '', num_char= 10, isup= True, isspec_char= True, isnum= True):
    if activity == 'GenPass':
        while True:
            password = ''.join(choice(a1 + a2 * isup + a3 * isnum + a4 * isspec_char) for i in range(num_char))
            if (any(c.islower() for c in password)
                    and any(c.isupper() for c in password) == isup
                    and (sum(c.isdigit() for c in password) >= 3) == isnum
                    and any(c in a4 for c in password) == isspec_char):
                break
        return password
    elif activity == 'PassTest':
        if type(password) == str:
            count = 0
            if any(c.islower() for c in password): count += 1
            if any(c.isupper() for c in password): count += 1
            if sum(c.isdigit() for c in password) >= 3: count += 1
            if any(c in a4 for c in password): count += 1
            return defense[count-1]
        else:
            try:
                count_array = []
                for i in password:
                    count = 0
                    if any(c.islower() for c in i): count += 1
                    if any(c.isupper() for c in i): count += 1
                    if sum(c.isdigit() for c in i) >= 3: count += 1
                    if any(c in a4 for c in i): count += 1
                    count_array.append(defense[count-1])
                return count_array
            except:
                return 'Unexpected format'







# Ниже представлен блок по генерации 30 разных паролей и записи их в файл 'testpass.txt'
password = ''
for i in range(10):
    password += generate('GenPass', num_char= 20, isup= True, isspec_char= True, isnum= True) + '\n'


for i in range(10):
    password += generate('GenPass', num_char= 17, isup= False, isspec_char= True, isnum= True) + '\n'


for i in range(10):
    password += generate('GenPass', num_char= 15, isup= False, isspec_char= False, isnum= False) + '\n'


with open('testpass.txt', 'w') as file:
            file.write(password)
            file.close()





# Ниже представлен блок по тестированию 30 разных паролей из файла 'testpass.txt'
password_array = []
with open('testpass.txt', 'r') as file:
    for line in file:
        password_array.append(line)
    file.close()

count_array = '\n'.join(generate('PassTest', password_array))
print(count_array)
