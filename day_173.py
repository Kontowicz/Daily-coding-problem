# Write a function to flatten a nested dictionary. Namespace the keys with a period.

def isDictionaty(variable):
    return type(variable) == type({1:1})

def makeFlat(orginal, flatten, path):
    if not isDictionaty(orginal):
        flatten[path] = orginal
        return

    for key in orginal:
        newPath = '{}.{}'.format(path, key) if path else key
        makeFlat(orginal[key], flatten, newPath)

def flat(dict):
    toReturn = {}
    makeFlat(dict, toReturn, '')
    return toReturn

d = {
    "key": 3,
    "foo": {
        "a": 5,
        "bar": {
            "baz": 8
        }
    }
}

assert flat(d) == {
    "key": 3,
    "foo.a": 5,
    "foo.bar.baz": 8
}