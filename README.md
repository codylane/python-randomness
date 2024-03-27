Python Randomness
=================

This is a small demo repo used to demonstrate ways Python can be used
generate random number generators for games or for science.


# Bootstraping the project

- Install GNU Make [GNU Make Download](https://www.gnu.org/software/make/#download)

- Then run `make` on the command line to download and install all the
  Pythons listed in the [.init.env](./.init.env) file

- You only have to do ^^ once. After that all you have to do to
  bootstrap the project is (from a Bash shell):

  ```
  . ./init.sh
  ```

# Problem Scenarios

## Scenario

- I have 3 variables (A, B, C)

- I use a random range generator to generate a range of random numbers
    between [1, 3] where 1 is the low range and 3 is included in the
    range.

- The mapping per index is as follows
  ```
  INDEX_MAPPING = {
    1: 'A',
    2: 'B',
    3: 'C',
  }
  ```

## The Challenge

- The issue is this test provided the randomness for this result:
  - A is 65%
  - B is 12%
  - C is 33%

- **Total Randomness %** = `(65 + 12 + 33)` = `110`

- Random chance of A is 65%
- Random chance of B is 12%
- Random chance of B is 33%

## The Goal

- Right now there is a random picker given a Min/Max to be incluse fo the value
  provided.

- **How then do we weight the chances without random 1-100 and then if
    1-65 ....**


# Run Tests

```
tox
```

## List of tests to run

```
tox -l
```

## Run a specific test

This only runs the `bandit` tests

```
tox -e bandit
```
