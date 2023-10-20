name=[ "may", "kein", "kain", "radi" ]
yearing=[ 5, 10, 1, 3 ]
photo=[[ "may", "kein", "kain", "radi" ],
[ "may", "kein", "brin", "deny" ],
[ "kon", "kain", "may", "coni" ]]

def solution(name,yearing,photo):
    return [sum(yearing[name.index(j)] for j in i if j in name) for i in photo]

print(solution(name,yearing,photo))