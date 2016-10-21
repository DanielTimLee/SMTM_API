import datetime

from sqlalchemy.dialects.mysql import BIGINT
from sqlalchemy.dialects.mysql import TIMESTAMP
from sqlalchemy.sql.expression import text

from app import app, db


class BoardModel(db.Model):
    __bind_key__ = app.config.get('DEFAULT_DATABASE')
    __tablename__ = 'boards'
    __table_args__ = {
        'schema': __bind_key__,
        'mysql_engine': 'InnoDB',
        'mysql_charset': 'utf8',
        'extend_existing': True
    }

    id = db.Column(
        BIGINT(20, unsigned=True),
        primary_key=True,
        index=True
    )
    name = db.Column(
        db.String(80),
        unique=True,
        nullable=False
    )
    title = db.Column(
        db.String(100),
        nullable=False
    )
    created_date = db.Column(
        TIMESTAMP,
        default=datetime.datetime.utcnow,
        server_default=text('CURRENT_TIMESTAMP')
    )

    documents = db.relationship(
        'DocumentModel',
        backref='board',
        lazy='dynamic'
    )
