from db import Db


class User:
   def __init__(self):
       self.table = 'user'
       self.db = Db()



   def create(self, name, first_name, email, password):
       query = f'INSERT INTO {self.table} (name, first_name, email, password ) VALUES (%s, %s, %s, %s)'
       params = (name, first_name, email, password)
       self.db.executeQuery(query, params)


   def read(self):
       query = f'SELECT * FROM {self.table}'
       return self.db.fetch(query)


   def update(self, id, name, first_name, email, password):
       query = f'UPDATE {self.table} SET name=%s, first_name=%s, email=%s, password=%s WHERE id=%s'
       params = (name, first_name, email, password, id)
       self.db.executeQuery(query, params)


   def delete(self, id):
       query = f'DELETE FROM {self.table} WHERE id=%s'
       params = (id,)
       self.db.executeQuery(query, params)


   def find(self, id):
       query = f'SELECT * FROM {self.table} WHERE id=%s'
       params = (id,)
       return self.db.fetch(query, params)
