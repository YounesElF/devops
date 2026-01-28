#!/bin/bash

echo "=============================="
echo " Ap6 – REST API experiment (curl forms)"
echo " API: httpbin.org"
echo "=============================="
echo

curl -i -X POST https://httpbin.org/post \
  -F "username=younes" \
  -F "password=123456"

echo
echo "=============================="
echo " Ap6 finished"
echo "=============================="

