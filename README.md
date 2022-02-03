# DB-benchmark
This is my personal tool for benchmarking various database engines. It asesses the average time those engines take to complete the simplest tasks: creating one record, reading one record, updating one record and deleting one record.

## How to use
* Run `pip install -r requirements.txt --user` to install required libraries;
* Copy the `.env.template` file into `.env` and edit the list of database engines in it to only benchmark those that you want;
* Start the database engines;
* Complete the engine-specific steps described below;
* Run `./app.py` to start the benchmarking process.

Depending on the benchmarked databases, you will also need to complete additional steps:

### For PostgreSQL:
* Install psycopg2 library: `pip install psycopg2 --user`;
* Create a database and user for the app to utilise;
* Change variables that start with `POSTGRES_` in the `.env` file accordingly to your configuration.
