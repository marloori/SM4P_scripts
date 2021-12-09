import numpy as np
import math

def sampling(inlist, size):
    sample = [np.random.choice(inlist, replace=True) for s in range(size)]
    return sample


def correct_sampling(inlist, size):
    sample = []
    for i in range(size):
        x = np.random.uniform()
        index = 0
        if ((x >= 0) and (x < 0.1)):
            index = 0
        elif ((x >= 0.1) and (x < 0.2)):
            index = 1
        elif ((x >= 0.2) and (x < 0.3)):
            index = 2
        elif ((x >= 0.3) and (x < 0.4)):
            index = 3
        elif ((x >= 0.4) and (x < 0.5)):
            index = 4
        elif ((x >= 0.5) and (x < 0.6)):
            index = 5
        elif ((x >= 0.6) and (x < 0.7)):
            index = 6
        elif ((x >= 0.7) and (x < 0.8)):
            index = 7
        elif ((x >= 0.8) and (x < 0.9)):
            index = 8
        elif ((x >= 0.9) and (x < 1)):
            index = 9
        sample.append(inlist[index])
    return sample


def bootstrap(population, nsamples, samplesize):
    bootstrapestimate = 0
    bootstrapsamples = [sampling(population, samplesize) for i in
            range(nsamples)]
    for sample in bootstrapsamples:
        means = []
        meanvalue = np.mean(sample)
        means.append(meanvalue)
        bootstrapestimate = np.mean(means)
    return bootstrapestimate


def correct_bootstrap(population, nsamples, samplesize):
    bootstrapestimate = 0
    bootstrapsamples = [correct_sampling(population, samplesize) for i in
            range(nsamples)]
    for sample in bootstrapsamples:
        means = []
        meanvalue = np.mean(sample)
        means.append(meanvalue)
        bootstrapestimate = np.mean(means)
    return bootstrapestimate


data = [2.3, 4.7, 8.9, 4.4, 0.9, 5.2, 1.2, 7.3, 0.5, 6.0]
bootstrapresult_10 = bootstrap(data, 10, 10)
bootstrapresult_100 = bootstrap(data, 100, 10)
bootstrapresult_1000 = bootstrap(data, 1000, 10)
bootstrapresult_10000 = bootstrap(data, 10000, 10)
bootstrapresult_100000 = bootstrap(data, 100000, 10)
corrbootstrap_10 = correct_bootstrap(data, 10, 10)
corrbootstrap_100 = correct_bootstrap(data, 100, 10)
corrbootstrap_1000 = correct_bootstrap(data, 1000, 10)
corrbootstrap_10000 = correct_bootstrap(data, 10000, 10)
corrbootstrap_100000 = correct_bootstrap(data, 100000, 10)


print("True value: {0}, 10 iterations bootstrap result:\
        {1}, 10 iterations corrected bootstrap result:\
        {2}".format(np.mean(data), bootstrapresult_10, corrbootstrap_10))
print("True value: {0}, 100 iterations bootstrap result:\
        {1}, 100 iterations corrected bootstrap result:\
        {2}".format(np.mean(data), bootstrapresult_100, corrbootstrap_100))
print("True value: {0}, 1000 iterations bootstrap result:\
        {1}, 1000 iterations corrected bootstrap result:\
        {2}".format(np.mean(data), bootstrapresult_1000, corrbootstrap_1000))
print("True value: {0}, 10000 iterations bootstrap result:\
        {1}, 10000 iterations corrected bootstrap result:\
        {2}".format(np.mean(data), bootstrapresult_10000, corrbootstrap_10000))
print("True value: {0}, 100000 iterations bootstrap result:\
        {1}, 100000 iterations corrected bootstrap result:\
        {2}".format(np.mean(data), bootstrapresult_100000, corrbootstrap_100000))
