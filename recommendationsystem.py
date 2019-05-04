#lightfm - library to apply various recommender system

import numpy as np
import scipy as sc
from lightfm.datasets import fetch_movielens
from lightfm import LightFM


#fetch data and format it 

data =fetch_movielens(min_rating=4.0)

print(repr(data['train']))
print(repr(data['test']))


#create model 
#warp is weighted average rank pairwise : uses gradient descent 
model=LightFM(loss="warp")

#train model

model.fit(data['train'],epochs=30,num_threads=2)

def sample_recommendation(model,data,user_id):

	#number of users and movies in training data

	n_users,n_items=data["train"].shape

	for userid in user_id:

		#we are now getting known positives from our data. Lightfm creates >5 rating as positives and 4 or below as -ve to make it binary 

		known_positive=data["item_labels"][data["train"].tocsr()[user_id].indices]

		#movies our model predicts they will like 

		score=model.predict(userid,np.arange(n_items))

		#rank them in order of most liked to least
		topitmes=data["item_labels"][np.argsort(-score)]

		print("User %s"%userid)
		print("Known positives :")
		for i in known_positive[:3]:
			print("%s"%i)

		print("Recommendations :")
		for i in topitmes[:3]:
			print("%s"%i)



sample_recommendation(model,data,[3,43,290])

