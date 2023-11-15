import string
import random
def generate_password(length,use_letters=True,use_symbols=True,use_numbers=True):
    characters=" "
    if use_letters:
        characters+=string.ascii_letters
    if use_symbols:
        characters+=string.punctuation
    if use_numbers:
        characters+=string.digits
        
    if not characters:
        print("Error: You must select at least one character type.")
        return
    
    password="".join(random.choice(characters) for _ in range(length))
    return password

def main():
    print("Command-line Password Generator")
    length=int(input("Enter the password lenght: "))
    use_letters=input("Include letters (y/n): ").lower()=="y"
    use_symbols=input("Include symbols (y/n): ").lower()=="y"
    use_numbers=input("Include numbers (y/n): ").lower()=="y"
    
    password=  generate_password(length,use_letters,use_symbols,use_numbers)
    if password:
        print(f"Generated Password: {password}")


if __name__ == '__main__':
    main()
        