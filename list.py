#Coded By Dark Slad3
#A Product Of ToxicNoob

import os
import sys
import time

def psb(z):
    for e in z + '\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.03)

def printAllKLength(set, k): 
  
    n = len(set)  
    printAllKLengthRec(set, "", n, k) 
  

def printAllKLengthRec(set, prefix, n, k): 
      

    if (k == 0) : 
        print(prefix) 
        return

    for i in range(n): 
  

        newPrefix = prefix + set[i] 
          
        printAllKLengthRec(set, newPrefix, n, k - 1) 
  

if __name__ == "__main__": 
      
    os.system("clear")
    time.sleep(1)
    print ("\033[92m")
    os.system("figlet Toxic Noobs")
    print("\033[3;90m 			      Security is a Illusion\033[0;92m")
    time.sleep(0.6)
    psb("\n\n[!] Loading.....")
    time.sleep(0.7)
    psb("\n[!] Please Wait.....")
    time.sleep(1)

    print ("\033[92m")
    os.system(" clear")
    os.system("figlet Toxic List")
    print("		A Product of ToxicNoob")
    print ("\n")
    time.sleep(0.8)
    print("[01] Wordlist with Numbers and Alphabets (1,2,3,a,b,c) . \n")
    print("[02] Wordlist with Numbers only (1,2,3) . \n")
    print("[03] Wordlist with Alphabets only (a,b,c) . \n \n")
    time.sleep(0.6)
    inp = input("[*] Enter Your Choice:> ")
    
    if inp == (""):
        print(" \n \nEnter right option!")
        exit()
    file = input("\n \n[*] Enter a File name:> ")
    if file == "":
        file = "pass"
       
    if inp == ("1" or "01"):
        set1 = ['a','b','c','d','f','g','h','i','j','k','l','m','n','p','q','r','s','t','u','v','w','x','y','z','1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
    elif inp == ("2" or "02"):
        set1 = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
    elif inp == ("3" or "03"):
        set1 = ['a','b','c','d','f','g','h','i','j','k','l','m','n','p','q','r','s','t','u','v','w','x','y','z']

    lnt = input(" \n[*] Input password Lenth (Max 15, Default 4):> ")
    if(lnt == ""):
        k = (4)
    elif(lnt == "1"):
        k = (1)
    elif(lnt == "2"):
        k = (2)
    elif(lnt == "3"):
        k = (3)
    elif(lnt == "4"):
        k = (4)
    elif(lnt == "5"):
        k = (5)
    elif(lnt == "6"):
        k = (6)
    elif(lnt == "7"):
        k = (7)
    elif(lnt == "8"):
        k = (8)
    elif(lnt == "9"):
        k = (9)
    elif(lnt == "10"):
        k = (10)
    elif(lnt == "11"):
        k = (11)
    elif(lnt == "12"):
        k = (12)
    elif(lnt == "13"):
        k = (13)
    elif(lnt == "14"):
        k = (14)
    elif(lnt == "15"):
        k = (15)

    else:
        exit()

    print(" \n \nPlease wait some time..... \n\033[37;40m")
    time.sleep(0.5)
    sys.stdout = open(file+".txt", "w")
    printAllKLength(set1, k)
    sys.stdout.close()
