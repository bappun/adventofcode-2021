def part1(input):
    # If 1 is more common, store True
    # Note: we could break out of a loop earlier if sum is > length/2
    result = [x > len(input)/2 for x in [sum(x) for x in zip(*input)]]

    gamma_rate = ''
    epsilon_rate = ''
    for x in result:
        gamma_rate += str(int(x))
        epsilon_rate += str(int(not x))

    return int(gamma_rate, 2) * int(epsilon_rate, 2)


def part2(input):
    pass


# MAIN
with open("input.txt", "r") as f:
    input = []
    while line := f.readline():
        element = [int(x) for x in line.strip()]
        input.append(element)

print(part1(input))
print(part2(input))
