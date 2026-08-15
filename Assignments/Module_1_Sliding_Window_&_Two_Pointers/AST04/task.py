def pairInSortedRotated(arr, target):
    n = len(arr)

    if n < 2:
        return False

    # Find the pivot: smallest element
    i = 0
    while i < n - 1 and arr[i] <= arr[i + 1]:
        i += 1

    # If no rotation, smallest is index 0
    if i == n - 1:
        low = 0
        high = n - 1
    else:
        low = i + 1
        high = i

    # Circular two-pointer search
    while low != high:
        current_sum = arr[low] + arr[high]

        if current_sum == target:
            return True

        if current_sum < target:
            low = (low + 1) % n
        else:
            high = (high - 1 + n) % n

    return False


if __name__ == '__main__':
    arr = list(map(int, input().split()))
    target = int(input())
    print(pairInSortedRotated(arr, target))