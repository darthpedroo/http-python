#!/bin/bash
echo

echo "Running /files/index.html"

curl -i http://localhost:4221/files/index.html
echo
echo "-------------------" 
echo
echo
echo

echo "Running /files/foo"

curl -i http://localhost:4221/files/foo
echo
echo "-------------------"
echo
echo
echo

echo "Running /files/nonexistent"
curl -i http://localhost:4221/files/nonexistent
