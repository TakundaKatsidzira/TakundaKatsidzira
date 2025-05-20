"""
Comma code assignment
Write a function that takes a list value as an argument and returns
a string with all the items separated by a comma and a space, with and
inserted before the last item. For example, passing the previous spam list to
the function would return 'apples, bananas, tofu, and cats'.
But your function should be able to work with any list value passed to it
"""
def comma_code(items):
    if not items:
        return ''
    elif len(items) == 1:
        return items[0]
    elif len(items) == 2:
        return f"{items[0]} and {items[1]}"
    else:
        return ', '.join(items[:-1]) + f", and {items[-1]}"

def main():
    # Example usage
    food = ['apples', 'bananas', 'tofu', 'cats']
    print("There's", comma_code(food))  # Output: apples, bananas, tofu, and cats
    

if __name__ == "__main__":
    main()