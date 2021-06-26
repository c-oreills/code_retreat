R=50
S=set(range(R))
b={c:1 for c in ((0,2),(1,3),(2,1),(2,2),(2,3))}
o=(-1,0,1)
while 1:
 b = {(x,y):int(sum(b.get(((x+u)%R,(y+v)%R),0) for u in o for v in o)+10*b.get((x,y),0) in (3,13,14)) for x in S for y in S}
 for y in S: print(''.join('.#'[b[x,y]] for x in S))
