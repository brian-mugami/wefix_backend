from flask import request, jsonify
from flask.views import MethodView
from flask_smorest import Blueprint,abort
from .models import UserModel
from werkzeug.security import generate_password_hash,check_password_hash
from .db import db
from producer import publish
from .schemas import UserSchema, LoginSchema
from flask import session

auth = Blueprint("auth", __name__, description="Authentication blueprint")

@auth.route("/register")
class RegisterView(MethodView):
    @auth.arguments(UserSchema)
    @auth.response(201, UserSchema)
    def post(self, data):
        user = UserModel.query.filter_by(email=data["email"]).first()
        if user:
            abort(409, message="User already exists")
        first_name = data["first_name"]
        last_name = data["last_name"]
        company_name = data["company_name"]
        password = data["password"]
        email = data["email"]
        phone = data["phone"]
        image = data["image"]
        location = data["location"]
        usertype = data["usertype"]
        new_user = UserModel(
            first_name= first_name,
            last_name= last_name,
            company_name=company_name,
            password=generate_password_hash(password, "sha256"),
            email=email,
            phone=phone,
            image=image,
            location=location,
            usertype=usertype
        )
        db.session.add(new_user)
        db.session.commit()
        publish("user created", new_user.json())

        return new_user

@auth.route("/login")
class LoginUser(MethodView):
    @auth.arguments(LoginSchema)
    @auth.response(202, LoginSchema)
    def post(self,data):
        user = UserModel.query.filter_by(email=data["email"]).first()
        if user is not None:
            if check_password_hash(user.password, data["password"]):
                session["user_id"] = user.id #session.get("user_id")
                return user
            else:
                abort(400, message="User password is wrong")
        else:
            abort(404, message="User not found")

