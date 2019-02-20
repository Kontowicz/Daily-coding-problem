# Using a function rand7() that returns an integer from 1 to 7 (inclusive) with uniform probability, implement a function rand5() that returns an integer from 1 to 5 (inclusive).

def rand7():
    pass

def rand5():
    return (rand7() - 1) + (5*(rand7() - 1))