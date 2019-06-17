# Given an array of elements, return the length of
# the longest subarray where all its elements are distinct.
def longest(arr, collection=set()):
    if not arr:
        return len(collection)

    if arr[0] in collection:
        return len(collection)

    collection = collection.copy()
    collection.add(arr[0])

    return max(longest(arr[1:], collection),
               longest(arr[1:]))

print(longest([5, 1, 3, 5, 2, 3, 4, 1]))