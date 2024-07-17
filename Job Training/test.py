def solution(data: str) -> bool:
    clean_string = [] 

    for char in data.lower():
        if char.isalpha(): 
            clean_string.append("".join(char))
    
    # 2 pointer technique 
    start = 0
    end = len(clean_string) - 1

    print(clean_string)

    if end == 1:
        return True
    
    while start < end:
        if clean_string[start] == clean_string[end]:
            start += 1
            end -= 1
        else:
            return False

    return True

# Example usage
print(solution("A man, a plan, a canal: Panama")) # Output: True
print(solution("race a car")) # Output: False
print(solution("r")) # Output: False

