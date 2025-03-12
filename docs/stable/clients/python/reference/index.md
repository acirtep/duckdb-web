---
layout: docu
redirect_from:
- /docs/api/python/reference/index
- /docs/api/python/reference/index/
- /docs/clients/python/reference/index
title: Python Client API
---

The API reference documentation is structured as follows:

1. [duckdb](#duckdb)
2. [DuckDBPyConnection](#duckdbpyconnection)
3. [DuckDBPyRelation](#duckdbpyrelation)
4. [Expressions](#expressions)
5. [Values](#values)
6. [Exceptions](#exceptions)


## duckdb

### aggregate

aggregate(df: pandas.DataFrame, aggr_expr: object, group_expr: str = '', *, connection: duckdb.DuckDBPyConnection = None) -> [duckdb.duckdb.DuckDBPyRelation](#duckdbpyrelation)

Compute the aggregate aggr_expr by the optional groups group_expr on the relation




### alias

alias(df: pandas.DataFrame, alias: str, *, connection: duckdb.DuckDBPyConnection = None) -> [duckdb.duckdb.DuckDBPyRelation](#duckdbpyrelation)

Rename the relation object to new alias




### append

append(table_name: str, df: pandas.DataFrame, *, by_name: bool = False, connection: duckdb.DuckDBPyConnection = None) -> duckdb.DuckDBPyConnection

Append the passed DataFrame to the named table




### array_type

array_type(type: duckdb.duckdb.typing.DuckDBPyType, size: int, *, connection: duckdb.DuckDBPyConnection = None) -> duckdb.duckdb.typing.DuckDBPyType

Create an array type object of 'type'




### arrow

arrow(*args, **kwargs)
Overloaded function.

1. arrow(rows_per_batch: int = 1000000, *, connection: duckdb.DuckDBPyConnection = None) -> pyarrow.lib.Table

Fetch a result as Arrow table following execute()

2. arrow(rows_per_batch: int = 1000000, *, connection: duckdb.DuckDBPyConnection = None) -> pyarrow.lib.Table

Fetch a result as Arrow table following execute()

3. arrow(arrow_object: object, *, connection: duckdb.DuckDBPyConnection = None) -> [duckdb.duckdb.DuckDBPyRelation](#duckdbpyrelation)

Create a relation object from an Arrow object




### begin

begin(*, connection: duckdb.DuckDBPyConnection = None) -> duckdb.DuckDBPyConnection

Start a new transaction




### checkpoint

checkpoint(*, connection: duckdb.DuckDBPyConnection = None) -> duckdb.DuckDBPyConnection

Synchronizes data in the write-ahead log (WAL) to the database data file (no-op for in-memory connections)




### close

close(*, connection: duckdb.DuckDBPyConnection = None) -> None

Close the connection




### commit

commit(*, connection: duckdb.DuckDBPyConnection = None) -> duckdb.DuckDBPyConnection

Commit changes performed within a transaction




### connect

connect(database: object = ':memory:', read_only: bool = False, config: dict = None) -> duckdb.DuckDBPyConnection

Create a DuckDB database instance. Can take a database file name to read/write persistent data and a read_only flag if no changes are desired




### create_function

create_function(name: str, function: Callable, parameters: object = None, return_type: duckdb.duckdb.typing.DuckDBPyType = None, *, type: duckdb.duckdb.functional.PythonUDFType = <PythonUDFType.NATIVE: 0>, null_handling: duckdb.duckdb.functional.FunctionNullHandling = <FunctionNullHandling.DEFAULT: 0>, exception_handling: duckdb.duckdb.PythonExceptionHandling = <PythonExceptionHandling.DEFAULT: 0>, side_effects: bool = False, connection: duckdb.DuckDBPyConnection = None) -> duckdb.DuckDBPyConnection

Create a DuckDB function out of the passing in Python function so it can be used in queries




### cursor

cursor(*, connection: duckdb.DuckDBPyConnection = None) -> duckdb.DuckDBPyConnection

Create a duplicate of the current connection




### decimal_type

decimal_type(width: int, scale: int, *, connection: duckdb.DuckDBPyConnection = None) -> duckdb.duckdb.typing.DuckDBPyType

Create a decimal type with 'width' and 'scale'




### default_connection

default_connection() -> duckdb.DuckDBPyConnection

Retrieve the connection currently registered as the default to be used by the module




### description

description(*, connection: duckdb.DuckDBPyConnection = None) -> typing.Optional[list]

Get result set attributes, mainly column names




### df

df(*args, **kwargs)
Overloaded function.

1. df(*, date_as_object: bool = False, connection: duckdb.DuckDBPyConnection = None) -> pandas.DataFrame

Fetch a result as DataFrame following execute()

2. df(*, date_as_object: bool = False, connection: duckdb.DuckDBPyConnection = None) -> pandas.DataFrame

Fetch a result as DataFrame following execute()

3. df(df: pandas.DataFrame, *, connection: duckdb.DuckDBPyConnection = None) -> [duckdb.duckdb.DuckDBPyRelation](#duckdbpyrelation)

Create a relation object from the DataFrame df




### distinct

distinct(df: pandas.DataFrame, *, connection: duckdb.DuckDBPyConnection = None) -> [duckdb.duckdb.DuckDBPyRelation](#duckdbpyrelation)

Retrieve distinct rows from this relation object




### dtype

dtype(type_str: str, *, connection: duckdb.DuckDBPyConnection = None) -> duckdb.duckdb.typing.DuckDBPyType

Create a type object by parsing the 'type_str' string




### duplicate

duplicate(*, connection: duckdb.DuckDBPyConnection = None) -> duckdb.DuckDBPyConnection

Create a duplicate of the current connection




### enum_type

enum_type(name: str, type: duckdb.duckdb.typing.DuckDBPyType, values: list, *, connection: duckdb.DuckDBPyConnection = None) -> duckdb.duckdb.typing.DuckDBPyType

Create an enum type of underlying 'type', consisting of the list of 'values'




### execute

execute(query: object, parameters: object = None, *, connection: duckdb.DuckDBPyConnection = None) -> duckdb.DuckDBPyConnection

Execute the given SQL query, optionally using prepared statements with parameters set




### executemany

executemany(query: object, parameters: object = None, *, connection: duckdb.DuckDBPyConnection = None) -> duckdb.DuckDBPyConnection

Execute the given prepared statement multiple times using the list of parameter sets in parameters




### extract_statements

extract_statements(query: str, *, connection: duckdb.DuckDBPyConnection = None) -> list

Parse the query string and extract the Statement object(s) produced




### fetch_arrow_table

fetch_arrow_table(rows_per_batch: int = 1000000, *, connection: duckdb.DuckDBPyConnection = None) -> pyarrow.lib.Table

Fetch a result as Arrow table following execute()




### fetch_df

fetch_df(*, date_as_object: bool = False, connection: duckdb.DuckDBPyConnection = None) -> pandas.DataFrame

Fetch a result as DataFrame following execute()




### fetch_df_chunk

fetch_df_chunk(vectors_per_chunk: int = 1, *, date_as_object: bool = False, connection: duckdb.DuckDBPyConnection = None) -> pandas.DataFrame

Fetch a chunk of the result as DataFrame following execute()




### fetch_record_batch

fetch_record_batch(rows_per_batch: int = 1000000, *, connection: duckdb.DuckDBPyConnection = None) -> pyarrow.lib.RecordBatchReader

Fetch an Arrow RecordBatchReader following execute()




### fetchall

fetchall(*, connection: duckdb.DuckDBPyConnection = None) -> list

Fetch all rows from a result following execute




### fetchdf

fetchdf(*, date_as_object: bool = False, connection: duckdb.DuckDBPyConnection = None) -> pandas.DataFrame

Fetch a result as DataFrame following execute()




### fetchmany

fetchmany(size: int = 1, *, connection: duckdb.DuckDBPyConnection = None) -> list

Fetch the next set of rows from a result following execute




### fetchnumpy

fetchnumpy(*, connection: duckdb.DuckDBPyConnection = None) -> dict

Fetch a result as list of NumPy arrays following execute




### fetchone

fetchone(*, connection: duckdb.DuckDBPyConnection = None) -> typing.Optional[tuple]

Fetch a single row from a result following execute




### filesystem_is_registered

filesystem_is_registered(name: str, *, connection: duckdb.DuckDBPyConnection = None) -> bool

Check if a filesystem with the provided name is currently registered




### filter

filter(df: pandas.DataFrame, filter_expr: object, *, connection: duckdb.DuckDBPyConnection = None) -> [duckdb.duckdb.DuckDBPyRelation](#duckdbpyrelation)

Filter the relation object by the filter in filter_expr




### from_arrow

from_arrow(arrow_object: object, *, connection: duckdb.DuckDBPyConnection = None) -> [duckdb.duckdb.DuckDBPyRelation](#duckdbpyrelation)

Create a relation object from an Arrow object




### from_csv_auto

from_csv_auto(path_or_buffer: object, **kwargs) -> [duckdb.duckdb.DuckDBPyRelation](#duckdbpyrelation)

Create a relation object from the CSV file in 'name'




### from_df

from_df(df: pandas.DataFrame, *, connection: duckdb.DuckDBPyConnection = None) -> [duckdb.duckdb.DuckDBPyRelation](#duckdbpyrelation)

Create a relation object from the DataFrame in df




### from_parquet

from_parquet(*args, **kwargs)
Overloaded function.

1. from_parquet(file_glob: str, binary_as_string: bool = False, *, file_row_number: bool = False, filename: bool = False, hive_partitioning: bool = False, union_by_name: bool = False, compression: object = None, connection: duckdb.DuckDBPyConnection = None) -> [duckdb.duckdb.DuckDBPyRelation](#duckdbpyrelation)

Create a relation object from the Parquet files in file_glob

2. from_parquet(file_globs: list[str], binary_as_string: bool = False, *, file_row_number: bool = False, filename: bool = False, hive_partitioning: bool = False, union_by_name: bool = False, compression: object = None, connection: duckdb.DuckDBPyConnection = None) -> [duckdb.duckdb.DuckDBPyRelation](#duckdbpyrelation)

Create a relation object from the Parquet files in file_globs




### from_query

from_query(query: object, *, alias: str = '', params: object = None, connection: duckdb.DuckDBPyConnection = None) -> [duckdb.duckdb.DuckDBPyRelation](#duckdbpyrelation)

Run a SQL query. If it is a SELECT statement, create a relation object from the given SQL query, otherwise run the query as-is.




### get_table_names

get_table_names(query: str, *, connection: duckdb.DuckDBPyConnection = None) -> set[str]

Extract the required table names from a query




### install_extension

install_extension(extension: str, *, force_install: bool = False, repository: object = None, repository_url: object = None, version: object = None, connection: duckdb.DuckDBPyConnection = None) -> None

Install an extension by name, with an optional version and/or repository to get the extension from




### interrupt

interrupt(*, connection: duckdb.DuckDBPyConnection = None) -> None

Interrupt pending operations




### limit

limit(df: pandas.DataFrame, n: int, offset: int = 0, *, connection: duckdb.DuckDBPyConnection = None) -> [duckdb.duckdb.DuckDBPyRelation](#duckdbpyrelation)

Only retrieve the first n rows from this relation object, starting at offset




### list_filesystems

list_filesystems(*, connection: duckdb.DuckDBPyConnection = None) -> list

List registered filesystems, including builtin ones




### list_type

list_type(type: duckdb.duckdb.typing.DuckDBPyType, *, connection: duckdb.DuckDBPyConnection = None) -> duckdb.duckdb.typing.DuckDBPyType

Create a list type object of 'type'




### load_extension

load_extension(extension: str, *, connection: duckdb.DuckDBPyConnection = None) -> None

Load an installed extension




### map_type

map_type(key: duckdb.duckdb.typing.DuckDBPyType, value: duckdb.duckdb.typing.DuckDBPyType, *, connection: duckdb.DuckDBPyConnection = None) -> duckdb.duckdb.typing.DuckDBPyType

Create a map type object from 'key_type' and 'value_type'




### order

order(df: pandas.DataFrame, order_expr: str, *, connection: duckdb.DuckDBPyConnection = None) -> [duckdb.duckdb.DuckDBPyRelation](#duckdbpyrelation)

Reorder the relation object by order_expr




### pl

pl(rows_per_batch: int = 1000000, *, connection: duckdb.DuckDBPyConnection = None) -> duckdb::PolarsDataFrame

Fetch a result as Polars DataFrame following execute()




### project

project(df: pandas.DataFrame, *args, groups: str = '', connection: duckdb.DuckDBPyConnection = None) -> [duckdb.duckdb.DuckDBPyRelation](#duckdbpyrelation)

Project the relation object by the projection in project_expr




### query

query(query: object, *, alias: str = '', params: object = None, connection: duckdb.DuckDBPyConnection = None) -> [duckdb.duckdb.DuckDBPyRelation](#duckdbpyrelation)

Run a SQL query. If it is a SELECT statement, create a relation object from the given SQL query, otherwise run the query as-is.




### query_df

query_df(df: pandas.DataFrame, virtual_table_name: str, sql_query: str, *, connection: duckdb.DuckDBPyConnection = None) -> [duckdb.duckdb.DuckDBPyRelation](#duckdbpyrelation)

Run the given SQL query in sql_query on the view named virtual_table_name that refers to the relation object




### read_csv

read_csv(path_or_buffer: object, **kwargs) -> [duckdb.duckdb.DuckDBPyRelation](#duckdbpyrelation)

Create a relation object from the CSV file in 'name'




### read_json

read_json(path_or_buffer: object, *, columns: typing.Optional[object] = None, sample_size: typing.Optional[object] = None, maximum_depth: typing.Optional[object] = None, records: typing.Optional[str] = None, format: typing.Optional[str] = None, date_format: typing.Optional[object] = None, timestamp_format: typing.Optional[object] = None, compression: typing.Optional[object] = None, maximum_object_size: typing.Optional[object] = None, ignore_errors: typing.Optional[object] = None, convert_strings_to_integers: typing.Optional[object] = None, field_appearance_threshold: typing.Optional[object] = None, map_inference_threshold: typing.Optional[object] = None, maximum_sample_files: typing.Optional[object] = None, filename: typing.Optional[object] = None, hive_partitioning: typing.Optional[object] = None, union_by_name: typing.Optional[object] = None, hive_types: typing.Optional[object] = None, hive_types_autocast: typing.Optional[object] = None, connection: duckdb.DuckDBPyConnection = None) -> [duckdb.duckdb.DuckDBPyRelation](#duckdbpyrelation)

Create a relation object from the JSON file in 'name'




### read_parquet

read_parquet(*args, **kwargs)
Overloaded function.

1. read_parquet(file_glob: str, binary_as_string: bool = False, *, file_row_number: bool = False, filename: bool = False, hive_partitioning: bool = False, union_by_name: bool = False, compression: object = None, connection: duckdb.DuckDBPyConnection = None) -> [duckdb.duckdb.DuckDBPyRelation](#duckdbpyrelation)

Create a relation object from the Parquet files in file_glob

2. read_parquet(file_globs: list[str], binary_as_string: bool = False, *, file_row_number: bool = False, filename: bool = False, hive_partitioning: bool = False, union_by_name: bool = False, compression: object = None, connection: duckdb.DuckDBPyConnection = None) -> [duckdb.duckdb.DuckDBPyRelation](#duckdbpyrelation)

Create a relation object from the Parquet files in file_globs




### register

register(view_name: str, python_object: object, *, connection: duckdb.DuckDBPyConnection = None) -> duckdb.DuckDBPyConnection

Register the passed Python Object value for querying with a view




### register_filesystem

register_filesystem(filesystem: fsspec.AbstractFileSystem, *, connection: duckdb.DuckDBPyConnection = None) -> None

Register a fsspec compliant filesystem




### remove_function

remove_function(name: str, *, connection: duckdb.DuckDBPyConnection = None) -> duckdb.DuckDBPyConnection

Remove a previously created function




### rollback

rollback(*, connection: duckdb.DuckDBPyConnection = None) -> duckdb.DuckDBPyConnection

Roll back changes performed within a transaction




### row_type

row_type(fields: object, *, connection: duckdb.DuckDBPyConnection = None) -> duckdb.duckdb.typing.DuckDBPyType

Create a struct type object from 'fields'




### rowcount

rowcount(*, connection: duckdb.DuckDBPyConnection = None) -> int

Get result set row count




### set_default_connection

set_default_connection(connection: duckdb.DuckDBPyConnection) -> None

Register the provided connection as the default to be used by the module




### sql

sql(query: object, *, alias: str = '', params: object = None, connection: duckdb.DuckDBPyConnection = None) -> [duckdb.duckdb.DuckDBPyRelation](#duckdbpyrelation)

Run a SQL query. If it is a SELECT statement, create a relation object from the given SQL query, otherwise run the query as-is.




### sqltype

sqltype(type_str: str, *, connection: duckdb.DuckDBPyConnection = None) -> duckdb.duckdb.typing.DuckDBPyType

Create a type object by parsing the 'type_str' string




### string_type

string_type(collation: str = '', *, connection: duckdb.DuckDBPyConnection = None) -> duckdb.duckdb.typing.DuckDBPyType

Create a string type with an optional collation




### struct_type

struct_type(fields: object, *, connection: duckdb.DuckDBPyConnection = None) -> duckdb.duckdb.typing.DuckDBPyType

Create a struct type object from 'fields'




### table

table(table_name: str, *, connection: duckdb.DuckDBPyConnection = None) -> [duckdb.duckdb.DuckDBPyRelation](#duckdbpyrelation)

Create a relation object for the named table




### table_function

table_function(name: str, parameters: object = None, *, connection: duckdb.DuckDBPyConnection = None) -> [duckdb.duckdb.DuckDBPyRelation](#duckdbpyrelation)

Create a relation object from the named table function with given parameters




### tf

tf(*, connection: duckdb.DuckDBPyConnection = None) -> dict

Fetch a result as dict of TensorFlow Tensors following execute()




### tokenize

tokenize(query: str) -> list

Tokenizes a SQL string, returning a list of (position, type) tuples that can be used for e.g., syntax highlighting




### torch

torch(*, connection: duckdb.DuckDBPyConnection = None) -> dict

Fetch a result as dict of PyTorch Tensors following execute()




### type

type(type_str: str, *, connection: duckdb.DuckDBPyConnection = None) -> duckdb.duckdb.typing.DuckDBPyType

Create a type object by parsing the 'type_str' string




### union_type

union_type(members: object, *, connection: duckdb.DuckDBPyConnection = None) -> duckdb.duckdb.typing.DuckDBPyType

Create a union type object from 'members'




### unregister

unregister(view_name: str, *, connection: duckdb.DuckDBPyConnection = None) -> duckdb.DuckDBPyConnection

Unregister the view name




### unregister_filesystem

unregister_filesystem(name: str, *, connection: duckdb.DuckDBPyConnection = None) -> None

Unregister a filesystem




### values

values(*args, connection: duckdb.DuckDBPyConnection = None) -> [duckdb.duckdb.DuckDBPyRelation](#duckdbpyrelation)

Create a relation object from the passed values




### view

view(view_name: str, *, connection: duckdb.DuckDBPyConnection = None) -> [duckdb.duckdb.DuckDBPyRelation](#duckdbpyrelation)

Create a relation object for the named view




### write_csv

write_csv(df: pandas.DataFrame, filename: str, *, sep: object = None, na_rep: object = None, header: object = None, quotechar: object = None, escapechar: object = None, date_format: object = None, timestamp_format: object = None, quoting: object = None, encoding: object = None, compression: object = None, overwrite: object = None, per_thread_output: object = None, use_tmp_file: object = None, partition_by: object = None, write_partition_columns: object = None, connection: duckdb.DuckDBPyConnection = None) -> None

Write the relation object to a CSV file in 'file_name'




## DuckDBPyConnection



**Bases**: pybind11_object
































### append

append(self: [duckdb.duckdb.DuckDBPyConnection](#duckdbpyconnection), table_name: str, df: pandas.DataFrame, *, by_name: bool = False) -> [duckdb.duckdb.DuckDBPyConnection](#duckdbpyconnection)

Append the passed DataFrame to the named table




### array_type

array_type(self: [duckdb.duckdb.DuckDBPyConnection](#duckdbpyconnection), type: duckdb.duckdb.typing.DuckDBPyType, size: int) -> duckdb.duckdb.typing.DuckDBPyType

Create an array type object of 'type'




### arrow

arrow(self: [duckdb.duckdb.DuckDBPyConnection](#duckdbpyconnection), rows_per_batch: int = 1000000) -> pyarrow.lib.Table

Fetch a result as Arrow table following execute()




### begin

begin(self: [duckdb.duckdb.DuckDBPyConnection](#duckdbpyconnection)) -> [duckdb.duckdb.DuckDBPyConnection](#duckdbpyconnection)

Start a new transaction




### checkpoint

checkpoint(self: [duckdb.duckdb.DuckDBPyConnection](#duckdbpyconnection)) -> [duckdb.duckdb.DuckDBPyConnection](#duckdbpyconnection)

Synchronizes data in the write-ahead log (WAL) to the database data file (no-op for in-memory connections)




### close

close(self: [duckdb.duckdb.DuckDBPyConnection](#duckdbpyconnection)) -> None

Close the connection




### commit

commit(self: [duckdb.duckdb.DuckDBPyConnection](#duckdbpyconnection)) -> [duckdb.duckdb.DuckDBPyConnection](#duckdbpyconnection)

Commit changes performed within a transaction




### create_function

create_function(self: [duckdb.duckdb.DuckDBPyConnection](#duckdbpyconnection), name: str, function: Callable, parameters: object = None, return_type: duckdb.duckdb.typing.DuckDBPyType = None, *, type: duckdb.duckdb.functional.PythonUDFType = <PythonUDFType.NATIVE: 0>, null_handling: duckdb.duckdb.functional.FunctionNullHandling = <FunctionNullHandling.DEFAULT: 0>, exception_handling: duckdb.duckdb.PythonExceptionHandling = <PythonExceptionHandling.DEFAULT: 0>, side_effects: bool = False) -> [duckdb.duckdb.DuckDBPyConnection](#duckdbpyconnection)

Create a DuckDB function out of the passing in Python function so it can be used in queries




### cursor

cursor(self: [duckdb.duckdb.DuckDBPyConnection](#duckdbpyconnection)) -> [duckdb.duckdb.DuckDBPyConnection](#duckdbpyconnection)

Create a duplicate of the current connection




### decimal_type

decimal_type(self: [duckdb.duckdb.DuckDBPyConnection](#duckdbpyconnection), width: int, scale: int) -> duckdb.duckdb.typing.DuckDBPyType

Create a decimal type with 'width' and 'scale'




### description

Get result set attributes, mainly column names




### df

df(self: [duckdb.duckdb.DuckDBPyConnection](#duckdbpyconnection), *, date_as_object: bool = False) -> pandas.DataFrame

Fetch a result as DataFrame following execute()




### dtype

dtype(self: [duckdb.duckdb.DuckDBPyConnection](#duckdbpyconnection), type_str: str) -> duckdb.duckdb.typing.DuckDBPyType

Create a type object by parsing the 'type_str' string




### duplicate

duplicate(self: [duckdb.duckdb.DuckDBPyConnection](#duckdbpyconnection)) -> [duckdb.duckdb.DuckDBPyConnection](#duckdbpyconnection)

Create a duplicate of the current connection




### enum_type

enum_type(self: [duckdb.duckdb.DuckDBPyConnection](#duckdbpyconnection), name: str, type: duckdb.duckdb.typing.DuckDBPyType, values: list) -> duckdb.duckdb.typing.DuckDBPyType

Create an enum type of underlying 'type', consisting of the list of 'values'




### execute

execute(self: [duckdb.duckdb.DuckDBPyConnection](#duckdbpyconnection), query: object, parameters: object = None) -> [duckdb.duckdb.DuckDBPyConnection](#duckdbpyconnection)

Execute the given SQL query, optionally using prepared statements with parameters set




### executemany

executemany(self: [duckdb.duckdb.DuckDBPyConnection](#duckdbpyconnection), query: object, parameters: object = None) -> [duckdb.duckdb.DuckDBPyConnection](#duckdbpyconnection)

Execute the given prepared statement multiple times using the list of parameter sets in parameters




### extract_statements

extract_statements(self: [duckdb.duckdb.DuckDBPyConnection](#duckdbpyconnection), query: str) -> list

Parse the query string and extract the Statement object(s) produced




### fetch_arrow_table

fetch_arrow_table(self: [duckdb.duckdb.DuckDBPyConnection](#duckdbpyconnection), rows_per_batch: int = 1000000) -> pyarrow.lib.Table

Fetch a result as Arrow table following execute()




### fetch_df

fetch_df(self: [duckdb.duckdb.DuckDBPyConnection](#duckdbpyconnection), *, date_as_object: bool = False) -> pandas.DataFrame

Fetch a result as DataFrame following execute()




### fetch_df_chunk

fetch_df_chunk(self: [duckdb.duckdb.DuckDBPyConnection](#duckdbpyconnection), vectors_per_chunk: int = 1, *, date_as_object: bool = False) -> pandas.DataFrame

Fetch a chunk of the result as DataFrame following execute()




### fetch_record_batch

fetch_record_batch(self: [duckdb.duckdb.DuckDBPyConnection](#duckdbpyconnection), rows_per_batch: int = 1000000) -> pyarrow.lib.RecordBatchReader

Fetch an Arrow RecordBatchReader following execute()




### fetchall

fetchall(self: [duckdb.duckdb.DuckDBPyConnection](#duckdbpyconnection)) -> list

Fetch all rows from a result following execute




### fetchdf

fetchdf(self: [duckdb.duckdb.DuckDBPyConnection](#duckdbpyconnection), *, date_as_object: bool = False) -> pandas.DataFrame

Fetch a result as DataFrame following execute()




### fetchmany

fetchmany(self: [duckdb.duckdb.DuckDBPyConnection](#duckdbpyconnection), size: int = 1) -> list

Fetch the next set of rows from a result following execute




### fetchnumpy

fetchnumpy(self: [duckdb.duckdb.DuckDBPyConnection](#duckdbpyconnection)) -> dict

Fetch a result as list of NumPy arrays following execute




### fetchone

fetchone(self: [duckdb.duckdb.DuckDBPyConnection](#duckdbpyconnection)) -> typing.Optional[tuple]

Fetch a single row from a result following execute




### filesystem_is_registered

filesystem_is_registered(self: [duckdb.duckdb.DuckDBPyConnection](#duckdbpyconnection), name: str) -> bool

Check if a filesystem with the provided name is currently registered




### from_arrow

from_arrow(self: [duckdb.duckdb.DuckDBPyConnection](#duckdbpyconnection), arrow_object: object) -> [duckdb.duckdb.DuckDBPyRelation](#duckdbpyrelation)

Create a relation object from an Arrow object




### from_csv_auto

from_csv_auto(self: [duckdb.duckdb.DuckDBPyConnection](#duckdbpyconnection), path_or_buffer: object, **kwargs) -> [duckdb.duckdb.DuckDBPyRelation](#duckdbpyrelation)

Create a relation object from the CSV file in 'name'




### from_df

from_df(self: [duckdb.duckdb.DuckDBPyConnection](#duckdbpyconnection), df: pandas.DataFrame) -> [duckdb.duckdb.DuckDBPyRelation](#duckdbpyrelation)

Create a relation object from the DataFrame in df




### from_parquet

from_parquet(*args, **kwargs)
Overloaded function.

1. from_parquet(self: [duckdb.duckdb.DuckDBPyConnection](#duckdbpyconnection), file_glob: str, binary_as_string: bool = False, *, file_row_number: bool = False, filename: bool = False, hive_partitioning: bool = False, union_by_name: bool = False, compression: object = None) -> [duckdb.duckdb.DuckDBPyRelation](#duckdbpyrelation)

Create a relation object from the Parquet files in file_glob

2. from_parquet(self: [duckdb.duckdb.DuckDBPyConnection](#duckdbpyconnection), file_globs: list[str], binary_as_string: bool = False, *, file_row_number: bool = False, filename: bool = False, hive_partitioning: bool = False, union_by_name: bool = False, compression: object = None) -> [duckdb.duckdb.DuckDBPyRelation](#duckdbpyrelation)

Create a relation object from the Parquet files in file_globs




### from_query

from_query(self: [duckdb.duckdb.DuckDBPyConnection](#duckdbpyconnection), query: object, *, alias: str = '', params: object = None) -> [duckdb.duckdb.DuckDBPyRelation](#duckdbpyrelation)

Run a SQL query. If it is a SELECT statement, create a relation object from the given SQL query, otherwise run the query as-is.




### get_table_names

get_table_names(self: [duckdb.duckdb.DuckDBPyConnection](#duckdbpyconnection), query: str) -> set[str]

Extract the required table names from a query




### install_extension

install_extension(self: [duckdb.duckdb.DuckDBPyConnection](#duckdbpyconnection), extension: str, *, force_install: bool = False, repository: object = None, repository_url: object = None, version: object = None) -> None

Install an extension by name, with an optional version and/or repository to get the extension from




### interrupt

interrupt(self: [duckdb.duckdb.DuckDBPyConnection](#duckdbpyconnection)) -> None

Interrupt pending operations




### list_filesystems

list_filesystems(self: [duckdb.duckdb.DuckDBPyConnection](#duckdbpyconnection)) -> list

List registered filesystems, including builtin ones




### list_type

list_type(self: [duckdb.duckdb.DuckDBPyConnection](#duckdbpyconnection), type: duckdb.duckdb.typing.DuckDBPyType) -> duckdb.duckdb.typing.DuckDBPyType

Create a list type object of 'type'




### load_extension

load_extension(self: [duckdb.duckdb.DuckDBPyConnection](#duckdbpyconnection), extension: str) -> None

Load an installed extension




### map_type

map_type(self: [duckdb.duckdb.DuckDBPyConnection](#duckdbpyconnection), key: duckdb.duckdb.typing.DuckDBPyType, value: duckdb.duckdb.typing.DuckDBPyType) -> duckdb.duckdb.typing.DuckDBPyType

Create a map type object from 'key_type' and 'value_type'




### pl

pl(self: [duckdb.duckdb.DuckDBPyConnection](#duckdbpyconnection), rows_per_batch: int = 1000000) -> duckdb::PolarsDataFrame

Fetch a result as Polars DataFrame following execute()




### query

query(self: [duckdb.duckdb.DuckDBPyConnection](#duckdbpyconnection), query: object, *, alias: str = '', params: object = None) -> [duckdb.duckdb.DuckDBPyRelation](#duckdbpyrelation)

Run a SQL query. If it is a SELECT statement, create a relation object from the given SQL query, otherwise run the query as-is.




### read_csv

read_csv(self: [duckdb.duckdb.DuckDBPyConnection](#duckdbpyconnection), path_or_buffer: object, **kwargs) -> [duckdb.duckdb.DuckDBPyRelation](#duckdbpyrelation)

Create a relation object from the CSV file in 'name'




### read_json

read_json(self: [duckdb.duckdb.DuckDBPyConnection](#duckdbpyconnection), path_or_buffer: object, *, columns: typing.Optional[object] = None, sample_size: typing.Optional[object] = None, maximum_depth: typing.Optional[object] = None, records: typing.Optional[str] = None, format: typing.Optional[str] = None, date_format: typing.Optional[object] = None, timestamp_format: typing.Optional[object] = None, compression: typing.Optional[object] = None, maximum_object_size: typing.Optional[object] = None, ignore_errors: typing.Optional[object] = None, convert_strings_to_integers: typing.Optional[object] = None, field_appearance_threshold: typing.Optional[object] = None, map_inference_threshold: typing.Optional[object] = None, maximum_sample_files: typing.Optional[object] = None, filename: typing.Optional[object] = None, hive_partitioning: typing.Optional[object] = None, union_by_name: typing.Optional[object] = None, hive_types: typing.Optional[object] = None, hive_types_autocast: typing.Optional[object] = None) -> [duckdb.duckdb.DuckDBPyRelation](#duckdbpyrelation)

Create a relation object from the JSON file in 'name'




### read_parquet

read_parquet(*args, **kwargs)
Overloaded function.

1. read_parquet(self: [duckdb.duckdb.DuckDBPyConnection](#duckdbpyconnection), file_glob: str, binary_as_string: bool = False, *, file_row_number: bool = False, filename: bool = False, hive_partitioning: bool = False, union_by_name: bool = False, compression: object = None) -> [duckdb.duckdb.DuckDBPyRelation](#duckdbpyrelation)

Create a relation object from the Parquet files in file_glob

2. read_parquet(self: [duckdb.duckdb.DuckDBPyConnection](#duckdbpyconnection), file_globs: list[str], binary_as_string: bool = False, *, file_row_number: bool = False, filename: bool = False, hive_partitioning: bool = False, union_by_name: bool = False, compression: object = None) -> [duckdb.duckdb.DuckDBPyRelation](#duckdbpyrelation)

Create a relation object from the Parquet files in file_globs




### register

register(self: [duckdb.duckdb.DuckDBPyConnection](#duckdbpyconnection), view_name: str, python_object: object) -> [duckdb.duckdb.DuckDBPyConnection](#duckdbpyconnection)

Register the passed Python Object value for querying with a view




### register_filesystem

register_filesystem(self: [duckdb.duckdb.DuckDBPyConnection](#duckdbpyconnection), filesystem: fsspec.AbstractFileSystem) -> None

Register a fsspec compliant filesystem




### remove_function

remove_function(self: [duckdb.duckdb.DuckDBPyConnection](#duckdbpyconnection), name: str) -> [duckdb.duckdb.DuckDBPyConnection](#duckdbpyconnection)

Remove a previously created function




### rollback

rollback(self: [duckdb.duckdb.DuckDBPyConnection](#duckdbpyconnection)) -> [duckdb.duckdb.DuckDBPyConnection](#duckdbpyconnection)

Roll back changes performed within a transaction




### row_type

row_type(self: [duckdb.duckdb.DuckDBPyConnection](#duckdbpyconnection), fields: object) -> duckdb.duckdb.typing.DuckDBPyType

Create a struct type object from 'fields'




### rowcount

Get result set row count




### sql

sql(self: [duckdb.duckdb.DuckDBPyConnection](#duckdbpyconnection), query: object, *, alias: str = '', params: object = None) -> [duckdb.duckdb.DuckDBPyRelation](#duckdbpyrelation)

Run a SQL query. If it is a SELECT statement, create a relation object from the given SQL query, otherwise run the query as-is.




### sqltype

sqltype(self: [duckdb.duckdb.DuckDBPyConnection](#duckdbpyconnection), type_str: str) -> duckdb.duckdb.typing.DuckDBPyType

Create a type object by parsing the 'type_str' string




### string_type

string_type(self: [duckdb.duckdb.DuckDBPyConnection](#duckdbpyconnection), collation: str = '') -> duckdb.duckdb.typing.DuckDBPyType

Create a string type with an optional collation




### struct_type

struct_type(self: [duckdb.duckdb.DuckDBPyConnection](#duckdbpyconnection), fields: object) -> duckdb.duckdb.typing.DuckDBPyType

Create a struct type object from 'fields'




### table

table(self: [duckdb.duckdb.DuckDBPyConnection](#duckdbpyconnection), table_name: str) -> [duckdb.duckdb.DuckDBPyRelation](#duckdbpyrelation)

Create a relation object for the named table




### table_function

table_function(self: [duckdb.duckdb.DuckDBPyConnection](#duckdbpyconnection), name: str, parameters: object = None) -> [duckdb.duckdb.DuckDBPyRelation](#duckdbpyrelation)

Create a relation object from the named table function with given parameters




### tf

tf(self: [duckdb.duckdb.DuckDBPyConnection](#duckdbpyconnection)) -> dict

Fetch a result as dict of TensorFlow Tensors following execute()




### torch

torch(self: [duckdb.duckdb.DuckDBPyConnection](#duckdbpyconnection)) -> dict

Fetch a result as dict of PyTorch Tensors following execute()




### type

type(self: [duckdb.duckdb.DuckDBPyConnection](#duckdbpyconnection), type_str: str) -> duckdb.duckdb.typing.DuckDBPyType

Create a type object by parsing the 'type_str' string




### union_type

union_type(self: [duckdb.duckdb.DuckDBPyConnection](#duckdbpyconnection), members: object) -> duckdb.duckdb.typing.DuckDBPyType

Create a union type object from 'members'




### unregister

unregister(self: [duckdb.duckdb.DuckDBPyConnection](#duckdbpyconnection), view_name: str) -> [duckdb.duckdb.DuckDBPyConnection](#duckdbpyconnection)

Unregister the view name




### unregister_filesystem

unregister_filesystem(self: [duckdb.duckdb.DuckDBPyConnection](#duckdbpyconnection), name: str) -> None

Unregister a filesystem




### values

values(self: [duckdb.duckdb.DuckDBPyConnection](#duckdbpyconnection), *args) -> [duckdb.duckdb.DuckDBPyRelation](#duckdbpyrelation)

Create a relation object from the passed values




### view

view(self: [duckdb.duckdb.DuckDBPyConnection](#duckdbpyconnection), view_name: str) -> [duckdb.duckdb.DuckDBPyRelation](#duckdbpyrelation)

Create a relation object for the named view




## DuckDBPyRelation



**Bases**: pybind11_object


































### aggregate

aggregate(self: [duckdb.duckdb.DuckDBPyRelation](#duckdbpyrelation), aggr_expr: object, group_expr: str = '') -> [duckdb.duckdb.DuckDBPyRelation](#duckdbpyrelation)

Compute the aggregate aggr_expr by the optional groups group_expr on the relation




### alias

Get the name of the current alias




### any_value

any_value(self: [duckdb.duckdb.DuckDBPyRelation](#duckdbpyrelation), column: str, groups: str = '', window_spec: str = '', projected_columns: str = '') -> [duckdb.duckdb.DuckDBPyRelation](#duckdbpyrelation)

Returns the first non-null value from a given column




### apply

apply(self: [duckdb.duckdb.DuckDBPyRelation](#duckdbpyrelation), function_name: str, function_aggr: str, group_expr: str = '', function_parameter: str = '', projected_columns: str = '') -> [duckdb.duckdb.DuckDBPyRelation](#duckdbpyrelation)

Compute the function of a single column or a list of columns by the optional groups on the relation




### arg_max

arg_max(self: [duckdb.duckdb.DuckDBPyRelation](#duckdbpyrelation), arg_column: str, value_column: str, groups: str = '', window_spec: str = '', projected_columns: str = '') -> [duckdb.duckdb.DuckDBPyRelation](#duckdbpyrelation)

Finds the row with the maximum value for a value column and returns the value of that row for an argument column




### arg_min

arg_min(self: [duckdb.duckdb.DuckDBPyRelation](#duckdbpyrelation), arg_column: str, value_column: str, groups: str = '', window_spec: str = '', projected_columns: str = '') -> [duckdb.duckdb.DuckDBPyRelation](#duckdbpyrelation)

Finds the row with the minimum value for a value column and returns the value of that row for an argument column




### arrow

arrow(self: [duckdb.duckdb.DuckDBPyRelation](#duckdbpyrelation), batch_size: int = 1000000) -> pyarrow.lib.Table

Execute and fetch all rows as an Arrow Table




### avg

avg(self: [duckdb.duckdb.DuckDBPyRelation](#duckdbpyrelation), column: str, groups: str = '', window_spec: str = '', projected_columns: str = '') -> [duckdb.duckdb.DuckDBPyRelation](#duckdbpyrelation)

Computes the average on a given column




### bit_and

bit_and(self: [duckdb.duckdb.DuckDBPyRelation](#duckdbpyrelation), column: str, groups: str = '', window_spec: str = '', projected_columns: str = '') -> [duckdb.duckdb.DuckDBPyRelation](#duckdbpyrelation)

Computes the bitwise AND of all bits present in a given column




### bit_or

bit_or(self: [duckdb.duckdb.DuckDBPyRelation](#duckdbpyrelation), column: str, groups: str = '', window_spec: str = '', projected_columns: str = '') -> [duckdb.duckdb.DuckDBPyRelation](#duckdbpyrelation)

Computes the bitwise OR of all bits present in a given column




### bit_xor

bit_xor(self: [duckdb.duckdb.DuckDBPyRelation](#duckdbpyrelation), column: str, groups: str = '', window_spec: str = '', projected_columns: str = '') -> [duckdb.duckdb.DuckDBPyRelation](#duckdbpyrelation)

Computes the bitwise XOR of all bits present in a given column




### bitstring_agg

bitstring_agg(self: [duckdb.duckdb.DuckDBPyRelation](#duckdbpyrelation), column: str, min: typing.Optional[object] = None, max: typing.Optional[object] = None, groups: str = '', window_spec: str = '', projected_columns: str = '') -> [duckdb.duckdb.DuckDBPyRelation](#duckdbpyrelation)

Computes a bitstring with bits set for each distinct value in a given column




### bool_and

bool_and(self: [duckdb.duckdb.DuckDBPyRelation](#duckdbpyrelation), column: str, groups: str = '', window_spec: str = '', projected_columns: str = '') -> [duckdb.duckdb.DuckDBPyRelation](#duckdbpyrelation)

Computes the logical AND of all values present in a given column




### bool_or

bool_or(self: [duckdb.duckdb.DuckDBPyRelation](#duckdbpyrelation), column: str, groups: str = '', window_spec: str = '', projected_columns: str = '') -> [duckdb.duckdb.DuckDBPyRelation](#duckdbpyrelation)

Computes the logical OR of all values present in a given column




### close

close(self: [duckdb.duckdb.DuckDBPyRelation](#duckdbpyrelation)) -> None

Closes the result




### columns

Return a list containing the names of the columns of the relation.




### count

count(self: [duckdb.duckdb.DuckDBPyRelation](#duckdbpyrelation), column: str, groups: str = '', window_spec: str = '', projected_columns: str = '') -> [duckdb.duckdb.DuckDBPyRelation](#duckdbpyrelation)

Computes the number of elements present in a given column




### create

create(self: [duckdb.duckdb.DuckDBPyRelation](#duckdbpyrelation), table_name: str) -> None

Creates a new table named table_name with the contents of the relation object




### create_view

create_view(self: [duckdb.duckdb.DuckDBPyRelation](#duckdbpyrelation), view_name: str, replace: bool = True) -> [duckdb.duckdb.DuckDBPyRelation](#duckdbpyrelation)

Creates a view named view_name that refers to the relation object




### cross

cross(self: [duckdb.duckdb.DuckDBPyRelation](#duckdbpyrelation), other_rel: [duckdb.duckdb.DuckDBPyRelation](#duckdbpyrelation)) -> [duckdb.duckdb.DuckDBPyRelation](#duckdbpyrelation)

Create cross/cartesian product of two relational objects




### cume_dist

cume_dist(self: [duckdb.duckdb.DuckDBPyRelation](#duckdbpyrelation), window_spec: str, projected_columns: str = '') -> [duckdb.duckdb.DuckDBPyRelation](#duckdbpyrelation)

Computes the cumulative distribution within the partition




### dense_rank

dense_rank(self: [duckdb.duckdb.DuckDBPyRelation](#duckdbpyrelation), window_spec: str, projected_columns: str = '') -> [duckdb.duckdb.DuckDBPyRelation](#duckdbpyrelation)

Computes the dense rank within the partition




### describe

describe(self: [duckdb.duckdb.DuckDBPyRelation](#duckdbpyrelation)) -> [duckdb.duckdb.DuckDBPyRelation](#duckdbpyrelation)

Gives basic statistics (e.g., min, max) and if NULL exists for each column of the relation.




### description

Return the description of the result




### df

df(self: [duckdb.duckdb.DuckDBPyRelation](#duckdbpyrelation), *, date_as_object: bool = False) -> pandas.DataFrame

Execute and fetch all rows as a pandas DataFrame




### distinct

distinct(self: [duckdb.duckdb.DuckDBPyRelation](#duckdbpyrelation)) -> [duckdb.duckdb.DuckDBPyRelation](#duckdbpyrelation)

Retrieve distinct rows from this relation object




### dtypes

Return a list containing the types of the columns of the relation.




### except_

except_(self: [duckdb.duckdb.DuckDBPyRelation](#duckdbpyrelation), other_rel: [duckdb.duckdb.DuckDBPyRelation](#duckdbpyrelation)) -> [duckdb.duckdb.DuckDBPyRelation](#duckdbpyrelation)

Create the set except of this relation object with another relation object in other_rel




### execute

execute(self: [duckdb.duckdb.DuckDBPyRelation](#duckdbpyrelation)) -> [duckdb.duckdb.DuckDBPyRelation](#duckdbpyrelation)

Transform the relation into a result set




### explain

explain(self: [duckdb.duckdb.DuckDBPyRelation](#duckdbpyrelation), type: duckdb.duckdb.ExplainType = 'standard') -> str




### favg

favg(self: [duckdb.duckdb.DuckDBPyRelation](#duckdbpyrelation), column: str, groups: str = '', window_spec: str = '', projected_columns: str = '') -> [duckdb.duckdb.DuckDBPyRelation](#duckdbpyrelation)

Computes the average of all values present in a given column using a more accurate floating point summation (Kahan Sum)




### fetch_arrow_reader

fetch_arrow_reader(self: [duckdb.duckdb.DuckDBPyRelation](#duckdbpyrelation), batch_size: int = 1000000) -> pyarrow.lib.RecordBatchReader

Execute and return an Arrow Record Batch Reader that yields all rows




### fetch_arrow_table

fetch_arrow_table(self: [duckdb.duckdb.DuckDBPyRelation](#duckdbpyrelation), batch_size: int = 1000000) -> pyarrow.lib.Table

Execute and fetch all rows as an Arrow Table




### fetch_df_chunk

fetch_df_chunk(self: [duckdb.duckdb.DuckDBPyRelation](#duckdbpyrelation), vectors_per_chunk: int = 1, *, date_as_object: bool = False) -> pandas.DataFrame

Execute and fetch a chunk of the rows




### fetchall

fetchall(self: [duckdb.duckdb.DuckDBPyRelation](#duckdbpyrelation)) -> list

Execute and fetch all rows as a list of tuples




### fetchdf

fetchdf(self: [duckdb.duckdb.DuckDBPyRelation](#duckdbpyrelation), *, date_as_object: bool = False) -> pandas.DataFrame

Execute and fetch all rows as a pandas DataFrame




### fetchmany

fetchmany(self: [duckdb.duckdb.DuckDBPyRelation](#duckdbpyrelation), size: int = 1) -> list

Execute and fetch the next set of rows as a list of tuples




### fetchnumpy

fetchnumpy(self: [duckdb.duckdb.DuckDBPyRelation](#duckdbpyrelation)) -> dict

Execute and fetch all rows as a Python dict mapping each column to one numpy arrays




### fetchone

fetchone(self: [duckdb.duckdb.DuckDBPyRelation](#duckdbpyrelation)) -> typing.Optional[tuple]

Execute and fetch a single row as a tuple




### filter

filter(self: [duckdb.duckdb.DuckDBPyRelation](#duckdbpyrelation), filter_expr: object) -> [duckdb.duckdb.DuckDBPyRelation](#duckdbpyrelation)

Filter the relation object by the filter in filter_expr




### first

first(self: [duckdb.duckdb.DuckDBPyRelation](#duckdbpyrelation), column: str, groups: str = '', projected_columns: str = '') -> [duckdb.duckdb.DuckDBPyRelation](#duckdbpyrelation)

Returns the first value of a given column




### first_value

first_value(self: [duckdb.duckdb.DuckDBPyRelation](#duckdbpyrelation), column: str, window_spec: str = '', projected_columns: str = '') -> [duckdb.duckdb.DuckDBPyRelation](#duckdbpyrelation)

Computes the first value within the group or partition




### fsum

fsum(self: [duckdb.duckdb.DuckDBPyRelation](#duckdbpyrelation), column: str, groups: str = '', window_spec: str = '', projected_columns: str = '') -> [duckdb.duckdb.DuckDBPyRelation](#duckdbpyrelation)

Computes the sum of all values present in a given column using a more accurate floating point summation (Kahan Sum)




### geomean

geomean(self: [duckdb.duckdb.DuckDBPyRelation](#duckdbpyrelation), column: str, groups: str = '', projected_columns: str = '') -> [duckdb.duckdb.DuckDBPyRelation](#duckdbpyrelation)

Computes the geometric mean over all values present in a given column




### histogram

histogram(self: [duckdb.duckdb.DuckDBPyRelation](#duckdbpyrelation), column: str, groups: str = '', window_spec: str = '', projected_columns: str = '') -> [duckdb.duckdb.DuckDBPyRelation](#duckdbpyrelation)

Computes the histogram over all values present in a given column




### insert

insert(self: [duckdb.duckdb.DuckDBPyRelation](#duckdbpyrelation), values: object) -> None

Inserts the given values into the relation




### insert_into

insert_into(self: [duckdb.duckdb.DuckDBPyRelation](#duckdbpyrelation), table_name: str) -> None

Inserts the relation object into an existing table named table_name




### intersect

intersect(self: [duckdb.duckdb.DuckDBPyRelation](#duckdbpyrelation), other_rel: [duckdb.duckdb.DuckDBPyRelation](#duckdbpyrelation)) -> [duckdb.duckdb.DuckDBPyRelation](#duckdbpyrelation)

Create the set intersection of this relation object with another relation object in other_rel




### join

join(self: [duckdb.duckdb.DuckDBPyRelation](#duckdbpyrelation), other_rel: [duckdb.duckdb.DuckDBPyRelation](#duckdbpyrelation), condition: object, how: str = 'inner') -> [duckdb.duckdb.DuckDBPyRelation](#duckdbpyrelation)

Join the relation object with another relation object in other_rel using the join condition expression in join_condition. Types supported are 'inner' and 'left'




### lag

lag(self: [duckdb.duckdb.DuckDBPyRelation](#duckdbpyrelation), column: str, window_spec: str, offset: int = 1, default_value: str = 'NULL', ignore_nulls: bool = False, projected_columns: str = '') -> [duckdb.duckdb.DuckDBPyRelation](#duckdbpyrelation)

Computes the lag within the partition




### last

last(self: [duckdb.duckdb.DuckDBPyRelation](#duckdbpyrelation), column: str, groups: str = '', projected_columns: str = '') -> [duckdb.duckdb.DuckDBPyRelation](#duckdbpyrelation)

Returns the last value of a given column




### last_value

last_value(self: [duckdb.duckdb.DuckDBPyRelation](#duckdbpyrelation), column: str, window_spec: str = '', projected_columns: str = '') -> [duckdb.duckdb.DuckDBPyRelation](#duckdbpyrelation)

Computes the last value within the group or partition




### lead

lead(self: [duckdb.duckdb.DuckDBPyRelation](#duckdbpyrelation), column: str, window_spec: str, offset: int = 1, default_value: str = 'NULL', ignore_nulls: bool = False, projected_columns: str = '') -> [duckdb.duckdb.DuckDBPyRelation](#duckdbpyrelation)

Computes the lead within the partition




### limit

limit(self: [duckdb.duckdb.DuckDBPyRelation](#duckdbpyrelation), n: int, offset: int = 0) -> [duckdb.duckdb.DuckDBPyRelation](#duckdbpyrelation)

Only retrieve the first n rows from this relation object, starting at offset




### list

list(self: [duckdb.duckdb.DuckDBPyRelation](#duckdbpyrelation), column: str, groups: str = '', window_spec: str = '', projected_columns: str = '') -> [duckdb.duckdb.DuckDBPyRelation](#duckdbpyrelation)

Returns a list containing all values present in a given column




### map

map(self: [duckdb.duckdb.DuckDBPyRelation](#duckdbpyrelation), map_function: Callable, *, schema: typing.Optional[object] = None) -> [duckdb.duckdb.DuckDBPyRelation](#duckdbpyrelation)

Calls the passed function on the relation




### max

max(self: [duckdb.duckdb.DuckDBPyRelation](#duckdbpyrelation), column: str, groups: str = '', window_spec: str = '', projected_columns: str = '') -> [duckdb.duckdb.DuckDBPyRelation](#duckdbpyrelation)

Returns the maximum value present in a given column




### mean

mean(self: [duckdb.duckdb.DuckDBPyRelation](#duckdbpyrelation), column: str, groups: str = '', window_spec: str = '', projected_columns: str = '') -> [duckdb.duckdb.DuckDBPyRelation](#duckdbpyrelation)

Computes the average on a given column




### median

median(self: [duckdb.duckdb.DuckDBPyRelation](#duckdbpyrelation), column: str, groups: str = '', window_spec: str = '', projected_columns: str = '') -> [duckdb.duckdb.DuckDBPyRelation](#duckdbpyrelation)

Computes the median over all values present in a given column




### min

min(self: [duckdb.duckdb.DuckDBPyRelation](#duckdbpyrelation), column: str, groups: str = '', window_spec: str = '', projected_columns: str = '') -> [duckdb.duckdb.DuckDBPyRelation](#duckdbpyrelation)

Returns the minimum value present in a given column




### mode

mode(self: [duckdb.duckdb.DuckDBPyRelation](#duckdbpyrelation), column: str, groups: str = '', window_spec: str = '', projected_columns: str = '') -> [duckdb.duckdb.DuckDBPyRelation](#duckdbpyrelation)

Computes the mode over all values present in a given column




### n_tile

n_tile(self: [duckdb.duckdb.DuckDBPyRelation](#duckdbpyrelation), window_spec: str, num_buckets: int, projected_columns: str = '') -> [duckdb.duckdb.DuckDBPyRelation](#duckdbpyrelation)

Divides the partition as equally as possible into num_buckets




### nth_value

nth_value(self: [duckdb.duckdb.DuckDBPyRelation](#duckdbpyrelation), column: str, window_spec: str, offset: int, ignore_nulls: bool = False, projected_columns: str = '') -> [duckdb.duckdb.DuckDBPyRelation](#duckdbpyrelation)

Computes the nth value within the partition




### order

order(self: [duckdb.duckdb.DuckDBPyRelation](#duckdbpyrelation), order_expr: str) -> [duckdb.duckdb.DuckDBPyRelation](#duckdbpyrelation)

Reorder the relation object by order_expr




### percent_rank

percent_rank(self: [duckdb.duckdb.DuckDBPyRelation](#duckdbpyrelation), window_spec: str, projected_columns: str = '') -> [duckdb.duckdb.DuckDBPyRelation](#duckdbpyrelation)

Computes the relative rank within the partition




### pl

pl(self: [duckdb.duckdb.DuckDBPyRelation](#duckdbpyrelation), batch_size: int = 1000000) -> duckdb::PolarsDataFrame

Execute and fetch all rows as a Polars DataFrame




### product

product(self: [duckdb.duckdb.DuckDBPyRelation](#duckdbpyrelation), column: str, groups: str = '', window_spec: str = '', projected_columns: str = '') -> [duckdb.duckdb.DuckDBPyRelation](#duckdbpyrelation)

Returns the product of all values present in a given column




### project

project(self: [duckdb.duckdb.DuckDBPyRelation](#duckdbpyrelation), *args, groups: str = '') -> [duckdb.duckdb.DuckDBPyRelation](#duckdbpyrelation)

Project the relation object by the projection in project_expr




### quantile

quantile(self: [duckdb.duckdb.DuckDBPyRelation](#duckdbpyrelation), column: str, q: object = 0.5, groups: str = '', window_spec: str = '', projected_columns: str = '') -> [duckdb.duckdb.DuckDBPyRelation](#duckdbpyrelation)

Computes the exact quantile value for a given column




### quantile_cont

quantile_cont(self: [duckdb.duckdb.DuckDBPyRelation](#duckdbpyrelation), column: str, q: object = 0.5, groups: str = '', window_spec: str = '', projected_columns: str = '') -> [duckdb.duckdb.DuckDBPyRelation](#duckdbpyrelation)

Computes the interpolated quantile value for a given column




### quantile_disc

quantile_disc(self: [duckdb.duckdb.DuckDBPyRelation](#duckdbpyrelation), column: str, q: object = 0.5, groups: str = '', window_spec: str = '', projected_columns: str = '') -> [duckdb.duckdb.DuckDBPyRelation](#duckdbpyrelation)

Computes the exact quantile value for a given column




### query

query(self: [duckdb.duckdb.DuckDBPyRelation](#duckdbpyrelation), virtual_table_name: str, sql_query: str) -> [duckdb.duckdb.DuckDBPyRelation](#duckdbpyrelation)

Run the given SQL query in sql_query on the view named virtual_table_name that refers to the relation object




### rank

rank(self: [duckdb.duckdb.DuckDBPyRelation](#duckdbpyrelation), window_spec: str, projected_columns: str = '') -> [duckdb.duckdb.DuckDBPyRelation](#duckdbpyrelation)

Computes the rank within the partition




### rank_dense

rank_dense(self: [duckdb.duckdb.DuckDBPyRelation](#duckdbpyrelation), window_spec: str, projected_columns: str = '') -> [duckdb.duckdb.DuckDBPyRelation](#duckdbpyrelation)

Computes the dense rank within the partition




### record_batch

record_batch(self: [duckdb.duckdb.DuckDBPyRelation](#duckdbpyrelation), batch_size: int = 1000000) -> pyarrow.lib.RecordBatchReader

Execute and return an Arrow Record Batch Reader that yields all rows




### row_number

row_number(self: [duckdb.duckdb.DuckDBPyRelation](#duckdbpyrelation), window_spec: str, projected_columns: str = '') -> [duckdb.duckdb.DuckDBPyRelation](#duckdbpyrelation)

Computes the row number within the partition




### select

select(self: [duckdb.duckdb.DuckDBPyRelation](#duckdbpyrelation), *args, groups: str = '') -> [duckdb.duckdb.DuckDBPyRelation](#duckdbpyrelation)

Project the relation object by the projection in project_expr




### select_dtypes

select_dtypes(self: [duckdb.duckdb.DuckDBPyRelation](#duckdbpyrelation), types: object) -> [duckdb.duckdb.DuckDBPyRelation](#duckdbpyrelation)

Select columns from the relation, by filtering based on type(s)




### select_types

select_types(self: [duckdb.duckdb.DuckDBPyRelation](#duckdbpyrelation), types: object) -> [duckdb.duckdb.DuckDBPyRelation](#duckdbpyrelation)

Select columns from the relation, by filtering based on type(s)




### set_alias

set_alias(self: [duckdb.duckdb.DuckDBPyRelation](#duckdbpyrelation), alias: str) -> [duckdb.duckdb.DuckDBPyRelation](#duckdbpyrelation)

Rename the relation object to new alias




### shape

Tuple of # of rows, # of columns in relation.




### show

show(self: [duckdb.duckdb.DuckDBPyRelation](#duckdbpyrelation), *, max_width: typing.Optional[int] = None, max_rows: typing.Optional[int] = None, max_col_width: typing.Optional[int] = None, null_value: typing.Optional[str] = None, render_mode: object = None) -> None

Display a summary of the data




### sort

sort(self: [duckdb.duckdb.DuckDBPyRelation](#duckdbpyrelation), *args) -> [duckdb.duckdb.DuckDBPyRelation](#duckdbpyrelation)

Reorder the relation object by the provided expressions




### sql_query

sql_query(self: [duckdb.duckdb.DuckDBPyRelation](#duckdbpyrelation)) -> str

Get the SQL query that is equivalent to the relation




### std

std(self: [duckdb.duckdb.DuckDBPyRelation](#duckdbpyrelation), column: str, groups: str = '', window_spec: str = '', projected_columns: str = '') -> [duckdb.duckdb.DuckDBPyRelation](#duckdbpyrelation)

Computes the sample standard deviation for a given column




### stddev

stddev(self: [duckdb.duckdb.DuckDBPyRelation](#duckdbpyrelation), column: str, groups: str = '', window_spec: str = '', projected_columns: str = '') -> [duckdb.duckdb.DuckDBPyRelation](#duckdbpyrelation)

Computes the sample standard deviation for a given column




### stddev_pop

stddev_pop(self: [duckdb.duckdb.DuckDBPyRelation](#duckdbpyrelation), column: str, groups: str = '', window_spec: str = '', projected_columns: str = '') -> [duckdb.duckdb.DuckDBPyRelation](#duckdbpyrelation)

Computes the population standard deviation for a given column




### stddev_samp

stddev_samp(self: [duckdb.duckdb.DuckDBPyRelation](#duckdbpyrelation), column: str, groups: str = '', window_spec: str = '', projected_columns: str = '') -> [duckdb.duckdb.DuckDBPyRelation](#duckdbpyrelation)

Computes the sample standard deviation for a given column




### string_agg

string_agg(self: [duckdb.duckdb.DuckDBPyRelation](#duckdbpyrelation), column: str, sep: str = ',', groups: str = '', window_spec: str = '', projected_columns: str = '') -> [duckdb.duckdb.DuckDBPyRelation](#duckdbpyrelation)

Concatenates the values present in a given column with a separator




### sum

sum(self: [duckdb.duckdb.DuckDBPyRelation](#duckdbpyrelation), column: str, groups: str = '', window_spec: str = '', projected_columns: str = '') -> [duckdb.duckdb.DuckDBPyRelation](#duckdbpyrelation)

Computes the sum of all values present in a given column




### tf

tf(self: [duckdb.duckdb.DuckDBPyRelation](#duckdbpyrelation)) -> dict

Fetch a result as dict of TensorFlow Tensors




### to_arrow_table

to_arrow_table(self: [duckdb.duckdb.DuckDBPyRelation](#duckdbpyrelation), batch_size: int = 1000000) -> pyarrow.lib.Table

Execute and fetch all rows as an Arrow Table




### to_csv

to_csv(self: [duckdb.duckdb.DuckDBPyRelation](#duckdbpyrelation), file_name: str, *, sep: object = None, na_rep: object = None, header: object = None, quotechar: object = None, escapechar: object = None, date_format: object = None, timestamp_format: object = None, quoting: object = None, encoding: object = None, compression: object = None, overwrite: object = None, per_thread_output: object = None, use_tmp_file: object = None, partition_by: object = None, write_partition_columns: object = None) -> None

Write the relation object to a CSV file in 'file_name'




### to_df

to_df(self: [duckdb.duckdb.DuckDBPyRelation](#duckdbpyrelation), *, date_as_object: bool = False) -> pandas.DataFrame

Execute and fetch all rows as a pandas DataFrame




### to_parquet

to_parquet(self: [duckdb.duckdb.DuckDBPyRelation](#duckdbpyrelation), file_name: str, *, compression: object = None, field_ids: object = None, row_group_size_bytes: object = None, row_group_size: object = None, overwrite: object = None, per_thread_output: object = None, use_tmp_file: object = None, partition_by: object = None, write_partition_columns: object = None, append: object = None) -> None

Write the relation object to a Parquet file in 'file_name'




### to_table

to_table(self: [duckdb.duckdb.DuckDBPyRelation](#duckdbpyrelation), table_name: str) -> None

Creates a new table named table_name with the contents of the relation object




### to_view

to_view(self: [duckdb.duckdb.DuckDBPyRelation](#duckdbpyrelation), view_name: str, replace: bool = True) -> [duckdb.duckdb.DuckDBPyRelation](#duckdbpyrelation)

Creates a view named view_name that refers to the relation object




### torch

torch(self: [duckdb.duckdb.DuckDBPyRelation](#duckdbpyrelation)) -> dict

Fetch a result as dict of PyTorch Tensors




### type

Get the type of the relation.




### types

Return a list containing the types of the columns of the relation.




### union

union(self: [duckdb.duckdb.DuckDBPyRelation](#duckdbpyrelation), union_rel: [duckdb.duckdb.DuckDBPyRelation](#duckdbpyrelation)) -> [duckdb.duckdb.DuckDBPyRelation](#duckdbpyrelation)

Create the set union of this relation object with another relation object in other_rel




### unique

unique(self: [duckdb.duckdb.DuckDBPyRelation](#duckdbpyrelation), unique_aggr: str) -> [duckdb.duckdb.DuckDBPyRelation](#duckdbpyrelation)

Number of distinct values in a column.




### update

update(self: [duckdb.duckdb.DuckDBPyRelation](#duckdbpyrelation), set: object, *, condition: object = None) -> None

Update the given relation with the provided expressions




### value_counts

value_counts(self: [duckdb.duckdb.DuckDBPyRelation](#duckdbpyrelation), column: str, groups: str = '') -> [duckdb.duckdb.DuckDBPyRelation](#duckdbpyrelation)

Computes the number of elements present in a given column, also projecting the original column




### var

var(self: [duckdb.duckdb.DuckDBPyRelation](#duckdbpyrelation), column: str, groups: str = '', window_spec: str = '', projected_columns: str = '') -> [duckdb.duckdb.DuckDBPyRelation](#duckdbpyrelation)

Computes the sample variance for a given column




### var_pop

var_pop(self: [duckdb.duckdb.DuckDBPyRelation](#duckdbpyrelation), column: str, groups: str = '', window_spec: str = '', projected_columns: str = '') -> [duckdb.duckdb.DuckDBPyRelation](#duckdbpyrelation)

Computes the population variance for a given column




### var_samp

var_samp(self: [duckdb.duckdb.DuckDBPyRelation](#duckdbpyrelation), column: str, groups: str = '', window_spec: str = '', projected_columns: str = '') -> [duckdb.duckdb.DuckDBPyRelation](#duckdbpyrelation)

Computes the sample variance for a given column




### variance

variance(self: [duckdb.duckdb.DuckDBPyRelation](#duckdbpyrelation), column: str, groups: str = '', window_spec: str = '', projected_columns: str = '') -> [duckdb.duckdb.DuckDBPyRelation](#duckdbpyrelation)

Computes the sample variance for a given column




### write_csv

write_csv(self: [duckdb.duckdb.DuckDBPyRelation](#duckdbpyrelation), file_name: str, *, sep: object = None, na_rep: object = None, header: object = None, quotechar: object = None, escapechar: object = None, date_format: object = None, timestamp_format: object = None, quoting: object = None, encoding: object = None, compression: object = None, overwrite: object = None, per_thread_output: object = None, use_tmp_file: object = None, partition_by: object = None, write_partition_columns: object = None) -> None

Write the relation object to a CSV file in 'file_name'




### write_parquet

write_parquet(self: [duckdb.duckdb.DuckDBPyRelation](#duckdbpyrelation), file_name: str, *, compression: object = None, field_ids: object = None, row_group_size_bytes: object = None, row_group_size: object = None, overwrite: object = None, per_thread_output: object = None, use_tmp_file: object = None, partition_by: object = None, write_partition_columns: object = None, append: object = None) -> None

Write the relation object to a Parquet file in 'file_name'




## Expression



**Bases**: pybind11_object



















































### alias

alias(self: [duckdb.duckdb.Expression](#expression), arg0: str) -> [duckdb.duckdb.Expression](#expression)


Create a copy of this expression with the given alias.

Parameters:
        name: The alias to use for the expression, this will affect how it can be referenced.

Returns:
        Expression: self with an alias.




### asc

asc(self: [duckdb.duckdb.Expression](#expression)) -> [duckdb.duckdb.Expression](#expression)


Set the order by modifier to ASCENDING.




### between

between(self: [duckdb.duckdb.Expression](#expression), lower: [duckdb.duckdb.Expression](#expression), upper: [duckdb.duckdb.Expression](#expression)) -> [duckdb.duckdb.Expression](#expression)




### cast

cast(self: [duckdb.duckdb.Expression](#expression), type: duckdb.duckdb.typing.DuckDBPyType) -> [duckdb.duckdb.Expression](#expression)


Create a CastExpression to type from self

Parameters:
        type: The type to cast to

Returns:
        CastExpression: self::type




### collate

collate(self: [duckdb.duckdb.Expression](#expression), collation: str) -> [duckdb.duckdb.Expression](#expression)




### desc

desc(self: [duckdb.duckdb.Expression](#expression)) -> [duckdb.duckdb.Expression](#expression)


Set the order by modifier to DESCENDING.




### get_name

get_name(self: [duckdb.duckdb.Expression](#expression)) -> str


Return the stringified version of the expression.

Returns:
        str: The string representation.




### isin

isin(self: [duckdb.duckdb.Expression](#expression), *args) -> [duckdb.duckdb.Expression](#expression)


Return an IN expression comparing self to the input arguments.

Returns:
        DuckDBPyExpression: The compare IN expression




### isnotin

isnotin(self: [duckdb.duckdb.Expression](#expression), *args) -> [duckdb.duckdb.Expression](#expression)


Return a NOT IN expression comparing self to the input arguments.

Returns:
        DuckDBPyExpression: The compare NOT IN expression




### isnotnull

isnotnull(self: [duckdb.duckdb.Expression](#expression)) -> [duckdb.duckdb.Expression](#expression)


Create a binary IS NOT NULL expression from self

Returns:
        DuckDBPyExpression: self IS NOT NULL




### isnull

isnull(self: [duckdb.duckdb.Expression](#expression)) -> [duckdb.duckdb.Expression](#expression)


Create a binary IS NULL expression from self

Returns:
        DuckDBPyExpression: self IS NULL




### nulls_first

nulls_first(self: [duckdb.duckdb.Expression](#expression)) -> [duckdb.duckdb.Expression](#expression)


Set the NULL order by modifier to NULLS FIRST.




### nulls_last

nulls_last(self: [duckdb.duckdb.Expression](#expression)) -> [duckdb.duckdb.Expression](#expression)


Set the NULL order by modifier to NULLS LAST.




### otherwise

otherwise(self: [duckdb.duckdb.Expression](#expression), value: [duckdb.duckdb.Expression](#expression)) -> [duckdb.duckdb.Expression](#expression)


Add an ELSE <value> clause to the CaseExpression.

Parameters:
        value: The value to use if none of the WHEN conditions are met.

Returns:
        CaseExpression: self with an ELSE clause.




### show

show(self: [duckdb.duckdb.Expression](#expression)) -> None


Print the stringified version of the expression.




### when

when(self: [duckdb.duckdb.Expression](#expression), condition: [duckdb.duckdb.Expression](#expression), value: [duckdb.duckdb.Expression](#expression)) -> [duckdb.duckdb.Expression](#expression)


Add an additional WHEN <condition> THEN <value> clause to the CaseExpression.

Parameters:
        condition: The condition that must be met.
        value: The value to use if the condition is met.

Returns:
        CaseExpression: self with an additional WHEN clause.




## StatementType

Members:

INVALID

SELECT

INSERT

UPDATE

CREATE

DELETE

PREPARE

EXECUTE

ALTER

TRANSACTION

COPY

ANALYZE

VARIABLE_SET

CREATE_FUNC

EXPLAIN

DROP

EXPORT

PRAGMA

VACUUM

CALL

SET

LOAD

RELATION

EXTENSION

LOGICAL_PLAN

ATTACH

DETACH

MULTI

COPY_DATABASE

**Bases**: pybind11_object


### ALTER

Members:

INVALID

SELECT

INSERT

UPDATE

CREATE

DELETE

PREPARE

EXECUTE

ALTER

TRANSACTION

COPY

ANALYZE

VARIABLE_SET

CREATE_FUNC

EXPLAIN

DROP

EXPORT

PRAGMA

VACUUM

CALL

SET

LOAD

RELATION

EXTENSION

LOGICAL_PLAN

ATTACH

DETACH

MULTI

COPY_DATABASE




### ANALYZE

Members:

INVALID

SELECT

INSERT

UPDATE

CREATE

DELETE

PREPARE

EXECUTE

ALTER

TRANSACTION

COPY

ANALYZE

VARIABLE_SET

CREATE_FUNC

EXPLAIN

DROP

EXPORT

PRAGMA

VACUUM

CALL

SET

LOAD

RELATION

EXTENSION

LOGICAL_PLAN

ATTACH

DETACH

MULTI

COPY_DATABASE




### ATTACH

Members:

INVALID

SELECT

INSERT

UPDATE

CREATE

DELETE

PREPARE

EXECUTE

ALTER

TRANSACTION

COPY

ANALYZE

VARIABLE_SET

CREATE_FUNC

EXPLAIN

DROP

EXPORT

PRAGMA

VACUUM

CALL

SET

LOAD

RELATION

EXTENSION

LOGICAL_PLAN

ATTACH

DETACH

MULTI

COPY_DATABASE




### CALL

Members:

INVALID

SELECT

INSERT

UPDATE

CREATE

DELETE

PREPARE

EXECUTE

ALTER

TRANSACTION

COPY

ANALYZE

VARIABLE_SET

CREATE_FUNC

EXPLAIN

DROP

EXPORT

PRAGMA

VACUUM

CALL

SET

LOAD

RELATION

EXTENSION

LOGICAL_PLAN

ATTACH

DETACH

MULTI

COPY_DATABASE




### COPY

Members:

INVALID

SELECT

INSERT

UPDATE

CREATE

DELETE

PREPARE

EXECUTE

ALTER

TRANSACTION

COPY

ANALYZE

VARIABLE_SET

CREATE_FUNC

EXPLAIN

DROP

EXPORT

PRAGMA

VACUUM

CALL

SET

LOAD

RELATION

EXTENSION

LOGICAL_PLAN

ATTACH

DETACH

MULTI

COPY_DATABASE




### COPY_DATABASE

Members:

INVALID

SELECT

INSERT

UPDATE

CREATE

DELETE

PREPARE

EXECUTE

ALTER

TRANSACTION

COPY

ANALYZE

VARIABLE_SET

CREATE_FUNC

EXPLAIN

DROP

EXPORT

PRAGMA

VACUUM

CALL

SET

LOAD

RELATION

EXTENSION

LOGICAL_PLAN

ATTACH

DETACH

MULTI

COPY_DATABASE




### CREATE

Members:

INVALID

SELECT

INSERT

UPDATE

CREATE

DELETE

PREPARE

EXECUTE

ALTER

TRANSACTION

COPY

ANALYZE

VARIABLE_SET

CREATE_FUNC

EXPLAIN

DROP

EXPORT

PRAGMA

VACUUM

CALL

SET

LOAD

RELATION

EXTENSION

LOGICAL_PLAN

ATTACH

DETACH

MULTI

COPY_DATABASE




### CREATE_FUNC

Members:

INVALID

SELECT

INSERT

UPDATE

CREATE

DELETE

PREPARE

EXECUTE

ALTER

TRANSACTION

COPY

ANALYZE

VARIABLE_SET

CREATE_FUNC

EXPLAIN

DROP

EXPORT

PRAGMA

VACUUM

CALL

SET

LOAD

RELATION

EXTENSION

LOGICAL_PLAN

ATTACH

DETACH

MULTI

COPY_DATABASE




### DELETE

Members:

INVALID

SELECT

INSERT

UPDATE

CREATE

DELETE

PREPARE

EXECUTE

ALTER

TRANSACTION

COPY

ANALYZE

VARIABLE_SET

CREATE_FUNC

EXPLAIN

DROP

EXPORT

PRAGMA

VACUUM

CALL

SET

LOAD

RELATION

EXTENSION

LOGICAL_PLAN

ATTACH

DETACH

MULTI

COPY_DATABASE




### DETACH

Members:

INVALID

SELECT

INSERT

UPDATE

CREATE

DELETE

PREPARE

EXECUTE

ALTER

TRANSACTION

COPY

ANALYZE

VARIABLE_SET

CREATE_FUNC

EXPLAIN

DROP

EXPORT

PRAGMA

VACUUM

CALL

SET

LOAD

RELATION

EXTENSION

LOGICAL_PLAN

ATTACH

DETACH

MULTI

COPY_DATABASE




### DROP

Members:

INVALID

SELECT

INSERT

UPDATE

CREATE

DELETE

PREPARE

EXECUTE

ALTER

TRANSACTION

COPY

ANALYZE

VARIABLE_SET

CREATE_FUNC

EXPLAIN

DROP

EXPORT

PRAGMA

VACUUM

CALL

SET

LOAD

RELATION

EXTENSION

LOGICAL_PLAN

ATTACH

DETACH

MULTI

COPY_DATABASE




### EXECUTE

Members:

INVALID

SELECT

INSERT

UPDATE

CREATE

DELETE

PREPARE

EXECUTE

ALTER

TRANSACTION

COPY

ANALYZE

VARIABLE_SET

CREATE_FUNC

EXPLAIN

DROP

EXPORT

PRAGMA

VACUUM

CALL

SET

LOAD

RELATION

EXTENSION

LOGICAL_PLAN

ATTACH

DETACH

MULTI

COPY_DATABASE




### EXPLAIN

Members:

INVALID

SELECT

INSERT

UPDATE

CREATE

DELETE

PREPARE

EXECUTE

ALTER

TRANSACTION

COPY

ANALYZE

VARIABLE_SET

CREATE_FUNC

EXPLAIN

DROP

EXPORT

PRAGMA

VACUUM

CALL

SET

LOAD

RELATION

EXTENSION

LOGICAL_PLAN

ATTACH

DETACH

MULTI

COPY_DATABASE




### EXPORT

Members:

INVALID

SELECT

INSERT

UPDATE

CREATE

DELETE

PREPARE

EXECUTE

ALTER

TRANSACTION

COPY

ANALYZE

VARIABLE_SET

CREATE_FUNC

EXPLAIN

DROP

EXPORT

PRAGMA

VACUUM

CALL

SET

LOAD

RELATION

EXTENSION

LOGICAL_PLAN

ATTACH

DETACH

MULTI

COPY_DATABASE




### EXTENSION

Members:

INVALID

SELECT

INSERT

UPDATE

CREATE

DELETE

PREPARE

EXECUTE

ALTER

TRANSACTION

COPY

ANALYZE

VARIABLE_SET

CREATE_FUNC

EXPLAIN

DROP

EXPORT

PRAGMA

VACUUM

CALL

SET

LOAD

RELATION

EXTENSION

LOGICAL_PLAN

ATTACH

DETACH

MULTI

COPY_DATABASE




### INSERT

Members:

INVALID

SELECT

INSERT

UPDATE

CREATE

DELETE

PREPARE

EXECUTE

ALTER

TRANSACTION

COPY

ANALYZE

VARIABLE_SET

CREATE_FUNC

EXPLAIN

DROP

EXPORT

PRAGMA

VACUUM

CALL

SET

LOAD

RELATION

EXTENSION

LOGICAL_PLAN

ATTACH

DETACH

MULTI

COPY_DATABASE




### INVALID

Members:

INVALID

SELECT

INSERT

UPDATE

CREATE

DELETE

PREPARE

EXECUTE

ALTER

TRANSACTION

COPY

ANALYZE

VARIABLE_SET

CREATE_FUNC

EXPLAIN

DROP

EXPORT

PRAGMA

VACUUM

CALL

SET

LOAD

RELATION

EXTENSION

LOGICAL_PLAN

ATTACH

DETACH

MULTI

COPY_DATABASE




### LOAD

Members:

INVALID

SELECT

INSERT

UPDATE

CREATE

DELETE

PREPARE

EXECUTE

ALTER

TRANSACTION

COPY

ANALYZE

VARIABLE_SET

CREATE_FUNC

EXPLAIN

DROP

EXPORT

PRAGMA

VACUUM

CALL

SET

LOAD

RELATION

EXTENSION

LOGICAL_PLAN

ATTACH

DETACH

MULTI

COPY_DATABASE




### LOGICAL_PLAN

Members:

INVALID

SELECT

INSERT

UPDATE

CREATE

DELETE

PREPARE

EXECUTE

ALTER

TRANSACTION

COPY

ANALYZE

VARIABLE_SET

CREATE_FUNC

EXPLAIN

DROP

EXPORT

PRAGMA

VACUUM

CALL

SET

LOAD

RELATION

EXTENSION

LOGICAL_PLAN

ATTACH

DETACH

MULTI

COPY_DATABASE




### MULTI

Members:

INVALID

SELECT

INSERT

UPDATE

CREATE

DELETE

PREPARE

EXECUTE

ALTER

TRANSACTION

COPY

ANALYZE

VARIABLE_SET

CREATE_FUNC

EXPLAIN

DROP

EXPORT

PRAGMA

VACUUM

CALL

SET

LOAD

RELATION

EXTENSION

LOGICAL_PLAN

ATTACH

DETACH

MULTI

COPY_DATABASE




### PRAGMA

Members:

INVALID

SELECT

INSERT

UPDATE

CREATE

DELETE

PREPARE

EXECUTE

ALTER

TRANSACTION

COPY

ANALYZE

VARIABLE_SET

CREATE_FUNC

EXPLAIN

DROP

EXPORT

PRAGMA

VACUUM

CALL

SET

LOAD

RELATION

EXTENSION

LOGICAL_PLAN

ATTACH

DETACH

MULTI

COPY_DATABASE




### PREPARE

Members:

INVALID

SELECT

INSERT

UPDATE

CREATE

DELETE

PREPARE

EXECUTE

ALTER

TRANSACTION

COPY

ANALYZE

VARIABLE_SET

CREATE_FUNC

EXPLAIN

DROP

EXPORT

PRAGMA

VACUUM

CALL

SET

LOAD

RELATION

EXTENSION

LOGICAL_PLAN

ATTACH

DETACH

MULTI

COPY_DATABASE




### RELATION

Members:

INVALID

SELECT

INSERT

UPDATE

CREATE

DELETE

PREPARE

EXECUTE

ALTER

TRANSACTION

COPY

ANALYZE

VARIABLE_SET

CREATE_FUNC

EXPLAIN

DROP

EXPORT

PRAGMA

VACUUM

CALL

SET

LOAD

RELATION

EXTENSION

LOGICAL_PLAN

ATTACH

DETACH

MULTI

COPY_DATABASE




### SELECT

Members:

INVALID

SELECT

INSERT

UPDATE

CREATE

DELETE

PREPARE

EXECUTE

ALTER

TRANSACTION

COPY

ANALYZE

VARIABLE_SET

CREATE_FUNC

EXPLAIN

DROP

EXPORT

PRAGMA

VACUUM

CALL

SET

LOAD

RELATION

EXTENSION

LOGICAL_PLAN

ATTACH

DETACH

MULTI

COPY_DATABASE




### SET

Members:

INVALID

SELECT

INSERT

UPDATE

CREATE

DELETE

PREPARE

EXECUTE

ALTER

TRANSACTION

COPY

ANALYZE

VARIABLE_SET

CREATE_FUNC

EXPLAIN

DROP

EXPORT

PRAGMA

VACUUM

CALL

SET

LOAD

RELATION

EXTENSION

LOGICAL_PLAN

ATTACH

DETACH

MULTI

COPY_DATABASE




### TRANSACTION

Members:

INVALID

SELECT

INSERT

UPDATE

CREATE

DELETE

PREPARE

EXECUTE

ALTER

TRANSACTION

COPY

ANALYZE

VARIABLE_SET

CREATE_FUNC

EXPLAIN

DROP

EXPORT

PRAGMA

VACUUM

CALL

SET

LOAD

RELATION

EXTENSION

LOGICAL_PLAN

ATTACH

DETACH

MULTI

COPY_DATABASE




### UPDATE

Members:

INVALID

SELECT

INSERT

UPDATE

CREATE

DELETE

PREPARE

EXECUTE

ALTER

TRANSACTION

COPY

ANALYZE

VARIABLE_SET

CREATE_FUNC

EXPLAIN

DROP

EXPORT

PRAGMA

VACUUM

CALL

SET

LOAD

RELATION

EXTENSION

LOGICAL_PLAN

ATTACH

DETACH

MULTI

COPY_DATABASE




### VACUUM

Members:

INVALID

SELECT

INSERT

UPDATE

CREATE

DELETE

PREPARE

EXECUTE

ALTER

TRANSACTION

COPY

ANALYZE

VARIABLE_SET

CREATE_FUNC

EXPLAIN

DROP

EXPORT

PRAGMA

VACUUM

CALL

SET

LOAD

RELATION

EXTENSION

LOGICAL_PLAN

ATTACH

DETACH

MULTI

COPY_DATABASE




### VARIABLE_SET

Members:

INVALID

SELECT

INSERT

UPDATE

CREATE

DELETE

PREPARE

EXECUTE

ALTER

TRANSACTION

COPY

ANALYZE

VARIABLE_SET

CREATE_FUNC

EXPLAIN

DROP

EXPORT

PRAGMA

VACUUM

CALL

SET

LOAD

RELATION

EXTENSION

LOGICAL_PLAN

ATTACH

DETACH

MULTI

COPY_DATABASE



































### name

name(self: object) -> str




### value





## Expressions

### CaseExpression

CaseExpression(condition: [duckdb.duckdb.Expression](#expression), value: [duckdb.duckdb.Expression](#expression)) -> [duckdb.duckdb.Expression](#expression)




### CoalesceOperator

CoalesceOperator(*args) -> [duckdb.duckdb.Expression](#expression)




### ColumnExpression

ColumnExpression(*args) -> [duckdb.duckdb.Expression](#expression)

Create a column reference from the provided column name




### ConstantExpression

ConstantExpression(value: object) -> [duckdb.duckdb.Expression](#expression)

Create a constant expression from the provided value




### DefaultExpression

DefaultExpression() -> [duckdb.duckdb.Expression](#expression)




### FunctionExpression

FunctionExpression(function_name: str, *args) -> [duckdb.duckdb.Expression](#expression)




### LambdaExpression

LambdaExpression(lhs: object, rhs: [duckdb.duckdb.Expression](#expression)) -> [duckdb.duckdb.Expression](#expression)




### StarExpression

StarExpression(*args, **kwargs)
Overloaded function.

1. StarExpression(*, exclude: object = None) -> [duckdb.duckdb.Expression](#expression)

2. StarExpression() -> [duckdb.duckdb.Expression](#expression)



## Values

### BinaryValue



**Bases**: Value


### BitValue



**Bases**: Value


### BlobValue



**Bases**: Value


### BooleanValue



**Bases**: Value


### DateValue



**Bases**: Value


### DecimalValue



**Bases**: Value


### DoubleValue



**Bases**: Value


### FloatValue



**Bases**: Value


### HugeIntegerValue



**Bases**: Value


### IntegerValue



**Bases**: Value


### IntervalValue



**Bases**: Value


### LongValue



**Bases**: Value


### NullValue



**Bases**: Value


### ShortValue



**Bases**: Value


### StringValue



**Bases**: Value


### TimeTimeZoneValue



**Bases**: Value


### TimeValue



**Bases**: Value


### TimestampMilisecondValue



**Bases**: Value


### TimestampNanosecondValue



**Bases**: Value


### TimestampSecondValue



**Bases**: Value


### TimestampTimeZoneValue



**Bases**: Value


### TimestampValue



**Bases**: Value


### UUIDValue



**Bases**: Value


### UnsignedBinaryValue



**Bases**: Value


### UnsignedIntegerValue



**Bases**: Value


### UnsignedLongValue



**Bases**: Value


### UnsignedShortValue



**Bases**: Value


### Value



**Bases**: object

## Exceptions

### BinderException

Common base class for all non-exit exceptions.

**Bases**: ProgrammingError


### CatalogException

Common base class for all non-exit exceptions.

**Bases**: ProgrammingError


### ConnectionException

Common base class for all non-exit exceptions.

**Bases**: OperationalError


### ConstraintException

Common base class for all non-exit exceptions.

**Bases**: IntegrityError


### ConversionException

Common base class for all non-exit exceptions.

**Bases**: DataError


### DataError

Common base class for all non-exit exceptions.

**Bases**: DatabaseError


### Error

Common base class for all non-exit exceptions.

**Bases**: Exception


### FatalException

Common base class for all non-exit exceptions.

**Bases**: DatabaseError


### HTTPException

Thrown when an error occurs in the httpfs extension, or whilst downloading an extension.

**Bases**: IOException


### IOException

Common base class for all non-exit exceptions.

**Bases**: OperationalError


### IntegrityError

Common base class for all non-exit exceptions.

**Bases**: DatabaseError


### InternalError

Common base class for all non-exit exceptions.

**Bases**: DatabaseError


### InternalException

Common base class for all non-exit exceptions.

**Bases**: InternalError


### InterruptException

Common base class for all non-exit exceptions.

**Bases**: DatabaseError


### InvalidInputException

Common base class for all non-exit exceptions.

**Bases**: ProgrammingError


### InvalidTypeException

Common base class for all non-exit exceptions.

**Bases**: ProgrammingError


### NotImplementedException

Common base class for all non-exit exceptions.

**Bases**: NotSupportedError


### NotSupportedError

Common base class for all non-exit exceptions.

**Bases**: DatabaseError


### OperationalError

Common base class for all non-exit exceptions.

**Bases**: DatabaseError


### OutOfMemoryException

Common base class for all non-exit exceptions.

**Bases**: OperationalError


### OutOfRangeException

Common base class for all non-exit exceptions.

**Bases**: DataError


### ParserException

Common base class for all non-exit exceptions.

**Bases**: ProgrammingError


### PermissionException

Common base class for all non-exit exceptions.

**Bases**: DatabaseError


### ProgrammingError

Common base class for all non-exit exceptions.

**Bases**: DatabaseError


### SequenceException

Common base class for all non-exit exceptions.

**Bases**: DatabaseError


### SerializationException

Common base class for all non-exit exceptions.

**Bases**: OperationalError


### SyntaxException

Common base class for all non-exit exceptions.

**Bases**: ProgrammingError


### TransactionException

Common base class for all non-exit exceptions.

**Bases**: OperationalError


### TypeMismatchException

Common base class for all non-exit exceptions.

**Bases**: DataError


### Warning

Common base class for all non-exit exceptions.

**Bases**: Exception
