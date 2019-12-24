import time
import logging
import sys
import argparse

out_hdlr = logging.StreamHandler(sys.stdout)
fmt = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
out_hdlr.setFormatter(fmt)
out_hdlr.setLevel(logging.INFO)
logging.getLogger().addHandler(out_hdlr)
logging.getLogger().setLevel(logging.INFO)

parser = argparse.ArgumentParser(description='Chomp (consume) some memory.')
parser.add_argument('--megabytes', help="How many megabytes should this run chomp?")

args = parser.parse_args()

# handle unset param and just eat 256Gbytes
if not args.megabytes:
    args.megabytes = 256000

logging.info("Chomping %s megabytes..." % (args.megabytes)) 

chomp_dict = {}

for i in range(0,int(args.megabytes)):
    
    chomp_dict[i] = bytearray(1024000)

    if not (i+1)%100:

        logging.info("Chomped %i megabytes" % (i+1))
        time.sleep(1)

while True:

    logging.info("Done chomping... Now sleeping every 20s")
    time.sleep(20)
