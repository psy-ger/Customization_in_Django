"""Utilities for direct database access.

This module provides a helper to execute raw SQL and return results
as a list of dictionaries. Use the ORM for most queries; this helper
is for cases where raw SQL is required.
"""

from typing import Any, Dict, Iterable, List, Optional

from django.db import connection


def run_custom_sql(sql: str, params: Optional[Iterable[Any]] = None) -> List[Dict[str, Any]]:
    """Execute raw SQL and return rows as a list of dicts.

    Args:
        sql: SQL statement to execute.
        params: Optional parameters for the SQL statement.

    Returns:
        A list of dictionaries mapping column names to values.
    """
    with connection.cursor() as cursor:
        cursor.execute(sql, list(params or []))
        columns = [col[0]
                   for col in cursor.description] if cursor.description else []
        rows = cursor.fetchall()

    return [dict(zip(columns, row)) for row in rows]
