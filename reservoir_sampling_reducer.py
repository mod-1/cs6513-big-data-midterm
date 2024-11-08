import sys
import random


def read_mapper_output(input, separator='\t'):
    for line in input:
        yield line.rstrip().split(separator, 1)

def main():
    reservoir = []
    # input comes from STDIN (standard input)
    line = read_mapper_output(sys.stdin)
    for l in line:
        k, sentence = int(l[0]), l[1]
        if len(reservoir) < k:
            reservoir.append(sentence)
        else:
            m = random.randint(0, k)
            if m < k:
                reservoir[m] = sentence
    return reservoir


if __name__ == "__main__":
    sampling = main()
    for sentence in sampling:
        print(sentence)