M = [13023, 201527, 4294967291]
N = [
    21179556, 5337795, 18437072,
    11383457, 16076557, 13286032,
    37655692, 471675, 21030418,
    33533337, 9666873, 6884524, 111490,
    18371648
]
mm = ""
nn = ""
kk = ""

for n in N:
    res = (n * M[0] + M[1])
    print()
    res1 = res % M[2]
    res2 = res // M[2]
    print("res=%15i %10x, res2=%3i %2x, res1=%15i %10x" % (res, res, res2, res2, res1, res1))

    res = res1
    a = hex(res)
    if a.startswith('-'):
        a = a[1:]
    a = a[2:]
    if a.endswith('L'):
        a = a[:-1]
    while len(a) % 2 != 0:
        a = '0' + a

    res3 = (res * M[0] + M[1]) % M[2]
    res4 = (res3 * M[0] + M[1]) % M[2]
    print(res,res3,res4)

    nn += chr(res & 0xff) + chr(res3 & 0xff) + chr(res4 & 0xff)
    mm += a
    print(nn,mm)
    input('')

print("\n")
#print(kk) wafev19772@scarden.com
print(nn)
#print(mm.decode("hex"))
