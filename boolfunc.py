from functools import partial

def to_bin(number, n_bits=0):
    bits_array = []
    while number != 0:
        bits_array.append(number % 2)
        number = number >> 1
    while len(bits_array) < n_bits:
        bits_array.append(0)
    bits_array.reverse()
    return bits_array

def apply(function, number, n_vars):
    number = to_bin(number, n_vars)
    for i in range(n_vars):
        function = partial(function,number[i])
    return function()

def test(function, n_vars):
    truth_table = []
    for n in range(2**n_vars):
        truth_table.append(apply(function, n, n_vars))
    return truth_table

def find_minterms(truth_table):
    minterms = []
    for k,v in enumerate(truth_table):
        if v == 1:
            minterms.append(k)
    return minterms

def create_function(minterms, n_vars):
    for k,m in enumerate(minterms):
        pass


def main():
    print(find_minterms(test((lambda x, y: x or y), 2)))

if __name__ == "__main__":
    main()