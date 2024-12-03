class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        result = []
        n = len(s)

        # Process the string in chunks of 2k characters
        for i in range(0, n, 2 * k):
            # Reverse the first k characters of the current chunk
            result.append(s[i:i+k][::-1])
            # Append the next k characters without reversing (if any)
            result.append(s[i+k:i+2*k])

        # Join the result list into a string and return
        return ''.join(result)
