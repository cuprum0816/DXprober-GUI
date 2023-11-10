import sqlite3


class Database:
    def __init__(self):
        pass  # db_path is '/config/song.db'


def initialize(db_path='./config/song.db'):  # Database initialization
    conn = sqlite3.connect(db_path)
    csr = conn.cursor()
    csr.execute('CREATE TABLE SONGS\n'
                '                    (\n'
                '                    SongName varchar(255),\n'
                '                    Rating varchar(255),\n'
                '                    Date date,\n'
                '                    ')
