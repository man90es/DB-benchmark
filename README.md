# DB-benchmark
This is my personal tool for benchmarking various database engines. It assesses the average time those engines take to complete the simplest tasks: creating one record, reading one record, updating one record and deleting one record.

## How to use
* Run `pip install -r requirements.txt --user` to install the required libraries;
* Start the database engines;
* Install additional libraries engine-specific libraries and complete additional steps described in a table below;
* Copy the `.env.template` file into `.env` and edit variables related to the engines accordingly to your configuration;
* Run `./app.py` to start the benchmarking process.

| Database engine | Required libraries | Additional steps                                  |
| --------------- | ------------------ | ------------------------------------------------- |
| NanoDB          | None               | None                                              |
| PostgreSQL      | psycopg2           | Create a database and user for the app to utilise |
