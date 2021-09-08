from typing import Any, Callable, List, Tuple


def cache(func: Callable, count: int) -> Callable:
    lst = []

    def fin(*args) -> Tuple[List, Any]:
        a = func(*args)
        if len(lst) < count:
            lst.append(a)
        return lst, a
    return fin
