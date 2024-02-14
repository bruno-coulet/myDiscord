from db import Db


class Message:
    def __init__(self):
       self.table = 'message'
       self.db = Db()


    def create(self, name, channel_id, content):
       query = f'INSERT INTO {self.table} (name, channel, content) VALUES (%s, %s, %s)'
       params = (name, channel_id, content)
       self.db.executeQuery(query, params)



    def read(self):
       query = f'SELECT * FROM {self.table}'
       return self.db.fetch(query)


    def update(self, id, name, channel_id, content):
       query = f'UPDATE {self.table} SET name=%s, channel_id=%s, content=%s WHERE id=%s'
       params = (name, channel_id, content, id)
       self.db.executeQuery(query, params)


    def delete(self, id):
       query = f'DELETE FROM {self.table} WHERE id=%s'
       params = (id,)
       self.db.executeQuery(query, params)


    def find(self, id):
       query = f'SELECT * FROM {self.table} WHERE id=%s'
       params = (id,)
       return self.db.fetch(query, params)

