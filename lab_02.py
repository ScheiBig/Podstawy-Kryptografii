import random
import math


def gdc(a: int, b: int):
    return b if a == 0 else gdc(b % a, a)


def prime(fro: int, to: int) -> int:
    r = random.randint(fro, to)
    while True:
        is_prime = True
        for i in range(2, math.ceil(math.sqrt(r))):
            if r % i == 0:
                is_prime = False
                break

        if is_prime:
            return r

        r += 1


def find_mod_inv(a: int, m: int) -> int:
    (r, new_r) = (m, a)
    (t, new_t) = (int(0), int(1))

    while new_r != 0:
        quo = r // new_r
        (t, new_t) = (new_t, t - quo * new_t)
        (r, new_r) = (new_r, r - quo * new_r)

    if r > 1:
        return None
    elif t < 0:
        return t + m
    else:
        return t


p = prime(2**40, 2**44)
q = prime(2**40, 2**44)
print(f"p: {p}, q: {q}")

n = p * q
phi = (p - 1)*(q - 1)
e = 2 ** 16 + 1
assert gdc(e, phi) == 1

d = find_mod_inv(e, phi)
print(f"d: {d}")

assert d != None

msg = 420
crypt = pow(msg, e, n)
decrypt = pow(crypt, d, n)
print(f"og message: {msg}")
print(f"encrypted message: {crypt}")
print(f"decrypted message: {decrypt}")
