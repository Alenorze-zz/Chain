import os
import json



def write_block(name, amount, to_whom, hash=''):
    
    blockchain_dir = os.curdir + '/blockchain/' #./blockchain/test

    files = os.listdir(blockchain_dir)
    files = sorted([int(i) for i in files])

    last_file = files[-1]

    data = {'name': name,
            'amount': amount,
            'to_whom': to_whom,
            'hash': prev_hash}
    with open(blockchain_dir + 'test', 'w') as file:
        json.dump(data, file, indent=4, ensure_ascii=False)


def main():
    write_block(name='Klossy', amount='22', to_whom='Me')

if __name__ == '__main__':
    main()
