from cryptography.fernet import Fernet

'''write_key() is to create a Key.key'''
'''def write_key():
    keyy=Fernet.generate_key()
    with open('Key.key','wb') as key_file:
        key_file.write(keyy)
write_key()
'''
def load_key():
    file=open('Key.key','rb')
    key=file.read()
    file.close()
    return key

key=load_key()
fer=Fernet(key)


def view():
    with open('Password.txt','r') as f:
        for line in f.readlines():
            data=line.rstrip()
            user, passw=data.split("|")
            print(f"Username:-{user} | Password:-{fer.decrypt(passw.encode()).decode()}")
            '''{fer.decrypt(passw.encode()).decode()}")'''

def add():
    name=input('Enter Username:- ')
    pwd=input('Enter Password:- ')
    with open('Password.txt','a') as f:
        f.write(name + "|" + fer.encrypt(pwd.encode()).decode() + '\n')

user_name=input("Enter Your Username:- ")

if user_name=="Manash01":
    master_pass=input("Enter Your Master-Password:- ")
    if master_pass=="Undriling01":
        print("Welcome Mr. Manash Baruah")
        while True:
            mode=input("You wants to add password or wants to view existing passwords (view/add) or q to Quit:- ").lower()
            if mode=='q':
                print("Quit Successfully.")
                break


            if mode=="view":
                view()
                        

            elif mode=="add":
                        add()
                        
            else:
                print('Invalid Response!')
                continue
    else:
        print("Wrong Password! Try again")
else:
    print("Wrong Username! Try again")