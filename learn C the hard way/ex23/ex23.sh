# !/bin/bash
set -e

echo "loading ..."
./ex23_test_faster_unit 10000 c
./ex23_test_faster_unit 10000 g
./ex23_test_faster_unit 10000 s
echo ""

echo "loading ..."
./ex23_test_faster_unit 100000 c
./ex23_test_faster_unit 100000 g
./ex23_test_faster_unit 100000 s
echo ""

echo "loading ..."
./ex23_test_faster_unit 1000000 c
./ex23_test_faster_unit 1000000 g
./ex23_test_faster_unit 1000000 s
echo ""

echo "loading ..."
./ex23_test_faster_unit 10000000 c
./ex23_test_faster_unit 10000000 g
./ex23_test_faster_unit 10000000 s
echo ""

echo "finished all test"



