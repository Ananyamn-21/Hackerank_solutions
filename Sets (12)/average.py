# Task

# Now, let's use our knowledge of sets and help Mickey.

# Ms. Gabriel Williams is a botany professor at District College.
# One day, she asked her student Mickey to compute the average
# of all the plants with distinct heights in her greenhouse.

def average(array):
    heights = set(array)
    distinct_average = sum(heights) / len(heights)
    return distinct_average


if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)