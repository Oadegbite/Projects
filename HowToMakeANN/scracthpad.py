#mutiple test changing hiddenNodes
MNIST_30_hidden = NerualNetwork(hiddenNodes=30,inputNodes=784,outputNodes=10,learningRate=0.3)
MNIST_50_hidden = NerualNetwork(hiddenNodes=50,inputNodes=784,outputNodes=10,learningRate=0.3)
MNIST_80_hidden = NerualNetwork(hiddenNodes=80,inputNodes=784,outputNodes=10,learningRate=0.3)
MNIST_150_hidden = NerualNetwork(hiddenNodes=150,inputNodes=784,outputNodes=10,learningRate=0.3)
MNIST_250_hidden = NerualNetwork(hiddenNodes=250,inputNodes=784,outputNodes=10,learningRate=0.3)
MNIST_500_hidden = NerualNetwork(hiddenNodes=500,inputNodes=784,outputNodes=10,learningRate=0.3)
MNIST_1000_hidden = NerualNetwork(hiddenNodes=1000,inputNodes=784,outputNodes=10,learningRate=0.3)

#mutiple test changing learningrate using 100 nodes with known 95% test rate trained @2 epcohes
MNIST_1_learning = NerualNetwork(hiddenNodes=100,inputNodes=784,outputNodes=10,learningRate=0.1)
MNIST_2_learning = NerualNetwork(hiddenNodes=100,inputNodes=784,outputNodes=10,learningRate=0.2)
MNIST_3_learning = NerualNetwork(hiddenNodes=100,inputNodes=784,outputNodes=10,learningRate=0.3)
MNIST_4_learning = NerualNetwork(hiddenNodes=100,inputNodes=784,outputNodes=10,learningRate=0.4)
MNIST_5_learning = NerualNetwork(hiddenNodes=100,inputNodes=784,outputNodes=10,learningRate=0.5)
MNIST_6_learning = NerualNetwork(hiddenNodes=100,inputNodes=784,outputNodes=10,learningRate=0.6)
MNIST_7_learning = NerualNetwork(hiddenNodes=100,inputNodes=784,outputNodes=10,learningRate=0.7)
MNIST_8_learning = NerualNetwork(hiddenNodes=100,inputNodes=784,outputNodes=10,learningRate=0.8)
MNIST_9_learning = NerualNetwork(hiddenNodes=100,inputNodes=784,outputNodes=10,learningRate=0.9)
