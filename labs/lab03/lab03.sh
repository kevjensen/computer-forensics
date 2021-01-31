#!/usr/bin/bash

arg2=$2

function square ()
{
local sqr_num=arg2

sqr_result=$(( sqr_num*sqr_num ))
echo $(( sqr_result ))
}

if [ $1 -gt $2 ]; then
echo $1;
else echo $2;
fi

for (( i=1; i<=$1; i++ )) #C++ > Bash
do 
	echo "Bash is great"
done

if [ $(( $(( $2 ))%2 )) = 0 ]; then
square 
fi

array=($(( $1 )) $(( $2 )))
echo ${#array[0]}
echo ${#array[@]}
