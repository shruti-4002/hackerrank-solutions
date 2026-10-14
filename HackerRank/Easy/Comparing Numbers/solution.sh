# HackerRank Problem: Comparing Numbers
# Link: https://www.hackerrank.com/challenges/bash-tutorials---comparing-numbers/problem
# Difficulty: Easy
# Language: bash

read num1
read num2

if(($num1>$num2))
then
echo "X is greater than Y"
fi

if(($num1<$num2))
then
echo "X is less than Y"
fi

if(($num1==$num2))
then
echo "X is equal to Y"
fi
