# 20. Creating a Custom Exception
# Assignment:
# Create a custom exception InvalidAgeError. Write a function check_age(age) that raises this exception if age < 18. Handle it with try...except.


class InvalidAgeError(Exception):
    def __init__(self, age):
        super().__init__(f"Invalid age: {age}. Must be at least 18.")


def check_age(age):
    if age < 18:
        raise InvalidAgeError(age)
    print("Access granted.")


if __name__ == "__main__":
    try:
        user_age = 16
        check_age(user_age)
    except InvalidAgeError as err:
        print(f"Error: {err}")
