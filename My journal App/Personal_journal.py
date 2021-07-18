import os
def header():
    print("____________________________________________")
    print("PERSONAL JOURNAL APP")
    print("___________________________________________")

def create_Journal():
    f=open("my_journal.txt","wt")
    f.close()

def append():
    with open('my_journal.txt','a') as f:
        journal=[]
        print("Enter your journal and press 'E' to stop:: ")

        while (1):
            lol=input()
            if(lol ==('E'or'e')):
                break
            journal.append(lol)
        for text in journal:
            f.write('%s\n' % text)


def read():
    with open("my_journal.txt",'r') as fin:
        fin.seek(0)
        print(fin.read())


def main():
    header()
    print("What do you want to do?")
    print("Press 'V' for viewing your journal")
    print("Press 'A' for apppending your journal")
    print("Press 'W' to clear all the file and writing again")
    ans='y'
    while(ans!='n'):
        choice=input("Enter your choice")

        if(choice=='V' or choice=='v'):
            read()
        elif(choice =='A' or choice =='a'):
            append()
        elif(choice == 'W' or choice =='w'):
            create_Journal()
            append()
        else:
            print("Invalid choice!")

        print(".....Do you want to continue :: y/n?")
        ans=input()
        if(ans!='y' or ans!='n'):
            print("Invalid choice .......")

print("****************************")
print("current working directory ::",os.getcwd())
print("name of the operating system::",os.name)     # we get output as "nt" which means we are using window
print("****************************")




main()
