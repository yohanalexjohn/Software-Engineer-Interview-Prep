# Missing Range 

Given:
Given a sorted integer array where the range of elements are [0, 99] inclusive, return its missing ranges.
For example, given [0, 1, 3, 50, 75], return [“2”, “4->49”, “51->74”, “76->99”]

```python
def solution(data: list) -> list:
    curr_num = 0
    start_range = 0
    end_range = 0

    result = []
    
    for i in range(len(data)):
        curr_num = data[i] 
        next_num = data[i+1] if (i + 1 < len(data)) else 100 

        if curr_num == next_num:
            continue  

        start_range = curr_num + 1
        end_range = next_num - 1

        if start_range == end_range:
            result.append(f"{start_range}")

        elif start_range != next_num and end_range != curr_num:
            result.append(f"{start_range} -> {end_range}")  

    return result 

print(solution([0, 1, 3, 50, 75]))
```
