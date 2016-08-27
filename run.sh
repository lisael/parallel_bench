#! /bin/bash

make -s -j 1 &> report.md
./sum.py > summary.md 
