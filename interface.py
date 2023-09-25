from flask import Flask, render_template, jsonify, request
import config1
from utils import HotalReservation
import traceback

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict_charges', methods = ['GET','POST'])
def predict_charges():
    try:
        if request.method == 'POST':
            data = request.form.get

            # print("User Data is :",data)
            no_of_adults = int(data('no_of_adults'))
            no_of_children = int(data('no_of_children'))
            no_of_weekend_nights= int(data('no_of_weekend_nights'))
            required_car_parking_space= int(data('required_car_parking_space'))
            room_type_reserved= data('room_type_reserved')
            market_segment_type= data('market_segment_type')
            no_of_previous_cancellations= int(data('no_of_previous_cancellations'))
            no_of_special_requests= data('no_of_special_requests')
            type_of_meal_plan_Meal= data('type_of_meal_plan')
            no_of_week_nights=data('no_of_week_nights')
            lead_time=data('lead_time')                            
            arrival_year =data('arrival_year')                  
            arrival_month =data('arrival_month')                        
            arrival_date =data('arrival_date') 
            repeated_guest =data('repeated_guest')
            no_of_previous_bookings_not_canceled=data('no_of_previous_bookings_not_canceled')
            avg_price_per_room=data('avg_price_per_room')
            # booking_status =data('booking_status')  

            Hotal_res = HotalReservation(no_of_adults,no_of_children, no_of_weekend_nights,required_car_parking_space,
            room_type_reserved,market_segment_type,no_of_previous_cancellations,no_of_special_requests,type_of_meal_plan_Meal,
            no_of_week_nights,lead_time,arrival_year ,arrival_month,arrival_date,repeated_guest,
            avg_price_per_room,no_of_previous_bookings_not_canceled)
            pred_res = Hotal_res.get_predicted_res()

            # return  jsonify({"Result" : f"Hotal : {pred_res}"})
            if pred_res == 0:
                return render_template('index.html',prediction = 'Cancelled')
            else:
                return render_template('index.html',prediction = 'Not Cancelled')
            # return  render_template('index.html',prediction = pred_res)


        else:
            data = request.args.get

            # print("User Data is ::::",data)
            no_of_adults = int(data('no_of_adults'))
            no_of_children = int(data('no_of_children'))
            no_of_weekend_nights= int(data('no_of_weekend_nights'))
            required_car_parking_space= int(data('required_car_parking_space'))
            room_type_reserved= data('room_type_reserved')
            market_segment_type= data('market_segment_type')
            no_of_previous_cancellations= int(data('no_of_previous_cancellations'))
            no_of_special_requests= int(data('no_of_special_requests'))
            type_of_meal_plan_Meal= data('type_of_meal_plan')
            no_of_week_nights=int(data('no_of_week_nights'))
            lead_time=data('lead_time')                        
            arrival_year =int(data('arrival_year'))              
            arrival_month =data('arrival_month')                      
            arrival_date =data('arrival_date') 
            repeated_guest =int(data('repeated_guest'))
            avg_price_per_room=data('avg_price_per_room')
            no_of_previous_bookings_not_canceled =data('no_of_previous_bookings_not_canceled')  


            Hotal_res = HotalReservation(no_of_adults,no_of_children, no_of_weekend_nights,required_car_parking_space,
            room_type_reserved,market_segment_type,no_of_previous_cancellations,no_of_special_requests,type_of_meal_plan_Meal,
            no_of_week_nights,lead_time,arrival_year ,arrival_month,arrival_date,repeated_guest,
            avg_price_per_room,no_of_previous_bookings_not_canceled)
            pred_res = Hotal_res.get_predicted_res()

            # return  jsonify({"Result" : f"Hotal Reservation status : {pred_res}"})
            if pred_res == 0:
                return render_template('index.html',prediction = 'Cancelled')
            else:
                return render_template('index.html',prediction = 'Not Cancelled')
            # return  render_template('index.html',prediction = pred_res)
        
            
    except:
        print(traceback.print_exc())
        # return  jsonify({"Message" : "Unsuccessful"})

if __name__ == "__main__":
    app.run(host = "0.0.0.0", port = config1.PORT_NUMBER,debug=False)