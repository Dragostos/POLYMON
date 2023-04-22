def print_stats(level):
    print("level", level)
    print("health:", 68 + ((level - 1) * 2))
    print("defense:", int(40 + ((level - 2) * 1.5)))
    print("\n\n")


if __name__ == "__main__":
    test_level = 1
    while test_level < 21:
        print_stats(test_level)
        test_level += 1
