import random
import numpy as np
import pandas as pd

######################################################################
# Rule for pigs' race
#
# 1. Pink pig:
#       * Adult pig's weight should be in range from 20kg to 150kg.
#       * Taste normal.
# 2. Brown pig:
#       * Adult pig's weight should be in range from 150kg to 250kg.
#       * Taste good.
# 3. Black pig:
#       * Adult pig's weight should be in range from 250kg to 400kg.
#       * Taste delicious.
#
# The most important aspect for pigs' race is weight, then taste.
######################################################################

# Number of data M
M = 20

# k features
k = ['weight', 'taste']

# Weight is normal distributed.
weight_mu = 210
weight_sigma = 75
weight = [random.gauss(mu=weight_mu, sigma=weight_sigma) for i in range(M)]

# Taste is uniform distributed.
taste_type = ['normal', 'good', 'delicious']
taste = [taste_type[round(random.uniform(0.5,3.5))-1] for i in range(M)]

# Race annotation
race = []
for i in range(M):
    if (20 <= weight[i] < 150) and taste[i] == 'normal':
        race.append('pink')
    elif (150 <= weight[i] < 250) and taste[i] == 'good':
        race.append('brown')
    elif (250 <= weight[i] < 400) and taste[i] == 'delicious':
        race.append('black')
    elif weight[i] < 20:
        race.append('pink')
    elif weight[i] >= 400:
        race.append('black')
    elif 20 <= weight[i] < 150:
        race.append('pink')
    elif 150 <= weight[i] < 250:
        race.append('brown')
    elif 250 <= weight[i] < 400:
        race.append('black')

data = pd.DataFrame({'weight': weight, 'taste': taste, 'race': race})
data.to_csv('data/pig.csv', index=False)