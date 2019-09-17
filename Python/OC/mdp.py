import hashlib
from getpass import getpass

secret_word = getpass('Secret word: ')
print('Your secret word is `%s`' % secret_word)

def list_all_available_crypted_pass():
    available_algorithms = hashlib.algorithms_guaranteed
    available_algorithms = list(available_algorithms)

    print('\n\n' + repr(available_algorithms) + '\n')

    for algorithm in available_algorithms:
        hash_algorithm = getattr(hashlib, algorithm)
        crypted_pass = hash_algorithm(secret_word.encode())

        try:
            print('`{clear_pass}` {algo} cipher: `{hashed}`({lenght})'.format(
                clear_pass=secret_word,
                algo='\x1b[32m' + algorithm + '\x1b[0m',
                hashed=crypted_pass.hexdigest(),
                lenght=len(crypted_pass.hexdigest()),
            ))
        except Exception as e:
            print('Cannot print crypted pass for \x1b[31m%s\x1b[0m' % algorithm)
            print(str(e) + '\n')
            pass

list_all_available_crypted_pass()
