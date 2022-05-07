
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

    #random.shuffle(x_array)
    #random.shuffle(y_array)


def solution():

    white = 0
    yellow = 0
    pink = 0

    
    # Contiene la somma delle celle orizzontali o verticali di modulo 0, 1 o 2
    h_sums = [0] * 3
    v_sums = [0] * 3

    for i in range(1, n + 1):
        mod = i % 3
        h_sums[mod] += x_array[i - 1]
        v_sums[mod] += y_array[i -  1]


    
    # White
    # Rettangolo 1 -> base: somma delle celle orizzontali con i % 3 == 1, altezza: somma delle celle verticali con i % 3 == 1
    # Rettangolo 2 -> base: somma delle celle orizzontali con i % 3 == 2, altezza: somma delle celle verticali con i % 3 == 0
    # Rettangolo 3 -> base: somma delle celle orizzontali con i % 3 == 0, altezza: somma delle celle verticali con i % 3 == 2

    # Yellow - Sfasato di 1 rispetto a white
    # Rettangolo 1 -> base: somma delle celle orizzontali con i % 3 == 1, altezza: somma delle celle verticali con i % 3 == 2
    # Rettangolo 2 -> base: somma delle celle orizzontali con i % 3 == 2, altezza: somma delle celle verticali con i % 3 == 1
    # Rettangolo 3 -> base: somma delle celle orizzontali con i % 3 == 0, altezza: somma delle celle verticali con i % 3 == 0

    # Pink - Sfasato di 1 rispetto a white
    # Rettangolo 1 -> base: somma delle celle orizzontali con i % 3 == 1, altezza: somma delle celle verticali con i % 3 == 0
    # Rettangolo 2 -> base: somma delle celle orizzontali con i % 3 == 2, altezza: somma delle celle verticali con i % 3 == 2
    # Rettangolo 3 -> base: somma delle celle orizzontali con i % 3 == 0, altezza: somma delle celle verticali con i % 3 == 1

        
    white = h_sums[1] * v_sums[1] + h_sums[2] * v_sums[0] + h_sums[0] * v_sums[2]     
    yellow = h_sums[1] * v_sums[2] + h_sums[2] * v_sums[1] + h_sums[0] * v_sums[0]     
    pink = h_sums[1] * v_sums[0] + h_sums[2] * v_sums[2] + h_sums[0] * v_sums[1]     

    return (yellow, pink, white)


with open("Problem_112/input2_2.txt", "r") as f:
    input = f.readlines()

    parse_input(input)


print(solution())