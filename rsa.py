# -*- coding: utf-8 -*-

from random import random
from prime_num import generate_prime, AlgEvklid, Zpow, generate_prime_fix_len, AlgEvklid_ex
import sys

def generate_rsa_key(bits_len):
    p = None
    q = None
    while p is None:
        p = generate_prime_fix_len(bits_len)     # generate 1st prime
    while q is None:
        q = generate_prime_fix_len(bits_len)     # generate 2nd prime

    n = p*q                             # modulo

    phi = (p - 1) * (q - 1)             # Euler function of n

    # let's start to generate RSA key

    pos = 256
    e = 2**pos+1
    x = 0
    y = 0
    while AlgEvklid(phi, e, x, y) != 1:
        pos <<= 1
        e = pos ** 2 + 1

    res = AlgEvklid_ex(phi, e)
    d = res['y']
    if d < 0:
        d += phi
    print (d + phi)*e % phi

    public_key = {
        'e': e,
        'n': n
    }

    private_key = {
        'd': d,
        'n': n
    }
    return {
        'public_key': public_key,
        'private_key': private_key
    }


def main():

    p = generate_rsa_key()

    mes = bytearray(b"Hello, RSA!")

    fin = sys.stdin()


    print mes
    v = ""
    for i in mes:
        v += hex(i)[2:]
    v = '0x' + v
    v = int(v, 16)
    cr = Zpow(v, p['public_key']['e'], p['public_key']['n'])
    print cr
    mes = Zpow(cr, p['private_key']['d'], p['private_key']['n'])
    print mes
    tmp = hex(mes)[2:-1]
    print tmp
    print tmp.decode("hex")
    return


if __name__ == "__main__":
    main()


