#!/bin/bash

TOTAL=5000
echo "Mandando $TOTAL requests concurrentes a http://localhost:4221/ ..."

SECONDS=0  # inicializa contador

for i in $(seq 1 $TOTAL); do
    curl -s http://localhost:4221/ &
done

wait

echo "Tiempo total: $SECONDS segundos"
