import random
import time

def repeatable_random(seed):
    random.seed(a=seed, version=2)
    return str(random.randint(1,1000000))

def test():
    while 1:
        print(repeatable_random("23452345563456"))
        time.sleep(1) 

if __name__ == '__main__':
    test()
