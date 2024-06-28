# -*- coding: utf-8 -*-
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Optional, Length


class DescriptionForm(FlaskForm):
    description = TextAreaField('描述', validators=[Optional(),
                                                    Length(0, 500, message='最大长度500。')])
    submit = SubmitField("保存")


class TagForm(FlaskForm):
    tag = StringField('编辑类别', validators=[Optional(),
                                              Length(0, 64, message='最大长度40。')])
    submit = SubmitField("保存")
