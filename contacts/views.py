from loguru import logger
from flask import Blueprint, render_template, redirect, request
from . import db
from .models import Contact, Phone, Address, Date
from .forms import SearchForm, AddContactForm
from .utils import db_add_contact, db_upd_contact
from .search import db_search

contact = Blueprint("contact", __name__)


@contact.route("/", methods=["GET", "POST"])
def list_contact():
    contacts = Contact.query.all()
    form = SearchForm()
    if form.is_submitted():
        logger.info(form.search_string.data)
        return redirect(f"/search/{form.search_string.data}")
    return render_template("list.html", contacts=contacts, form=form)


@contact.route("/search/<search_string>")
def search_contact(search_string):
    contacts = []
    if search_string != "":
        contacts = db_search(search_string)
    return render_template("search.html", contacts=contacts)


@contact.route("/view/<int:contact_id>")
def view_contact(contact_id):
    return render_template("view.html", contact_id=contact_id)


@contact.route("/delete/<int:contact_id>")
def del_contact(contact_id):
    form_contact = Contact.query.filter_by(contact_id=contact_id).first_or_404()
    db.session.delete(form_contact)
    db.session.commit()
    return redirect("/")


@contact.route("/add", methods=["GET", "POST"])
def add_contact():
    form_contact = Contact()
    form_contact.phones = [Phone()]
    form_contact.addresses = [Address()]
    form_contact.dates = [Date()]

    form = AddContactForm(obj=form_contact)

    if form.validate_on_submit():
        db_add_contact(
            form.fname.data,
            form.lname.data,
            form.mname.data,
            form.phones.data,
            form.addresses.data,
            form.dates.data,
        )
        return redirect("/")
    return render_template("add.html", form=form)


@contact.route("/edit/<int:contact_id>", methods=["GET", "POST"])
def edit_contact(contact_id):
    from_database_contact = Contact.query.filter_by(
        contact_id=contact_id
    ).first_or_404()
    form_contact = Contact(
        fname=from_database_contact.fname,
        lname=from_database_contact.lname,
        mname=from_database_contact.mname,
    )
    form_contact.phones = []
    form_contact.addresses = []
    form_contact.dates = []
    if len(from_database_contact.phones) != 0:
        for phone in from_database_contact.phones:
            next_phone = Phone(
                phone_type=phone.phone_type,
                area_code=phone.area_code,
                number=phone.number,
            )
            form_contact.phones.append(next_phone)
    else:
        form_contact.phones = [Phone()]
    if len(from_database_contact.addresses) != 0:
        for address in from_database_contact.addresses:
            next_address = Address(
                address_type=address.address_type,
                address=address.address,
                city=address.city,
                state=address.state,
                zip=address.zip,
            )
            form_contact.addresses.append(next_address)
    else:
        form_contact.addresses = [Address()]
    if len(from_database_contact.dates) != 0:
        for date in from_database_contact.dates:
            next_date = Date(date_type=date.date_type, date=date.date)
            form_contact.dates.append(next_date)
    else:
        form_contact.dates = [Date()]

    form = AddContactForm(obj=form_contact)
    if form.validate_on_submit():
        db_upd_contact(
            contact_id,
            form.fname.data,
            form.lname.data,
            form.mname.data,
            form.phones.data,
            form.addresses.data,
            form.dates.data,
        )
        return redirect("/")
    return render_template("edit.html", form=form)
