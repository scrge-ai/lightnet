import numpy as np
import os

"""
def load_layer(path, name):
    #for i in range(len(name_list)):
    layer_config = open("path/" + name + "_config", "r")
    layer_type = layer_config.readline()
    if(layer_type == "dense"):
        weights = np.load("path/" + name + "_weights.npy")
        biases = np.load("path/" + name + "_biases.npy")
"""
class Activation:
    def __init__(self, func, grad):
        self.func = func
        self.grad = grad

class FeedForward:
    def __init__(self):
        pass

    def call(self, inlayer):
        pass

    def backprop(self, memo, a, z): #TODO
        pass

    def apply_grads(self, grads):
        pass

    def save_layer(self):
        pass

"""
class FeedForward: #two completely connected layers; can be thought of as a nn with 0 hidden layers
    def __init__(self, weights, biases, activation): #TODO: add more customization (for flatten layers, etc.)
        self.weights = weights #output layer shape is determined by weights
        self.biases = biases
        self.activation = activation #class activation

    def call(self, inlayer):
        #return self.activation.func(inlayer @ self.weights + self.biases), inlayer @ self.weights + self.biases
        return self.activation.func(np.dot(inlayer, self.weights)+self.biases), np.dot(inlayer, self.weights)+self.biases
"""

class Sequential: #links many FeedForwards into a completely connected ANN
    def __init__(self, varsArr, name="sequential"):
        self.varsArr = varsArr #weights, biases, that kind of stuff
        self.trainableArr = [False for i in range(len(varsArr))]
        self.name = name

    def call(self, inlayer, training=False):
        ret = []
        ret_noactivation = []
        noactivation = np.copy(inlayer)
        for i in range(len(self.varsArr)):
            ret.append(inlayer)
            ret_noactivation.append(noactivation)
            inlayer, noactivation = self.varsArr[i].call(inlayer)
        ret.append(inlayer)
        ret_noactivation.append(noactivation)

        if(not training):
            return inlayer
        else:
            return ret, ret_noactivation

    def save(self):
        path = self.name
        if not os.path.isdir(path):
            os.makedirs(path)
        for i in range(len(self.varsArr)):
            self.varsArr[i].save_layer(path)
            
class Loss: #includes both gradient and loss function
    def __init__(self, loss, grad):
        self.loss = loss
        self.grad = grad #gradient with respect to output layer (output layer as input)

    def getLoss(self, model, x, y): #x = logit, y = label
        return self.loss(model.call(x), y)

    def getGrad(self, y, yhat, i):
        return self.grad(y, yhat, i)

class AutoGrad:
    def __init__(self, loss):
        self.loss = loss #class Loss type (sorry for potential confusion)
    
    def getGrad(self, model):
        pass

class Optimizer:
    def __init__(self, loss, gradcalc, lr=0.1):
        self.loss = loss
        self.gradcalc = gradcalc
        self.lr = lr
    
    def step(self):
        pass

#not using this for now o7
class TrainSession: #optimizer
    def __init__(self, model, loss, autograd):
        self.model = model
        self.loss = loss
        self.autograd = autograd #autograd calculates gradient step for each train step

    def trainStep(self):
        pass
        