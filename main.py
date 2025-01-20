from modules.transfer import start_transfer


def main():
    # Спрашиваем пользователя, хочет ли он начать раскидку баланса и сохраняем ответ в переменную choice
    choice = input("Начать раскидку баланса? [Y/N]: ")

    # Если пользователь ответил "YES" или "Y" (в любом регистре), то запускаем функцию start_transfer
    if choice.upper() in ["YES", "Y"]:
        start_transfer()
    else:
        print("Выход...")
        exit()


if __name__ == "__main__":
    main()
