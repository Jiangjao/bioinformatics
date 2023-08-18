# !/bin/bash

echo "Running unit tests:"

# color the output nicely
GREEN='\033[0;32m'
RED='\033[0;31m'
CYAN='\033[0;36m'
NC='\033[0m'

for i in tests/*_tests
do
	echo $i
	if test -f $i
	then
		echo $i
		if $VALGRIND ./$i 2>> tests/tests.log
		then
			echo $i PASS
        else
			echo "${RED}ERROR in test $i:${NC} here's tests/tests/log" 
			echo "For more info, see tests.log"
			echo "------"
			tail tests/tests.log
			exit 1
        fi
    fi
done

echo ""
