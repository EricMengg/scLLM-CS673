import eel
import wx
import os
from ultil import predict_method, further_tune
from pymongo.mongo_client import MongoClient
from urllib.parse import quote_plus

eel.init("web")

@eel.expose
def get_data():
    return "Data from python"

@eel.expose
def predict(address, bs, model, output):
    filename = address
    script_dir = os.path.dirname(__file__)
    if filename == "SampleData1":
        print("Using Sample Dataset 1")
        filename = os.path.join(script_dir, "data\\demo.h5ad")
    if model == "":
        default_model_path = os.path.join(script_dir, "model\\default_state_dict.pth")
        model = default_model_path
    output_path = os.path.join(script_dir, output)
    print("Address:", filename)
    print("Batch Size:", bs)
    print("Output Title:", output_path)
    print("Model:", model)
    predict_method(filename, bs, model, output_path)
    return ""

@eel.expose
def get_model(address, bs, lr, epoch, output):
    filename = address
    script_dir = os.path.dirname(__file__)
    if filename == "SampleData1":
        print("Using Sample Dataset 1")
        filename = os.path.join(script_dir, "data\\demo.h5ad")
    output_path = os.path.join(script_dir, "model\\" + output)
    print("Address:", filename)
    print("Batch Size:", bs)
    print("Learning Rate:", lr)
    print("Number of Epoch:", epoch)
    print("Output Title:", output_path)
    further_tune(filename, bs, lr, epoch, output_path)
    return ""

@eel.expose
def getFile(wildcard="*"):
    app = wx.App(None)
    style = wx.FD_OPEN | wx.FD_FILE_MUST_EXIST
    dialog = wx.FileDialog(None, 'Open', wildcard=wildcard, style=style)
    if dialog.ShowModal() == wx.ID_OK:
        path = dialog.GetPath()
    else:
        path = None
    dialog.Destroy()
    return path

@eel.expose
def getModel(wildcard="*"):
    app = wx.App(None)
    style = wx.FD_OPEN | wx.FD_FILE_MUST_EXIST
    dialog = wx.FileDialog(None, 'Open', wildcard=wildcard, style=style)
    if dialog.ShowModal() == wx.ID_OK:
        path = dialog.GetPath()
    else:
        path = None
    dialog.Destroy()
    return path

@eel.expose
def register(username, userPassword):
    password = quote_plus("45@wK@ugk5nQsRp")
    uri = f"mongodb://sllxakura:{password}@ac-3viqyqd-shard-00-00.wac3u8s.mongodb.net:27017,ac-3viqyqd-shard-00-01.wac3u8s.mongodb.net:27017,ac-3viqyqd-shard-00-02.wac3u8s.mongodb.net:27017/?ssl=true&replicaSet=atlas-82ox5v-shard-0&authSource=admin&retryWrites=true&w=majority&appName=Cluster1"
    client = MongoClient(uri)
    db = client['user_database']
    users = db.users
    try:
        client.admin.command('ping')
        print("Pinged your deployment. You successfully connected to MongoDB!")
        print(username)
        print(userPassword)
        if users.find_one({"username": username}):
            print("Username already exists. Please try a different username.")
            return "Username already exists. Please try a different username."
        
        users.insert_one({"username": username, "password": userPassword})
        print("Registration successful!")
        return "Success"
    except Exception as e:
        print("error")
        print(e)
        return "Error Connection"

@eel.expose
def login(username, userPassword):
    password = quote_plus("45@wK@ugk5nQsRp")
    uri = f"mongodb://sllxakura:{password}@ac-3viqyqd-shard-00-00.wac3u8s.mongodb.net:27017,ac-3viqyqd-shard-00-01.wac3u8s.mongodb.net:27017,ac-3viqyqd-shard-00-02.wac3u8s.mongodb.net:27017/?ssl=true&replicaSet=atlas-82ox5v-shard-0&authSource=admin&retryWrites=true&w=majority&appName=Cluster1"
    client = MongoClient(uri)
    db = client['user_database']
    users = db.users
    try:
        client.admin.command('ping')
        print("Pinged your deployment. You successfully connected to MongoDB!")
        print(username)
        print(userPassword)
        user = users.find_one({"username": username})
        if not user:
            print("Username not found. Please register first.")
            return "Username not found. Please register first."
        # Verify the password
        if userPassword == user['password']:
            print("Login successful! Welcome back.")
            return "Success"
        else:
            print("Incorrect password. Please try again.")
            return "Incorrect password. Please try again."
        
    except Exception as e:
        print(e)
        return "Error Connection"

eel.start("start.html")