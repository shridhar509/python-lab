# hello.py
def main():
    names = input("Enter your names (comma-separated): ").split(',')
    for name in names:
        print(f"Hello, {name.strip()}!")

if __name__ == "__main__":
    main()
