'''

삼각수, 오각수, 육각수는 아래 식으로 구할 수 있습니다.

삼각수	 	Tn = n (n + 1) / 2	 	1, 3, 6, 10, 15, ...
오각수	 	Pn = n (3n − 1) / 2	 	1, 5, 12, 22, 35, ...
육각수	 	Hn = n (2n − 1)	 	1, 6, 15, 28, 45, ...
여기서 T285 = P165 = H143 = 40755 가 됩니다.

오각수와 육각수도 되는, 그 다음으로 큰 삼각수를 구하세요.

아직 미완성
'''

def t(n):
    return n * (n + 1) / 2

def j(n):
    return n * (3 * n - 1) / 2

def h(n):
    return n * (2 * n - 1)

t2 = 286
j2 = 166
h2 = 144

while (t(t2)!=j(j2)!=h(h2)) :
    if min(t(t2),j(j2),h(h2)) == t(t2) :
        t2+=1
    if min(t(t2),j(j2),h(h2)) == j(j2) :
        j2+=1
    if min(t(t2),j(j2),h(h2)) == h(h2) :
        h2+=1

print(t(t2))
print(j(j2))
print(h(h2))
