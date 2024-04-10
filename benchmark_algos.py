#!/usr/bin/env python
# coding: utf-8 #


import random
import timeit


DEFAULT_TEST_TIMES = 10 ** 5


def generate_weights(weights, weight_map):
    start_counter = 0
    last_index = 0
    array = []

    for weight in weights:
        for _ in range(start_counter, weight):
            array.append(weight_map[weight])
        start_counter = 0
        last_index += weight

    return array


def generate_weighted_random_ints(weights, weight_map):
    results = []

    size = len(weights)

    index_map = {
        i + 1: 0
        for i in range(0, len(weight_map.values()))
    }

    while len(results) < size:
        random_index = int(random.random() * size)
        random_value = weights[random_index]

        if index_map[random_value] < weight_map[random_value]:
            index_map[random_value] += 1
            results.append(random_value)

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
        generate_weighted_random_ints(weights=[66, 12, 22])
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

    weight_map = {
        weight: i + 1
        for i, weight in enumerate(weights)
    }

    generated_weights = [
        _
        for _ in generate_weights(weights=weights, weight_map=weight_map)
    ]

    weight_map = {
        i + 1: weight
        for i, weight in enumerate(weights)
    }

    results = generate_weighted_random_ints(
        weight_map=weight_map,
        weights=generated_weights,
    )

    calculate_results(results)

    # do_benchmark_mr_music(times=DEFAULT_TEST_TIMES)
    # do_benchmark_mr_shlep(times=DEFAULT_TEST_TIMES)
