from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.fields.html5 import EmailField
from wtforms.validators import Length, required, EqualTo
from wtforms_alchemy import Unique
from wtforms_components import Email, ModelForm

from app.models.application.user import UserModel


class SignUpForm(ModelForm):
    username = StringField('ID', [
        required(message='ID는 필수 항목입니다.'),
        Length(min=4, max=20, message='%(min)d글자 이상 %(max)d글자 이하로 입력해주세요.'),
        Unique(UserModel.username, message='이미 존재하는 아이디입니다.')
    ])
    password = PasswordField('Password', [
        required(message='비밀번호는 필수 항목입니다.'),
        Length(min=6, max=20, message='%(min)d 이상 %(max)d 이하로 입력해주세요.')
    ])
    confirm_password = PasswordField('Confirm Password', [
        required(message='비밀번호 확인값은 필수 항목입니다.'),
        EqualTo('password', message='비밀번호와 비밀번호 확인값이 일치하지 않습니다.')
    ])
    name = StringField('Name', [
        required(message='이름은 필수 항목입니다.'),
        Length(min=2, max=10, message='%(min)d 이상 %(max)d 이하로 입력해주세요.')
    ])
    nickname = StringField('Nickname', [
        required(message='닉네임은 필수 항목입니다.'),
        Length(min=4, max=20),
        Unique(UserModel.nickname, message='이미 존재하는 닉네임입니다.')
    ])
    email = EmailField('Email', [
        required(message='이메일은 필수 항목입니다.'),
        Email(message='유효한 이메일 주소를 입력해주세요.'),
        Unique(UserModel.email, message='이미 존재하는 이메일입니다.')
    ])
    company = StringField('Company', [
        required(message='소속은 필수 항목입니다.'),
        Length(min=2, max=20, message='%(min)d 이상 %(max)d 이하로 입력해주세요.')
    ])


class SignInForm(FlaskForm):
    username = StringField('ID', [
        required(message='ID는 필수 항목입니다.'),
        Length(min=4, max=20, message='%(min)d글자 이상 %(max)d글자 이하로 입력해주세요.'),
    ])
    password = PasswordField('Password', [
        required(message='비밀번호는 필수 항목입니다.'),
        Length(min=6, max=20, message='%(min)d 이상 %(max)d 이하로 입력해주세요.')
    ])
