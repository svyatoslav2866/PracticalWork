class User:
    def __init__(self, name, login, password):
        self.name = name
        self.login = login
        self.password = password

    def get_user(self):
        print(self.name, self.login, self.password)


user1 = User("Alex", "chupakabra", "12345678")
user2 = User("john", "father100-7", "daducktetr234")
user3 = User("Andrew", "superman20years", "87654321T")

while True:
    choice = input("please enter user number: ")
    if choice == "1":
        print(f"name : {user1.name}, login : {user1.login}, password : {user1.password}")
    elif choice == "2":
        print(f"name : {user2.name}, login : {user2.login}, password : {user2.password}")
    elif choice == "3":
        print(f"name : {user3.name}, login : {user3.login}, password : {user3.password}")
    elif choice == "4":
        break