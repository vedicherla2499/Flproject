from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()
class EmployeeTable(db.Model):
    __tablename__='Fun'
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(50),nullable=True)
    age=db.Column(db.Integer,nullable=True)
    salary=db.Column(db.Integer,nullable=True)

