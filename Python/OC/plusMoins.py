from random import Random

def get_seed(a=0, b=100):
    r_cls = Random()
    return r_cls.randint(a, b)

def QA_user(secret):
    ans = input("Choose a number:")
    if ans > secret:
        print("Less")
    elif (ans < secret):
        print("more")
    else:
        return True
    return False

def game_ui():
    print("Welcome to plus Less or more Game !")
    a = input("The secret number will be between :")
    try:
        a = int(a);
    except:
        a = 0
    b = input("And:")
    try:
        b = int(b);
    except:
        b = 100
    secret = get_seed(a, b)
    while QA_user(secret) is not True:
        pass
    print("Congrats, you won !")


if __name__ == '__main__':
    game_ui()
