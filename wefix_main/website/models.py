import enum
from dataclasses import dataclass
from datetime import datetime
from .db import db


class ChargeChoices(enum.Enum):
    PER_HOUR = "PER_HOUR"
    PER_DAY = "PER_DAY"
    PER_MONTH = "PER_MONTH"
    PER_YEAR = "PER_YEAR"


class ExperienceChoices(enum.Enum):
    one_year = "< 1 YEAR"
    one_year_plus = "> 1 YEAR"
    three_years = "3 YEARS +"


class DurationChoices(enum.Enum):
    one_week = "1 WEEK"
    one_day = "1 DAY"
    one_month = "LESS THAN A MONTH"
    three_months = "LESS THAN 3 MONTHS"
    one_year = "1 YEAR"
    other = "OTHER"


class WorkerChoices(enum.Enum):
    WORKER = "WORKER"
    SEEKER = "SEEKER"
    COMPANY = "COMPANY"

class UserModel(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True, unique=True)
    usertype = db.Column(db.String(), db.Enum(WorkerChoices))
    first_name = db.Column(db.String())
    last_name = db.Column(db.String())
    company_name = db.Column(db.String())
    password = db.Column(db.String(), nullable=False)
    email = db.Column(db.String(), unique=True)
    phone = db.Column(db.String(), unique=True)
    register_date = db.Column(db.DateTime, default=datetime.utcnow())
    image = db.Column(db.String())
    location = db.Column(db.Integer, db.ForeignKey("locations.id", ondelete="SET NULL"), nullable=True)

    worker = db.relationship("WorkersModel", lazy="dynamic")
    seeker = db.relationship("SeekersModel", lazy="dynamic")

    def json(self):
        return {
            "usertype": self.usertype,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "company_name": self.company_name,
            "email": self.email,
            "phone": self.phone,
            "password": self.password,
            "image": self.image,
            "location": self.location
        }

class LocationModel(db.Model):
    __tablename__ = "locations"
    id = db.Column(db.Integer, primary_key=True, autoincrement=False)
    name = db.Column(db.String(), unique=True)

    users = db.relationship("UserModel", lazy="dynamic")

class WorkersModel(db.Model):
    __tablename__ = "workers"

    id = db.Column(db.Integer, primary_key=True)
    availability = db.Column(db.Boolean, default=True)
    charge = db.Column(db.Integer)
    charge_type = db.Column(db.Enum(ChargeChoices))
    experience = db.Column(db.Enum(ExperienceChoices))
    work_description = db.Column(db.String())
    user_id = db.Column(db.Integer, db.ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
    work_type = db.Column(db.Integer, db.ForeignKey("worktypes.id", ondelete="SET NULL"), nullable=True)

    seeker = db.relationship("SeekersModel", secondary="connection", back_populates="worker")


class SeekersModel(db.Model):
    __tablename__ = "seekers"

    id = db.Column(db.Integer, primary_key=True)
    job_description = db.Column(db.String())
    duration = db.Column(db.Enum(DurationChoices))
    image = db.Column(db.String())
    user_id = db.Column(db.Integer, db.ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
    worktype = db.Column(db.Integer, db.ForeignKey("worktypes.id", ondelete="SET NULL"), nullable=True)

    worker = db.relationship("WorkersModel", secondary="connection", back_populates="seeker")


@dataclass
class WorkerTypeModel(db.Model):
    __tablename__ = "worktypes"
    id: int
    name: str

    id = db.Column(db.Integer, primary_key=True, autoincrement=False)
    name = db.Column(db.String(), unique=True)

    workers = db.relationship("WorkersModel", lazy="dynamic")
    seekers = db.relationship("SeekersModel", lazy="dynamic")


class ConnectionModel(db.Model):
    __tablename__ = "connection"
    __table_args__ = (db.UniqueConstraint("seeker_id", "worker_id", name="unique_seeker_worker"),)

    id = db.Column(db.Integer, primary_key=True)
    worker_id = db.Column(db.Integer, db.ForeignKey("workers.id", ondelete="CASCADE"), nullable=False)
    seeker_id = db.Column(db.Integer, db.ForeignKey("seekers.id", ondelete="CASCADE"), nullable=False)
    likes = db.Column(db.Integer, default=0)
    comments = db.Column(db.String())
