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
    letters = [chr(i) for i in range(ord('a'), ord('a') + 1 + n_vars)]
    variables = []
    function = []
    for m in minterms:
        bin_minterm = to_bin(m, n_vars)
        for v in range(n_vars):
            if not bin_minterm[v]:
                function.append("not")
            function.append(letters[v])
            function.append("and")        
        function.pop(-1)
        function.append("or")
    function.pop(-1)
    function = " ".join(function)
    print(function)
    def b_function(a=0,b=0,c=0,d=0,e=0,f=0,g=0,h=0,i=0,j=0,k=0,l=0,m=0,n=0,o=0,p=0,q=0,r=0,s=0,t=0,u=0,v=0,w=0,x=0,y=0,z=0):
        return int(eval(function))
    return b_function
        


def main():
    r_mint = find_minterms(test((lambda x, y: int(x != y)), 2))
    print(r_mint)
    print(find_minterms(test(create_function(r_mint, 2), 2)))

if __name__ == "__main__":
    main()