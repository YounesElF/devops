#!/bin/bash

echo "=============================="
echo " Ap5 – Eigen REST API experiment (curl)"
echo " API  : Open-Meteo"
echo " City : Brussels"
echo "=============================="
echo

API_URL="https://api.open-meteo.com/v1/forecast"
LAT="50.85"
LON="4.35"

echo "→ Sending HTTP GET request..."
echo

curl -i "${API_URL}?latitude=${LAT}&longitude=${LON}&current_weather=true"

echo
echo "=============================="
echo " End of Ap5 experiment"
echo "=============================="

