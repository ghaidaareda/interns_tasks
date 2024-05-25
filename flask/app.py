from datetime import datetime
from flask import Flask, render_template, request, redirect, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate ,migrate
import json
from uuid import uuid4

app = Flask(__name__)

#database configurations
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'

db = SQLAlchemy(app)


# create file storage database as json file
'''
class FileStorage:
    __file_path = 'file.json'
    __objects = {}

    def all(self):
        """ to return dictionary of all users """
        return self.__objects
    
    def new(self, user):
        """ add new user in __objects"""
        self.__objects[user.id] = user
        print(self.__objects)

    def save(self):
        """ selization all users in __object dic to json file """
        json_dic = {}
        for k, v in self.__objects.items():
            json_dic[k] = v.to_dict()               # error in using to_dict class method on the retrieved data from JSON

        with open(self.__file_path, 'w', encoding='UTF-8') as jfile:
            json.dump(json_dic, jfile)

    def reload(self):
        """ deserialize the json file to __objects to keep all storage in json file"""
        try:
            with open(self.__file_path, 'r', encoding='UTF-8') as rfile:
                data = json.load(rfile)
                for k, v in data.items():
                    self.__objects[k] = v 
        except IOError:
            pass
'''
#storage = FileStorage()



#users model
class User(db.Model):
    
    id = db.Column(db.String(60), nullable=False, primary_key=True)
    fname = db.Column(db.String(20), nullable=False)
    lname = db.Column(db.String(128), nullable=False)
    img_url = db.Column(db.String(255), nullable=False)
    register_date = db.Column(db.DateTime, nullable=False, default= datetime.now())

    def __init__(self, *args, **kwargs):
        """ constructor """
        if(not kwargs or 'id' not in kwargs): 
            self.id = str(uuid4())
            self.register_date = datetime.now()
            if kwargs:
                for k,v in kwargs.items():
                    setattr(self, k, v)

    def to_dict(self):
        """ convert instance created to dictionary to convert it to json """
        dictionary = {}
        attributes = self.__dict__.copy()
        attributes.pop('_sa_instance_state', None)
        dictionary.update(attributes)
        dictionary['register_date'] = self.register_date.isoformat() 
        return dictionary


migrate = Migrate(app, db)



@app.route('/')
def home():
    users_data = User.query.all()
    return render_template('home.html', users_data=users_data)


@app.route('/json')
def users_data_asjson():
    users = User.query.all()
    users_json = [user.to_dict() for user in users]
    return jsonify(users_json)


@app.route('/create')
def add_user():
    return render_template('add.html')


@app.route('/create', methods=['POST'])
def create_user():
    """
    function to get user input data
    and store it in db 
    """
    fname = request.form.get('first_name')
    lname = request.form.get('last_name')
    img_url = request.form.get('img_url')
    
    if fname != '' and lname != '' and img_url != '':
        data = User(fname=fname, lname=lname, img_url=img_url)
        
        #storage.new(data)
        #storage.save()
        #storage.reload()
        
        db.session.add(data)
        db.session.commit()
        

        return redirect('/')
    else:
        return redirect('/')
    

@app.route('/delete/<id>')
def delete_user(id):
    data = User.query.get(id)
    db.session.delete(data)
    db.session.commit()
    return redirect('/')



@app.route('/get_user/<id>', methods=['GET'])
def get_user(id):
    data = User.query.get(id)
    data = data.to_dict()
    return jsonify(data)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
