from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager, create_access_token
from werkzeug.security import generate_password_hash, check_password_hash
# migrate
from flask_migrate import Migrate
from sqlalchemy import text
from dotenv import load_dotenv
import os
import re

# Load environment variables from .env file
load_dotenv()

# create the app
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL')
app.config['JWT_SECRET_KEY'] = os.environ.get('SECRET_KEY')


# this variable, db, will be used for all SQLAlchemy commands
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
def create_admin_profile():
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

@app.route('/admin/login', methods=['POST'])
def admin_login():
    data = request.get_json()
    login = data.get('login')
    password = data.get('password')

    if not login or not password:
        return jsonify({'error': 'Both login and password are required'}), 400
    
    admin = Admin.query.filter_by(login=login).first()

    if admin and check_password_hash(admin.password, password):
        access_token = create_access_token(identity=admin.id)
        return jsonify(access_token=access_token), 200
    else:
        return jsonify({'error': 'Invalid login credentials'}), 401

@app.route('/signup', methods=['POST'])
def signup():
    data = request.get_json()
    user_exists = User.query.filter_by(email=data['email']).first()

    if user_exists:
        return jsonify({"error": "Email is already registered"}), 400

    if not re.fullmatch(regex, data['email']):
        return jsonify({"error": "Invalid Email"}), 400
    
    if len(data['password']) < 6:
        return jsonify({"error": "Invalid Password"}), 400
    
    hashed_password = generate_password_hash(data['password'], method='sha256')
    new_user = User(email=data['email'], password=hashed_password)
    db.session.add(new_user)
    db.session.commit()
    return jsonify({"message": "User registered successfully"}), 200
    

@app.route('/signin', methods=['POST'])
def signin():
    data = request.get_json()
    user = User.query.filter_by(email=data['email']).first() 
    print("Req data =>", data)
    print("DB query user", user)
    
    if user is None:
        return jsonify({"error": "Unauthorized"}), 401

    if not check_password_hash(user.password, data['password']):
        return jsonify({"error": "Invalid credentials!"}), 401
    access_token = create_access_token(identity=user.email)  
    email = user.email
    return jsonify({"email": email,"access_token": access_token})

@app.route('/delete-user/<int:id>', methods=['DELETE'])
def delete_user(id):
    user = User.query.get(id)

    if user is not None:
        db.session.delete(user)
        db.session.commit()
        return jsonify({"message": "Organization deleted successfully!"}), 200
    else:
        return jsonify({"message": "Organization not found"}), 404

    
if __name__ == '__main__':
    app.run(debug=True, port=8000)