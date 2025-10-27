def greet(name):
    return f"Hello, {name}! Welcome to Git and GitHub."
def goodbye(name):
    return f"Goodbye, {name}! Happy coding!"

if __name__ == "__main__":
    user_name = input("What's your name? ")
    message = greet(user_name)
    print(message)
    print("This is my first Git repository!")
    print(goodbye(user_name))