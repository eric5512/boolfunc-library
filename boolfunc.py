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
    function = []
    for m in minterms:
        bin_minterm = to_bin(m, n_vars)
        for v in range(n_vars):
            if not bin_minterm[v]:
                function.append("not")
            function.append("var[%s]" % v)
            function.append("and")        
        function.pop(-1)
        function.append("or")
    function.pop(-1)
    function = " ".join(function)
    print(function)
    def b_function(*var):
        return int(eval(function))
    return b_function

def simplify(f):
    pass
    #minimization with quine-Mccluskey



def main():
    r_mint = find_minterms(test((lambda x, y: int(x != y)), 2))
    print(r_mint)
    print(find_minterms(test(create_function(r_mint, 2), 2)))

if __name__ == "__main__":
    main()