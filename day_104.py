# Determine whether a doubly linked list is a palindrome. What if it’s singly linked?
# If list is sigly linked i would use stack, or reverse list and comapare it with orignal.

def isPalindrome(start, end, list):
    end -= 1
    while start <= end:
        if list[start] != list[end]:
            return False
        start += 1
        end -= 1
    
    return True