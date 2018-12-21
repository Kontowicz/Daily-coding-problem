# Implement an autocomplete system. That is, given a query string s and a set of all possible query strings,
# return all strings in the set that have s as a prefix.
# For example, given the query string de and the set of strings [dog, deer, deal], return [deer, deal].

# basic - fast to impelment aproach 

basic_dictionary = ['dog', 'deer', 'deal']

def autocomplete(prefix):
    to_return = []
    for word in basic_dictionary:
        if word[0:len(prefix)] == prefix:
            to_return.append(word)
    return to_return

assert autocomplete('de') == ['deer', 'deal']