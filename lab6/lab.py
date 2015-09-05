Nuk  = ["Ala", "Arg", "Asn", "Asp", "Cys", "Gln", "Glu", "Gly", "His", "Ile",\
        "Leu", "Lys", "Met", "Phe", "Pro", "Ser", "Thr", "Trp", "Tyr", "Val"
    ]
d    = -5

F= []

S= [[4], 
    [-1,  5],
    [-2,  0,  6],
    [-2, -2,  1,  6],
    [ 0, -3, -3, -3,  9],
    [-1,  1,  0,  0, -3,  5],
    [-1,  0,  0,  2, -4,  2,  5],
    [ 0, -2,  0, -1, -3, -2, -2,  6],
    [-2,  0,  1, -1, -3,  0,  0, -2,  8],
    [-1, -3, -3, -3, -1, -3, -3, -4, -3,  4],
    [-1, -2, -3, -4, -1, -2, -3, -4, -3,  2,  4],
    [-1,  2,  0, -1, -3,  1,  1, -2, -1, -3, -2,  5],
    [-1, -1, -2, -3, -1,  0, -2, -3, -2,  1,  2, -1,  5],
    [-2, -3, -3, -3, -2, -3, -3, -3, -1,  0,  0, -3,  0,  6],
    [-1, -2, -2, -1, -3, -1, -1, -2, -2, -3, -3, -1, -2, -4,  7],
    [ 1, -1,  1,  0, -1,  0,  0,  0, -1, -2, -2,  0, -1, -2, -1,  4],
    [ 0, -1,  0, -1, -1, -1, -1, -2, -2, -1, -1, -1, -1, -2, -1,  1,  5],
    [-3, -3, -4, -4, -2, -2, -3, -2, -2, -3, -2, -3, -1,  1, -4, -3, -2, 11],
    [-2, -2, -2, -3, -2, -1, -2, -3,  2, -1, -1, -2, -1,  3, -3, -2, -2,  2,  7],
    [ 0, -3, -3, -3, -1, -2, -2, -3, -3,  3,  1, -2,  1, -1, -2, -2,  0, -3, -1, 4]]
   #Ala,Arg,Asn,Asp,Cys,Gln,Glu,Gly,His,Ile,Leu,Lys,Met,Phe,Pro,Ser,Thr,Trp,Tyr,Val

def getF(A, B):

    global F

    lA = len(A) + 1
    lB = len(B) + 1

    F    = [ [d * i]*lB for i in range(lA) ]
    F[0] = [  d * i     for i in range(lB) ]

    for i in range(1, lA):
        for j in range(1, lB):

            if A[i - 1] > B[j - 1]: s = S[ A[i - 1] ][ B[j - 1] ]
            else          : s = S[ B[j - 1] ][ A[i - 1] ]
            
            Match   = F[i - 1][j - 1] + s
            Delete  = F[i - 1][j    ] + d
            Insert  = F[i    ][j - 1] + d

            F[i][j] = max(Match, Delete, Insert)

def getAligments(A, B):

    AligA = AligB = ""

    i = len(A)
    j = len(B)

    while i > 0 or j > 0:

        if A[i - 1] > B[j - 1]: s = S[ A[i - 1] ][ B[j - 1] ]
        else          : s = S[ B[j - 1] ][ A[i - 1] ]

        if i >= 0 and j >= 0 and F[i][j] == F[i - 1][j - 1] + s:

            AligA = Nuk[ A[i - 1] ] + AligA
            AligB = Nuk[ B[j - 1] ] + AligB

            i -= 1
            j -= 1

        elif i >= 0 and F[i][j] == F[i - 1][j] + d:

            AligA = Nuk[ A[i - 1] ] + AligA
            AligB = " - "           + AligB

            i -= 1

        else:

            AligA = " - "           + AligA
            AligB = Nuk[ B[j - 1] ] + AligB

            j -= 1

    return (AligA, AligB)

def getArr(text):

    arr = []

    while len(text):

        arr.append( Nuk.index(text[:3]) )
        text = text[3:]

    return arr

def main():

    text1 = raw_input()
    text2 = raw_input()

    arr1  = getArr(text1)
    arr2  = getArr(text2)

    getF(arr1, arr2)

    print "%s\n%s" % getAligments(arr1, arr2)

main()