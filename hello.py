def greet(name):
    return f"Hey {name}! Welcome to the world of Git and GitHub!"
def goodbye(name):
    return f"Goodbye, {name}! Happy coding!"

def calculate_birth_year(age):
    """Calculate approximate birth year from age"""
    from datetime import datetime
    current_year = datetime.now().year
    birth_year = current_year - age
    return birth_year

if __name__ == "__main__":
    user_name = input("What's your name? ")
    message = greet(user_name)
    print(message)
    print("This is my first Git repository!")

        # New age feature
    age = int(input("How old are you? "))
    birth_year = calculate_birth_year(age)
    print(f"You were born around {birth_year}!")
    print(goodbye(user_name))