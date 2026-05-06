class Solution:
    def isPalindrome(self, s: str) -> bool:
        text_list = []
        for ch in s:
            if ch != " " and ch.isalnum():
                text_list.append(ch.lower())
        
        print(text_list)
        start, end = 0, len(text_list) - 1

        while start < end:
            if text_list[start] != text_list[end]:
                return False
            start += 1
            end -= 1

        return True