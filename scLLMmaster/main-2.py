from pymongo.mongo_client import MongoClient
from urllib.parse import quote_plus

password = quote_plus("45@wK@ugk5nQsRp")

uri = f"mongodb://sllxakura:{password}@ac-3viqyqd-shard-00-00.wac3u8s.mongodb.net:27017,ac-3viqyqd-shard-00-01.wac3u8s.mongodb.net:27017,ac-3viqyqd-shard-00-02.wac3u8s.mongodb.net:27017/?ssl=true&replicaSet=atlas-82ox5v-shard-0&authSource=admin&retryWrites=true&w=majority&appName=Cluster1"

client = MongoClient(uri)
db = client['user_database']
users = db.users

def register():
    username = input("Enter a new username: ")
    if users.find_one({"username": username}):
        print("Username already exists. Please try a different username.")
        return
    
    password = input("Enter a new password: ")
    users.insert_one({"username": username, "password": password})
    print("Registration successful!")

def login():
    username = input("Enter your username: ")
    user = users.find_one({"username": username})
    if not user:
        print("Username not found. Please register first.")
        return
    password = input("Enter your password: ")
    
    # Verify the password
    if password == user['password']:
        print("Login successful! Welcome back.")
    else:
        print("Incorrect password. Please try again.")

def main():
    try:
        client.admin.command('ping')
        print("Pinged your deployment. You successfully connected to MongoDB!")
    except Exception as e:
        print(e)

    while True:
        action = input("Do you want to login or register? (login/register/exit): ").lower()
        if action == "login":
            login()
        elif action == "register":
            register()
        elif action == "exit":
            break
        else:
            print("Invalid input. Please type 'login', 'register', or 'exit'.")

if __name__ == "__main__":
    main()
