def solution(data:str) -> str:
    # Reverse the input string 
    # [::-1] start at the end position and slice each value until the first 
    reversed_data = data[::-1]

    start = 0
    end = len(data)

    final_string = []

    while start < end:
        if data[start] == reversed_data[start]:
            final_string.append(data[start])

        start += 1

    return "".join(final_string)

print(solution("caba"))

caba
abac