from trino.dbapi import connect
from trino.auth import BasicAuthentication
from sqlalchemy import create_engine
from sqlalchemy.schema import Table, MetaData
from sqlalchemy.sql.expression import select, text

engine = create_engine('trino://xxx:yyy@emr-t.data.avedian.info:8889/avedian_dwh')
connection = engine.connect()

rows = connection.execute(text("SELECT * FROM avedian_dwh.wh_olap.diagnosis_view LIMIT 10")).fetchall()
print(rows);