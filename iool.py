n = 0
length = 0
with open("061 fastq", 'r') as fr:
    for line in fr:
        if n % 4 == 1:
            length += len(
