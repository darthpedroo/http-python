#!/bin/bash

TOTAL=500
echo "Mandando $TOTAL requests concurrentes a http://localhost:4221/ ..."

SECONDS=0

for i in $(seq 1 $TOTAL); do
    curl -s http://localhost:4221/ &
done

wait

echo "Tiempo total: $SECONDS segundos"
