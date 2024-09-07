def main():
    total = 0
    for i in range(0,1000):
        if i % 3 == 0 or i % 5 == 0:
            print(f"Number: {i}")
            total += i 
    print(f"Sum of mulitples: {total}")


if __name__ == "__main__":
    main()