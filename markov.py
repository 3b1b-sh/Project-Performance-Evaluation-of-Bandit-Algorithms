import numpy as np
import random

class BinaryMarkovBandit:
    def __init__(self, matrix, reward) -> None:
        self.reward = np.zeros(2)
        self.reward[0] = reward[0]
        self.reward[1] = reward[1]
        self.matrix = matrix
        self.state = 0 # current state
    
    # stationary distribution
    def cal_stationary_dist(self):
        return np.array([self.matrix[1, 0] / (self.matrix[1, 0] + self.matrix[0, 1]), self.matrix[0, 1] / (self.matrix[1, 0] + self.matrix[0, 1])])


    # expect value 
    def mu(self):
        ans = 0
        station = self.cal_stationary_dist()
        for i in range(2):
            ans += self.reward[i] * station[i]
        return ans

    # sample
    def sample(self):
        if self.state == 0:
            p_00 = self.matrix[0, 0]
            if random.random() < p_00:
                self.state = 0
            else:
                self.state = 1
        else:
            p_11 = self.matrix[1, 1]
            if random.random() < p_11:
                self.state = 1
            else:
                self.state = 0
        return self.reward[self.state]




