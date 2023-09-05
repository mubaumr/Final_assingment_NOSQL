from fastapi import FastAPI
from reactpy.backend.fastapi import configure
from reactpy import component, event, html, use_state,web
from fastapi.middleware.cors import CORSMiddleware
from pymongo import MongoClient
from pymongo.server_api import ServerApi


@component
def MyCrud():
    ## Creating state
    alltodo = use_state([])
    full_name, set_full_name = use_state("")
    user_name, set_user_name = use_state("")
    email, set_email = use_state("")
    phone_number,set_phone_number=use_state("")
    password, set_password = use_state("")
    is_edit = use_state(False)
    full_nameedit, set_full_nameedit = use_state("")
    user_nameedit, set_user_nameedit = use_state("")
    emailedit, set_emailedit = use_state("")
    phone_numberedit, set_phone_numberedit = use_state("")
    passwordedit, set_passwordedit = use_state("")
    id_edit = use_state(0)
    edittodo =  use_state([])
    mui = web.module_from_template(
    "react",
    "@mui/material"
    
    )

    Button = web.export(mui,"Button")

    def mysubmit(event):
        newtodo = {"full_name": full_name, "user_name":user_name , "email":email , "phone_number": phone_number,"password":password}
        # push this to alltodo
        alltodo.set_value(alltodo.value + [newtodo])
        login(newtodo)  # function call to login function using the submitted data
       # looping data from alltodo to show on web
    
    def editbtn(b):
        is_edit.set_value(True)
        for i,x in enumerate(alltodo.value):
            if i == b:
                set_full_nameedit(x['full_name'])
                set_user_nameedit(x['user_name'])
                set_emailedit(x['email'])
                set_phone_numberedit(x['phone_number'])
                set_passwordedit(x['password'])
                id_edit.set_value(b)
    def savedata(event):
        for i,x in enumerate(alltodo.value):
            if i == id_edit.value:
                x['full_name'] = full_nameedit
                x['user_name'] = user_nameedit
                x['email']= emailedit
                x['phone_number']= phone_numberedit
                x['password'] = passwordedit
        is_edit.set_value(False)    
        set_full_nameedit("")
        set_user_nameedit("")
        set_emailedit("")
        set_phone_number("")
        set_passwordedit("")

        updatetodo = {"updatefull_name": full_nameedit, "updateuser_name": user_nameedit, "updateemail":emailedit, "updatephone_number" : phone_numberedit,"updatepassword" : passwordedit}
        edittodo.set_value(edittodo.value + [updatetodo])
        update(updatetodo)
    list = [
        html.li(
            {
              "key":b,
             
            },
            f"{b} => {i['full_name']} ; {i['user_name'] }; {i['email'] }; {i['phone_number']};{i['password']}, ",
        
        html.button({
           "on_click":lambda event, b=b:editbtn(b)
            },"edit"),
            )
            for b, i in enumerate(alltodo.value)
            
    ]
    def handle_event(event):
        print(event)
    
    return html.div(
                {"style": 
                {  
                "padding":"100px",
                "display": "flex",
                "align-items": "center",           
                "background-repeat":"no-repeat",
                "background-attachment":"fixed",
                "background-size":"cover",
                "backgeound-opacity" : "0.5",
                "flex-wrap": "wrap",
                "background_image":"url(https://muba07.neocities.org/d40b857c7494488125144120fe4cb996.jpg)",
                "min-height": "600px",
                }
                },
             html.form(
                html.b(html.h1(
                    {"style": {"font-family": "	Copperplate",
                                "font-size": "40px",
                                "letter-spacing":"4px",
                                "text-shadow":"0 0 3px black",
                                "border":"8.5px Black",
                                "border-radius": "20px",
                                "opcaity":"0%",
                                "flex-wrap": "wrap",
                                "background-color":"hsl(197, 52%, 39%)",
                                "background-opacity":"0%",
                                "padding": "15px 25px",
                                "border-style": "outset",
                                "box-sizing": "border-box",
                                "color":"white"}}
                    ,"Welcome to future of fashion",)),
                    html.br(),
            html.input(
                {
                    "type": "test",
                    "placeholder": "full_name",
                    "valign":"middle",
                    "style": {"padding": "10px","margin":"1rem"},
                    "on_change": lambda event: set_full_name(event["target"]["value"]),
                }
            ),

            html.input(
                {
                    "type": "test",
                    "placeholder": "user_name",
                    "style": {"padding": "10px","margin":"1rem"},
                    "on_change": lambda event: set_user_name(event["target"]["value"]),
                }
            ),
             html.input(
                {
                    "type": "test",
                    "placeholder": "email",
                    "style": {"padding": "10px","margin":"1rem"},
                    "on_change": lambda event: set_email(event["target"]["value"]),
                }
            ),
            html.input(
                {
                    "type": "test",
                    "placeholder": "phone_number",
                    "style": {"padding": "10px","margin":"1rem"},
                    "on_change": lambda event: set_phone_number(event["target"]["value"]),
                }
            ),
            html.input(
                {
                    "type": "test",
                    "placeholder": "password",
                    "style": {"padding": "10px","margin":"1rem"},
                    "on_change": lambda event: set_password(event["target"]["value"]),
                }
            ),
            Button(
                { 
                    "type": "create",
                    "size":"medium",
                    "style": {"padding": "10px"},
                    "bold":"70",
                    "color":"primary",
                    "variant":"contained",
                    "on_click": event(
                        lambda event: mysubmit(event), prevent_default=True
                    ),
                },
                "Create",
            ),
        ),   
            html.div(
                 html.input(
                {
                    "type": "test",
                    "value":full_nameedit,
                    "style":{"padding": "10px","margin":"2rem","display":"none" if is_edit.value == False else "block"},
                    "placeholder": "update full name",
                    "on_change": lambda event: set_full_nameedit(event["target"]["value"]), 
                },
                  
            ),
            html.input(
                {
                    "type": "test",
                    "value":user_nameedit,
                    "style":{"padding": "10px","margin":"2rem","display":"none" if is_edit.value == False else "block"},
                    "placeholder": "update user name",
                    "on_change": lambda event: set_user_nameedit(event["target"]["value"]),
                    
                },
               
            ),
            html.input(
                {
                    "type": "test",
                    "value":emailedit,
                    "placeholder": "update email",
                    "style":{"padding": "10px","margin":"2rem","display":"none" if is_edit.value == False else "block"},
                    "on_change": lambda event: set_emailedit(event["target"]["value"]),
                    
                },
               
            ),
            html.input(
                {
                    "type": "test",
                    "value":phone_numberedit,
                    "style":{"padding": "10px","margin":"2rem","display":"none" if is_edit.value == False else "block"},
                    "placeholder": "update phone number",
                    "on_change": lambda event: set_phone_numberedit(event["target"]["value"]),
                    
                },
               
            ),
            html.input(
                {
                    "type": "test",
                    "value":passwordedit,
                    "style":{"padding": "10px","margin":"2rem","display":"none" if is_edit.value == False else "block"},
                    "placeholder": "update password",
                    "on_change": lambda event: set_passwordedit(event["target"]["value"]),
                    
                },
               
            ),
            
            Button(
                {
                    "type": "Update",
                    "size":"small",
                    "style":{"padding": "10px","display":"none" if is_edit.value == False else "block"},
                    "color":"secondary",
                    "variant":"contained",
                    "on_click": event(lambda event: savedata(event), prevent_default=True),
                },
                "Update",
            ),
             
        ),
        html.ul(list),   
    )


