import random
def genotp():
    otp=''
    ul=[chr(i) for i in range(ord('A'),ord('Z')+1)]
    ll=[chr(i) for i in range(ord('a'),ord('z')+1)]
    for i in range(0,2):
        otp=otp+str(random.randint(0,9))
        otp=otp+random.choice(ul)
        otp=otp+random.choice(ll)
    return otp