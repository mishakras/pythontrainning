import sqlite3


class TableData:
    def __init__(self, database, table_name):
        self.cursor = sqlite3.connect(database).cursor()
        self.table_name = table_name

    def __len__(self):
        self.cursor.execute('SELECT COUNT(*) from ' + self.table_name)
        return self.cursor.fetchone()[0]

    def __getitem__(self, name):
        self.cursor.execute('SELECT * from ' + self.table_name +
                            ' where name=?', (name,))
        return self.cursor.fetchone()

    def __contains__(self, name):
        self.cursor.execute('SELECT * from ' + self.table_name +
                            ' where name=?', (name,))
        return bool(self.cursor.fetchone())

    def __iter__(self):
        self.cursor.execute('SELECT * from ' + self.table_name)
        return self

    def __next__(self):
        row = self.cursor.fetchone()
        if row:
            return row
        else:
            raise StopIteration
