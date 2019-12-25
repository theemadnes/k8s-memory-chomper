import time
import logging
import sys
import argparse

# set up logging 
out_hdlr = logging.StreamHandler(sys.stdout)
fmt = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
out_hdlr.setFormatter(fmt)
out_hdlr.setLevel(logging.INFO)
logging.getLogger().addHandler(out_hdlr)
logging.getLogger().setLevel(logging.INFO)

# define command line arguments 
parser = argparse.ArgumentParser(description='Chomp (consume) some memory.')
parser.add_argument('--megabytes', '-m', dest='megabytes', type=int, help="How many megabytes should this run chomp?", default='1000')
parser.add_argument('--delay', '-d', dest='delay', type=int, help="How many seconds should the chomping delay after every 100MB?", default='1')

args = parser.parse_args()

logging.info("Chomping %i megabytes with a delay of %i seconds per 100MB..." % (args.megabytes, args.delay)) 

chomp_dict = {}

# memory consumption loop
for i in range(0, args.megabytes):
    
    chomp_dict[i] = bytearray(1024000)

    # log every 100MB
    if not (i+1)%100:

        logging.info("Chomped %i megabytes" % (i+1))
        
        time.sleep(args.delay)

# done chomping, now just log & sleep
while True:

    logging.info("Done chomping %i megabytes... Now sleeping every %is" % (args.megabytes, args.delay))
    
    time.sleep(args.delay)
