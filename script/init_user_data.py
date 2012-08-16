#encoding=utf-8
from pycms.account.model import User
from pycms.db.util import DBSession


def init():
    session = DBSession()

    admin = User(username='admin', email='admin@xxxx.com')
    admin.set_password('asdfjk')
    admin.is_active=True
    admin.is_superuser=True

    ahao = User(username='ahao', email='ahao@163.com')
    ahao.set_password('asdfjk')

    session.add(admin)
    session.add(ahao)
    session.commit()

if __name__ == '__main__':
    init()
