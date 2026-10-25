# Revising the Select Query I

**Difficulty:** Easy  
**Topics:** N/A  
**HackerRank URL:** [Revising the Select Query I](https://www.hackerrank.com/challenges/revising-the-select-query/problem)

## Problem Description

Query all columns for all American cities in the **CITY** table with populations larger than `100000`. The **CountryCode** for America is `USA`.

The **CITY** table is described as follows:

![CITY.jpg](https://s3.amazonaws.com/hr-challenge-images/8137/1449729804-f21d187d0f-CITY.jpg)

## Examples



## Constraints



## Solution

```db2
// HackerRank Problem: Revising the Select Query I
// Link: https://www.hackerrank.com/challenges/revising-the-select-query/problem
// Difficulty: Easy
// Language: db2


/*
    Enter your query here and follow these instructions:
    1. Please append a semicolon ";" at the end of the query and enter your query in a single line to avoid error.
    2. The AS keyword causes errors, so follow this convention: "Select t.Field From table1 t" instead of "select t.Field From table1 AS t"
    3. Type your code immediately after comment. Don't leave any blank line.
*/

SELECT * FROM CITY 
WHERE COUNTRYCODE='USA' AND POPULATION>100000;

```

---
<div align="center">

**🔄 Synced with [CommitSync](https://www.google.com/search?q=CommitSync+extension)**

*Automatically organized and synced by CommitSync.*

</div>
