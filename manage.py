from . import create_app,db

from .models import User,Role

@manager.shell
def make_shell_context():
    return dict(db = db,User = User, Role = Role)
if __name__ == '__main__':
    manager.run()
