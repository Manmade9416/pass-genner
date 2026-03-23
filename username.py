import argparse
import secrets
import string

def generate_username(NoNums):
    """
    Generates a random, readable username.
    Example: "Quantum_Viper423"
    """
    username_chars = []
    if NoNums != True: # If True then skip number selection
        numslen = secrets.choice([3, 4, 5]) # Random choice to have 3, 4 or 5 nums in username
        nums = ''.join(secrets.choice(string.digits) for i in range(numslen))
        username_chars.append(nums)
    
    with open("words.txt", "r", encoding="utf-8") as f:
        text = f.read()
        words = text.split()
        
        if username_chars: # If list has something then 1 or 2 words is fine
            for i in range(secrets.choice([1, 2])):
                username_chars.append(secrets.choice(words))
        else: # If list has nothing then we must have two words
            for i in range(2):
                username_chars.append(secrets.choice(words))
    
    try:
        if int(username_chars[0]): # if first list item is a number then cool
            if len(username_chars) > 2:
                username = f"{username_chars[1]}_{username_chars[2]}{username_chars[0]}"
            else:
                username = f"{username_chars[1]}{username_chars[0]}"
    except ValueError: # catch error if first list item is not a number and make password differently
        username = f"{username_chars[0][0].upper()}{username_chars[1]}_{username_chars[0]}"
    
    return username
    
def main():
    P = argparse.ArgumentParser()
    P.add_argument("--NoNumbers", help="If you want username withou numbers", action="store_true")
    args = P.parse_args()
    
    print(f"Your username is {generate_username(args.NoNumbers)}")

if __name__ == "__main__":
    main()