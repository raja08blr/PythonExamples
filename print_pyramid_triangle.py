def pyramid_tri(r):
    for x in range(r):
        print(' '*(r-x-1)+'*'*(2*x+1))
pyramid_tri(5)