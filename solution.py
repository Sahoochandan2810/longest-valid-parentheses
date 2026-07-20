class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack = [-1]
        max_length = 0

        for i, char in enumerate(s):
            if char == '(':
                stack.append(i)
            else:
                stack.pop()

                if not stack:
                    stack.append(i)
                else:
                    current_length = i - stack[-1]
                    max_length = max(max_length, current_length)

        return max_length


if __name__ == "__main__":
    solution = Solution()

    test_cases = [
        ("(()", 2),
        (")()())", 4),
        ("", 0),
        ("()()", 4),
        ("((()))", 6),
        (")(", 0)
    ]

    for test_input, expected_output in test_cases:
        result = solution.longestValidParentheses(test_input)
        print(f"Input: {test_input!r}")
        print(f"Output: {result}")
        print(f"Expected: {expected_output}")
        print("-" * 30)