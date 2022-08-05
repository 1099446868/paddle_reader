import sqlite3


class DB(object):
    table_name = ''
    where_sql = ' '
    select_sql = ' '
    cursor = None

    def __init__(self):
        self.conn = sqlite3.connect('reader.db')
        self.c = self.conn.cursor()

    def table(self, table_name):
        self.table_name = table_name
        return self

    # param dict data
    def insert(self, data):
        fields = ''
        value = ''
        for key, val in data.items():
            fields += str(key) + ','
            value += "'" + str(val) + "',"
        fields = fields[:-1]
        value = value[:-1]
        sql = "insert into " + self.table_name + ' (' + fields + ') values(' + value + ')'
        print(sql)
        self.execute(sql)

    # param dict data
    def where(self, data):
        where_sql = ' '
        for key, val in data.items():
            where_sql += str(key) + '=' + str(val) + ' and'
        self.where_sql = where_sql[:-3]
        return self

    # param list data|*
    def select(self, data):
        if data == '*':
            select_sql = ' * '
        else:
            select_sql = ' '
            for val in data:
                select_sql += str(val) + ','
            select_sql = select_sql[:-1]

        sql = "select " + select_sql + " from " + self.table_name
        if self.where_sql != ' ':
            sql += " where " + self.where_sql
        self.query(sql)
        return self

    def query(self, sql):
        self.cursor = self.c.execute(sql)
        return self

    def first(self):
        res = []
        for row in self.cursor:
            res.append(row)
        if not res:
            return ()
        return res[0]

    def get(self):
        res = []
        for row in self.cursor:
            res.append(row)
        return res

    def execute(self, sql):
        self.c.execute(sql)
        self.conn.commit()

    def close(self):
        self.conn.close()
        self.conn = None
