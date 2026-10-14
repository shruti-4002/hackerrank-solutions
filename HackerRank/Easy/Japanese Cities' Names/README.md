# Japanese Cities' Names

**Difficulty:** Easy  
**Topics:** N/A  
**HackerRank URL:** [Japanese Cities' Names](https://www.hackerrank.com/challenges/japanese-cities-name/problem)

## Problem Description

Query the names of all the Japanese cities in the **CITY** table. The **COUNTRYCODE** for Japan is `JPN`. **
The CITY** table is described as follows:

![](https://s3.amazonaws.com/hr-challenge-images/8137/1449729804-f21d187d0f-CITY.jpg)

## Examples



## Constraints



## Solution

```db2
// HackerRank Problem: Japanese Cities' Names
// Link: https://www.hackerrank.com/challenges/japanese-cities-name/problem
// Difficulty: Easy
// Language: db2

SELECT NAME
FROM CITY
WHERE COUNTRYCODE='JPN';
```

---
<div align="center">

**🔄 Synced with [CommitSync](https://www.google.com/search?q=CommitSync+extension)**

*Automatically organized and synced by CommitSync.*

</div>
