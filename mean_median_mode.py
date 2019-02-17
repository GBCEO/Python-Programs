#Program to calculate Mean, Median and Mode of an array of integers

def calc_mean(N,arr):
    return (sum(arr)/N)

def calc_median(N,arr):
    arr.sort()
    if N % 2 == 0:
        return (arr[N//2-1] + arr[N//2])/2
    else:
        return arr[N//2]

def calc_mode(N,arr):
    arr.sort()
    count = {}
    max_val = 0
    mode = None
    for i in arr:
        if i in count.keys():
            count[i] += 1
        else:
            count[i] = 1
        if count[i] > max_val:
            max_val = count[i]
            mode = i
    return mode



if __name__ == "__main__":
    N = int(input())
    arr = [int(x) for x in input().split()]
    print("%0.1f"%calc_mean(N,arr))
    print("%0.1f"%calc_median(N,arr))
    print("%d"%calc_mode(N,arr))

