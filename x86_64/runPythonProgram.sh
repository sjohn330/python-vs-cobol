#!/bin/bash
startTime=$SECONDS
echo "Running py_vs_X_assign2.py"
python3  py_vs_X_assign2.py
duration=$((SECONDS-$startTime))

echo "Elapsed Time (Seconds): $duration"