# Python-Algorithms
A compelte series of various pyhton algorithms categorized from the web.


## Plot class probabilities calculated by the VotingClassifier
Plot the class probabilities of the first sample in a toy dataset predicted by three different classifiers and averaged by the VotingClassifier.

First, three examplary classifiers are initialized (LogisticRegression, GaussianNB, and RandomForestClassifier) and used to initialize a soft-voting VotingClassifier with weights [1, 1, 5], which means that the predicted probabilities of the RandomForestClassifier count 5 times as much as the weights of the other classifiers when the averaged probability is calculated.

To visualize the probability weighting, we fit each classifier on the training set and plot the predicted class probabilities for the first sample in this example dataset.

## Monkey theorem: A simple example
From the runestone academy we implement an algorithm showing the infinite monkey theorem in practice
We test whether or not a random array of characters from the english alphabet is close to a chosen quote.
First we define a function that generates a sequence of random characters from a to b including space. Secondly we create a function for printing the number of elements that are
identical between two strings. Last but not least a main() function runs to indicate whether our program can generate a sequence close to a given string.

>> Example given: "me thinks it is like a wiesel"     (line from Shakespear)
