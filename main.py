class simplex:
    def standardize(inp):
        pos = -1
        for x in range(len(inp)):
            if isinstance(inp[x], str):
                pos = x
                if '>' in inp[x]:
                    inp[x] = -1
                elif '<' in inp[x]:
                    inp[x] = 1
                break
        print (inp)




r1 =[1,1,'>=',2]
