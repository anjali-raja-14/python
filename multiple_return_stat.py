import statistics
def mean_median_mode(list):
    return statistics.mean(list),statistics.median(list),statistics.mode(list)
print("End of function")
a,b,c=mean_median_mode([1,2,3,4,5])
print(f"Mean: {a}\nMedian: {b}\nMode: {c}")