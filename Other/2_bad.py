
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



    global white, yellow, pink

    x_helper = [0, 0, 0, 0]
    y_helper = [0, 0, 0, 0]

    white_b_1 = 0
    white_h_1 = 0

    white_b_2 = 0
    white_h_2 = 0

    white_b_3 = 0
    white_h_3 = 0

    yellow_b_1 = 0
    yellow_h_1 = 0

    yellow_b_2 = 0
    yellow_h_2 = 0

    yellow_b_3 = 0
    yellow_h_3 = 0

    pink_b_1 = 0
    pink_h_1 = 0

    pink_b_2 = 0
    pink_h_2 = 0

    pink_b_3 = 0
    pink_h_3 = 0

    for i in range(1, n + 1):
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

        
        mod = i % 3

        if mod == 1:
            white_b_1 += x_array[i - 1]
            white_h_1 += y_array[i - 1]

            yellow_b_1 += x_array[i - 1]
            yellow_h_2 += y_array[i - 1] 

            pink_b_1 += x_array[i - 1]
            pink_h_3 += y_array[i - 1] 
        elif mod == 2:
            white_b_2 += x_array[i - 1]
            white_h_3 += y_array[i - 1]

            yellow_b_2 += x_array[i - 1]
            yellow_h_1 += y_array[i - 1] 

            pink_b_2 += x_array[i - 1]
            pink_h_2 += y_array[i - 1] 
        else:
            white_b_3 += x_array[i - 1]
            white_h_2 += y_array[i - 1]

            yellow_b_3 += x_array[i - 1]
            yellow_h_3 += y_array[i - 1] 

            pink_b_3 += x_array[i - 1]
            pink_h_1 += y_array[i - 1] 


    
    white = white_b_1 * white_h_1 + white_b_2 * white_h_2 + white_b_3 * white_h_3
    yellow = yellow_b_1 * yellow_h_1 + yellow_b_2 * yellow_h_2 + yellow_b_3 * yellow_h_3
    pink = pink_b_1 * pink_h_1 + pink_b_2 * pink_h_2 + pink_b_3 * pink_h_3




with open("Problem_112/input2_2.txt", "r") as f:
    input = f.readlines()

    parse_input(input)
    
    print(n)
    print(x_array)
    print(y_array)


solution()

print(yellow)
print(pink)
print(white)
