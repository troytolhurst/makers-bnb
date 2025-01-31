from peewee import *
from creds import *
from lib.person import Person
from lib.space import Space

db = PostgresqlDatabase(db_name, user=user, password=password, host=host)


class Booking(Model):
    id = AutoField()
    space_id = ForeignKeyField(Space, backref="bookings")
    start_date = DateField()
    end_date = DateField()
    approved = BooleanField(default=False)
    response = BooleanField(default=False)
    user_id = ForeignKeyField(Person)

    class Meta:
        database = db
