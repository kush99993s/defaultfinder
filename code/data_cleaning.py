import pandas as pd
from data_collection import DataCollection
import json


class Cleaning(object):
	def __init__(self, number_file_read =2):
		data  = DataCollection()
		
		dict_ = data.read_file(number_file_read)
		
		self.df = self.convert_to_data_frame(dict_)
		
		self.country_code_dict = {}
		self.town_dict={}
		self.sector_dict={}
		self.theme_dict={}
		self.geo_level_dict={}
		self.activity_dict={}
		self.repayment_interval_dict = {}
		self.status_dic={}
		
		self.fill_dictionarys()
		self.change_all_variable()
		

	def convert_to_data_frame(self, dictionary_):
		df = pd.DataFrame(dictionary_)
		return df

	def fill_dictionarys(self):
		for i, j in enumerate(self.df.country_code.unique()):
			self.country_code_dict[j] = i

		for i, j in enumerate(self.df.town.unique()):
			self.town_dict[j] = i

		for i, j in enumerate(self.df.sector.unique()):
			self.sector_dict[j] = i

		for i, j in enumerate(self.df.theme.unique()):
			self.theme_dict[j] = i

		for i, j in enumerate(self.df.geo_level.unique()):
			self.geo_level_dict[j] = i

		for i, j in enumerate(self.df.activity.unique()):
			self.activity_dict[j] = i

		for i, j in enumerate(self.df.repayment_interval.unique()):
			self.repayment_interval_dict[j] = i 

		for i, j in enumerate(self.df.status.unique()):
			self.status_dic[j] = i

	def change_all_variable(self):
		self.change_gender()
		self.change_picture()
		self.replace_values()
		self.delete_columns()
		self.change_text()
		
	
	
		

	def replace_values(self):
		self.df.country_code = self.df.country_code.apply(lambda x : self.change_country_code(x))
		self.df.town = self.df.town.apply(lambda x : self.change_town(x))
		self.df.sector = self.df.sector.apply(lambda x : self.change_sector(x))
		self.df.theme = self.df.theme.apply(lambda x : self.change_theme(x))
		self.df.geo_level = self.df.geo_level.apply(lambda x : self.change_geo_level(x))
		self.df.activity = self.df.activity.apply(lambda x : self.chage_activity(x))
		self.df.repayment_interval = self.df.repayment_interval.apply(lambda x: self.change_repayment_interval(x))
		self.df.status = self.df.status.apply(lambda x : self.change_status(x))
		self.df.basket_amount = self.df.basket_amount.fillna(-2)
		self.df.repayment_term = self.df.repayment_term.fillna(-2)

	def delete_columns(self):
		del self.df["bulkEntries"]
		del self.df["tags"]
		del self.df["bonus_credit_eligibility"]
		del self.df["use"]
		del self.df["video"]
		del self.df["gender"]

	def text_change(self,x):
		try:
			return x.encode("ascii", "ignore").replace("<i>", " ").replace("</i>", " ").replace("<br>", " ").replace("</br>", " ")
		except:
			None

			
	def change_text(self):
		self.df.description = self.df.description.apply(lambda x: self.text_change(x) )
		
	def find_male(self,x):
	    temp_m = 0
	    for j in range(len(x)):
	        if x[j] == "M":
	            temp_m +=1
	    return temp_m
	
	def find_female(self, x):
	    temp_f = 0
	    for j in range(len(x)):
	        if x[j] == "F":
	            temp_f +=1
	    return temp_f
	
	def change_gender(self):
		self.df["num_male"] = self.df.gender.apply(lambda x: self.find_male(x))
		self.df["num_female"] = self.df.gender.apply(lambda x: self.find_female(x))
		self.df["male_ratio"] = self.df.num_male/self.df.num_borrowers
		

	def number_picture(self, x):
		number_picture_ = 0
		for j in range(len(x)):
			if x[j] == True:
				number_picture_ += 1
		return number_picture_

	def change_picture(self):
		self.df["number_of_picture"] = self.df.has_picture.apply(lambda x: self.number_picture(x))
		self.df["ratio_of_picture"] = self.df["number_of_picture"]/self.df.num_borrowers
		del self.df["has_picture"]
   
	def change_country_code(self, x):
	    if x in self.country_code_dict:
	        return self.country_code_dict[x]
	    else:
	        return -2
	
	def change_town(self, x):
		if x in self.town_dict:
			return self.town_dict[x]
		else:
			return -2
	
	def change_sector(self,x ):

	    if x in self.sector_dict:
	        return self.sector_dict[x]
	    else:
	        return -2

	def change_theme(self, x):
	    if x in self.theme_dict:
	        return self.theme_dict[x]
	    else:
	        return -2

	def change_geo_level(self, x):
	    if x in self.geo_level_dict:
	        return self.geo_level_dict[x]
	    else:
	        return -2

	def chage_activity(self, x):
		if x in self.activity_dict:
			return self.activity_dict[x]
		else:
			return -2


	def change_repayment_interval(self, x):
		if x in self.repayment_interval_dict:
			return self.repayment_interval_dict[x]
		else:
			return -2
	
	def change_status(self, x):
		if x in self.status_dic:
			return self.status_dic[x]
		else:
			return -2

class Saving(object):
	def __init__(self, number_file_read =2):
		clean = Cleaning(number_file_read)
		self.df = clean.df
		self.country_code_dict = clean.country_code_dict
		self.town_dict=clean.town_dict
		self.sector_dict=clean.sector_dict
		self.theme_dict=clean.theme_dict
		self.geo_level_dict=clean.geo_level_dict
		self.activity_dict=clean.activity_dict
		self.repayment_interval_dict = clean.repayment_interval_dict
		self.status_dic=clean.status_dic
		self.number_of_files = number_file_read

	def save_files(self):
		self.df.to_csv("/home/patanjalichanakya/Documents/Galvanize/project/data/%s.csv" %self.number_of_files)
		dict_ = {"country_code_dict":self.country_code_dict, "town_dict":self.town_dict, "sector_dict":self.sector_dict, "theme_dict": self.theme_dict, "geo_level_dict":self.geo_level_dict,\
				 "activity_dict":self.activity_dict, "repayment_interval_dict": self.repayment_interval_dict, "status_dic":self.status_dic, "number_of_files":self.number_of_files}
		for file_name, content in dict_.iteritems():
			with open("/home/patanjalichanakya/Documents/Galvanize/project/data/%s_%s.json" %(file_name, self.number_of_files), 'w') as f:
				json.dump(content, f) 		
