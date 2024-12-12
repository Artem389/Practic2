
# Список пользователей
users = []

# Список лекарств
medicines = []

# --- Управление пользователями ---

def register_user():
    """Регистрирует нового пользователя."""
    username = input("Введите имя пользователя: ")
    password = input("Введите пароль: ")
    users.append({'username': username, 'password': password, 'role': 'user', 'history': []})
    print("Пользователь успешно зарегистрирован!")
    # Изменяем роль пользователя на администратора, только если имя пользователя 'admin'
    if username.lower() == 'admin':  # Проверка на регистр
        change_user_role(username, 'admin')

def login():
    """Авторизует пользователя."""
    username = input("Введите имя пользователя: ")
    password = input("Введите пароль: ")
    for user in users:
        if user['username'] == username and user['password'] == password:
            return user
    print("Неверный логин или пароль!")
    return None

def change_password(user):
    """Изменяет пароль пользователя."""
    new_password = input("Введите новый пароль: ")
    user['password'] = new_password
    print("Пароль успешно изменен!")

def change_user_role(username, role):
    """Меняет роль пользователя.  Находит пользователя по имени и меняет его роль."""
    for user in users:
        if user['username'] == username:
            user['role'] = role
            print(f"Роль пользователя {username} изменена на {role}")
            return
    print(f"Пользователь {username} не найден")

# --- Управление лекарствами ---

def add_medicine():
    """Добавляет новое лекарство."""
    medicine = {}
    medicine['Название'] = input("Название лекарства: ")
    medicine['Производитель'] = input("Производитель: ")
    while True:
        try:
            medicine['Цена'] = float(input("Цена: "))
            break
        except ValueError:
            print("Неверный формат цены. Попробуйте ещё раз.")
    while True:
        try:
            medicine['Количество'] = int(input("Количество: "))
            break
        except ValueError:
            print("Неверный формат количества. Попробуйте ещё раз.")
    medicines.append(medicine)
    print("Лекарство добавлено.")

def delete_medicine():
    """Удаляет лекарство."""
    if not medicines:
        print("Список лекарств пуст.")
        return

    print("Текущий список лекарств:")
    for i, medicine in enumerate(medicines):
        print(f"{i+1}. {medicine}")

    while True:
        try:
            index = int(input("Введите номер лекарства для удаления: ")) - 1
            if 0 <= index < len(medicines):
                del medicines[index]
                print("Лекарство удалено.")
                break
            else:
                print("Неверный номер лекарства.")
        except ValueError:
            print("Неверный формат номера. Попробуйте ещё раз.")

def edit_medicine():
    """Редактирует информацию о лекарстве."""
    if not medicines:
        print("Список лекарств пуст.")
        return

    print("Текущий список лекарств:")
    for i, medicine in enumerate(medicines):
        print(f"{i+1}. {medicine}")

    while True:
        try:
            index = int(input("Введите номер лекарства для редактирования: ")) - 1
            if 0 <= index < len(medicines):
                medicine = medicines[index]
                medicine['name'] = input(f"Новое название ({medicine['name']}): ") or medicine['name']
                medicine['manufacturer'] = input(f"Новый производитель ({medicine['manufacturer']}): ") or medicine['manufacturer']
                while True:
                    try:
                        medicine['price'] = float(input(f"Новая цена ({medicine['price']}): "))
                        break
                    except ValueError:
                        print("Неверный формат цены.")
                while True:
                    try:
                        medicine['quantity'] = int(input(f"Новое количество ({medicine['quantity']}): "))
                        break
                    except ValueError:
                        print("Неверный формат количества.")
                print("Лекарство изменено.")
                break
            else:
                print("Неверный номер лекарства.")
        except ValueError:
            print("Неверный формат номера. Попробуйте ещё раз.")

def search_medicine():
    """Ищет лекарства по названию или производителю."""
    search_term = input("Введите поисковый запрос: ").lower()
    results = [med for med in medicines if search_term in med['name'].lower() or search_term in med['manufacturer'].lower()]
    if results:
        print("Найденные лекарства:")
        for medicine in results:
            print(medicine)
    else:
        print("Лекарства не найдены.")

def sort_medicines():
    """Сортирует лекарства по заданному критерию."""
    sort_by = input("Сортировать по (Название/Цена/Производитель): ").lower()
    reverse = input("Обратный порядок? (Да/Нет): ").lower() == 'Да'

    try:
        if sort_by == 'Название':
            medicines.sort(key=lambda x: x['Название'], reverse=reverse)
        elif sort_by == 'Цена':
            medicines.sort(key=lambda x: x['Цена'], reverse=reverse)
        elif sort_by == 'Производитель':
            medicines.sort(key=lambda x: x['Производитель'], reverse=reverse)
        else:
            print("Неверный параметр сортировки.")
            return

        print("Отсортированный список лекарств:")
        for medicine in medicines:
            print(medicine)

    except Exception as e:
        print(f"Ошибка при сортировке: {e}")


def show_medicine_catalog():
    """Выводит каталог лекарств."""
    if medicines:
        for medicine in medicines:
            print(medicine)
    else:
        print("Список лекарств пуст.")



# --- Главный цикл ---

def main():
    """Главная функция приложения."""
    logged_in_user = None  # Переменная для отслеживания авторизованного пользователя

    while True:
        if logged_in_user is None:  # Главное меню (до авторизации)
            print("\nГлавное меню:")
            print("1. Регистрация")
            print("2. Вход")
            print("3. Выход")
            choice = input("Выберите действие: ")

            if choice == '1':
                register_user()
            elif choice == '2':
                logged_in_user = login()  # После успешного входа, logged_in_user будет содержать данные пользователя
            elif choice == '3':
                break
            else:
                print("Неверный выбор.")
        else:
            if logged_in_user['role'] == 'admin':
                # Меню администратора
                while True:
                    print("\nМеню администратора:")
                    print("1. Добавить лекарство")
                    print("2. Удалить лекарство")
                    print("3. Редактировать лекарство")
                    print("4. Поиск лекарства")
                    print("5. Сортировка лекарств")
                    print("6. Просмотреть каталог лекарств")
                    print("7. Выйти")
                    choice = input("Выберите действие: ")
                    if choice == '1':
                        add_medicine()
                    elif choice == '2':
                        delete_medicine()
                    elif choice == '3':
                        edit_medicine()
                    elif choice == '4':
                        search_medicine()
                    elif choice == '5':
                        sort_medicines()
                    elif choice == '6':
                        show_medicine_catalog()
                    elif choice == '7':
                        logged_in_user = None  # Выход из меню администратора
                        break
                    else:
                        print("Неверный выбор.")
            else:  # Меню пользователя
                # Меню пользователя
                while True:
                    print("\nМеню пользователя:")
                    print("1. Просмотреть каталог лекарств")
                    print("2. Поиск лекарства")
                    print("3. Сортировка лекарств")
                    print("4. Изменить пароль")
                    print("5. Выйти")
                    choice = input("Выберите действие: ")
                    if choice == '1':
                        show_medicine_catalog()
                    elif choice == '2':
                        search_medicine()
                    elif choice == '3':
                        sort_medicines()
                    elif choice == '4':
                        change_password(logged_in_user)
                    elif choice == '5':
                        logged_in_user = None  # Выход из меню пользователя
                        break
                    else:
                        print("Неверный выбор.")

if __name__ == "__main__":
    main()
