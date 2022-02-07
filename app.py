#!/usr/bin/python

from dotenv import dotenv_values
from timeit import default_timer as timer

from gen_dummy_data import gen_dummy_data


def run_with_parameters(controllers, n_tests):
	time_results = []

	print("Generating dummy data...")
	(cr_data, up_data) = gen_dummy_data(n_tests)
	print("Dummy data generated")

	# Start tests
	for ci, controller in enumerate(controllers):
		time_results.append([None, None, None, None])

		print("Testing", controller.name, "...")

		# Test creating records
		start = timer()
		for i in range(n_tests):
			controller.create_one(i, cr_data[i])
		time_results[ci][0] = (timer() - start) / n_tests

		# Test reading records
		start = timer()
		for i in range(n_tests):
			controller.read_one(i)
		time_results[ci][1] = (timer() - start) / n_tests

		# Test updating records
		start = timer()
		for i in range(n_tests):
			controller.update_one(i, up_data[i])
		time_results[ci][2] = (timer() - start) / n_tests

		# Test deleting records
		start = timer()
		for i in range(n_tests):
			controller.delete_one(i)
		time_results[ci][3] = (timer() - start) / n_tests

	# Print out the results
	print("All controller tests complete")
	for ci, controller in enumerate(controllers):
		print(f"\n{controller.name} results:")

		for ti, result in enumerate(time_results[ci]):
			print((
				"\tCreate",
				"\tRead",
				"\tUpdate",
				"\tDelete")[ti], end="\t")

			result *= 1000
			print(f"{result:.2f}ms")

	print("")


# Read .env and run the tests
if __name__ == "__main__":
	controllers = []

	config = dotenv_values(".env")
	turned_on = config["DATABASES"].lower().split(",")
	n_tests = int(config["N_TESTS"])

	if "mongo" in turned_on:
		try:
			from controllers.MongoController import MongoController
			controllers.append(MongoController(
				config["MONGO_HOST"],
				config["MONGO_PORT"],
			))
		except ImportError:
			print("pymongo is not installed, skipping MongoDB benchmarking")

	if "mysql" in turned_on:
		try:
			from controllers.MySQLController import MySQLController
			controllers.append(MySQLController(
				config["MYSQL_USER"],
				config["MYSQL_PASSWORD"],
				config["MYSQL_HOST"],
				config["MYSQL_PORT"],
				config["MYSQL_DB"],
			))
		except ImportError:
			print("mysql-connector-python is not installed, skipping MySQL benchmarking")

	if "nanodb" in turned_on:
		from controllers.NanoController import NanoController
		controllers.append(NanoController("http://127.0.0.1:3000"))

	if "postgres" in turned_on:
		try:
			from controllers.PostgresController import PostgresController
			controllers.append(PostgresController(
				config["POSTGRES_USER"],
				config["POSTGRES_PASSWORD"],
				config["POSTGRES_HOST"],
				config["POSTGRES_PORT"],
				config["POSTGRES_DB"],
			))
		except ImportError:
			print("psycopg2 is not installed, skipping PostgreSQL benchmarking")

	run_with_parameters(controllers, n_tests)
