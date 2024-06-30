from database.database import User


def get_login(db, login):
    return db.query(User).filter(User.login == login).first()
