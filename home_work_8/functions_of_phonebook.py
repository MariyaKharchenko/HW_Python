def show_menu():
    print('1. Распечатать справочник',
        '2. Найти телефон по фамилии',
        '3. Изменить номер телефона',
        '4. Удалить запись',
        '5. Найти абонента по номеру телефона',
        '6. Добавить абонента в справочник',
        '7. Закончить работу', sep = '\n')
    choice=int(input('Введите номер действия: '))
    return choice



def work_with_phonebook():


    choice=show_menu()

    phone_book=read_csv('phonebook.csv')

    while (choice!=7):

        if choice==1:
            print_result(phone_book)
            print()
        elif choice==2:
            last_name=input('lastname ')
            print(find_by_lastname(phone_book,last_name))
            print()
        elif choice==3:
            last_name=input('lastname ')
            new_number=input('new number ')
            print(change_number(phone_book,last_name,new_number))
            print()
        elif choice==4:
            lastname=input('lastname ')
            delete_by_lastname(phone_book,lastname)
            print()
        elif choice==5:
            number=input('number ')
            print(find_by_number(phone_book,number))
            print()
        elif choice==6:
            user_data=input('Введите фамилию, имя, номер телефона и описание абонента через пробел: ')
            add_user(phone_book,user_data)
            write_csv('phonebook.csv',phone_book)
            print()


        choice=show_menu()

def read_csv(filename):

    phone_book=[]

    fields=['Фамилия', 'Имя', 'Телефон', 'Описание']



    with open(filename,'r',encoding='utf-8') as phb:

        for line in phb:

            record = dict(zip(fields, line.split(',')))

        # dict(( (фамилия,Иванов),(имя, Точка),(номер,8928) ))

            phone_book.append(record)

        return phone_book
    
def write_csv(filename , phone_book):

    with open('phonebook.csv','w',encoding='utf-8') as phout:
        for i in range(len(phone_book)):
            s = ''
            for j in phone_book[i].values():
                s += j + ','
            phout.write(f'{s[:-1]}')
                        
def print_result(phone_book):
    for i in phone_book:
        print(i)

def find_by_lastname(phone_book,last_name):
    for i in phone_book:
        if i.get('Фамилия') == last_name:
            res = (f"{i.get('Фамилия')}: {i.get('Телефон')}")
            return res

        
def change_number(phone_book,last_name,new_number):
    for i in phone_book:
        if i.get('Фамилия') == last_name:
            for j in i:
                if j == 'Телефон':
                    i[j] = new_number
                    print(i[j])
                    return i

def delete_by_lastname(phone_book,last_name):
        for i in range(len(phone_book)):
            if last_name in phone_book[i].get('Фамилия'):
                del phone_book[i]
                return print_result(phone_book)
            
def find_by_number(phone_book,number):
    for i in phone_book:
        if i.get('Телефон') == number:
            return i

                
def add_user(phone_book,user_data):
    new_dict = {}
    a = user_data.split()
    new_dict['Фамилия'] = a[0]
    new_dict['Имя'] = a[1]
    new_dict['Телефон'] = a[2]
    new_dict['Описание'] = ' '.join(a[3:])

    phone_book.append(new_dict)
    print(phone_book)

work_with_phonebook()








