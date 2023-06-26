def strStr( haystack: str, needle: str) -> int:
    x = len(haystack)
    y = len(needle)
    for i in range(0, x - y + 1):
        if haystack[i:i + y] == needle:
            return i
    return -1

print("index :",strStr("butsadsad","sad"))