# coding: utf-8

import random


INDEX_MAP = {
    1: 'A',
    2: 'B',
    3: 'C',
}


def random_generator(size, start=None, end=None, **kwargs):
    '''Generates a list of random numbers

    params:
        size (int)  - Required
                    - The number of total items the generator should perform
                      calculations.
        start (int) - Optional - The start of the range. Defaults to `1`
        end (int)   - Optional -The end of the range. Defaults to `size + 1`
        kwargs (dict): To be passed to random.randrange

    returns:
        (list) - Of random numbers

    '''
    start = start or 1
    end = end or (size + 1)

    for _ in range(0, size):
        yield int(random.random() * end) + 1


def weighted_random_generator(weights, size, start=None, end=None, **kwargs):  # noqa: E501
    '''Do it

    '''
    results = []

    start = start or 0
    end = end or size

    bean_counter = {
        i: 0
        for i in INDEX_MAP
    }

    while len(results) < size:
        random_iterator = random_generator(
                size=end,
                start=start,
                end=end,
                **kwargs,
        )

        rand_nums = [n for n in random_iterator]

        for rand_num in rand_nums:
            if bean_counter[rand_num] < weights[rand_num - 1]:
                bean_counter[rand_num] += 1
                if len(results) < size:
                    results.append(rand_num)

    return results


if __name__ == '__main__':
    results = weighted_random_generator(
        weights=[66, 12, 22],
        size=100,
        start=1,
        end=3,
    )

    assert len(results) == 100

    print(results)

    data = {
        i: 0
        for i in INDEX_MAP
    }

    for result in results:
        data[result] += 1

    assert sum(data.values()) == 100

    print(data)
