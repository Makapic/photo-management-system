# -*- coding: utf-8 -*-
from flask_login import current_user
from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed, FileRequired
from wtforms import StringField, PasswordField, SubmitField, TextAreaField, HiddenField, ValidationError
from wtforms.validators import DataRequired, Length, Email, EqualTo, Optional, Regexp

from pms.models import User


class EditProfileForm(FlaskForm):
    name = StringField('姓名', validators=[DataRequired(),
                                           Length(1, 30, message='长度1-30位。')])
    username = StringField('用户名', validators=[DataRequired(), Length(1, 20),
                                                   Regexp('^[a-zA-Z0-9]*$',
                                                          message='用户名应只包含数字与大小写字母。')])
    website = StringField('网站', validators=[Optional(), Length(0, 255)])
    location = StringField('城市', validators=[Optional(), Length(0, 50)])
    bio = TextAreaField('概述', validators=[Optional(), Length(0, 120)])
    submit = SubmitField('确定')

    def validate_username(self, field):
        if field.data != current_user.username and User.query.filter_by(username=field.data).first():
            raise ValidationError('用户名已被使用。')


class UploadAvatarForm(FlaskForm):
    image = FileField('上传图像', validators=[
        FileRequired(),
        FileAllowed(['jpg', 'png'], '文件格式应为 .jpg 或 .png.')
    ])
    submit = SubmitField('确定')


class CropAvatarForm(FlaskForm):
    x = HiddenField()
    y = HiddenField()
    w = HiddenField()
    h = HiddenField()
    submit = SubmitField('裁剪并更新')


class ChangeEmailForm(FlaskForm):
    email = StringField('新邮箱', validators=[DataRequired(), Length(1, 254), Email()])
    submit = SubmitField('确定')

    def validate_email(self, field):
        if User.query.filter_by(email=field.data.lower()).first():
            raise ValidationError('该邮箱已被使用。')


class ChangePasswordForm(FlaskForm):
    old_password = PasswordField('旧密码', validators=[DataRequired()])
    password = PasswordField('新密码', validators=[
        DataRequired(), Length(8, 128), EqualTo('password2')])
    password2 = PasswordField('确认密码', validators=[DataRequired()])
    submit = SubmitField('确定')


class DeleteAccountForm(FlaskForm):
    username = StringField('确认您的用户名', validators=[DataRequired(), Length(1, 20)])
    submit = SubmitField('永久注销')

    def validate_username(self, field):
        if field.data != current_user.username:
            raise ValidationError('用户名错误。')
