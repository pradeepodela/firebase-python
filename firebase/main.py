import pyrebase



cfg = {
    'apiKey': "AIzaSyBwRBcKz9DC68UVsMBygkANr_QixS0ZaKA",
    'authDomain': "mypy-19226.firebaseapp.com",
    'databaseURL':'https://mypy-19226-default-rtdb.firebaseio.com/',
    'projectId': "mypy-19226",
    'storageBucket': "mypy-19226.appspot.com",
    'messagingSenderId': "990787705081",
    'appId': "1:990787705081:web:ab15b33b11bbea973dea28",
    'measurementId': "G-298F64SX86"

}
print('configering.....')

firebase = pyrebase.initialize_app(cfg)
print('app configered')
db = firebase.database()
auth = firebase.auth()
Storage = firebase.storage()






def login():

    mail = input('enter your mail:- ')
    password = input('Enter your Password:- ')

    try :
        auth.sign_in_with_email_and_password(mail,password)
        print('successfully signedin')
    except:
        print('plese check your login cradiantiles')

def signup():

    mail = input('enter your mail:- ')
    password = input('Enter your Password:- ')
    try :
        auth.create_user_with_email_and_password(mail,password)
        print('successfully created your account')
    except:
        print('email already exist')
    
def storage_fb():

    filename = input('enter file name:- ')
    path = input('enter path :- ')
    path = f'{path}/{filename}'

    Storage.child(path).put(filename)
    print('upploaded file')


def get_storage():
    filename = input('enter file name:- ')
    path = input('enter path :- ')
    path = f'{path}/{filename}'
    print(Storage.child(path).get_url(None))


def download():
    filename = input('enter file name:- ')
    path = input('enter path :- ')
    path = f'{path}/{filename}'
    Storage.child(path).download('','image.png')
    print('successfully file downloaded')


def database():
    data = {
        'name':'pradeep',
        'mailid':'odelapradeep@protomail.com',
        'phno': 6304576616
    }

    db.child('data').push(data)
    print('successfully pushed data')


##### CREATING YOUR OWN USER ID ######
def database2():
    data = {
        'name':'pradeep',
        'mailid':'odelapradeep@protomail.com',
        'phno': 6304576616
    }

    db.child('data').child('my_id').set(data)
    print('successfully pushed data')


##### UPDATEING THE DATABASE #######
def update():
    db.child('data').child('my_id').update({'name':'pradeepodela'})
    print('successfully updated data')



##### GET DATA ######
def get_db():

    data = db.child('data').get() 

    for person in data.each():
        print(person.val())
        print(person.key())


def get_db1():

    data = db.child('data').get() 

    for person in data.each():
        if person.val()['name'] == 'pradeepodela':
            print(person.val()['mailid'])
            print(person.key())


def delete():
    db.child('data').child('new').remove()



def delete_spef():
    data = db.child('data').get() 

    for person in data.each():
        if person.val()['name'] == 'pradeepodela':

            db.child('data').child(person.key()).child('phno').remove()
           
delete_spef()