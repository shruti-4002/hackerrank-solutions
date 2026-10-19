# Valid Palindrome

**Difficulty:** Easy  
**Topics:** Two Pointers, String  
**LeetCode URL:** [Valid Palindrome](https://leetcode.com/problems/valid-palindrome/)

## Problem Description

<p>A phrase is a <strong>palindrome</strong> if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.</p>

<p>Given a string <code>s</code>, return <code>true</code><em> if it is a <strong>palindrome</strong>, or </em><code>false</code><em> otherwise</em>.</p>

<p>&nbsp;</p>

## Examples

<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;A man, a plan, a canal: Panama&quot;
<strong>Output:</strong> true
<strong>Explanation:</strong> &quot;amanaplanacanalpanama&quot; is a palindrome.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;race a car&quot;
<strong>Output:</strong> false
<strong>Explanation:</strong> &quot;raceacar&quot; is not a palindrome.
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> s = &quot; &quot;
<strong>Output:</strong> true
<strong>Explanation:</strong> s is an empty string &quot;&quot; after removing non-alphanumeric characters.
Since an empty string reads the same forward and backward, it is a palindrome.
</pre>

## Constraints

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= s.length &lt;= 2 * 10<sup>5</sup></code></li>
	<li><code>s</code> consists only of printable ASCII characters.</li>
</ul>

## Solution

```python3
# LeetCode Problem: Valid Palindrome
# Link: https://leetcode.com/problems/valid-palindrome/
# Difficulty: Easy
# Language: python3

class Solution:
    def isPalindrome(self, s: str) -> bool:

        start=0;
        s=" ".join(s.split());
        s=s.lower();
        end=len(s)-1;
        while start<end:
            if (s[start]).isalnum()!=True:
                start+=1;
            elif (s[end]).isalnum()!=True:
                end-=1;
            elif s[start]!=s[end]:
                return False;
            else:
                start+=1;
                end-=1;
            
        

        return True;
        
        
```

---
<div align="center">

**🔄 Synced with [CommitSync](https://www.google.com/search?q=CommitSync+extension)**

*Automatically organized and synced by CommitSync.*

</div>
