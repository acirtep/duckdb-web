import inspect

import duckdb


def get_doc_for_duckdb():
    doc = ""

    duckdb_class_members = inspect.getmembers(duckdb)

    # remove the modules
    duckdb_class_members = [
        member for member in duckdb_class_members if not inspect.ismodule(member[1])
    ]

    # get the expressions related
    expression_classes = [
        member[1]
        for member in duckdb_class_members
        if check_if_related_to_expression(member[1])
    ]
    expressions_doc = get_doc_for_expressions(expression_classes)

    # get the exception classes
    exception_classes = [
        member[1]
        for member in duckdb_class_members
        if inspect.isclass(member[1]) and issubclass(member[1], Exception)
    ]
    exceptions_doc = get_doc_for_exceptions(exception_classes)

    # get the value based classes
    value_classes = [
        member[1]
        for member in duckdb_class_members
        if inspect.isclass(member[1]) and issubclass(member[1], duckdb.Value)
    ]
    values_doc = get_doc_for_values(value_classes)

    # get the built-in functions and methods for duckdb class
    builtin_members = [
        member[1]
        for member in duckdb_class_members
        if inspect.isbuiltin(member[1])
        and member[1] not in exception_classes + expression_classes + value_classes
    ]

    doc = f"{doc}\n## duckdb"
    for builtin_member in builtin_members:
        doc = f"{doc}\n{get_doc_for_member(builtin_member.__name__, builtin_member, header="###")}"

    for member_name, member in duckdb_class_members:
        if (
            member
            in exception_classes + expression_classes + value_classes + builtin_members
        ):
            continue

        if member_name not in [
            "DuckDBPyRelation",
            "DuckDBPyConnection",
            "Expression",
            "StatementType",
        ]:
            continue

        doc = f"{doc}\n{get_doc_for_member(member_name, member, header="##")}"
        doc = get_doc_for_class_members(class_member=member, doc=doc)

    doc = doc + '\n' + expressions_doc + '\n' + values_doc + '\n' + exceptions_doc
    doc = doc.replace(
        "duckdb.duckdb.DuckDBPyRelation",
        "[duckdb.duckdb.DuckDBPyRelation](#duckdbpyrelation)",
    )
    doc = doc.replace(
        "duckdb.duckdb.DuckDBPyConnection",
        "[duckdb.duckdb.DuckDBPyConnection](#duckdbpyconnection)",
    )
    doc = doc.replace(
        "duckdb.duckdb.Expression", "[duckdb.duckdb.Expression](#expression)"
    )
    return doc


def get_doc_for_member(member_name, member, header):
    if member_name.startswith("_"):
        return ""

    bases = ""
    if hasattr(member, "__bases__"):
        bases = f"**Bases**: {','.join([base.__name__ for base in member.__bases__])}"
    return f"""
{header} {member_name}

{inspect.getdoc(member) if inspect.getdoc(member) else ''}

{bases}
"""


def check_if_related_to_expression(member):
    if not callable(member):
        return False
    member_docs = inspect.getdoc(member)
    if not member_docs:
        return False
    return '-> duckdb.duckdb.Expression' in member_docs


def get_doc_for_class_members(class_member, doc, header="###"):
    if not inspect.isclass(class_member):
        return doc

    for member_name, member_value in inspect.getmembers(class_member):
        doc = f"{doc}\n{get_doc_for_member(member_name, member_value, header)}"

    return doc


def get_doc_for_exceptions(exception_classes):
    doc = f"## Exceptions"
    for exception_class in exception_classes:
        doc = f"{doc}\n{get_doc_for_member(exception_class.__name__, exception_class, header="###")}"
        doc = get_doc_for_class_members(exception_classes, doc, header="####")

    return doc


def get_doc_for_values(value_classes):
    doc = f"## Values"
    for value_class in value_classes:
        doc = f"{doc}\n{get_doc_for_member(value_class.__name__, value_class, header="###")}"
        doc = get_doc_for_class_members(value_classes, doc, header="####")

    return doc


def get_doc_for_expressions(expression_classes):
    doc = f"## Expressions"
    for expression_class in expression_classes:
        doc = f"{doc}\n{get_doc_for_member(expression_class.__name__, expression_class, header="###")}"
        doc = get_doc_for_class_members(expression_class, doc, header="####")

    return doc


def main():
    with open("docs/stable/clients/python/reference/index.md", "w") as f:
        f.write(
            """\
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

"""
        )
        doc = get_doc_for_duckdb()

        f.write(doc)


if __name__ == "__main__":
    main()
