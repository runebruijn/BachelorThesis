# -*- coding: utf-8 -*-
import string, sys
from os import listdir
from os.path import isfile, join


# Correct encoding and remove duplicates
def main():
    for i in range(1,6):
        mypath = "test_dataset/JPvsRC/EN00" + str(i) #Path to the directory containing the files to be processed
        allfiles = [f for f in listdir(mypath)]
        txtfiles = []
        x = 1
        for file in allfiles:
            f = open(mypath+"/"+file, "r")
            txtfile = f.read()
            txtfile = txtfile.rstrip()
            print(txtfile)
            f.close()
            if file[0] == "J":
                f2= open(mypath+"/known0"+str(x)+".txt","w+")
                f2.write(txtfile)
                f2.close()
                x += 1
            elif file[0] == "R":
                f2= open(mypath+"/unknown.txt","w+")
                f2.write(txtfile)
                f2.close()



if __name__ == "__main__":
    main()
