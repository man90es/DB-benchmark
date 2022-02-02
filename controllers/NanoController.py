import json
import requests


class NanoController():
	name = "NanoDB"

	def __init__(self, addr):
		self.addr = addr

	def _create_address(self, table, identifier):
		return "{}/{}:{}".format(self.addr, table, identifier)

	def create_one(self, identifier, data):
		addr = self._create_address("bench", identifier)
		# Returns True if record was created, otherwise False
		return requests.put(addr, data=json.dumps(data)).ok

	def read_one(self, identifier):
		addr = self._create_address("bench", identifier)
		# Returns data read from database as parsed JSON
		return requests.get(addr).json()

	def update_one(self, identifier, data):
		# Returns True if record was updated, otherwise False
		return self.create_one(identifier, data)

	def delete_one(self, identifier):
		addr = self._create_address("bench", identifier)
		# Returns True if record was deleted, otherwise False
		return requests.delete(addr).ok
