from sklearn import tree 

#model is decision tree which classifies each data point into one branch 
#height,weight(kg),shoesize
x=[[180,77,9],[150,50,5],[156,52,6],[190,89,10],[170,70,8],[140,40,5],[175,90,8],[166,83,9],[159,45,7]]

y=['male','female','female','male','male','female','male','female','female']

clf=tree.DecisionTreeClassifier()

clf=clf.fit(x,y)

predict=clf.predict([156,67,6])

print(predict)
