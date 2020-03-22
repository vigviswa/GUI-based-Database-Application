from datetime import datetime
from . import db
from .models import Contact, Phone, Address, Date


def db_add_contact(fname, lname, mname, phones, addresses, dates):
    new_contact = create_contact(fname, lname, mname, phones, addresses, dates)
    db.session.add(new_contact)
    db.session.commit()


def db_upd_contact(contact_id, fname, lname, mname, phones, addresses, dates):
    Contact.query.filter_by(contact_id=contact_id).delete()
    db.session.commit()
    new_contact = create_contact(
        fname, lname, mname, phones, addresses, dates, contact_id
    )
    db.session.add(new_contact)
    db.session.commit()


def create_contact(fname, lname, mname, phones, addresses, dates, contact_id=None):
    new_contact = Contact(fname=fname, lname=lname, mname=mname, contact_id=contact_id)
    list_phones = []
    list_addresses = []
    list_dates = []
    phones = [d for d in phones if d["phone_type"] not in ["", None]]
    for phone in phones:
        list_phones.append(
            Phone(
                phone_type=phone["phone_type"],
                area_code=phone["area_code"],
                number=phone["number"],
            )
        )
    addresses = [d for d in addresses if d["address_type"] is not ""]
    for address in addresses:
        try:
            zip_from_form = int(address["zip"])
            list_addresses.append(
                Address(
                    address_type=address["address_type"],
                    address=address["address"],
                    city=address["city"],
                    state=address["state"],
                    zip=zip_from_form,
                )
            )
        except ValueError:
            pass
    dates = [d for d in dates if d["date_type"] is not ""]
    for date in dates:
        try:
            date_from_form = datetime.strptime(date["date"], "%Y-%m-%d").date()
            list_dates.append(Date(date_type=date["date_type"], date=date_from_form))
        except ValueError:
            pass
    if len(list_addresses) > 0:
        new_contact.addresses = list_addresses
    if len(list_phones) > 0:
        new_contact.phones = list_phones
    if len(list_dates) > 0:
        new_contact.dates = list_dates
    return new_contact
