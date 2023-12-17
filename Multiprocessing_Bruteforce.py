from string import ascii_lowercase,ascii_uppercase,digits,punctuation
from itertools import product
import time
import multiprocessing
 
n = 6
def code(arg,allletters,pw,found):
    argl = [arg]
    for _ in range(1,n):
        for i in product(*argl):        
            if ''.join(i) == pw:
                found.set()
        argl.append(allletters)

def main():
    pw = input()
    allletters = ascii_lowercase + ascii_uppercase + digits + punctuation
    a = ascii_lowercase[0:13]
    b = ascii_lowercase[13::]
    c = ascii_uppercase[0:13]
    d = ascii_uppercase[13::]
    
    found = multiprocessing.Event()

    arglist = [a,b,c,d,digits,punctuation]
    process = []    
    t1 = time.time()

    for arg in arglist: 
        p = multiprocessing.Process(target=code,args=[arg,allletters,pw,found])
        p.start()
        process.append(p)

    while True:
        foundcond = found.is_set()
        prend = all(not p.is_alive() for p in process)
        if foundcond:
            for p in process:
                p.terminate()
            t2 = time.time()
            print(f'found in {t2-t1} seconds')
            break    
        elif prend:
            print('sorry')   
            break 

if __name__ == '__main__':
    main()        