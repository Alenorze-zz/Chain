import os
import json
import hashlib


blockchain_dir = os.curdir + '/blockchain/' #./blockchain/[file]

def get_hash(filename):
    file = open(blockchain_dir + filename, 'rb').read()
    return hashlib.md5(file).hexdigest()

def get_files():
    files = os.listdir(blockchain_dir)
    return sorted([int(i) for i in files])

def check_integrity():

    files = get_files()

    for file in files[1:]:
        f = open(blockchain_dir + str(file))
        h = json.load(f)['hash']

        prev_file = str(file - 1)
        actual_hash = get_hash(prev_file)

        if h == actual_hash:
            res = 'Ok'
        else:
            res = 'Corrupted'
        print("Block {} is: {}".format(prev_file, res))

def write_block(name, amount, to_whom, hash=''):

    files = get_files()
    last_file = files[-1]
    filename = str(last_file + 1)

    prev_hash = get_hash(str(last_file))

    data = {'name': name,
            'amount': amount,
            'to_whom': to_whom,
            'hash': prev_hash}

    with open(blockchain_dir + filename, 'w') as file:
        json.dump(data, file, indent=4, ensure_ascii=False)


def main():
    write_block(name='Klossy', amount='22', to_whom='Me')

if __name__ == '__main__':
    main()
