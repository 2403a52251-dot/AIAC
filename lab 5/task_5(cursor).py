def greet_user(name: str, gender: str) -> str:
    """
    Return a greeting with an appropriate title, supporting gender-neutral.

    Supported genders: male, female, non-binary/nonbinary/nb, other/unspecified.
    """
    g = (gender or "").strip().lower()
    if g == "male":
        title = "Mr."
    elif g == "female":
        title = "Ms."
    elif g in {"non-binary", "nonbinary", "nb"}:
        title = "Mx."
    else:
        title = "Mx."  # default gender-neutral title
    return f"Hello, {title} {name}! Welcome."


def main() -> None:
    name = input("Enter your name: ")
    gender = input("Enter your gender (male/female/non-binary/other): ")
    print(greet_user(name, gender))


if __name__ == "__main__":
    main()


