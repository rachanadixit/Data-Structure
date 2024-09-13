from collections import defaultdict

sparse = {
    (1,1): 89,
    (3,1): 90,
    (3,3): 93,
    (3,2): 65
}

no_std = 4
no_sub = 4

def avg_grade_per_sub_and_max_grade(sparse, no_std, no_sub):
    sub_totals = defaultdict(int)
    sub_count = defaultdict(int)
    sub_max = defaultdict(lambda: float('-inf'))

    for (i, j), grade in sparse.items():
        sub_totals[j] += grade
        sub_count[j] += 1
        if grade > sub_max[j]:
            sub_max[j] = grade

    sub_averages = {}
    for j in range(no_sub):
        if sub_count[j] > 0:
            sub_averages[j] = sub_totals[j] / sub_count[j]
        else:
            sub_averages[j] = 0

    return {
        'average': sub_averages,
        'max': dict(sub_max)
    }

# Test the function
result = avg_grade_per_sub_and_max_grade(sparse, no_std, no_sub)
print(result)