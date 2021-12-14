def part1(input):
    previous_number = None
    increased_count = 0
    for number in input:
        if previous_number and number > previous_number:
            increased_count += 1
        previous_number = number
    return increased_count


def part1_alt(input):
    return sum(a < b for a, b in zip(input, input[1:]))


def part2(input):
    input_sum = []
    for i in range(len(input)):
        input_sum.append(sum(input[i:i+3]))
    return part1(input_sum)


def part2_alt(input):
    return sum(a < b for a, b in zip(input, input[3:]))


# MAIN
with open("input.txt", "r") as f:
    input = [int(number) for number in f.readlines()]

print(part1(input))
print(part2(input))
