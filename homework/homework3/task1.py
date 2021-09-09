from typing import Any, Callable, List, Tuple


def cache(func: Callable, count: int) -> Callable:
    lst = []

    def fin(*args) -> Tuple[List, Any]:
        for i in lst:
            if i[0] == [*args]:
                return i[1]
        a = func(*args)
        if len(lst) < count:
            lst.append([[*args], a])
        return a
    return fin
