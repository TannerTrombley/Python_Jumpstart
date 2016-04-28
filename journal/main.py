from journal import journal


def main():
    print_header()
    run_event_loop()

def print_header():
    print('-------------------------')
    print('      Journal App')
    print('-------------------------')

def run_event_loop():

    # load the command mapping
    command_functions = {
        'l': list_entries,
        'a': add_entry,
        'e': edit_entry,
        'x': lambda: None
    }

    #Choose which journal to open
    open_journal()

    cmd = None

    # Run the loop until the user enters x
    while cmd != 'x':
        cmd = input('[L]ist entries, [A]dd an entry, E[x]it: ').lower().strip()

        result = command_functions.get(cmd)
        if not result:
            print('Invalid command.', end='\n', flush=True)
        result()

    print('Done')


def open_journal():
    pass


def list_entries():
    print('list')


def add_entry():
    print('add')


def edit_entry():
    pass


if __name__ == '__main__':
    main()