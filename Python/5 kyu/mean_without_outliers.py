"""
The mean and standard deviation of a sample of data can be thrown off if the
sample contains one or many outlier(s) :


For this reason, it is usually a good idea to check for and remove outliers
before computing the mean or the standard deviation of a sample. To this aim,
your function will receive a list of numbers representing a sample of data.
Your function must remove any outliers and return the mean of the sample,
rounded to two decimal places (round only at the end).

Since there is no objective definition of "outlier" in statistics, your
function will also receive a cutoff, in standard deviation units. So for
example if the cutoff is 3, then any value that is more than 3 standard
deviations above or below the mean must be removed. Notice that, once outlying
values are removed in a first "sweep", other less extreme values may then
"become" outliers, that you'll have to remove as well!

Example :

sample = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 100]
cutoff = 3
clean_mean(sample, cutoff) → 5.5

Note : since we are not computing the sample standard deviation for inferential
purposes, the denominator is n, not n - 1.

# Recursion #Statistics #Algorithms #Data Science
 """
import numpy as np

def clean_mean(sample:list, cutoff:int) -> float:
    while True:
        # Calculate the mean and standard deviation of the current sample
        mean = np.mean(sample)
        std = np.std(sample)

        # Identify outliers based on the cutoff
        outliers = [x for x in sample if abs(x - mean) > cutoff * std]

        # Remove outliers from the sample
        sample = [x for x in sample if x not in outliers]

        # If no more outliers are found, exit the loop
        if not outliers:
            break

    # Calculate the mean of the cleaned sample and round to two decimal places
    cleaned_mean = round(np.mean(sample), 2)

    return cleaned_mean

if __name__ == "__main__":
# Example usage
    sample = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 100]
    cutoff = 3
    result = clean_mean(sample, cutoff)
    print(result)  # Output: 5.5
    assert clean_mean(sample, cutoff) == 5.5
