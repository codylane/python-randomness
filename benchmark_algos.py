#!/usr/bin/env python
# coding: utf-8 #


import random
import timeit


DEFAULT_TEST_TIMES = 10 ** 5


def generate_weights(weight_map):
    start_counter = 0
    last_index = 0
    array = []

    for weight in weights:
        for _ in range(start_counter, weight):
            array.append(weight_map[weight])
        start_counter = 0
        last_index += weight

    return array


def generate_weighted_random_ints(weights, weight_map, size):
    results = []

    index_map = {
        v: 0
        for _, v in weight_map.items()
    }

    while len(results) < size:
        random_index = int(random.random() * size)
        random_result = weights[random_index]

        __import__('pdb').set_trace()
        if index_map[random_result] < weight_map.keys()[random_result - 1]:
            index_map[random_result] += 1
            __import__('pdb').set_trace()
            results.append(random_result)

        print(len(results))
    return results


def calculate_results(results):
    ones = [_ for _ in results if _ == 1]
    twos = [_ for _ in results if _ == 2]
    threes = [_ for _ in results if _ == 3]

    data = {
        'results': {
            ':size': len(ones) + len(twos) + len(threes),
        },
        'totals': {
            'ones': len(ones),
            'twos': len(twos),
            'threes': len(threes),
        }
    }

    return data


def do_benchmark_mr_music(times=None):
    times = times or DEFAULT_TEST_TIMES

    stmt = '''
        generate_weighted_random_ints(weights=[66, 12, 22], size=100)'
    '''

    result = timeit.timeit(
        setup='from __main__ import generate_weighted_random_ints',
        stmt=stmt,
        number=times,
    )

    print_benchmark_result(times=times, result=result)

    return result


def do_benchmark_mr_shlep(times=None):
    times = times or DEFAULT_TEST_TIMES

    result = timeit.timeit(
        setup='from randomness import weighted_random_generator',
        stmt='weighted_random_generator(weights=[66, 12, 22], size=100, start=1, end=3)',  # noqa: E501
        number=times,
    )

    print_benchmark_result(times=times, result=result)

    return result


def print_benchmark_result(times, result):
    return f'=Ran algorithm {times} and it took {result} seconds'


if __name__ == '__main__':
    weights = [66, 12, 22]
    size = 100

    weight_map = {
        i + 1: value
        for i, value in enumerate(weights)
    }
    __import__('pdb').set_trace()

    weights = [_ for _ in generate_weights(weight_map=weight_map)]

    results = generate_weighted_random_ints(
        size=size,
        weight_map=weight_map,
        weights=weights,
    )

    calculate_results(results)

    do_benchmark_mr_music(times=DEFAULT_TEST_TIMES)
    do_benchmark_mr_shlep(times=DEFAULT_TEST_TIMES)
