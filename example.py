import numpy as np
from random import choice
import scipy
import matplotlib.pyplot as plt
class Restaurant:
    def __init__(self, mu, dev):
        self.mu = mu
        self.dev = dev
    def sample(self):
        return np.random.normal(self.mu, self.dev)

def explore_only(candidates, num_days):
    scores = []
    for _ in range(num_days):
        scores.append(choice(candidates).sample())
    return sum(scores)

def exploit_only(candidates, num_days):
    scores = [c.sample() for c in candidates]
    chosen = candidates[np.argmax(scores)]
    for _ in range(num_days - len(candidates)):
        scores.append(chosen.sample())
    return sum(scores)

def ucb1(candidates, num_days):
    scores = []
    history = {idx: [c.sample()] for idx,c in enumerate(candidates)}
    for t in range(len(candidates), num_days):
        mu_plus_ucb = [np.mean(history[idx]) + np.sqrt(2*np.log(t) / len(history[idx])) for idx in range(len(candidates))]
        chosen = candidates[np.argmax(mu_plus_ucb)]
        
        score = chosen.sample()
        scores.append(score)
        history[candidates.index(chosen)].append(score)
    return sum(scores)

def example_normal(a=10):
    mu1, sigma1 = 1, 0.8
    mu2, sigma2 = 2, 0.2

    x = np.linspace(-1, 4, 1000)

    pdf1 = scipy.stats.norm.pdf(x, mu1, sigma1)
    pdf2 = scipy.stats.norm.pdf(x, mu2, sigma2)

    plt.plot(x, pdf1, label='Norm(1, 0.8$^2$)')
    plt.plot(x, pdf2, label='Norm(2, 0.2$^2$)')

    plt.xlabel('X')
    plt.ylabel('Probability Density')
    plt.title('PDF Curves for Normal Distributions')

    plt.legend()

    plt.show()