app = FastAPI()
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi 
app = FastAPI()
#copy and paste the mongo DB URI 
uri="mongodb+srv://admin:admin123@cluster0.ksvd0uq.mongodb.net/"
client= MongoClient (uri, server_api=ServerApi("1"))  #camel case
#defining the Db name
db= client ["Project"]
collection=db["User"]
#checking the connection
try:
    client.admin.command("Ping")
    print("Successfully Connected MongoDB")
except Exception as e:
    print(e)
def login(
    login_data: dict,
 ): # removed async, since await makes code  execution pause for the promise to resolve anyway. doesnt
    full_name= login_data["full_name"]
    user_name = login_data["user_name"]
    email = login_data["email"]
    phone_number = login_data["phone_number"]
    password = login_data ["password"]
    # Create a document to insert into the collection
    document = {"full_name":full_name, "user_name":user_name, "email":email,"phone_number": phone_number, "password": password}
    # logger.info("sample log messege")
    print(document)
    #Insert the docoument into the collection
    post_id = collection.insert_one(document).inserted_id #insert document
    print(post_id)
    print({"Login successful"})
def update(
    update_data: dict,
 ): # removed async, since await makes code  execution pause for the promise to resolve anyway. doesnt
    full_nameedit= update_data["updatefull_name"]
    user_nameedit = update_data["updateuser_name"]
    emailedit = update_data["updateemail"]
    phone_numberedit = update_data["updatephone_number"]
    passwordedit = update_data ["updatepassword"]
    # Create a document to insert into the collection
    updatedocument = {"updatefull_name":full_nameedit, "updateuser_name":user_nameedit, "updateemail":emailedit,"updatephone_number": phone_numberedit, "updateupassword": passwordedit}
    # logger.info("sample log messege")
    print(updatedocument)
    #Insert the docoument into the collection
    updatepost_id = collection.insert_one(updatedocument).inserted_id #insert document
    print(updatepost_id)
    print({"Updated successful"}) 

def new_func(update_data):
    emailedit = update_data["update email"]
    return emailedit
configure(app, MyCrud)

