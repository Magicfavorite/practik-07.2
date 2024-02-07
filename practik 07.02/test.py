def makecloser(par):
    loc = par
    def power(p):
        return p ** loc
    return power

fsqr = makecloser(2)
fcub = makecloser(3)
for i in range(5):
    print((i, fsqr(i), fcub(i)))

#var = 1
#fun = outer(var)
#print(fun())


#for i in range(3):
#    print(i)
#
#
#print(i)