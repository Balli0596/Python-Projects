from cryptography.fernet import Fernet
def write_key():
     key = Fernet.generate_key()
     with open("keys.key","wb") as key_file:
         key_file.write(key)

def load_key():
     file=open("key.key","rb")
     key = file.read()
     file.close()
     return key

print("welcome to password manager")
pwd=input("what is your password")
key=load_key()
fer=Fernet(key)




# def view():
#     with open('password.txt','a') as f:
#         for line in f.readline():
            
#             data=line.rstrip()
#             user,passw=data.split("|")
#             print("User:", user, "| Password:", passw)

# fer.decrypt(passw.encode()).decode()
def view():
    with open('password.txt', 'r') as f:  # 'r' to read, not 'a'
        for line in f.readlines():
            data = line.rstrip()
            parts = data.split("|")
            if len(parts) == 2:
                 user, pwd = parts
                 print("User:", user, " Password:", fer.decrypt(pwd.encode()).decode()+"\n")
            else:
                 print("Skipping invalid line:", data)

            
def add():
    name=input('account name:')
    pwd=input('password:')
    with open('password.txt','a') as f:
        f.write(name +"|"+  fer.encrypt(pwd.encode()).decode() +"\n")

while True:
    mode=input("would you like to add anew password or view visiting ones(view,add) or to press q to quit")
    if(mode=="q"):
        break
    if(mode=="view"):
        view()
    elif(mode=="add"):
        add()
    else:
        print("invalid options ")