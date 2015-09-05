# -*- coding: utf-8 -*-

FILE_FORMAT_STRING = "o{}.mol2"
FILE_NUMBERS       = range(1, 14)

FILE_NAMES         = map(FILE_FORMAT_STRING.format, FILE_NUMBERS)

ATOM_NAME          = "@<TRIPOS>ATOM"
BOND_NAME          = "@<TRIPOS>BOND"

LAMBDAS            = [255, 275, 370, 460, 580, 693, 411,  432, 518, 267, 432, 291, 251]

def get_n(N_C, N_Ar):
    
    n1 = float(N_C - 6) / 4
    n2 = float(N_Ar - 6) / 5

    return  n1                                   if n1 == n2 or N_Ar == N_C else \
            n1 - float(abs(N_Ar - N_C)) / 2 + 1  if n1 % 1 != 0.0    else \
            float(abs(N_Ar - N_C)) / 2

def calc_lamb(d):

    return 120 * d + 100

def get_color(lamb):

    return  "бесцветный"        if lamb < 400 or lamb > 760 else \
            "зеленовато-жёлтый" if lamb < 435 else \
            "жёлтый"            if lamb < 480 else \
            "оранжевый"         if lamb < 490 else \
            "красный"           if lamb < 500 else \
            "пурпурный"         if lamb < 560 else \
            "фиолетовый"        if lamb < 580 else \
            "синий"             if lamb < 595 else \
            "голубой"           if lamb < 730 else \
            "зелёный"           

def main():

    for file_name in FILE_NAMES:

        text = open(file_name).read()

        text_ind_at = text.index(ATOM_NAME)
        text_ind_bo = text.index(BOND_NAME)

        atoms_text  = text[text_ind_at + len(ATOM_NAME) + 1 : text_ind_bo - 1]
        bonds_text  = text[text_ind_bo + len(BOND_NAME) + 1 : -1]

        N_C  = len([1 for at_str in atoms_text.split("\n") if at_str.split()[5][0] == "C"])

        '''N_Ar = 0
        n_ar = 0

        for bo_str in bonds_text.split("\n"):
            
            if bo_str.split()[3] == "ar":
                
                n_ar += 1
                N_Ar += 1 if N_Ar < n_ar else 0

            else:
                n_ar = 0'''

        N_Ar = len([1 for bo_str in bonds_text.split("\n") if bo_str.split()[3] == "ar"])

        n    = get_n(N_C, N_Ar)
        lamb = calc_lamb(n)

        print "N_C: %s, N_Ar: %s, n: %s, lamb: %s, цвет: %s" % (N_C, N_Ar, n, lamb, get_color(lamb))

main()