# python3

from collections import namedtuple

Bracket = namedtuple("Bracket", ["char", "position"])


def are_matching(left, right):
    return (left + right) in ["()", "[]", "{}"]


def find_mismatch(text):
    opening_brackets_stack = []
    matching = True
    counter = 0
    for i, next in enumerate(text):
        if next in "([{":
            # Process opening bracket, write your code here
            opening_brackets_stack.append(next)
        if next in ")]}":
            # Process closing bracket, write your code here
            matching = are_matching(opening_brackets_stack[-1], next)
            opening_brackets_stack.pop()
        counter = counter + 1
        if matching == False: return counter
    return False

def main():
    text = input()
    text = input()
    mismatch = find_mismatch(text)
    # Printing answer, write your code here
    if mismatch == False:
        print("Success")
    else:
        print(mismatch)

if __name__ == "__main__":
    main()
