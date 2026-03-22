import argparse
from errors_passgenner import *
import random
import secrets
import string

def password_gen(length, minnum, special):
    """ Generate Strong Passwords."""
    # Prevent minnum + special >= length
    if length <= 5:
        raise PasswordTooShortError("Password length too short.")
    if minnum + special > length:
        raise RulesExceedPasswordLengthError(
            "Total minimum requirements exceed password length."
            )
    if length > 256:
        raise PasswordTooLongError("Password length is too long.")
    
    # Character pools
    letters = string.ascii_letters
    amanumber = string.digits
    amaspecial = string.punctuation
    alphabet = string.digits + string.ascii_letters + string.punctuation
    
    # Password character storage
    password_chars = []
    
    # Checks to satisfy special characters and numbers requirements
    ## Some nums and some special chars
    if minnum > 0 and special > 0:  
        for i in range(minnum):
            password_chars.append(secrets.choice(amanumber))
        for i in range(special):
            password_chars.append(secrets.choice(amaspecial))

        remaining = length - minnum - special
        for i in range(remaining):
            password_chars.append(secrets.choice(alphabet))

        # Shuffle the Password chars and return password
        random.SystemRandom().shuffle(password_chars)
        return ''.join(password_chars)

    ## Some nums but no special chars
    elif minnum > 0 and special < 1:
        for i in range(minnum):
            password_chars.append(secrets.choice(amanumber))

        remaining = length - minnum
        for i in range(remaining):
            password_chars.append(secrets.choice(amanumber + letters))

        # Shuffle the Password chars and retun password
        random.SystemRandom().shuffle(password_chars)
        return ''.join(password_chars)

    ## Some special chars but no nums
    elif minnum < 1 and special > 0: 
        for i in range(special):
            password_chars.append(secrets.choice(amaspecial))
        
        remaining = length - special
        for i in range(remaining):
            password_chars.append(secrets.choice(amaspecial + letters))

        # Shuffle the Password chars and retun password
        random.SystemRandom().shuffle(password_chars)
        return ''.join(password_chars)

    ## Just letters, no nums and special chars
    elif minnum < 1 and special < 1:
        return ''.join(secrets.choice(letters) for i in range(length))
    

def main():
    """
    Passes the arguments into the password_gen()
    and prints out the password.
    """
    parser = argparse.ArgumentParser(
        description="Generate strong Passwords.")
    parser.add_argument("--Length", "-L", type=int, help="Length of Password. Default(64)", default=64)
    parser.add_argument("--Numbers", "-N", type=int, help="Least amount of numbers in the password. Default(3)", default=3)
    parser.add_argument("--Special", "-S", type=int, help="Least amount of special characters in the password. Default(3)", default=3)
    args = parser.parse_args()
    
    L = args.Length
    N = args.Numbers
    S = args.Special
    
    # Raise errors described in password_gen() if caught
    try:
        passwd = password_gen(L, N, S)
        print(f"> {passwd}")
    except PasswordTooShortError:
        print("Password length too short.")
    except PasswordTooLongError:
        print("Password length is too long.")
    except RulesExceedPasswordLengthError:
        print("Total minimum requirements exceed password length.")

if __name__ == "__main__":
    main()
