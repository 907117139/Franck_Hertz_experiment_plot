from flask_wtf import FlaskForm
from wtforms import FloatField,SubmitField, StringField
from wtforms.validators import DataRequired, InputRequired

def set_Frank_hertzForm(k):
    for i in range(k):
        setattr(Frank_hertzForm, 'point_' + str(i), FloatField(str(i/2) + 'V',validators=[InputRequired()]))

def set_Frank_hertzForm_1(k):
    for i in range(k):
        setattr(Frank_hertzForm_1, 'form1_point_' + str(i), FloatField(str(i / 2) + 'V', validators=[InputRequired()]))

def set_Frank_hertzForm_2(k):
    for i in range(k):
        setattr(Frank_hertzForm_2, 'form2_point_' + str(i), FloatField(str(i / 2) + 'V', validators=[InputRequired()]))

def set_Frank_hertzForm_3(k):
    for i in range(k):
        setattr(Frank_hertzForm_3, 'form3_point_' + str(i), FloatField(str(i / 2) + 'V', validators=[InputRequired()]))

def set_Frank_hertzForm_4(k):
    for i in range(k):
        setattr(Frank_hertzForm_4, 'form4_point_' + str(i), FloatField(str(i / 2) + 'V', validators=[InputRequired()]))

# 'point_' + str(i),point
# point_1, ponit_2
class Frank_hertzForm(FlaskForm):
    submit = SubmitField('提交')
    # point_0 = FloatField('point_0', validators=[DataRequired()])

    # def __init__(self, k):
    #     super(Frank_hertzForm, self).__init__()
    #     for i in range(k):
    #         setattr(self, 'point_' + str(i), FloatField(str(i/2) + 'V',validators=[DataRequired()]))

class Frank_hertzForm_1(FlaskForm):
    submit1 = SubmitField('提交')
    name1 = StringField('曲线名称', validators=[DataRequired()])


class Frank_hertzForm_2(FlaskForm):
    submit2 = SubmitField('提交')
    name2 = StringField('曲线名称', validators=[DataRequired()])


class Frank_hertzForm_3(FlaskForm):
    submit3 = SubmitField('提交')
    name3 = StringField('曲线名称', validators=[DataRequired()])


class Frank_hertzForm_4(FlaskForm):
    submit4 = SubmitField('提交')
    name4 = StringField('曲线名称', validators=[DataRequired()])