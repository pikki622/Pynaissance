import numpy as np


class GradientDescent:
    def __init__(self, learning_rate):
        """
        @param learning_rate: lambda, learning rate.
        """
        self.learning_rate = learning_rate

    def optimize(self, variables):
        """
        @param variables: variables for optimization
        @return opt_vars: optimized variables
        """
        return [self.learning_rate * var for var in variables]


class Momentum:
    def __init__(self, learning_rate):
        """
        @param learning_rate: lamda, learning rate
        """
        self.learning_rate = learning_rate
        self.alpha = 0.9

    def optimize(self, variables):
        """
        @param variables: variables for optimization
        @return opt_vars: optimized variables
        """
        if not hasattr(self, '_Momentum_v'):
            self.var = [0] * len(variables)

        for i in range(len(variables)):
            self.var += [(1 - self.alpha) * variables[i] + self.alpha * self.v[i]]

        return self.learning_rate * np.array(self.var)
