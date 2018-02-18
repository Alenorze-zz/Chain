import json



def write_block():
    data = {'name': 'Klossy',
            'amount': '22',
            'to_whom': 'Me',
            'hash': '123'}
    with open('test', 'w') as file:
        json.dump(data, file, indent=4, ensure_ascii=False)


def main():
    write_block()

if __name__ == '__main__':
    main()
