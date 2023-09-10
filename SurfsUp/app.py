# Import the dependencies.
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func,inspect
from flask import Flask, jsonify
import pandas as pd
import datetime as dt
import json

#################################################
# Database Setup
#################################################

engine = create_engine("sqlite:///Resources/hawaii.sqlite")

# reflect an existing database into a new model
Base=automap_base()
# reflect the tables
Base.prepare(autoload_with=engine)

# Save references to each table
Measurement=Base.classes.measurement
Station=Base.classes.station

# Create our session (link) from Python to the DB
session=Session(engine)

#################################################
# Flask Setup
#################################################
app = Flask(__name__)



#################################################
# Flask Routes
#################################################
@app.route("/")
def welcome():
    return (
        f"Welcome to the Climate API!<br/>"
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/<start><br/>"
        f"/api/v1.0/<start>/<end><br/>")
engine = create_engine("sqlite:///Resources/hawaii.sqlite")
#Convert query results to a dictionary.
# reflect an existing database into a new model
Base=automap_base()
# reflect the tables
Base.prepare(autoload_with=engine)
Measurement=Base.classes.measurement
Station=Base.classes.station

#Return the JSON representation of the dictionary.
@app.route("/api/v1.0/precipitation")
def precipitation_route():
    """Return the precipitation data as json"""
    # Starting from the most recent data point in the database.
    session=Session(engine) 
# Calculate the date one year from the last date in data set.
    sel=[Measurement.date,Measurement.prcp]
    year_prcp=session.query(*sel).\
        filter((Measurement.date)>=(2016,8,23)).filter((Measurement.date)<=dt.date(2017,8,23)).\
        group_by(Measurement.date).\
        order_by(Measurement.date).all()
# Perform a query to retrieve the data and precipitation scores
    year_prcp
    session.close()

# Save the query results as a Pandas DataFrame. Explicitly set the column names
    precipitation_df=pd.DataFrame(year_prcp,columns=['date','precipitation'])
    prcp_dict={}
    for i,row in precipitation_df.iterrows():
        key=row['date']
        value=row['precipitation']
        prcp_dict[key]=value

    return jsonify(prcp_dict)



@app.route("/api/v1.0/stations")
def station_route():
    """Return the station data as json"""
    # Design a query to calculate the total number of stations in the dataset
    session=Session(engine) 
    station_list=session.query(Station.station).all()
    station_list
    session.close()

    return json.dumps(station_list)


#Return a JSON list of temperature observations for the previous year.
@app.route("/api/v1.0/tobs")
def tobs_route():
    """Return the most active station tobs data as json"""
    #Query the dates and temperature observations of the most active station for the previous year of data.
    session=Session(engine) 
    sel=[Measurement.date,Measurement.tobs]
    year_temps=session.query(*sel).filter(Measurement.station=='USC00519281').\
        filter((Measurement.date)>=(2016,8,23)).filter((Measurement.date)<=dt.date(2017,8,23)).\
        group_by(Measurement.date).\
        order_by(Measurement.date).all()
    session.close()
    station_temp_df=pd.DataFrame(year_temps,columns=['Date','TOBS'])
    station_temp_df['Date']=pd.to_datetime(station_temp_df['Date'])
    station_temp_df = station_temp_df.sort_values(by='Date')
    station_temp_df

    return json.dumps(station_temp_df)

#Return a JSON list of the minimum temperature, the average temperature, and the maximum temperature for a specified start of start-end range.
@app.route("/api/v1.0/<start>")
def tobs_date(start):
    """Fetch the temperature information for a specific date and calculate average, min and max for all stations."""
    
    # Assuming you have imported the 'Measurement' model
#For a specified start, calculate TMIN, TAVG and TMAX for all the dates greater than or equal to the start date.
    session=Session(engine)    
    start_range_data = session.query(func.min(Measurement.tobs), func.max(Measurement.tobs), func.avg(Measurement.tobs)).filter((Measurement.date)>=start).filter((Measurement.date)<=dt.date(2017,8,23)).all()
    if start_range_data:
        min_start_range_temp = start_range_data[0][0]
        max_start_range_temp = start_range_data[0][1]
        average_start_range_temp = start_range_data[0][2]
    session.close()        
        # Return the results as JSON
        return jsonify({
            "start_date": start,
            "end_date":dt.date(2017,8,23),
            "minimum_temperature": min_start_range_temp,
            "maximum_temperature": max_start_range_temp,
            "average_temperature": average_start_range_temp
        })
    else:
        # Handle the case where no data is found for the given date
        return jsonify({"error": "Data not found for the specified date range"}), 404

#For a specified start date and end date, calculate TMIN, TAVG, and TMAX for the dates from the start date to the end date, inclusive.
@app.route("/api/v1.0/<start>/<end>")
def tobs_range_date(start,end):
    session=Session(engine) 
    range_data = session.query(func.min(Measurement.tobs), func.max(Measurement.tobs), func.avg(Measurement.tobs)).filter((Measurement.date)>=start).filter((Measurement.date)<=end).all()
    session.close()  

    if range_data:
        min_range_temp = range_data[0][0]
        max_range_temp = range_data[0][1]
        average_range_temp = range_data[0][2]
        
        # Return the results as JSON
        return jsonify({
            "start_date": start,
            "end_date":end,
            "minimum_temperature": min_range_temp,
            "maximum_temperature": max_range_temp,
            "average_temperature": average_range_temp
        })
    else:
        # Handle the case where no data is found for the given date
        return jsonify({"error": "Data not found for the specified date range"}), 404
    
if __name__ == "__main__":
    app.run(debug=True)