# Assume you have access to a function toss_biased() which returns 0 or 1 with a probability 
# that's not 50-50 (but also not 0-100 or 100-0). You do not know the bias of the coin.

def toss_biased():
    pass

def toss():
    f = toss_biased()
    s = toss_biased()
    if f == 0 and s==1:
        return 0
    if f == 1 and s==0:
        return 1
    return toss()