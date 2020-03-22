from sqlalchemy import or_
from .models import Contact, Phone, Address, Date


def db_search(search_string):
    search = f"%{search_string}%"
    return (
        Contact.query.outerjoin(Phone)
        .outerjoin(Address)
        .outerjoin(Date)
        .filter(
            or_(
                Contact.fname.like(search),
                Contact.lname.like(search),
                Contact.mname.like(search),
                Phone.phone_type.like(search),
                Phone.area_code.like(search),
                Phone.number.like(search),
                Address.address_type.like(search),
                Address.address.like(search),
                Address.city.like(search),
                Address.state.like(search),
                Address.zip.like(search),
                Date.date_type.like(search),
                Date.date.like(search),
            )
        )
    )
