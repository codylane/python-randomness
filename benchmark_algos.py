#!/usr/bin/env python
# coding: utf-8
#
import random
import timeit


def generate_weighted_random_ints(weights, size):
    start_counter = 0
    results = []

    last_index = 0
    array = []

    weight_map = {
        key: i + 1
        for i, key in enumerate(weights)
    }

    for weight in weights:
        for i in range(start_counter, weight):
            i += last_index
            array.append(weight_map[weight])
        start_counter = 0
        last_index += weight

    while len(results) < size:
        random_index = int(random.random() * sum(weights))
        results.append(array[random_index])

    return results


def calculate_results(results):
    ones = [_ for _ in results if _ == 1]
    twos = [_ for _ in results if _ == 2]
    threes = [_ for _ in results if _ == 3]

    print(len(ones) + len(twos) + len(threes))
    print(len(ones), len(twos), len(threes))
    print(results)

    return ones, twos, threes


def do_benchmark_mr_music(times=None):
    times = times or 10 ** 5

    result = timeit.timeit(
        setup='from __main__ import generate_weighted_random_ints',
        stmt='generate_weighted_random_ints(weights=[66, 12, 22], size=100)',  # noqa: E501
        number=times,
    )

    return result


def do_benchmark_mr_shlep(times=None):
    times = times or 10 ** 5

    result = timeit.timeit(
        setup='from randomness import weighted_random_generator',
        stmt='weighted_random_generator(weights=[66, 12, 22], size=100, start=1, end=3)',  # noqa: E501
        number=times,
    )

    return result


if __name__ == '__main__':
    weights = [66, 12, 22]
    size = 100

    results = generate_weighted_random_ints(weights=weights, size=size)
    calculate_results(results)

    print(do_benchmark_mr_music(times=10 ** 4))
    print(do_benchmark_mr_shlep(times=10 ** 4))
