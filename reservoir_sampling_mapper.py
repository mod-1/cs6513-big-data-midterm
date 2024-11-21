import sys
import random


def read_input(input):
    for line in input:
        yield line.strip().split('\n')

def main(k):
    reservoir = []
    # input comes from STDIN (standard input)
    lines = read_input(sys.stdin)
    i = 0
    for line in lines:
        for sentence in line:
            if sentence == '':
                continue
            if len(reservoir) < k:
                reservoir.append(sentence)
            else:
                m = random.randint(0, i - 1)
                if m < k:
                    reservoir[m] = sentence
            i += 1
    return reservoir

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python reservoir_sampling_mapper.py <k>")
        sys.exit(1)
    
    k = int(sys.argv[1])
    sampled_list = main(k)
    for sentence in sampled_list:
        print("%s%s%s" % (k, '\t', sentence))