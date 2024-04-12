# coding: utf-8

from inspect import cleandoc
import random
import timeit


class WeightedRandomizer:
    def __init__(self, weights):
        self.__max = .0
        self.__weights = []
        for value, weight in weights.items():
            self.__max += weight
            self.__weights.append((self.__max, value))

    def random(self):
        r = random.random() * self.__max
        for ceil, value in self.__weights:
            if ceil > r:
                return value

    def result_size(self, results, expected_size):
        total_size = sum([_ for _ in results.values()])

        if total_size != expected_size:
            raise ValueError(f'{total_size} != {expected_size}')

        return total_size


def do_benchmark(times=None):
    times = times or 10 ** 5

    setup = cleandoc(
        '''
        from __main__ import WeightedRandomizer

        w = {'A': 66.0, 'B': 12.0, 'C': 22.0}
        wr = WeightedRandomizer(w)
        total = 100 ** 1
        results = {'A': 0, 'B': 0, 'C': 0}
        '''
    )

    stmt = cleandoc(
        '''
        for i in range(total):
            results[wr.random()] += 1
        '''
    )

    seconds = timeit.timeit(
        setup=setup,
        stmt=stmt,
        number=times,
    )

    return {
        'seconds': seconds,
        'times': times,
        'called_times_per_second': times / seconds,
    }


def single_run(size=None):
    size = size or 100

    w = {'A': 66.0, 'B': 12.0, 'C': 22.0}

    wr = WeightedRandomizer(w)

    results = {'A': 0, 'B': 0, 'C': 0}
    for i in range(size):
        results[wr.random()] += 1

    results_size = wr.result_size(results, size)

    print(f'After {size} rounds the distribution is: {results} size={results_size}')  # noqa: E501

    return results
