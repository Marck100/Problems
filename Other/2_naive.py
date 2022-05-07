
n = 0
x_array = []
y_array = []

yellow = 0
pink = 0
white = 0


def parse_input(lines):
    global n, x_array, y_array

    n = int(lines[0])

    x_array = [int(x) for x in lines[1].split(" ")]
    y_array = [int(x) for x in lines[2].split(" ")]


def bad_solution():
    help = [[] for _ in range(n)]
    areas = []
    global yellow, pink, white

    for j in range(1, len(x_array) + 1):
        for i in range(1, len(y_array) + 1):
            mod = (i + j) % 3
            area = x_array[j - 1] * y_array[i - 1]
            help[j - 1].append(area)

            if mod == 0:
                yellow += area
            elif mod == 1:
                pink += area
            else:
                white += area

            areas.append(area)



with open("Problem_112/input2_2.txt", "r") as f:
    input = f.readlines()

    parse_input(input)
    
    print(n)
    print(x_array)
    print(y_array)


bad_solution()

print(yellow)
print(pink)
print(white)
