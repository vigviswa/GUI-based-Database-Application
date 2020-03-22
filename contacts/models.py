from . import db


class Contact(db.Model):
    contact_id = db.Column(db.Integer, primary_key=True)
    fname = db.Column(db.String(20), nullable=False)
    mname = db.Column(db.String(20), nullable=False)
    lname = db.Column(db.String(20), nullable=True)
    addresses = db.relationship(
        "Address", backref="contact", passive_deletes=True, lazy=True
    )
    phones = db.relationship(
        "Phone", backref="contact", passive_deletes=True, lazy=True
    )
    dates = db.relationship("Date", backref="contact", passive_deletes=True, lazy=True)

    def __repr__(self):
        return f"Contact({self.fname}, {self.lname}, {self.mname})"


class Address(db.Model):
    address_id = db.Column(db.Integer, primary_key=True)
    contact_id = db.Column(
        db.Integer,
        db.ForeignKey("contact.contact_id", ondelete="CASCADE"),
        nullable=False,
    )
    address_type = db.Column(db.String(20), nullable=False)
    address = db.Column(db.String(20), nullable=True)
    city = db.Column(db.String(20), nullable=True)
    state = db.Column(db.String(20), nullable=True)
    zip = db.Column(db.Integer, nullable=True)

    def __repr__(self):
        return f"Address({self.contact_id}, {self.address_type}, {self.address}, {self.city}, {self.state}, {self.zip})"


class Phone(db.Model):
    phone_id = db.Column(db.Integer, primary_key=True)
    contact_id = db.Column(
        db.Integer,
        db.ForeignKey("contact.contact_id", ondelete="CASCADE"),
        nullable=False,
    )
    phone_type = db.Column(db.String(20), nullable=False)
    area_code = db.Column(db.String(3), nullable=True)
    number = db.Column(db.String(7), nullable=True)

    def __repr__(self):
        return f"Phone({self.contact_id}, {self.phone_type}, {self.area_code}, {self.number})"


class Date(db.Model):
    date_id = db.Column(db.Integer, primary_key=True)
    contact_id = db.Column(
        db.Integer,
        db.ForeignKey("contact.contact_id", ondelete="CASCADE"),
        nullable=False,
    )
    date_type = db.Column(db.String(20), nullable=False)
    date = db.Column(db.Date, nullable=True)

    def __repr__(self):
        return f"Date({self.contact_id}, {self.date_type}, {self.date})"
