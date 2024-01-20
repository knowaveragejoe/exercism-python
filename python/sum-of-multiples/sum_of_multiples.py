def sum_of_multiples(limit, multiples):
    return sum(set([multiple * i for i in range(1, limit) for multiple in multiples if multiple * i < limit]))