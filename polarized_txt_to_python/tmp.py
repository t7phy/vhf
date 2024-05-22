if __name__ == "__main__":
    # unittest.main()

    with open("polarized/c1pg2qeq.cpp", "r") as file:
        def_line = str()

        for i, line in enumerate(file):
            if i == 0:
                def_line = line
            if i == 1:
                def_line += line
