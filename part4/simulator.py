file_path = "part4/guest_program.txt"

acc = 0

with open(file_path) as file:
    line = file.readline().strip("\n")
    while line:
        instruction = line.split()

        if instruction[0] == "add":
            print("[Guest] Executing: {}".format(line))
            acc += int(instruction[1])
        elif instruction[0] == "print":
            print("[Guest] Executing: {}".format(line))
            print("Accumulator value: {}".format(acc))
        elif instruction[0] == "scan_disk":
            print(
                "[VMM] Trapped privileged instruction '{}', emulating...".format(line)
            )
        elif instruction[0] == "halt":
            print(
                "[VMM] Trapped privileged instruction '{}'. Halting guest.".format(line)
            )
            break
        else:
            print("Invalid instruction! Program terminated. ")
            break

        line = file.readline().strip("\n")
