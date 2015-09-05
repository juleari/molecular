# -*- coding: utf-8 -*-

FILE_FORMAT_STRING = "o{}.mol2"
FILE_NUMBERS       = range(1, 8)

FILE_NAMES         = map(FILE_FORMAT_STRING.format, FILE_NUMBERS)

SMILES = {
    "O=CO"              : 3.75,     # муравьиная
    "CC(O)=O"           : 4.76,     # уксусная
    "CCC(=O)O"          : 4.88,     # пропионовая
    "CCCCC(O)=O"        : 4.82,     # валериановая
    "C(Cl)C(=O)O"       : 2.87,     # монохлоруксусная
    "ClC(Cl)(Cl)C(O)=O" : 0.77,     # трихлоруксусная
    "C(=O)(C(F)(F)F)O"  : 0.23,     # трифторуксусная
    "CC(O)C(=O)O"       : 3.86,     # молочная
    "C(=O)(C(=O)O)O"    : 1.25      # щавелевая
}

ATOM_NAME          = "@<TRIPOS>ATOM"
BOND_NAME          = "@<TRIPOS>BOND"

VALEN              = {"H": 10, "C": 8, "CL": 0.5, "O": 0.3, "F": 0.1}

def main():

    for file_name in FILE_NAMES:

        text = open(file_name).read()

        text_ind_at = text.index(ATOM_NAME)
        text_ind_bo = text.index(BOND_NAME)

        atoms_text  = text[text_ind_at + len(ATOM_NAME) + 1 : text_ind_bo - 1]
        
        N_C = sum([ float(at_str.split()[8]) * VALEN[at_str.split()[1]] for at_str in atoms_text.split("\n") ])

        print N_C

main()