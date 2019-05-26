"""
Compute the gereatest common divisor of two nonnegative integers p and q as follows:
If q is 0 the answer is p. If not divide p by q and take the remainder r. The answer is the greatest common divisor of q and r
"""
      
def gcd(p, q):

    if q == 0:
        return p
    r = p % q
    return gcd(q,r)

   
print(gcd(8, 14)) # -> 4

print(gcd(100, 0)) # -> 100

print(gcd(18, 84)) # - 6

