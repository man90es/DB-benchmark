import psycopg2


class PostgresController():
	name = "PostgreSQL"

	def __init__(self, user, password, host, port, db):
		self.conn = psycopg2.connect(user=user, password=password, host=host, port=port, database=db)
		self.conn.autocommit = True
		self.cur = self.conn.cursor()
		self.cur.execute("drop table if exists bench")
		self.cur.execute("create table bench (id serial primary key, stringvar varchar, numbervar integer)")

	def create_one(self, identifier, data):
		self.cur.execute("insert into bench (id, stringvar, numbervar) values (%s, %s, %s)", (identifier, data["stringvar"], data["numbervar"]))
		return self.cur.rowcount

	def read_one(self, identifier):
		self.cur.execute("select * from bench where id = %s", (identifier,))
		return self.cur.fetchone()

	def update_one(self, identifier, data):
		self.cur.execute("update bench set stringvar = %s, numbervar = %s where id = %s", (data["stringvar"], data["numbervar"], identifier))
		return self.cur.rowcount

	def delete_one(self, identifier):
		self.cur.execute("delete from bench where id = %s", (identifier,))
		return self.cur.rowcount
