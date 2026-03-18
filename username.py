import secrets
import string

def generate_username():
    """
    Generates a random, readable username.
    Example: "Quantum_Viper42"
    """
    username_chars = []
    nums = ''.join(secrets.choice(string.digits) for i in range(3))
    username_chars.append(nums)
    
    with open("words.txt", "r", encoding="utf-8") as f:
        text = f.read()
        words = text.split()
        rng = secrets.choice([1, 2])
        
        for i in range(rng):
            username_chars.append(secrets.choice(words))
        
    if len(username_chars) > 2:
        username = f"{username_chars[1]}_{username_chars[2]}{username_chars[0]}"
    else:
        username = f"{username_chars[1]}{username_chars[0]}"
        
    return username
    
def main():
    print(f"Your username is {generate_username()}")

if __name__ == "__main__":
    main()