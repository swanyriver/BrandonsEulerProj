import timeit

def runone(func,args):
    timein = timeit.time.time()
    func(*args)
    timetotal = timeit.time.time() - timein
    print "%s ran in %f seconds with args:"%(func.func_name,timetotal), args

def abtest(funcs, args, scale=False):
    """runs funcs[] with unpacked args[] displaying name and time to execute
       if scale then first item of arg is list of args to be iterated over"""
    for func in funcs:
        if scale:
            for s in args[0]:
                if len(args)>1: runone(func,[s,args[1:]])
                else: runone(func,[s])
        else: runone(func,args)



