from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.externals import joblib
import pickle
from random import shuffle
from sklearn.metrics import accuracy_score
from sklearn.linear_model import SGDClassifier
tf=TfidfVectorizer(analyzer='word')

def vectorizer(data):
	tfidf_matrix=tf.fit_transform(data)
	pickle.dump(tf,open('trainingmodels/tone/vectorizer.joblib.pkl',"wb"))
	print('vectorizer saved')
	matrix=tfidf_matrix.toarray()
	return matrix


def trainSVClassifier():
	data = []
	data_labels = []
	data1=[]
	'''
	with open("./subobj_data/subjective.txt") as f:
		for i in f: 
			data.append(i) 
			data_labels.append('subj')
 
	with open("./subobj_data/objective.txt") as f:
		for i in f: 
			data.append(i)
			data_labels.append('obj')
'''
	with open("./tone_data/anger/anger") as f:
		j=0
		for i in f:
			j+=1 
			data.append((i,'anger'))
			#data_labels.append('anger')
			if j==6500:
				break
	with open("./tone_data/fear/fear") as f:
		j=0
		for i in f:
			j+=1 
			data.append((i,'fear'))
			#data_labels.append('fear')
			if j==7000:
				break
	with open("./tone_data/love/love") as f:
		j=0
		for i in f:
			j+=1 
			data.append((i,'love'))
			#data_labels.append('love')
			if j==7500:
				break
	with open("./tone_data/sadness/sadness") as f:
		j=0
		for i in f: 
			j+=1
			data.append((i,'sadness'))
			#data_labels.append('sadness')
			if j==7000:
				break
	with open("./tone_data/joy/joy") as f:
		j=0
		for i in f:
			j+=1 
			data.append((i,'joy'))
			#data_labels.append('joy')
			if j==6500:
				break
	with open("./tone_data/surprise/surprise") as f:
		j=0
		for i in f:
			j+=1 
			data.append((i,'surprise'))
			#data_labels.append('surprise')
			if j==7500:
				break
	print(len(data))
	shuffle(data)	
	for entry in data:
		data1.append(entry[0])
		data_labels.append(entry[1])

	matrix=vectorizer(data1)
	X_train=matrix[:31500]
	y_train=data_labels[:31500]
	X_test=matrix[31500:]
	y_test=data_labels[31500:]
	print('Started training	')
	clf_svm=SGDClassifier(loss='modified_huber', penalty='l2',alpha=1e-3,max_iter=50,tol=None,random_state=42)
	clf_svm = clf_svm.fit(X=X_train, y=y_train)
	predict=clf_svm.predict(X_test)
	print(len(predict))
	print(accuracy_score(y_test,predict))
	print("Trained SV classifier")
	pickle.dump(clf_svm,open('tone_model_1/subj_clf.joblib.pkl',"wb"))
trainSVClassifier()

'''anger-1 fear-2 joy-3 surprise-6 5-sadness 4-love
'''