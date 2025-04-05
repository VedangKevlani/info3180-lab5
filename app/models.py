from . import db
import pytz
from datetime import datetime

timezone = pytz.timezone('UTC')

class Movie(db.Model):
    __tablename__ = "movies"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    poster = db.Column(db.String(255), nullable=False)
    created_at = db.Column(db.DateTime, default=lambda: datetime.now(timezone))
    director = db.Column(db.String(100))  # Example new field

    def __repr__(self):
        return f"<Movie Name {self.title}>"
