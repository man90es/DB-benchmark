# DB-benchmark
This is my personal tool for benchmarking various database engines. It assesses the average time those engines take to complete the simplest tasks: creating one record, reading one record, updating one record and deleting one record.

## My results
These are the results that I got for 10k executions on my hardware:
|            | NanoDB | PostgreSQL | MongoDB |
| ---------- | ------ | ---------- | ------- |
| **Create** | 1.58ms | 2.77ms     | 0.17ms  |
| **Read**   | 1.53ms | 0.05ms     | 0.21ms  |
| **Update** | 1.57ms | 2.82ms     | 0.21ms  |
| **Delete** | 1.54ms | 2.86ms     | 0.20ms  |

System specifications:
| Variable | Specification  |
| -------- | -------------- |
| CPU      | i5-10300H      |
| RAM      | 15.5GB         |
| HDD      | WD10SPZX-24Z   |
| Kernel   | 5.13.19-gentoo |
| FS       | ext4           |

## How to use
* Run `pip install -r requirements.txt --user` to install the required libraries;
* Start the database engines;
* Install additional engine-specific libraries and complete additional steps described in the table below;
* Copy the `.env.template` file into `.env` and edit the defined variables to match your configuration;
* Run `./app.py` to start the benchmarking process.

| Database engine | Required libraries | Additional steps                                  |
| --------------- | ------------------ | ------------------------------------------------- |
| NanoDB          | --                 | --                                                |
| PostgreSQL      | psycopg2           | Create a database and user for the app to utilise |
| MongoDB         | pymongo            | --                                                |
