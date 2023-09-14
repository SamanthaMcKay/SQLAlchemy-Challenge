# SQLAlchemy-Challenge

Used automap to find the classes and save each class to a table.
Explored the columns present in measurement and used that to query the precipitation readings for a year range. 
  Converted the collected data to a dataframe and created a basic plot of the precipitation.

  ![image](https://github.com/SamanthaMcKay/SQLAlchemy-Challenge/assets/132176159/ac5a37c7-635f-4a4e-8f4f-ae3c2e688a67)

Gathered summary statistics for the precipitation data.

  ![image](https://github.com/SamanthaMcKay/SQLAlchemy-Challenge/assets/132176159/8b7af3ce-e8f5-428b-863b-e935c11df6cd)

Found the most active station, filtered the temperature data to show only the most active station data, and found the minimum, maximum and average temperature for that station for a years time. 

Plotted the results of the active station temperature query in a histogram.

![image](https://github.com/SamanthaMcKay/SQLAlchemy-Challenge/assets/132176159/57d6cad9-9d1d-4824-9b15-c5d40127bfe5)

#Flask App

Set out the routes for the welcome page including start route that accepts user input for the start date.

Defined the precipitation app route to show the previously calculated precipitation information in a JSON form.

Defined the station app route to show a jsonified list of stations.

Defined the temperature(tobs) app route to show to temperature data for the most active station in JSON form.

Defined the app route where the user chooses a start date, and the app returns the temperature information (min, max, and avg) from the start date given to the end of the dates in the dataset in JSON form.

Defined the app route where the user chooses a start and end data and the app returns the temperature information (min, max, and avg) from the date range specified in JSON form.

![image](https://github.com/SamanthaMcKay/SQLAlchemy-Challenge/assets/132176159/384dcf53-5364-4ee6-b7a6-17178205e47b)


