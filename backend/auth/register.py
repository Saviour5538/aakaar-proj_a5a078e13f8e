from flask import Blueprint, request, jsonify
from flask_jwt_extended import create_access_token, get_jwt_identity
from werkzeug.security import generate_password_hash, check_password_hash
from backend.database import db
from backend.models import User
from backend.utils import send_email

auth_blueprint = Blueprint('auth', __name__)

@auth_blueprint.route('/api/v1/auth/register', methods=['POST'])
def register_user():
    try:
        data = request.get_json()
        if not data:
            return jsonify({'message': 'No data provided'}), 400
        email = data.get('email')
        password = data.get('password')
        if not email or not password:
            return jsonify({'message': 'Email and password are required'}), 400
        existing_user = User.query.filter_by(email=email).first()
        if existing_user:
            return jsonify({'message': 'User already exists'}), 400
        new_user = User(email=email, password=generate_password_hash(password))
        db.session.add(new_user)
        db.session.commit()
        send_email(email, 'Registration successful')
        return jsonify({'message': 'User created successfully'}), 201
    except Exception as e:
        return jsonify({'message': str(e)}), 500

@auth_blueprint.route('/api/v1/auth/login', methods=['POST'])
def login_user():
    try:
        data = request.get_json()
        if not data:
            return jsonify({'message': 'No data provided'}), 400
        email = data.get('email')
        password = data.get('password')
        if not email or not password:
            return jsonify({'message': 'Email and password are required'}), 400
        user = User.query.filter_by(email=email).first()
        if not user:
            return jsonify({'message': 'User does not exist'}), 400
        if not check_password_hash(user.password, password):
            return jsonify({'message': 'Invalid password'}), 400
        access_token = create_access_token(identity=user.id)
        return jsonify({'access_token': access_token}), 200
    except Exception as e:
        return jsonify({'message': str(e)}), 500

@auth_blueprint.route('/api/v1/projects', methods=['GET'])
def get_projects():
    try:
        projects = Project.query.all()
        return jsonify([project.to_dict() for project in projects]), 200
    except Exception as e:
        return jsonify({'message': str(e)}), 500

@auth_blueprint.route('/api/v1/projects', methods=['POST'])
def create_project():
    try:
        data = request.get_json()
        if not data:
            return jsonify({'message': 'No data provided'}), 400
        name = data.get('name')
        if not name:
            return jsonify({'message': 'Project name is required'}), 400
        new_project = Project(name=name)
        db.session.add(new_project)
        db.session.commit()
        return jsonify({'message': 'Project created successfully'}), 201
    except Exception as e:
        return jsonify({'message': str(e)}), 500