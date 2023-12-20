from string import ascii_lowercase,ascii_uppercase,digits,punctuation
from itertools import product
import time
import multiprocessing

def password_finder(n,arg,allletters,pw,found):    
 
 # making a list which will append 'allletters' after checking for a particular letter password 
    argls = [arg]   

 # starting of loop which will iterate from 1 to n letters
    for _ in range(1,n+1):
     # staring of loop which will unpack the 'argls' list and find the cartesian product    
        for i in product(*argls):        
        
            # checking if the product is same as the password
            if ''.join(i) == pw:
                found.set()   # sets the event true if password is found
        
        argls.append(allletters)  # appends the 'allletters' to iterate through next letter word

def main():

    n = int(input())  # the program will search upto n letter words
    password = input()
    
    # creating the list of all letters
    allletters = ascii_lowercase + ascii_uppercase + digits + punctuation

    # slicing of the word lists for more faster search in a process
    a = ascii_lowercase[0:13]
    b = ascii_lowercase[13::]
    c = ascii_uppercase[0:13]
    d = ascii_uppercase[13::]
    
    arglist = [a,b,c,d,digits,punctuation]
    
    # initialization of the event 
    found = multiprocessing.Event()
    
    t1 = time.time()  # start time

    process = []    

    # loop to create child processes
    for arg in arglist: 
        p = multiprocessing.Process(target = password_finder, args = [n,arg,allletters,password,found])
        p.start()
        process.append(p)

    # continuously checking if the event is true or all the processes have been terminated
    while True:
        
        foundcondition = found.is_set()  # checks if event is true
        pr_end = all(not p.is_alive() for p in process)  # checks if all processes have ended
        
        # if password is found, all the processes should be terminated
        if foundcondition:
            for p in process:
                p.terminate()
            
            t2 = time.time()  # end time
            print(f'Password was found in {t2-t1} seconds')
            break    
        
        elif pr_end:
            print('Password could not be found')   
            break 

if __name__ == '__main__':
    main()            
