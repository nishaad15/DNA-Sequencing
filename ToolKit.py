nucleotides=['A','T','G','C']
def check(seq):
    temp=seq.upper()
    for n in temp:
        if n not in nucleotides:
            return "invalid"
    return temp