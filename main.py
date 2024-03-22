from modules.fizzbuzz import fizzbuzz
from colors import red, green, yellow

def display_in_color(elt: str) -> str:
    match elt:
        case "Fizz":
            return red(elt)
        case "Buzz":
            return green(elt)
        case "FizzBuzz":
            return  yellow(elt)
        case _:
            return elt

if __name__ == "__main__":
    print("Kata FizzBuzz")
    for i in range(1, 101):
        print(display_in_color(fizzbuzz(i)), end=", ")
    print()
