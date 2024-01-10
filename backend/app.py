from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager, create_access_token
from werkzeug.security import generate_password_hash, check_password_hash
from flask_cors import CORS
from flask_migrate import Migrate
from sqlalchemy import text
from dotenv import load_dotenv
import os
import re

load_dotenv()

app = Flask(__name__)
CORS(app, resources={r"/api/*": {"origins": "https://imkozin.github.io"}})
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL')
app.config['JWT_SECRET_KEY'] = os.environ.get('SECRET_KEY')


db = SQLAlchemy(app)

@app.route('/test_db_connection')
def test_db_connection():
    try:
        result = db.session.execute(text("SELECT 1"))
        return "Database connection is working."
    except Exception as e:
        return f"Error: {str(e)}"

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    fname = db.Column(db.String(50), nullable=False)
    lname = db.Column(db.String(50), nullable=False)
    city = db.Column(db.String(100), nullable=False)
    login = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(1000), nullable=False)
    device_qty = db.Column(db.Integer)

class Admin(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    login = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(500), nullable=False)

migrate = Migrate(app, db)

jwt = JWTManager(app)

regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'

@app.route('/admin/create', methods=['POST'])
def create_admin():
    data = request.get_json()

    login = data.get('login')
    password = data.get('password')

    if not login or not password:
        return jsonify({'error': 'Both login and password are required'}), 400

    if Admin.query.filter_by(login=login).first():
        return jsonify({'error': 'Admin profile with this login already exists'}), 400

    hash = generate_password_hash(data['password'])

    new_admin = Admin(login=login, password=hash)

    db.session.add(new_admin)
    db.session.commit()

    return jsonify({'message': 'Admin profile created successfully'}), 201

@app.route('/api/login', methods=['POST'])
def login():
    data = request.get_json()
    login = data.get('login')
    password = data.get('password')

    if not login or not password:
        return jsonify({'error': 'Both login and password are required'}), 400

    user = User.query.filter_by(login=login).first()
    if user and check_password_hash(user.password, password):
        access_token = create_access_token(identity=user.login)
        return jsonify({'access_token': access_token, 'user_type': 'user', 'login': login}), 200

    admin = Admin.query.filter_by(login=login).first()
    if admin and check_password_hash(admin.password, password):
        access_token = create_access_token(identity=admin.id)
        return jsonify({'access_token': access_token, 'user_type': 'admin'}), 200

    return jsonify({'error': 'Invalid login credentials'}), 401

# @app.route('/admin/login', methods=['POST'])
# def admin_login():
#     data = request.get_json()
#     login = data.get('login')
#     password = data.get('password')

#     if not login or not password:
#         return jsonify({'error': 'Both login and password are required'}), 400
    
#     admin = Admin.query.filter_by(login=login).first()

#     if admin and check_password_hash(admin.password, password):
#         access_token = create_access_token(identity=admin.id)
#         return jsonify(access_token=access_token), 200
#     else:
#         return jsonify({'error': 'Invalid login credentials'}), 401

@app.route('/api/user/register', methods=['POST'])
def user_register():
    data = request.get_json()
    fname = data.get('fname')
    lname = data.get('lname')
    city = data.get('city')
    login = data.get('login')
    password = data.get('password')
    device_qty = data.get('device_qty')

    if not fname or not lname or not city or not login or not password:
        return jsonify({'error': 'All fields are required'}), 400

    user_exists = User.query.filter_by(login=data['login']).first()

    if user_exists:
        return jsonify({'error': 'User with this login already exists'}), 400

    if not re.fullmatch(regex, data['login']):
        return jsonify({"error": "Login should be a valid Email address"}), 400
    
    if len(data['password']) < 6:
        return jsonify({"error": "Password is too short,"}), 400
    
    if device_qty < 0:
        return jsonify({'error': 'Device quantity must be at least 0'}), 400
    
    hash_password = generate_password_hash(password)
    new_user = User(
        fname=fname,
        lname=lname,
        city=city,
        login=login,
        password=hash_password,
        device_qty=device_qty
    )
    db.session.add(new_user)
    db.session.commit()

    return jsonify({"message": "User registered successfully"}), 201


# @app.route('/user/login', methods=['POST'])
# def user_login():
#     data = request.get_json()
#     user = User.query.filter_by(email=data['email']).first() 
#     print("Req data =>", data)
#     print("DB query user", user)
    
#     if user is None:
#         return jsonify({"error": "Unauthorized"}), 401

#     if not check_password_hash(user.password, data['password']):
#         return jsonify({"error": "Invalid credentials!"}), 401
#     access_token = create_access_token(identity=user.email)  
#     email = user.email
#     return jsonify({"email": email,"access_token": access_token})

@app.route('/api/edit-user-device/<int:id>', methods=['PUT'])
def edit_device(id):
    user = User.query.get(id)
    
    if user is not None:
        data = request.get_json()
        new_device_qty = data.get('device_qty')

        if new_device_qty is not None:
            user.device_qty = new_device_qty
            db.session.commit()
            return jsonify({"message": "Device quantity updated successfully"}), 200
        else:
            return jsonify({"error": "Invalid device quantity"}), 400
    else:
        return jsonify({"error": "User not found"}), 404


@app.route('/api/edit-user/<int:id>', methods=['PUT'])
def edit_user(id):
    user = User.query.get(id)
    if user:
        try:
            data = request.get_json()
            user.fname = data.get('fname', user.fname)
            user.lname = data.get('lname', user.lname)
            user.city = data.get('city', user.city)
            user.login = data.get('login', user.login)
            password = data.get('password', user.password)
            user.device_qty = data.get('device_qty', user.device_qty)
            
            if not re.fullmatch(regex, user.login):
                return jsonify({"error": "Login should be a valid Email address"}), 400

            if len(password) < 6:
                return jsonify({"error": "Password is too short"}), 400
            
            hashed_password = generate_password_hash(password)
            user.password = hashed_password

            db.session.commit()

            return jsonify({"message": "User updated successfully"}), 200
        except Exception as e:
            return jsonify({"error": "Login should be unique"}), 500
    else:
        return jsonify({"message": "User not found"}), 404

@app.route('/api/delete-user/<int:id>', methods=['DELETE'])
def delete_user(id):
    user = User.query.get(id)

    if user is not None:
        db.session.delete(user)
        db.session.commit()
        return jsonify({"message": "User deleted successfully!"}), 200
    else:
        return jsonify({"message": "User not found"}), 404
    

@app.route('/api/get-user/<string:login>', methods=['GET'])
def get_user_data(login):
    user = User.query.filter_by(login=login).first()

    if user is not None:
        user_data = {
            'id': user.id,
            'fname': user.fname,
            'lname': user.lname,
            'city': user.city,
            'login': user.login,
            'password': user.password,
            'device_qty': user.device_qty
        }

        return jsonify({'user': user_data})
    else:
        return jsonify({'error': 'User not found'}), 404

@app.route('/api/users', methods=['GET'])
def get_users():
    users = User.query.all()

    user_list = []
    for user in users:
        user_data = {
            'id': user.id,
            'fname': user.fname,
            'lname': user.lname,
            'city': user.city,
            'login': user.login,
            'password': user.password,
            'device_qty': user.device_qty
        }

        user_list.append(user_data)

    return jsonify({'users': user_list})

if __name__ == '__main__':
    app.run(debug=True, port=8000)