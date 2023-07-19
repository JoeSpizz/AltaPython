#!/usr/bin/env python3
import shutil
import os


def main():
#allows file to be run from any locaiton in system
os.chdir("/home/student/AltaPython/")
#copy the file specifically referenced
shutil.copy("5g_research/sdn_network.txt", "5g_research/sdn_network.txt.copy")

#copy the directory referenced
shutil.copytree("5g_research/", "5g_research_backup/")

if __name__ == "__main__":
    main()
