from django.db import connection
from typing import List, Dict


def run_custom_sql(sql: str, params=None) -> List[Dict]:
    """Run a custom SQL query and return list of dicts.

    Use with care; prefer ORM for usual queries.
    """
    with connection.cursor() as cursor:
        cursor.execute(sql, params or [])
        columns = [col[0]
                   for col in cursor.description] if cursor.description else []
        rows = cursor.fetchall()
    result = [dict(zip(columns, row)) for row in rows]
    return result
