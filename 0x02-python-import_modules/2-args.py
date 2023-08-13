
if __name__ == "__main__":
    import sys

    args = sys.argv[1:]
    num_args = len(args)

    print("Number of argument(s):", num_args, end=" ")
    if num_args == 0:
        print(".", end="\n\n")
    elif num_args == 1:
        print("argument:", end="\n")
        print("1:", args[0])
    else:
        print("arguments:", end="\n")
        for i, arg in enumerate(args):
            print(i + 1, ":", arg)

