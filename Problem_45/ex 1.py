
max_x = 0
max_y = 0

number_of_monuments = 0
# Dizionario avente per chiave la posizione x dei monumenti e per valore un array contenente le y
monuments_scheme = {}

starting_y = 0


def parse_input(input):
   
    lines = input

    size = lines[0].split(" ")
    global max_x, max_y, number_of_monuments, monuments_scheme

  
    max_x = int(size[0])
    max_y = int(size[1])

    number_of_monuments = int(lines[1])

    monument_lines = input[2:]

    for coordinate_literal in monument_lines:
        split = coordinate_literal.split(" ")
        x = int(split[0])
        y = int(split[1])

        if x in monuments_scheme.keys():
            monuments_scheme[x].append(y)
        else:
            monuments_scheme[x] = [y]
        


# Media delle mediane
# La strada migliore da prendere deve essere la più vicina possibile a tutti i monumenti, evitando di trovarsi molto vicina ad alcuni
# e molto lontana da altri

def calc_starting_point(monuments):
    sum = 0
    count = 0
    # Per ogni posizione x lungo la quale(verticalmente) si distribuiscono i monumenti, vado a calcolare la mediana
    for key in monuments:
        y_array = sorted(monuments[key])
        mean = y_array[len(y_array)//2]
        
        sum += mean
        count += 1

    # Restituisco la media delle mediane calcolate
    return (sum//count)


def calc_path(starting_point, monuments):

    global max_x

    path = 0

    for x in monuments:
       
        element = monuments[x]
        min_y = min(element)
        max_y = max(element)

        # Calcolo in primis lo spazio verticale percorso per visitare i monumenti.
        # Lo si moltiplica per 2 dal momento che deve andare e tornare alla strada maestra.

        # I monumenti si trovano sia sopra che sotto la nostra strada(prende la distanza tra il monumento più in alto e quello più in basso)
        if starting_point >= min_y and starting_point <= max_y:
            path +=  (max_y - min_y) * 2
        # I monumenti si trovano sopra la nostra strada(prende la distanza tra la il monunento più in alto e la nostra strada)
        elif min_y > starting_point:
            path += (max_y - starting_point) * 2
        # I monumenti si trovano sotto la nostra strada(prende la distanza tra il monumento più in basso e la nostra strada)
        elif max_y < starting_point:
            path += (starting_point - min_y) * 2

    # Aggiungiamo lo spazio percorso orizzontalmente(la lunghezza orizzontale della strada stessa)
    # max_x è il numero di nodi della griglia, la lunghezza totale sarà, quindi, più piccola di 1  ------> .___.___.___. -> 4 nodi, ma 3 segmenti
    path += max_x - 1

    return path



with open("Problem_45/input1_2.txt", "r") as f:
    input = f.readlines()

    parse_input(input)

    starting_y = calc_starting_point(monuments_scheme)

    path = calc_path(starting_y, monuments_scheme)

    print(path)

