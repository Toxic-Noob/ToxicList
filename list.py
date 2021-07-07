#Created By Dark Sl4d3
#A product of Toxic Noobs
import os
import sys
import time

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
      
    print ("\033[92m")
    os.system(" clear")
    os.system("figlet Toxic List")
    print ("\n")
    print("[01] Wordlist with Numbers and Alphabets (1,2,3,a,b,c) . \n")
    print("[02] Wordlist with Numbers only (1,2,3) . \n")
    print("[03] Wordlist with Alphabets only (a,b,c) . \n \n")
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

    print(" \n \nPlease wait some time..... \n")
    time.sleep(0.5)
    sys.stdout = open(file+".txt", "w")
    printAllKLength(set1, k)
    sys.stdout.close()
