def part1(input):
    hposition = 0
    depth = 0
    for action in input:
        match action[0]:
            case "forward":
                hposition += action[1]
            case "up":
                depth -= action[1]
            case "down":
                depth += action[1]
    return hposition * depth


def part2(input):
    hposition = 0
    depth = 0
    aim = 0
    for action in input:
        match action[0]:
            case "forward":
                hposition += action[1]
                depth += aim * action[1]
            case "up":
                aim -= action[1]
            case "down":
                aim += action[1]
    return hposition * depth


# MAIN
with open("input.txt", "r") as f:
    input = []
    while line := f.readline():
        action = line.strip().split(' ')
        action[1] = int(action[1])
        input.append(action)

print(part1(input))
print(part2(input))
