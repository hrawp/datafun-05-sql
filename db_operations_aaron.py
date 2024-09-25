# Import from Python Standard Library first
import sqlite3
import pathlib


# Import from external packages
import pandas as pd

# Define paths using joinpath
db_file_path = pathlib.Path("sql").joinpath("project.db")

sql_file_path_insert = pathlib.Path("sql").joinpath("insert_records.sql")
sql_file_path_aggregate = pathlib.Path("sql").joinpath("query_aggregation.sql")
sql_file_path_filter = pathlib.Path("sql").joinpath("query_filter.sql")
sql_file_path_group = pathlib.Path("sql").joinpath("query_group_by.sql")
sql_file_path_join = pathlib.Path("sql").joinpath("query_join.sql")
sql_file_path_sorting = pathlib.Path("sql").joinpath("query_sorting.sql")
sql_file_path_update = pathlib.Path("sql").joinpath("update_records.sql")
sql_file_path_delete = pathlib.Path("sql").joinpath("delete_records.sql")

author_data_path = pathlib.Path("data").joinpath("authors.csv")
book_data_path = pathlib.Path("data").joinpath("books.csv")

def execute_sql_insert(db_file_path, sql_file_path_insert):
    with sqlite3.connect(db_file_path) as conn:
        with open(sql_file_path_insert, 'r') as file:
            sql_script = file.read()
        conn.executescript(sql_script)
        print(f"Executed SQL from {sql_file_path_insert}")

def execute_sql_aggregate(db_file_path, sql_file_path_aggregate):
    with sqlite3.connect(db_file_path) as conn:
        with open(sql_file_path_aggregate, 'r') as file:
            sql_script = file.read()
        conn.executescript(sql_script)
        print(f"Executed SQL from {sql_file_path_aggregate}")

def execute_sql_filter(db_file_path, sql_file_path_filter):
    with sqlite3.connect(db_file_path) as conn:
        with open(sql_file_path_filter, 'r') as file:
            sql_script = file.read()
        conn.executescript(sql_script)
        print(f"Executed SQL from {sql_file_path_filter}")

def execute_sql_group(db_file_path, sql_file_path_group):
    with sqlite3.connect(db_file_path) as conn:
        with open(sql_file_path_group, 'r') as file:
            sql_script = file.read()
        conn.executescript(sql_script)
        print(f"Executed SQL from {sql_file_path_group}")

def execute_sql_join(db_file_path, sql_file_path_join):
    with sqlite3.connect(db_file_path) as conn:
        with open(sql_file_path_join, 'r') as file:
            sql_script = file.read()
        conn.executescript(sql_script)
        print(f"Executed SQL from {sql_file_path_join}")

def execute_sql_sorting(db_file_path, sql_file_path_sorting):
    with sqlite3.connect(db_file_path) as conn:
        with open(sql_file_path_sorting, 'r') as file:
            sql_script = file.read()
        conn.executescript(sql_script)
        print(f"Executed SQL from {sql_file_path_sorting}")

def execute_sql_update(db_file_path, sql_file_path_update):
    with sqlite3.connect(db_file_path) as conn:
        with open(sql_file_path_update, 'r') as file:
            sql_script = file.read()
        conn.executescript(sql_script)
        print(f"Executed SQL from {sql_file_path_update}")

def execute_sql_delete(db_file_path, sql_file_path_delete):
    with sqlite3.connect(db_file_path) as conn:
        with open(sql_file_path_delete, 'r') as file:
            sql_script = file.read()
        conn.executescript(sql_script)
        print(f"Executed SQL from {sql_file_path_delete}")


def main():
  
    execute_sql_insert(db_file_path, sql_file_path_insert)
    execute_sql_aggregate(db_file_path, sql_file_path_aggregate)
    execute_sql_filter(db_file_path, sql_file_path_filter)
    execute_sql_group(db_file_path, sql_file_path_group)
    execute_sql_join(db_file_path, sql_file_path_join)
    execute_sql_sorting(db_file_path, sql_file_path_sorting)
    execute_sql_update(db_file_path, sql_file_path_update)
    execute_sql_delete(db_file_path, sql_file_path_delete)

if __name__ == "__main__":
    main()