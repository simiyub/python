import bisect
import random

"""
This function implements the method nextNum() such that,
given Random Numbers are [-1, 0, 1, 2, 3] 
and Probabilities of [0.01, 0.3, 0.58, 0.1, 0.01] 
if we call nextNum() 100 times we may get the following results.
-1: 1 times 0: 22 times 1: 57 times 2: 20 times 3: 0 times
"""

#TODO Potentially add another function that generates multiple random numbers using a generator



class RandomGenerator:

    def __init__(self, random_numbers, probabilities):
        """
        Does some validation of the random numbers and probabilities provided
        Initialises values provided
        """

        if len(random_numbers) != len(probabilities):
            raise ValueError(
                f'Probability is required for all random numbers provided. '
                f'Received {len(probabilities)} probabilities for {len(random_numbers)} random numbers.')

        def _validate_probabilities(values):
            if not any(x < 0.0 for x in values):
                if abs(sum(values) - 1.0) <= 1e-10:
                    return
                raise ValueError(
                    f'Probabilities provided ({values}) do not add up to exactly 1.0.".format(values)'
                )

            raise ValueError(f'Received negative probability {values}')

        def _validate_random_numbers(values):
            if len(values) == len(set(values)):
                return
            raise ValueError(f'Random numbers {values} contains duplicates')

        def _cumulative_probabilities():
            values = []
            value = 0
            for probability in self._probabilities:
                value += probability
                values.append(value)
            return values

        _validate_probabilities(probabilities)
        _validate_random_numbers(random_numbers)

        self._probabilities = probabilities
        self._random_numbers = random_numbers
        self._cumulative_probabilities = _cumulative_probabilities()
        #TODO run this in next random number index instead.

    def random_values_used(self):
        return tuple(self._random_numbers)

    def probabilities_used(self):
        return tuple(self._probabilities)

    def _next_random_number_index(self):
        """
        Obtains the index to store the next random
        number using the python bisect function
        """
        random_value = random.random()
        index = bisect.bisect_right(self._cumulative_probabilities, random_value)

        if index == len(self._cumulative_probabilities):
            raise ValueError(f'No valid index for {random_value} in {self._cumulative_probabilities}')
        return index

    def next_num(self):
        """
        Returns one of the randomNums.
        When this method is called multiple times over a long period,
        it should return the numbers roughly with the initialized probabilities.
        """
        return self._random_numbers[self._next_random_number_index()]
