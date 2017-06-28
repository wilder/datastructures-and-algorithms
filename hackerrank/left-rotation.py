def rotate_left(arr, rtimes):
    return arr[rtimes:] + arr[0:rtimes]

n, d = map(int, raw_input().strip().split(' '))
arr = map(int, raw_input().strip().split(' '))

arr = rotate_left(arr, d);

print ' '.join(map(str,arr))
