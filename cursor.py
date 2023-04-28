import snowflake.connector
import sys
import json

var = dict()
sys.path.append("D:\ETL\scripts")
with open("scripts\config.json.bak") as f:
    var = json.load(f)


def create_cursor():
    ctx = snowflake.connector.connect(
        user=var["user"],
        password=var["password"],
        account=var["account"],
        warehouse="samrat_wrk3",
        # database="bhatbhateni",
        # schema="transactions",
    )
    cs = ctx.cursor()
    return ctx, cs


def execute_query(SQL):
    cs = create_cursor()
    result = cs.execute(SQL)
    return result
