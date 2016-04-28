from datetime import date


def main():
    print_header()
    birth_date = get_birthday()
    days_between = compute_days_between_dates(birth_date, date.today())
    print_birthday_info(days_between)


def print_header():
    print('---------------------------')
    print('       Birthday App')
    print('---------------------------')


def get_birthday():
    while True:
        try:
            year = int(input('Enter Birth Year [yyyy]: '))
            month = int(input('Enter Birth Month [mm]: '))
            day = int(input('Enter Birth Day [dd]: '))

            birthday = date(year, month, day)

        except ValueError:
            print("Invalid date\n")
            continue
        else:
            return birthday


def compute_days_between_dates(birth_date, now):
    if birth_date < now:
        birth_date = birth_date.replace(year=now.year)
    return (birth_date - now).days


def print_birthday_info(days_between):
    if days_between > 0:
        print("Only {} days until your birthday!".format(days_between))
    elif days_between < 0:
        print("Your birthday was {} days ago".format(abs(days_between)))
    else:
        print("Happy Birthday!")


if __name__ == '__main__':
    main()
