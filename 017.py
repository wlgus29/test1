import sys

def comp1(seq: str) -> str:
    comp = ""
    for s in seq:
        if s == "A":
            comp += "T"
        elif s == "C":
            comp += "G"
        elif s == "G":
            comp += "C"
        elif s == "T":
            comp += "A"
    return comp 


def comp2(seq):
    comp = ""
    return comp

if__name__ == "__main__":
    if len(sys.argv) != 2:
        print(f"#usage: python {sys.argv[0]} [string]"
        sys.exit()
    
    seq = sys.argv[1]  #ATGTTATAG
    c1 = comp1(seq)
    c2 = comp2(seq)
    print(seq)
    print(c1)
    print(c2)





