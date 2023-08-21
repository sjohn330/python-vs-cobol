#!/bin/bash
startTime=$SECONDS
echo "Running sort.cbl..."
./sort
duration=$((SECONDS-$startTime))

echo "Elapsed Time (Seconds): $duration"

