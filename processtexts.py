# -*- coding: utf-8 -*-
import string, sys
from os import listdir
from os.path import isfile, join


# Correct encoding and remove duplicates
def main():
    mypath = "Dear Abby Pauline Phillips" #Path to the directory containing the files to be processed
    allfiles = [f for f in listdir(mypath)]
    txtfiles = []
    for file in allfiles:
        f = open(mypath+"/"+file, "r", encoding='latin1')
        txtfile = f.read()
        txtfile = utf8(txtfile)
        txtfile = txtfile.rstrip()
        txtfiles.append(txtfile)
        f.close()
        if txtfiles.count(txtfile) > 1:
            print("Duplicate: ", file)
            pass
        else:
            f2= open("ProcessedFiles/" + file,"w+")
            f2.write(txtfile)
            #print("No Duplicate: ", file)
            f2.close()

def utf8(str):
    if sys.version_info < (3, 0):
        return str.encode('utf-8')
    else:
        return str


if __name__ == "__main__":
    main()
