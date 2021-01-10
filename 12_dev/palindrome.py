def digits(x): 
    digit_list = []
    print("Initial value: ", x)
    while x != 0:
        div, mod = divmod(x, 10)
        digit_list.append(mod)
        x = div
    return digit_list

# digits(3534)
def is_palindrome_num(x):
    dlist = digits(x)
    for f, r in zip(dlist, reversed(dlist)):
        if f != r:
            return False
    return True

def is_palindrome_string(x):
    slist = list(x)
    for f, r in zip(slist, reversed(slist)):
        if f != r:
            return False
    return True

# Remove all whitespace in a string
# If you want to remove leading and ending spaces, use str.strip():
sentence = ' hello  apple'
sentence.strip()

# If you want to remove all space characters, use str.replace():
sentence = ' hello  apple'
sentence.replace(" ", "")

# If you want to remove duplicated spaces, use str.split():
sentence = ' hello  apple'
" ".join(sentence.split())


print(is_palindrome_num(25852))
print(is_palindrome_num(125462))
print(is_palindrome_string("Was it a cat I saw".replace(" ","").upper()))
