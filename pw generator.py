import secrets
import string

class PasswordGenerator:
    cap = string.ascii_uppercase
    small = string.ascii_lowercase
    digits = string.digits
    symb = string.punctuation

    def __init__(self, include_symbols: bool = True):
        if include_symbols:
            self.combo = self.cap + self.digits + self.small + self.symb
        else:
            self.combo = self.cap + self.digits + self.small

    def generate_password(self, length: int) -> str:
        return ''.join(secrets.choice(self.combo) for _ in range(length))

    def gen(self) -> None:
        while True:
            try:
                pass_len = int(input("Enter the desired length of password: "))
                if pass_len <= 0:
                    print("ERROR: Enter positive length values.")
                    continue

                include_symbols = input("Include symbols in the password? (yes/no): ").lower()
                if include_symbols not in ["yes", "no", "y", "n"]:
                    print("ERROR: Enter 'yes' or 'no'.")
                    continue

                generator = PasswordGenerator(include_symbols in ["yes", "y"])
                password = generator.generate_password(pass_len)
                print("The password is:", password)

                another = input("Do you want another password? (yes/no): ").lower()
                if another not in ["yes", "y"]:
                    break

            except ValueError:
                print("ERROR: Enter appropriate numerical value for the length.")

if __name__ == "__main__":
    PasswordGenerator().gen()