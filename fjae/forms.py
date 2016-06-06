from flask.ext.wtf import Form
from wtforms.fields import SelectField


class VehicleForm(Form):
    make = SelectField(u'', choices=())
    model = SelectField(u'', choices=())
