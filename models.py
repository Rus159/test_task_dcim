from extensions import db


class Room(db.Model):
    __tablename__ = 'room'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(64), unique=True, nullable=False)
    racks = db.relationship('Rack', lazy='dynamic')

    def to_dict(self):
        data = {
            'id': self.id,
            'name': self.name,
        }
        return data

    def __repr__(self):
        return f'<Room {self.name}>'


class Customer(db.Model):
    __tablename__ = 'customer'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(64), nullable=False)
    racks = db.relationship('Rack', lazy='dynamic')

    def to_dict(self):
        data = {
            'id': self.id,
            'name': self.name,
        }
        return data

    def __repr__(self):
        return f'<Customer id {self.id} {self.name}>'


class Rack(db.Model):
    __tablename__ = 'rack'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(64), nullable=False)
    size = db.Column(db.Integer, nullable=False)
    state = db.Column(db.String(64), nullable=False)
    customer = db.Column(db.Integer, db.ForeignKey('customer.id'))
    room_id = db.Column(db.Integer, db.ForeignKey('room.id'))

    def to_dict(self):
        data = {
            'id': self.id,
            'name': self.name,
            'size': self.size,
            'state': self.state,
            'customer': self.customer,
            'room_id': self.room_id,
        }
        return data

    def __repr__(self):
        return f'<Rack {self.name}>'
