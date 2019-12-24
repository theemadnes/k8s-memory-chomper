import time
#import sys
import argparse

parser = argparse.ArgumentParser(description='Chomp (consume) some memory.')
parser.add_argument('--megabytes', help="How many megabytes should this run chomp?")

args = parser.parse_args()

# handle unset param and just eat 256Gbytes
if not args.megabytes:
    args.megabytes = 256000

print("Chomping %s megabytes..." % (args.megabytes)) 

chomp_dict = {}

for i in range(0,int(args.megabytes)):
    
    chomp_dict[i] = bytearray(1024000)

    if not (i+1)%100:

        print("Chomped %i megabytes" % (i+1))
        time.sleep(1)

while True:

    print("Done chomping... Now sleeping every 20s")
    time.sleep(20)
