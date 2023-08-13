import dis

def print_module_names():
    with open("hidden_4.pyc", "rb") as file:
        bytecode = file.read()
        instructions = dis.get_instructions(bytecode)

        names = set()
        for instruction in instructions:
            if instruction.opname == "LOAD_CONST":
                const = instruction.argval
                if isinstance(const, str) and not const.startswith("__"):
                    names.add(const)

        for name in sorted(names):
            print(name)

if __name__ == "__main__":
    print_module_names()
