R=50
S=set(range(R))
O=-1,1,0
b={}
while 1:
 b={(x,y):int(2<sum((l:=b[(x+u)%R,(y+v)%R]) for u in O for v in O)-l/2<4 if b and not print('.#'[b[x,y]],end='\n '[x<R-1]) else (x,y) in {(0,2),(1,3),(2,1),(2,2),(2,3)}) for y in S for x in S}
