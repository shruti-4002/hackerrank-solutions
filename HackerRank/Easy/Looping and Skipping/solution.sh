# HackerRank Problem: Looping and Skipping
# Link: https://www.hackerrank.com/challenges/bash-tutorials---looping-and-skipping/problem
# Difficulty: Easy
# Language: bash

for((i=1;i<100;i++))
    do
    if((i%2!=0))
       then
     echo $i;
     fi
    
    done
