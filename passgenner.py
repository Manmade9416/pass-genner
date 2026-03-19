import argparse
import random
import secrets
import string

def password_gen(length, minnum, special):
    # Prevent minnum + special >= length
    if minnum + special >= length:
        raise ValueError("Total minimum requirements exceed password length.")
    
    # Character pools
    amanumber = string.digits
    amaspecial = string.punctuation
    alphabet = string.digits + string.ascii_letters + string.punctuation
    
    # Password character storage
    password_chars = []
    
    # Numbers to satisfy minnum 
    for i in range(minnum):
        password_chars.append(secrets.choice(amanumber))
    
    # Special chars to satisfy special
    for i in range(special):
        password_chars.append(secrets.choice(amaspecial))
    
    # Fill remaining length of the password
    remaining = length - minnum - special
    for i in range(remaining):
        password_chars.append(secrets.choice(alphabet))
        
    # Shuffle the Password Characters
    random.SystemRandom().shuffle(password_chars)
    
    return ''.join(password_chars)
    

def main():
    parser = argparse.ArgumentParser(
        description="Generate strong Passwords.")
    parser.add_argument("--Length", "-L", type=int, help="Length of Password. Default(24)", default=64)
    parser.add_argument("--Numbers", "-N", type=int, help="Least amount of numbers in the password. Default(3)", default=3)
    parser.add_argument("--Special", "-S", type=int, help="Least amount of special characters in the password. Default(3)", default=3)
    args = parser.parse_args()
    
    L = args.Length
    N = args.Numbers
    S = args.Special
    print("\n")
    print("-"*L)
    print(password_gen(L, N, S))
    print("-"*L)
    print("\n")
    
if __name__ == "__main__":
    main()
    
    
