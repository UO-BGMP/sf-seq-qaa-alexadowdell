#!usr/bin/env python
#22_3H
import argparse

parser = argparse.ArgumentParser(description="Quality Index Swapping")
parser.add_argument("-f", "--filepath", help="File", required=True, type=str)
args = parser.parse_args() #sets arguments as call-able

f = args.filepath

mean_scores = [0.0]*101

def convert_phred(letter):
    n = ord(letter)-33
    return n

i = 0
with open(f, "r") as fh:
    for line in fh:
        line = line.strip("\n")
        i+=1
        if i%4 == 0:
            j = 0
            for char in line:
                score = convert_phred(char)
                mean_scores[j] = mean_scores[j] + score
                j+=1
        if i%5000000: #for debugging on Talapas, print progress
    	    print("On line: ", i, flush = True)
    	    
for i in range(101):
    mean_scores[i] = mean_scores[i]/4050899

with open("22_3H_R1_dist_output.tsv", "w") as output:
    output.write("Base Position" + "\t" + "Mean Q_score" + "\n")
    for i in range(101):
        output.write(str(i) + "\t" + str(mean_scores[i]) + "\n")
