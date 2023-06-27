#     Создать телефонный справочник с возможностью импорта и экспорта данных в формате csv.
# Доделать задание вебинара и реализовать Update, Delete
# Информация о человеке: Фамилия, Имя, Телефон, Описание
# Корректность и уникальность данных не обязательны.
# Функционал программы
# 1) телефонный справочник хранится в памяти в процессе выполнения кода.
# Выберите наиболее удобную структуру данных для хранения справочника.
# 2) CRUD: Create, Read, Update, Delete
# Create: Создание новой записи в справочнике: ввод всех полей новой записи, занесение ее в справочник.
# Read: он же Select. Выбор записей, удовлетворяющих заданном фильтру:
# по первой части фамилии человека. Берем первое совпадение по фамилии.
# Update: Изменение полей выбранной записи. Выбор записи как и в Read, заполнение новыми значениями.
# Delete: Удаление записи из справочника. Выбор - как в Read.
# 3) экспорт данных в текстовый файл формата csv
# 4) импорт данных из текстового файла формата csv
# Используйте функции для реализации значимых действий в программе
# (*) Усложнение.
# Сделать тесты для функций
# Разделить на model-view-controller

# user = ['first_name', 'second_name', 'phone', 'note']
# dictionary = {1:['first_name', 'second_name', 'phone', 'note'], 2:['first_name', 'second_name', 'phone', 'note']}

def input_users()->list:
    user = []
    user.append(input('first_name - '))
    user.append(input('second_name - '))
    user.append(input('phone - '))
    user.append(input('note - '))
    return user

def create(pfone_dir_local:dict, idc:int, user:list)->dict:
    idc +=1
    pfone_dir_local[idc] = user
    return pfone_dir_local, idc

def menu():
    key_count = 0
    phone_dir = dict()
    print('Выберите действие')
    print('Введите 0, если хотите закончить работу')
    print('Введите 1, если хотите ввести пользователя')
    print('Введите 2, если хотите распечатать справочник')
    print('Введите 3, если хотите экспортировать справочник в .txt')
    print('Введите 4, если хотите экспортировать справочник в .csv')
    print('Введите 5, если хотите найти пользователя')
    print('Введите 6, если хотите редактировать справочник')
    print('Введите 7, если хотите удалить запись')
    print('Введите 8, если хотите импортировать справочник')
    while True:
        key = int(input('Выберите действие - '))
        if key == 0:
            break
        if key ==1:
            user = input_users()
            phone_dir, key_count = create(phone_dir,key_count,user)
        if key == 2:
            print(phone_dir)
        if key == 3:
            file_name = input('Выберите имя файла - ')
            export_phone_dir(phone_dir, file_name)
        if key == 4:
            file_name = input('Выберите имя файла - ')
            export_phone_dir1(phone_dir, file_name)  
        if key == 5:
            searching = input('Фамилия пользователя - ')  
            search_user(phone_dir,searching)
        if key == 6:
            searching = input('Фамилия пользователя - ') 
            edit(phone_dir, searching)
        if key == 7:
            searching = input('Фамилия пользователя - ') 
            deleting_entry(phone_dir, searching)
        if key == 8:
           file = input('Введите имя файла - ')
           import_file(phone_dir, file) 
        
def export_phone_dir(phone_dir: dict, file_name: str):
    MAIN_DIR = abspath(dirname(__file__))
    full_name = join(MAIN_DIR, file_name + '.txt')
    with open(full_name, mode='w',encoding='utf-8') as file:
        for idc, user in phone_dir.items():
            file.write(f'{idc},{user[0]},{user[1]},{user[2]},{user[3]}\n')

def export_phone_dir1(phone_dir: dict, file_name: str):
    MAIN_DIR = abspath(dirname(__file__))
    full_name = join(MAIN_DIR, file_name + '.csv')
    with open(full_name, mode='w',encoding='utf-8') as file:
        for idc, user in phone_dir.items():
            file.write(f'{idc},{user[0]},{user[1]},{user[2]},{user[3]}\n')

def import_file(phone_dir: dict, file: str):
    with open(file, 'r', encoding='utf-8') as data:
        phone_dir = data.read()
        print(phone_dir)
    return phone_dir

def search_user(phone_dir: dict, searching: str)->int:
    for idc, user in phone_dir.items():        
        if user[0].startswith(searching):
            print(phone_dir[idc])
    return idc
        
def edit(phone_dir:dict, searching: str)->dict:
    for idc, user in phone_dir.items():        
        if user[0].startswith(searching):
            print(phone_dir[idc])
            user = phone_dir[idc] 
            print('Выберите что изменить')
            print('Введите 0, если хотите закончить редактирование')
            print('Введите 1, если хотите изменить фамилию')
            print('Введите 2, если хотите изменить имя')
            print('Введите 3, если хотите изменить номер телефона')
            print('Введите 4, если хотите изменить примечание')
            while True:
                key = int(input('Выберите действие - '))
                if key == 0:
                    break
                if key == 1:
                    user[0]= input('Фамилия - ')
                    phone_dir[idc] = user
                if key == 2:
                    user[1]= input('Имя - ')
                    phone_dir[idc] = user
                if key == 3:
                    user[2]= input('Номер телефона - ')
                    phone_dir[idc] = user    
                if key == 4:
                    user[3]= input('Примечание - ')
                    phone_dir[idc] = user
                print(phone_dir[idc])
    return phone_dir

def deleting_entry(phone_dir:dict, searching: str)->dict:
    for idc, user in phone_dir.items():        
        if user[0].startswith(searching):
            print(phone_dir[idc]) 
            del(phone_dir[idc]) 
            print(phone_dir)
    return phone_dir
    




from os.path import join, abspath, dirname
menu()
