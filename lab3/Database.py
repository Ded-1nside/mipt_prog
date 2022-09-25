import csv

group_list = ("б03-101", "б03-102", "б03-103", "б03-104", "б03-105", "б03-106", "б03-107", "б03-108")

def add_student(table):
    try:
        entry = check_entry(input("Введите ФИО, курс и группу: ").strip())
        table.append(entry)
    except Exception as e:
        print(e.args[0])


def remove_student(table):
    name = tuple(input("Введите ФИО студента: ").strip().split())
    try:
        table.pop(table.index(next(x for x in table if x[:3] == name)))
    except StopIteration:
        print("Студент не найден!")


def list_of_group(table, args):
    try:
        group = args[1]

        for entry in table:
            if entry[-1].lower() == group:
                print(" ".join(entry))
    except IndexError:
        print("Укажите группу!")


def find_student(table, args):
    try:
        second_name, name = args[2], args[3]

        for entry in table:
            if second_name == entry[0].lower() and name == entry[1].lower():
                print(" ".join(entry))
    except IndexError:
        print("Укажите фамилию и имя студента.")


def check_entry(entry):
    entry = entry.split()

    try:
        course, group = entry[3], entry[4]
        if not ( float(course).is_integer() and 1 <= int(course) <= 6 ):
            raise ValueError("Недопустимый номер курса!")
        if group.lower() not in group_list:
            raise ValueError("Недопустимая группа!")
    except IndexError:
        raise ValueError("Требуемый формат записи: ФИО, номер курса, группа")

    return tuple(entry)


def save_data(f, table):
    f.seek(0)
    f.truncate()
    writer = csv.writer(f)
    writer.writerows(table)
    f.close()
    return open(f.name, "r+", encoding="utf8")



def end(cur_file, db):
    print("\nСохранение изменений...")
    cur_file = save_data(cur_file, db)
    cur_file.close()
    print("Выход")
    exit()


def main_loop(f, table):
    while True:
        try:
            cmd = input("Введите команду: ").strip().lower()
            if cmd == "сохранить изменения":
                f = save_data(f, table)
            elif cmd == "добавить студента":
                add_student(table)
            elif cmd == "удалить студента":
                remove_student(table)
            elif cmd.startswith("группа"):
                list_of_group(table, cmd.split())
            elif cmd.startswith("найти студента"):
                find_student(table, cmd.split())
            elif cmd in ("выход", "выйти"):
                end(f, table)
            else:
                print("Неизвестная команда!")
        except KeyboardInterrupt:
            end(f, table)


def reader(f):
    db = []
    success = True
    
    for i, row in enumerate(csv.reader(f)):
        try:
            db.append(check_entry(" ".join(row)))
        except Exception as e:
            print(f"При чтении файла на строке {i+1} возникла ошибка:")
            print(e.args[0])
            success = False
            break

    return db if success else None


def starter(f):
    db = reader(f)
    if db is not None:
        main_loop(f, db)
    exit() 


def opener():
    path = input("Укажите путь к файлу базы данных: ")
    success = False
    db_file = None
    try:
        db_file = open(path, "r+", encoding="utf8")
        success = True
    except FileNotFoundError:
        print("По указанному пути файл базы данных не найден!")
    except PermissionError:
        print("Доступ к файлу базы данных запрещён!")
    except:
        print("Неизвестная ошибка при открытии файла базы данных!")
    else:
        starter(db_file)
    finally:
        if not success:
            choose(path)


def create_file(path):
    try:
        db_file = open(path, "x", encoding="utf8")
    except FileExistsError:
        print("Такой файл уже существует!")
    except PermissionError:
        print("Недостаточно прав для создания файла!")
    except:
        print("Неизвестная ошибка при создании файла!")
    else:
        print(f"Файл {path} создан.")
        db_file = open(db_file.name, "r+", encoding="utf8")
        starter(db_file)


def choose(path):
    print("""Выберите:
    1) Ввести другой путь
    2) Создать по указанному пути пустой файл базы данных""")
    try:
        ans = int(input())

        if ans == 1:
            opener()
        elif ans == 2:
            create_file(path)
        else:
            raise ValueError
    except ValueError:
        print("Введите число 1 или 2!")


opener()