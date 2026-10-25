# Revising Aggregations - The Count Function

**Difficulty:** Easy  
**Topics:** N/A  
**HackerRank URL:** [Revising Aggregations - The Count Function](https://www.hackerrank.com/challenges/revising-aggregations-the-count-function/problem)

## Problem Description

Query a *count* of the number of cities in **CITY** having a *Population* larger than .

**Input Format**

The **CITY** table is described as follows:
![](https://s3.amazonaws.com/hr-challenge-images/8137/1449729804-f21d187d0f-CITY.jpg)

## Examples



## Constraints



## Solution

```db2
// HackerRank Problem: Revising Aggregations - The Count Function
// Link: https://www.hackerrank.com/challenges/revising-aggregations-the-count-function/problem
// Difficulty: Easy
// Language: db2


/*
    Enter your query here and follow these instructions:
    1. Please append a semicolon ";" at the end of the query and enter your query in a single line to avoid error.
    2. The AS keyword causes errors, so follow this convention: "Select t.Field From table1 t" instead of "select t.Field From table1 AS t"
    3. Type your code immediately after comment. Don't leave any blank line.
*/

SELECT count(Name) 
FROM CITY
WHERE POPULATION>100000;

```

---
<div align="center">

**🔄 Synced with [CommitSync](https://www.google.com/search?q=CommitSync+extension)**

*Automatically organized and synced by CommitSync.*

</div>
