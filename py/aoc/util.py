import time
import typing
from functools import wraps


def sliding_window(
    seq: typing.Sequence, size: int
) -> typing.Generator[typing.Sequence, None, None]:
    """
    Example: [1,2,3,4,5] -> [[1,2],[2,3],[3,4],[4,5]]
    :param seq:
    :param size:
    :return:
    """
    for i in range(len(seq) - size + 1):
        yield seq[i : i + size]


def batch(
    seq: typing.Sequence, size: int, allow_unequal: bool = False
) -> typing.Generator[typing.Sequence, None, None]:
    """
    Example: [1,2,3,4] -> [[1,2], [3, 4]]

    Unequal batches will raise an exception.
    :param allow_unequal:
    :param seq:
    :param size:
    :return:
    """
    if not allow_unequal and len(seq) % size != 0:
        raise Exception("Sequence cannot be batched equally")

    for i in range(0, len(seq), size):
        yield seq[i : i + size]


def adj(x: int, y: int, horizontal: bool = False):
    """
    Returns adjacent coords to x, y
    :param x:
    :param y:
    :param horizontal: include horizontal adjacents
    :return:
    """
    if horizontal:
        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                if dx == dy == 0:
                    continue
                yield x + dx, y + dy
    else:
        for dxy in [-1, 1]:
            yield x + dxy, y
            yield x, y + dxy


def benchmark(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Elapsed time for {func.__name__}: {end_time - start_time} seconds")
        return result

    return wrapper
