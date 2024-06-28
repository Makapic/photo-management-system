# -*- coding: utf-8 -*-
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms import ValidationError
from wtforms.validators import DataRequired, Length, Email, EqualTo, Regexp

from pms.models import User


class LoginForm(FlaskForm):
    email = StringField('邮箱', validators=[DataRequired(), Length(1, 254), Email()])
    password = PasswordField('密码', validators=[DataRequired()])
    remember_me = BooleanField('记住密码')
    submit = SubmitField('登录')


class RegisterForm(FlaskForm):
    name = StringField('姓名', validators=[DataRequired(),
                                           Length(1, 30, message='姓名长度1-30位。')])
    email = StringField('邮箱', validators=[DataRequired(), Length(1, 254),
                                            Email(message='请填写正确的邮箱。')])
    username = StringField('用户名', validators=[DataRequired(),
                                                 Length(1, 20, message='长度1-20位。'),
                                                 Regexp('^[a-zA-Z0-9]*$',
                                                        message='用户名应只包含数字和大小写字母。')])
    password = PasswordField('密码', validators=[
        DataRequired(), Length(8, 128, message='密码长度8-128位。'),
        EqualTo('password2', message='两次输入不一致。')])
    password2 = PasswordField('确认密码', validators=[DataRequired()])
    submit = SubmitField('提交')

    def validate_email(self, field):
        if User.query.filter_by(email=field.data.lower()).first():
            raise ValidationError('该邮箱已被使用。')

    def validate_username(self, field):
        if User.query.filter_by(username=field.data).first():
            raise ValidationError('用户名已被使用。')


class ForgetPasswordForm(FlaskForm):
    email = StringField('邮箱', validators=[DataRequired(), Length(1, 254),
                                            Email(message='请填写正确的邮箱。')])
    submit = SubmitField("确认")


class ResetPasswordForm(FlaskForm):
    email = StringField('邮箱', validators=[DataRequired(), Length(1, 254),
                                            Email(message='请填写正确的邮箱。')])
    password = PasswordField('新密码', validators=[
        DataRequired(), Length(8, 128, message='密码长度8-128位。'),
        EqualTo('password2', message='两次输入不一致。')])
    password2 = PasswordField('确认密码', validators=[DataRequired()])
    submit = SubmitField("确认")
