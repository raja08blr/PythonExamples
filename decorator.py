def div(a,b):
    print(a/b)

def smart_div(func):
    def innner(a,b):
        if a<b:
            a,b = b,a
        return func(a,b)
    return innner
div = smart_div(div)
div(2,4)