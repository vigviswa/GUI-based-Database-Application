from flask_wtf import FlaskForm as Form
from wtforms import Form as NoCsrfForm
from wtforms import FieldList
from wtforms.fields import StringField, FormField, SubmitField
from wtforms.validators import DataRequired, Length
from .models import Address, Phone, Date


class SearchForm(Form):
    search_string = StringField(
        "Search", validators=[DataRequired(), Length(min=1, max=20)]
    )
    submit = SubmitField("Search")


class AddPhoneForm(NoCsrfForm):
    phone_type = StringField("Type of Number")
    area_code = StringField("Area Code")
    number = StringField("Number")


class AddAddressForm(NoCsrfForm):
    address_type = StringField("Type of Address")
    address = StringField("Street Address")
    city = StringField("City")
    state = StringField("State")
    zip = StringField("Zip Code")


class AddDateForm(NoCsrfForm):
    date_type = StringField("Type of Date")
    date = StringField("Calendar Date")


class AddContactForm(Form):
    fname = StringField(
        "First Name", validators=[DataRequired(), Length(min=1, max=20)]
    )
    mname = StringField("Middle Name")
    lname = StringField("Last Name", validators=[DataRequired(), Length(min=1, max=20)])
    # we must provide empth Phone() instances else populate_obj will fail
    phones = FieldList(FormField(AddPhoneForm, default=lambda: Phone()))
    addresses = FieldList(FormField(AddAddressForm, default=lambda: Address()))
    dates = FieldList(FormField(AddDateForm, default=lambda: Date()))
    submit = SubmitField("Submit")
