import sqlite3


class TableData:
    def __init__(self, database, table_name):
        self.cursor = sqlite3.connect(database).cursor()
        self.name = table_name
        self.pos = 1
        self.iter = 0

    def __len__(self):
        temp = 0
        self.cursor.execute('SELECT * from ' + self.name)
        while _ := self.cursor.fetchone():
            temp += 1
        return temp

    def __getitem__(self, name):
        self.cursor.execute('SELECT * from ' + self.name + ' where name=?',
                            (name,))
        return self.cursor.fetchone()

    def __contains__(self, name):
        self.cursor.execute('SELECT * from ' + self.name + ' where name=?',
                            (name,))
        if self.cursor.fetchone():
            return True
        return False

    def __iter__(self):
        self.iteration = self.gen()
        return self

    def __next__(self):
        return next(self.iteration)

    def gen(self):
        self.cursor.execute('SELECT * from ' + self.name)
        while row := self.cursor.fetchone():
            yield row
        return
