#!/bin/bash

# CPU
sysbench --time=900 --threads=4 --cpu-max-prime=300000000 cpu run

# Memory
sysbench --time=600 --threads=4 --memory-total-size=40000G --memory-oper=read memory run
sysbench --time=600 --threads=4 --memory-total-size=40000G --memory-oper=write memory run

# Disk
sysbench --file-total-size=32G fileio prepare
sysbench --time=300 --threads=4 --file-test-mode=seqrd --file-total-size=32G fileio run
sysbench --time=300 --threads=4 --file-test-mode=seqwr --file-total-size=32G fileio run
sysbench --time=300 --threads=4 --file-test-mode=rndrd --file-total-size=32G fileio run
sysbench --time=300 --threads=4 --file-test-mode=rndwr --file-total-size=32G fileio run
