class ChainIterator:
    def __init__(self, *sequences: tuple[list, ...]) -> None:
        self.sequences = sequences
        self.index = 0
        self.sequence_index = 0

    def __iter__(self):
        return self

    def __next__(self):
        try:
            self.sequence_index += 1
            element = self.sequences[self.index][self.sequence_index-1]
            return element
        except IndexError:
            self.sequence_index = 1
            self.index += 1

            if self.index == len(self.sequences):
                raise StopIteration
            return self.sequences[self.index][self.sequence_index-1]
my_list_chain = ChainIterator([1, 2, 3],[4],[5])
for item in my_list_chain:
    print(item)

print('-' * 30)
class ZipIterator:
    def __init__(self, *sequences: tuple[list, ...]) -> None:
        self.sequences = sequences
        self.index = 0
        self.min_length = min(len(sequence) for sequence in sequences) if sequences else 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= self.min_length:
            raise StopIteration
        result = tuple(sequence[self.index] for sequence in self.sequences)
        self.index += 1
        return result

my_list_zip = ZipIterator([1, 2],[3, 4],[5, 6])
for item in my_list_zip:
    print(item)
print()
print('-' * 30)



def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False
    return True


def generate_primes(n):
    if n>1:
        yield 1

    for num in range(2, n+1):
        if is_prime(num):
            yield num

primes = generate_primes(11)
for prime in primes:
    print(prime)
print()
print('-' * 30)


def generate_combinations(sequence, k):
    def steps(start, current):
        if len(current) == k:
            yield tuple(current)
            return

        for i in range(start, len(sequence)):
            current.append(sequence[i])
            yield from steps(i+1, current)
            current.pop()

    yield from steps(0, [])


combinations = generate_combinations([1, 2, 3], 2)
for combination in combinations:
    print(combination)
print('-' * 30)

def flatten_iterable(lst):
    for item in lst:
        if type(item) is list:
            yield from flatten_iterable(item)
        else:
            yield item


flatten_list = flatten_iterable([1, 2,[3, [4], 5]])
for item in flatten_list:
    print(item)