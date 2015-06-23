from data_cleaning import OpenFile
import pandas as pd
import numpy as np
from sklearn.cross_validation import train_test_split
from sklearn.tree import DecisionTreeRegressor, DecisionTreeClassifier
from sklearn.metrics import recall_score
from sklearn.metrics import precision_score
from sklearn.metrics import confusion_matrix
from sklearn.svm import SVC
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import AdaBoostRegressor, RandomForestClassifier, GradientBoostingClassifier, GradientBoostingRegressor, RandomForestRegressor

class ModelBuilding():
	def __init__(self):
		open_ = OpenFile()
		self.data_ = open_.openfile()
		del self.data_["description"]
		del self.data_["funded_date"]
		del self.data_["Unnamed: 0"]
		condition_1 = self.data_["status"] == 0
		condition_2 = self.data_["status"] == 1
		self.data_ = self.data_[condition_1 | condition_2]

	def split_train_test(self):
		self.y = self.data_.pop("status")
		self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(self.data_, self.y, test_size=0.3, random_state=0)

	def build_decision_tree_regressor(self):
		regressor = DecisionTreeRegressor()
		regressor.fit(self.X_train, self.y_train)
		y_predicted = regressor.predict(self.X_test)
		return y_predicted, regressor

	def build_decision_tree_classifier(self):
		regressor = DecisionTreeClassifier()
		regressor.fit(self.X_train, self.y_train)
		y_predicted = regressor.predict(self.X_test)
		return y_predicted, regressor

	def build_AdaBoostRegressor(self):
		regressor = AdaBoostRegressor()
		regressor.fit(self.X_train, self.y_train)
		y_predicted = regressor.predict(self.X_test)
		return y_predicted, regressor

	def build_RandomForestClassifier(self):
		regressor = AdaBoostRegressor()
		regressor.fit(self.X_train, self.y_train)
		y_predicted = regressor.predict(self.X_test)
		return y_predicted, regressor

	def build_GradientBoostingClassifier(self):
		regressor = GradientBoostingClassifier()
		regressor.fit(self.X_train, self.y_train)
		y_predicted = regressor.predict(self.X_test)
		return y_predicted, regressor

	def build_GradientBoostingRegressor(self):
		regressor = GradientBoostingRegressor()
		regressor.fit(self.X_train, self.y_train)
		y_predicted = regressor.predict(self.X_test)
		return y_predicted, regressor

	def build_RandomForestRegressor(self):
		regressor = RandomForestRegressor()
		regressor.fit(self.X_train, self.y_train)
		y_predicted = regressor.predict(self.X_test)
		return y_predicted, regressor

	
	
	def build_svc(self):
		regressor = SVC()
		regressor.fit(self.X_train, self.y_train)
		y_predicted = regressor.predict(self.X_test)
		return y_predicted, regressor

	def build_logistic_regression(self):
		regressor = LogisticRegression()
		regressor.fit(self.X_train, self.y_train)
		y_predicted = regressor.predict(self.X_test)
		return y_predicted, regressor
	


	def evaluate_model(self, y_predicted):
		print "Recall", recall_score(self.y_test, y_predicted)
		print "Precision", precision_score(self.y_test, y_predicted)
		print "DecisionTreeClassifieronfusion matrix", confusion_matrix(self.y_test, y_predicted)

