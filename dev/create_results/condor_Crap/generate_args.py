orders = ["NNLO"]  # LO, NLO, NNLO
len_x = 1
len_z = 29
len_function = 20


with open("args.txt", "w") as f:
    for order in orders:
        for x in range(0, len_x):
            for z in range(0, len_z):
                for func in range(0, len_function):
                    f.write(f"{order} {x} {z} {func}\n")
