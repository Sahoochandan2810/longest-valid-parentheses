# Longest Valid Parentheses

## Problem

Given a string containing only `(` and `)`, find the length of the longest valid (well-formed) parentheses substring.

## Examples

### Example 1

**Input:**

```text
"(()"
```

**Output:**

```text
2
```

**Explanation:** The longest valid parentheses substring is `"()"`.

### Example 2

**Input:**

```text
")()())"
```

**Output:**

```text
4
```

**Explanation:** The longest valid parentheses substring is `"()()"`.

### Example 3

**Input:**

```text
""
```

**Output:**

```text
0
```

## Approach

I use a stack to store the indexes of unmatched parentheses.

The stack starts with `-1`, which acts as a base index for calculating the length of valid parentheses.

* If the current character is `'('`, its index is pushed onto the stack.
* If the current character is `')'`, the top index is removed.
* If the stack becomes empty, the current index is pushed as a new base index.
* Otherwise, the length of the current valid substring is calculated using:

```text
current index - stack top index
```

The maximum length found during the traversal is returned.

## Complexity

* **Time Complexity:** `O(n)`
* **Space Complexity:** `O(n)`

where `n` is the length of the input string.

## Solution

The solution is implemented in Python in (solution.py).
