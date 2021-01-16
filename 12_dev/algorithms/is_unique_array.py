def is_unique(arr):
    
    result = True
    breadcrumbs = {}

    for i, v in enumerate(arr):
        print(f"~~~~ LOOP ~~~~ arr[{i}] === {v}")
        if v in breadcrumbs:
            result = False
        else:
            breadcrumbs[v] = True
    return result

print("is unique:", is_unique([1,2,3,4,5,66,7,45]))