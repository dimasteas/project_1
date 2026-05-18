"""
Модуль для обработки списков банковских операций.
"""
from datetime import datetime
from typing import Any


def filter_by_state(
    operations: list[dict[str, Any]],
    state: str = 'EXECUTED'
) -> list[dict[str, Any]]:
    """
    Фильтрует список операций по заданному статусу.
    """
    result = []
    for op in operations:
        if op.get('state') == state:
            result.append(op)
    return result


def sort_by_date(
    operations: list[dict[str, Any]],
    descending: bool = True
) -> list[dict[str, Any]]:
    """
    Сортирует список операций по дате.
    """
    return sorted(
        operations,
        key=lambda op: datetime.fromisoformat(op['date']),
        reverse=descending
    )