# Revision 1 BEGIN/ 24Mar22
## Begin Derek Ruggirello here (24Mar22)

def gcd(a, b):
    if a > b:
        r = a % b
        if r == 0:
            print(b)
            return
        else:
            gcd(b, r)
    elif a < b:
        r = b % a
        if r == 0:
            print(b)
            return
        else:
            gcd(a, r)
    else:
        print(a)


gcd(1071, 462)
gcd(12, 8)
gcd(20, 24)
gcd(422, 49221)
gcd(293, 922)
gcd(38,204)

# Revision 1 FINAL 24Mar22
## End Derek Ruggirello here
# HALF-LIFE/Ron Bass/John Richards Sr./After-Burner Elite #