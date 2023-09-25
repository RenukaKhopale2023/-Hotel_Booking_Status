import pickle
import json
import config1
import numpy as np
import pandas as pd

class HotalReservation():

    def __init__(self,no_of_adults,no_of_children, no_of_weekend_nights,required_car_parking_space,
            room_type_reserved,market_segment_type,no_of_previous_cancellations,no_of_special_requests,type_of_meal_plan,no_of_week_nights,lead_time,arrival_year ,arrival_month,arrival_date,repeated_guest,avg_price_per_room,no_of_previous_bookings_not_canceled ) :
       self.no_of_adults = no_of_adults
       self.no_of_children = no_of_children
       self.no_of_weekend_nights= no_of_weekend_nights
       self.required_car_parking_space=required_car_parking_space
       self.room_type_reserved= room_type_reserved
       self.market_segment_type= market_segment_type
       self.no_of_previous_cancellations= no_of_previous_cancellations
       self.no_of_special_requests= no_of_special_requests
       self.type_of_meal_plan= type_of_meal_plan
       self.no_of_week_nights=no_of_week_nights
       self.lead_time=lead_time                  
       self.arrival_year=arrival_year          
       self.arrival_month=arrival_month                    
       self.arrival_date=arrival_date
       self.repeated_guest=repeated_guest
       self.avg_price_per_room=avg_price_per_room
       self.no_of_previous_bookings_not_canceled=no_of_previous_bookings_not_canceled 

    def __load_model(self): # Private Method
        # Load Model File
        with open(r'artifacts\regression_model.pkl', 'rb') as f:
            self.model = pickle.load(f)
            # print('self.model >>',self.model)

        # Load Project Data artifacts/knn_reg_model.pkl
        with open(r'artifacts/project_data.json','r') as f:
            self.project_data = json.load( f)
            # print("Project Data :",self.project_data)

        # Load Normal Scaler File
        with open(r'artifacts\std_scalar.pkl', 'rb') as f:
            self.scaler = pickle.load(f)
            # print('self.scaler >>',self.scaler)

    def get_predicted_res(self): # Public Method
        self.__load_model()
        array = np.zeros((1,self.model.n_features_in_))
        array[0][0] = self.no_of_adults
        array[0][1] = self.no_of_children
        array[0][2] = self.no_of_weekend_nights
        array[0][3] = self.no_of_week_nights
        array[0][4] = self.required_car_parking_space
        array[0][5] = self.project_data['room_type_reserved'][self.room_type_reserved]
        array[0][6] =  self.lead_time
        array[0][7] =  self.arrival_year
        array[0][8] =  self.arrival_month
        array[0][9] =  self.arrival_date
        array[0][10] = self.project_data['market_segment_type'][self.market_segment_type]
        array[0][11] =  self.repeated_guest
        array[0][12] = self.no_of_previous_cancellations
        array[0][13] =  self.no_of_previous_bookings_not_canceled
        array[0][14] =  self.avg_price_per_room
        array[0][15] =  self.no_of_special_requests
        type_of_meal_plan= 'type_of_meal_plan_' + self.type_of_meal_plan
        index = self.project_data['Column Names'].index(type_of_meal_plan)
        array[0][index] = 1


        # print("Test Array is :",array)
        scaled_test_array = self.scaler.fit_transform(array)  
        test_df = pd.DataFrame(scaled_test_array,columns=self.model.feature_names_in_)  

        predicted_res= np.around(self.model.predict(test_df)[0],3)
        # print("Predicted Charges :", predicted_res)
        return predicted_res

if __name__ == '__main__':
    cls = HotalReservation(2,2,2,2,'Room_Type 4','Online',0,0,'Meal Plan 1',2,200,2017,11,28,0,100,0)
    print(cls.get_predicted_res())