from functions import *
from Main import *
import time, sys
import glob
import os
import subprocess

SECONDS_TO_SLEEP = 60

while(True):
    list_of_files = glob.glob('/home/jake/twitterBot/torch-rnn/cv/*.t7')
    latest_file = max(list_of_files, key=os.path.getctime)
    print latest_file

    commandString = "./sample.sh " + latest_file + " > /home/jake/twitterBot/SAMPLE.txt"
    subprocess.call(commandString, shell=True)


    print("Sleeping for " + str(SECONDS_TO_SLEEP) + " seconds.")


    #Add tweet section



    exit()
    time.sleep(SECONDS_TO_SLEEP)

