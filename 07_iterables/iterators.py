iterable = ['Spring', 'Summer', 'Autumn', 'Winter']
iterator = iter(iterable)

# next(iterator)

def first(iterable):
    iterator = iter(iterable)
    try:
        return next(iterator)
    except StopIteration:
        raise ValueError("iterable is empty")

def first_list():
    var_list = ["1st", "2nd", "3rd"]
    return first(var_list)

def first_set():
    var_set = {"1st", "2nd", "3rd"}
    return first(var_set)
