import sqlite3


class TableData:
    def __init__(self, database, name):
        self.cursor = sqlite3.connect(database).cursor()
        self.name = name
        self.pos = 1
        self.iter = 0

    def __len__(self):
        temp = 0
        self.cursor.execute('SELECT * from ' + self.name)
        while _ := self.cursor.fetchone():
            temp += 1
        return temp

    def __getitem__(self, pred_name):
        self.cursor.execute('SELECT * from ' + self.name + ' where name=?',
                            (pred_name,))
        return self.cursor.fetchone()

    def __contains__(self, name):
        self.cursor.execute('SELECT * from ' + self.name)
        while row := self.cursor.fetchone():
            if row[0] == name:
                return True
        return False

    def __iter__(self):
        return self.gen()

    def gen(self):
        self.cursor.execute('SELECT * from ' + self.name)
        while row := self.cursor.fetchone():
            yield row
        return
