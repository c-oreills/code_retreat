R=50
S=set(range(R))
O=-1,1,0
b=0
while 1:b={(c:=(x,y)):int(2<sum((l:=b[(x+u)%R,(y+v)%R]) for u in O for v in O)-l/2<4 if b and print('.#'[b[c]],end='\n '[x<R-1])!=0 else c in zip((0,1,2,2,2),(2,3,1,2,3))) for y in S for x in S}
