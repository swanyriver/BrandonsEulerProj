import timeit

def abtest(funcs, args, verbose=False):
    """runs funcs[] with unpacked args[] displaying name and time to execute"""
    if type(args) is not list: args = [args]
    results =[]
    for func in funcs:
        timein = timeit.time.time()
        func(*args)
        timetotal = timeit.time.time() - timein
        results.append((func.func_name,timetotal))
        if verbose:
            print "%s ran in %f seconds with args:"% \
            (func.func_name,timetotal), args
    return results

def scaletest(func, args, verbose=False):
    """runs func with each argument in args displaying name and time to execute"""
    results =[]
    for arg in args:
        timein = timeit.time.time()

        if type(arg) is list: func(*arg)
        else: func(arg)

        timetotal = timeit.time.time() - timein
        results.append((arg,timetotal))
        if verbose:
            print "%s ran in %f seconds with args:"% \
            (func.func_name,timetotal), arg
    return results



