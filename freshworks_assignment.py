# Import the module
import json
import sys
import os
import glob
  
def checkKey(dic,key): 
    if key in dic.keys(): 
        return True 
    else: 
        return False
    
def createRecord(file_path):
    '''key_name=input("Enter a key name:")
    with open(file_path) as file:
        data=json.load(file)
        #print("The no.of records before insertion:"+str(len(data)))
        if(checkKey(data,key_name)):
            raise Exception("Key with the specified name already exists")
        else:
       
            print("Enter a JSON object: press ctrl+D to save")
            data_JSON={}
            while True:
                try:
                    k,d = input().split(":")
                    data_JSON[k]=d
                except EOFError:
                    break
            
            print(data_JSON,type(data_JSON))
            #print(data,type(data))
            #data[key_name]=data_JSON
            with open(file_path,"w") as file:
                json.dump(data_JSON,file,indent=5)
            print("record created successfully")'''
    key_name=input("enter a key name:")
    data={}
    print("Enter a JSON object: press ctrl+D to save")
    data_JSON={}
    while True:
        try:
            k,d = input().split(":")
            data_JSON[k]=d
        except EOFError:
            break
    data[key_name]=data_JSON
    with open(file_path,'a+') as file:
        json.dump(data,file,indent=5)
        print("creation successful")

def readRecord(file_path):
    with open(file_path) as file:
        data=json.load(file)
    print("The no.of records:"+str(len(data)))
    key_read=input("Enter a key to read the value against it:")
    if(checkKey(data,key_read)):
        print(json.dumps(data[key_read],indent=5))
    else:
        raise Exception("No such key exists")

def deleteRecord(file_path):
    with open(file_path) as file:
        data=json.load(file)
    print("The no.of records before deletion:"+str(len(data)))
    key_del=input("Enter a key to delete the record:")
    if(checkKey(data,key_del)):
        del data[key_del]
        with open(file_path,'w') as file:
            data=json.dump(data,file,indent=5)
        print("Record deleted Successfully\n")
        with open(file_path) as file:
            data=json.load(file)
        print("The no.of records after deletion:"+str(len(data)))
    else:
        raise Exception("No such key exists")

    

print("\nWelcome to Client key-value file")
print("You can create,read,delete records from the file\n")
print("\nPress 1 for creating a new record")
print("\nPress 2 for reading a record")
print("\nPress 3 for deleting a record")
file_path=None
OUTPUT_DIR=str(os.getcwd())
try:
    choice=int(input("Enter your choice:"))
    if(choice<4 and choice>0):
        print("Do you want to give file path?\nPress Y/y for YES, N/n for NO")
        file_choice=input()
        if(file_choice=="Y" or file_choice=="y"):
            file_path = input("Enter the path of your file: ")
            #check whether file is present or not
            if(not os.path.exists(file_path)):
                raise Exception("I did not find the file , "+str(file_path))
        elif(file_choice=="N" or file_choice=="n"):
            
            #print(OUTPUT_DIR)
            if(choice==1 or choice==3):
                with open(os.path.join(OUTPUT_DIR, 'clientsData_new.json'), 'w') as file:
                    file_path=file
            elif(choice==2):
                with open(os.path.join(OUTPUT_DIR, 'clientsData_new.json'), 'r') as file:
                    file_path=file
        else:
            raise Exception("Please select Y/y or N/n")
        
        if(choice==1):
            list_of_files = glob.glob(OUTPUT_DIR) 
            latest_file = max(list_of_files, key=os.path.getctime)
            try:
                if(int(os.stat(latest_file).st_size)>=1073741824):
                    raise Exception("file size exceeded 1gb")
                else:
                    if(file_choice=="n" or file_choice=="N"):
                        createRecord('clientsData_new.json')
                    else:
                        createRecord(file_path)
            except Exception as e:
                print(e)
        elif(choice==2):
            if(file_choice=="n" or file_choice=="N"):readRecord('clientsData_new.json')
            else:readRecord(file_path)
        elif(choice==3):
            if(file_choice=="n" or file_choice=="N"):deleteRecord('clientsData_new.json')
            else:deleteRecord(file_path) 
    else:
        raise Exception("\nPlease select a choice from 1,2,3")
except Exception as e:
    print(e)

