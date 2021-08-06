import json
import numpy as np
import pickle

__locations=None
__data_columns=None
__model=None

def get_estimated_price(location, size, sqft, bath, balcony):
        try:
                loc_index=__data_columns.index(location.lower())
        except:
                loc_index=-1
        x=np.zeros(len(__data_columns))
        x[0]=size
        x[1]=sqft
        x[2]=bath
        x[3]=balcony
        if loc_index>=0:
                x[loc_index]=1
        return round(__model.predict([x])[0],2)

def get_location_names():
	return __locations

def load_saved_artifacts():
	print("Loading Saved Artifacts----STARTING")
	global __data_columns
	global __locations
	global __model

	with open('./artifacts/columns.json','r') as f:
		__data_columns=json.load(f)['data_columns']
		__locations=__data_columns[4:]

	with open('./artifacts/Bangalore_House_Data_Model.pickle','rb') as fb:
		__model=pickle.load(fb)
	print("Artifacts----LOADED SUCCESSFULLY")

if __name__=='__main__':
	load_saved_artifacts()
	print(get_location_names())
	print(get_estimated_price('1st Block Jayanagar',4,2850.0,4.0,1.0))
