import hashlib
import csv
from collections import OrderedDict


print ("\nfor the project i had to make the range of possible passwords between 0000-9999 so whatever \nits not gonna be usefull i guess\n")
FIN = input("""
Enter the file to read the hashes from \n
format must be csv so (name,hash) \n
""")
FOUT =input("csv file to write the clear passwords to \n")

def hash_password_hack(input_file_name, output_file_name):
    # makes hashes
    clear_text = ""
    mydict = OrderedDict()
    for i in range(0, 10000):
        i = str(i).encode('utf-8') 
        encrypted = hashlib.sha256(i).hexdigest()
        mydict[i] = encrypted

    # reads csv and dumps hashes in dictianory
    with open(input_file_name, 'r') as hash_file:
        reader = csv.reader(hash_file)
        hash_dict = OrderedDict()
        for row in reader:
                hash_dict[row[0]] = row[1]
    # for i in list(hash_dict):
    #     print (i, hash_dict[i])
    #i.decode('utf-8')
    # checks the hashesh with hashes we got in csv and if the match it'll put them in a csv with cleared key like danial, 5104
    check_hash = []
    for i in list(mydict):
        matn = "%s" % (mydict[i])
        check_hash.append(mydict[i])
    for i in list(hash_dict):
        if hash_dict[i] in check_hash:
            ramza = list(mydict.keys())[list(mydict.values()).index(hash_dict[i])]
            esma = list(hash_dict.keys())[list(hash_dict.values()).index(hash_dict[i])],
            matn = "%s,%s\n" % (esma[0], ramza.decode('utf-8'))
            clear_text += matn
    with open(output_file_name, 'w') as passwords:
        passwords.write(clear_text)



decryptor(FIN, FOUT)