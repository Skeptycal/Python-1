from sklearn import tree

# [eye color, hair color]
# brown = 0, black = 1, blue = 2, blonde = 3, green = 4
X = [[0, 1], [2, 3], [2, 3], [4, 0], [1, 0]]

Y = ['male', 'female', 'male', 'female', 'male']

clf = tree.DecisionTreeClassifier()

clf = clf.fit(X,Y)
prediction = clf.predict([[0, 1]])
print prediction
