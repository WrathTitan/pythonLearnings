# Decision Trees

It starts by taking datapoints and splitting according to features/attributes, until we get some boundary, then we further go ahead and try to apply further conditions on the splitted datapoints, and so on. Until we reach the end or the min_split_points condition, i.e. 2 (by default in sklearn.tree.DecisionTreeClassifier)

Finally all the points that fell in a particular category are marked as needed and we finally get our required decision boundary. On the basis of which we can take a new point and pass it through the tree and classify it.

---

## Pros

- Decision trees are easy to interpret and visualize.
- It can easily capture Non-linear patterns.
- It requires fewer data preprocessing from the user, for example, there is no need to normalize columns.
- It can be used for feature engineering such as predicting missing values, suitable for variable selection.
- The decision tree has no assumptions about distribution because of the non-parametric nature of the algorithm.

## Cons

- Sensitive to noisy data. It can overfit noisy data.
- The small variation(or variance) in data can result in the different decision tree. This can be reduced by bagging and boosting algorithms.
- Decision trees are biased with imbalance dataset, so it is recommended that balance out the dataset before creating the decision tree.

---

### Entropy

Measure of impurity in a bunch of examples. It controls how a Decision tree decides where to split the data. Summation Pi log(1/Pi)

Entropy is the measure of uncertainty of a random variable, it characterizes the impurity of an arbitrary collection of examples. The higher the entropy the more the information content.

- The entropy typically changes when we use a node in a decision tree to partition the training instances into smaller subsets. Information gain is a measure of this change in entropy.
- Sklearn supports “entropy” criteria for Information Gain and if we want to use Information Gain method in sklearn then we have to mention it explicitly.

### Information Gain

Information Gain = Entropy(Parent) - [Weighted Average]entropy(children)

Decision Tree algorithm tries to maximise the information gain.

### Gini Index

- Gini Index is a metric to measure how often a randomly chosen element would be incorrectly identified.
- It means an attribute with lower gini index should be preferred.
- Sklearn supports “gini” criteria for Gini Index and by default, it takes “gini” value

---

### How does Decision Tree Work?

The basic idea behind any decision tree algorithm is as follows:

1. Select the best attribute using Attribute Selection Measures(ASM) to split the records.
2. Make that attribute a decision node and break the dataset into smaller subsets.
3. Start tree building by repeating this process recursively for each child until one of the condition will match:
   - All the tuples belong to the same attribute value.
   - There are no more remaining attributes.
   - There are no more instances.

### Attribute Selection Measures

Most popular selection measures are Information Gain, Gain Ratio, and Gini Index.

### Information Gain

Entropy measures the impurity of the input set. Entropy referred as the randomness or the impurity in the system. Information gain is the decrease in entropy. Information gain computes the difference between entropy before split and average entropy after split of the dataset based on given attribute values.

![img](https://res.cloudinary.com/dyd911kmh/image/upload/f_auto,q_auto:best/v1545934190/3_tvqfga.png)

Where, Pi is the probability that an arbitrary tuple in D belongs to class Ci.

![img](https://res.cloudinary.com/dyd911kmh/image/upload/f_auto,q_auto:best/v1545934190/4_vvrzww.png)

![img](https://res.cloudinary.com/dyd911kmh/image/upload/f_auto,q_auto:best/v1545934190/5_trlrj8.png)

Where,

- Info(D) is the average amount of information needed to identify the class label of a tuple in D.
- |Dj|/|D| acts as the weight of the jth partition.
- InfoA(D) is the expected information required to classify a tuple from D based on the partitioning by A.

The attribute A with the highest information gain, Gain(A), is chosen as the splitting attribute at node N().

### Gain Ratio

Information gain is biased for the attribute with many outcomes. It means it prefers the attribute with a large number of distinct values. For instance, consider an attribute with a unique identifier such as customer_ID has zero info(D) because of pure partition. This maximizes the information gain and creates useless partitioning.

![img](https://res.cloudinary.com/dyd911kmh/image/upload/f_auto,q_auto:best/v1545934190/6_zub2e8.png)

Where,

- |Dj|/|D| acts as the weight of the jth partition.
- v is the number of discrete values in attribute A.

The gain ratio can be defined as

![img](https://res.cloudinary.com/dyd911kmh/image/upload/f_auto,q_auto:best/v1545934190/7_xnqpo8.png)

The attribute with the highest gain ratio is chosen as the splitting attribute ([Source](http://www.enggjournals.com/ijcse/doc/IJCSE10-02-09-092.pdf)).

### Gini index

Another decision tree algorithm CART (Classification and Regression Tree) uses the Gini method to create split points.

![img](https://res.cloudinary.com/dyd911kmh/image/upload/f_auto,q_auto:best/v1545934190/8_k4ia8r.png)

Where, pi is the probability that a tuple in D belongs to class Ci.

The Gini Index considers a binary split for each attribute. You can compute a weighted sum of the impurity of each partition. If a binary split on attribute A partitions data D into D1 and D2, the Gini index of D is:

![img](https://res.cloudinary.com/dyd911kmh/image/upload/f_auto,q_auto:best/v1545934191/9_atnmbc.png)

In case of a discrete-valued attribute, the subset that gives the minimum gini index for that chosen is selected as a splitting attribute. In the case of continuous-valued attributes, the strategy is to select each pair of adjacent values as a possible split-point and point with smaller gini index chosen as the splitting point.

![img](https://res.cloudinary.com/dyd911kmh/image/upload/f_auto,q_auto:best/v1545934191/10_oqzzp6.png)

The attribute with minimum Gini index is chosen as the splitting attribute.

---

## Optimizing Decision Tree Performance

- **criterion : optional (default=”gini”) or Choose attribute selection measure**: This parameter allows us to use the different-different attribute selection measure. Supported criteria are “gini” for the Gini index and “entropy” for the information gain.
- **splitter : string, optional (default=”best”) or Split Strategy**: This parameter allows us to choose the split strategy. Supported strategies are “best” to choose the best split and “random” to choose the best random split.
- **max_depth : int or None, optional (default=None) or Maximum Depth of a Tree**: The maximum depth of the tree. If None, then nodes are expanded until all the leaves contain less than min_samples_split samples. The higher value of maximum depth causes overfitting, and a lower value causes underfitting ([Source](https://scikit-learn.org/stable/modules/generated/sklearn.tree.DecisionTreeClassifier.html)).

In Scikit-learn, optimization of decision tree classifier performed by only pre-pruning. Maximum depth of the tree can be used as a control variable for pre-pruning. In the following the example, you can plot a decision tree on the same data with max_depth=3. Other than pre-pruning parameters, You can also try other attribute selection measure such as entropy.