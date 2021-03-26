# Naive Bayes

Naive Bayes is used in classification tasks. It is a probabilistic machine learning algorithm based on the Bayes Theorem.

The name `naive` is used because it assumes that the features are independent of each other. That is changing the value of one feature, does not directly influence or change the value of any of the other features used in the algorithm.

![Explanation Of NB Image](./NaiveBayes.png)

### Pros and Cons of Naive Bayes



Where it is implemented and where it can't



## Joint Probability

When two or more random variables are dependent on each other then the probability of an outcome cannot be calculated directly from the probability formula.

Ex: **Independent event**: Picking red/blue/green/yellow balls from a bag. **With** replacement (If we **put the ball we picked back** in the bag).

Ex: **Dependent event**: Picking red/blue/green/yellow balls from a bag. **Without** replacement (If we **do not put the ball we picked back** in the bag). Or Tossing a coin 2 times. The head/tail that occurs in the second toss does not depend on the head/tail that occurs in the first toss.

## Conditional Probability

Conditional Probability is the likelihood of an event occurring given that something has already taken place.

Ex: Probability of there being a **fire given that we see smoke**. If smoke is there then there may or may not be fire and similarly if we see fire there may or may not be smoke.