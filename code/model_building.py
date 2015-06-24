from data_cleaning import OpenFile
import pandas as pd
import numpy as np
import cPickle 
from sklearn.cross_validation import train_test_split
from sklearn.tree import DecisionTreeRegressor, DecisionTreeClassifier
from sklearn.metrics import recall_score, accuracy_score
from sklearn.metrics import precision_score
from sklearn.metrics import confusion_matrix
from sklearn.svm import SVC
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import AdaBoostRegressor, RandomForestClassifier, GradientBoostingClassifier, GradientBoostingRegressor, RandomForestRegressor
from sklearn.metrics import roc_curve, auc
###########
# from helper import ....
##########

class ModelBuilding():
	def __init__(self):
		open_ = OpenFile()
		self.data_ = open_.openfile()
		del self.data_["description"]
		del self.data_["funded_date"]
		# del self.data_["Unnamed: 0"]
		condition_1 = self.data_["status"] == 0
		condition_2 = self.data_["status"] == 1
		self.data_ = self.data_[condition_1 | condition_2]

		self.X_train, self.X_test, self.y_train, self.y_test = self.split_train_test()
		#########################################################################################################
		'''LIST'''
		#########################################################################################################
		self.classifiers = [ DecisionTreeClassifier(), RandomForestClassifier(), GradientBoostingClassifier()]
		self.proba_list = []
		self.recall_classifier = []
		self.precision_classifier = []
		self.c_matrix_classifier = []
		self.y_predicted_all =[]
		self.fpr_all = []
		self.tpr_all = []
		self.accuracy_score_all = []
		self.auc_all = []

	def split_train_test(self):
		self.y = self.data_.pop("status")
		return train_test_split(self.data_, self.y, test_size=0.3, random_state=0)

 	def ML_classifier(self, est):
		est.fit(self.X_train, self.y_train)
		y_predicted = est.predict(self.X_test)
		proba_ = est.predict_proba(self.X_test)
		return y_predicted, proba_

	def evaluate_model(self, y_predicted):
		recall = recall_score(self.y_test, y_predicted)
		precision = precision_score(self.y_test, y_predicted)
		c_matrix = confusion_matrix(self.y_test, y_predicted)
		accuracy  = accuracy_score(self.y_test, y_predicted)
		return recall, precision, c_matrix, accuracy

	def evaluate_classifier(self):
		for classifier in self.classifiers:
			y_predicted, proba_ = self.ML_classifier(classifier)
			self.proba_list.append(proba_)
			y_predicted = np.round(y_predicted)
			y_predicted = y_predicted.astype(np.int64)
			self.y_predicted_all.append(y_predicted)
			recall, precision, c_matrix, accuracy = self.evaluate_model(y_predicted)
			self.recall_classifier.append(recall)
			self.precision_classifier.append(precision)
			self.c_matrix_classifier.append(c_matrix)
			self.accuracy_score_all.append(accuracy)
			for i, data in enumerate([self.recall_classifier, self.precision_classifier, self.accuracy_score_all]):
				with open("/home/patanjalichanakya/Documents/Galvanize/find_defaulter/data/%s.pickle" %i, 'w') as f:
					cPickle.dump(data, f) 	

	def roc_curve(self):
		for value in self.y_predicted_all:
			fpr, tpr, thresholds = roc_curve(self.y_test, value[:, 1])
			roc_auc = auc(fpr, tpr)
			self.fpr_all.append(fpr)
			self.tpr_all.append(tpr)
			self.auc_all.append(roc_auc)