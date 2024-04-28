from sqlalchemy import event
from . import tables

SEED_DATA = {
      'roles': [
            {
                  'role': 'user',
            },
            {
                  'role': 'seller',
            },
            {
                  'role': 'root',
            }
      ]
}

def initialize_table(target, connection, **kw):
    tablename = str(target)
    if tablename in SEED_DATA and len(SEED_DATA[tablename]) > 0:
        connection.execute(target.insert(), SEED_DATA[tablename])

def add_role_seed_event():
    event.listen(tables.Role.__table__,"after_create",initialize_table)