# Challenge 3-1
# The CBC padding oracle

from Cryptopals_main import AESCode, create_rand_byte_fun

def main():
    # Randomly encrypt a random string from Challenge_3-17.txt
    c3_1 = AESCode(key='random', iv='random')  # Random cipher

    # Create function that randomly returns a string from Challenge_3-17.txt as a byte
    c3_1_rand_byte_fun = create_rand_byte_fun('..\Challenge_3-17.txt', 'b64')

    # Create oracle out of random cipher and byte generator
    c3_1_oracle = c3_1.gen_cbc_oracle_rand(c3_1_rand_byte_fun)

    # See example generation
    c3_1.easybyte.b = c3_1_oracle()
    print(c3_1.easybyte.b)

    # As in previous challenges, AESCode.cbc_solve solves the cipher and attempts to unpad
    # An error will be raised if unpadding runs into a problem (ex: incorrect padding)
    print(c3_1.cbc_solve().decode())


if __name__ == "__main__":
    main()
