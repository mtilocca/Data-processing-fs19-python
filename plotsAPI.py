from plotting import plotLive
from plotting import plotRecorded
from DataSet import dataRetrieve



recorded = True # if the data we are plotting is recorded data or not 
Fs19_connection  = False # Simulated data = False, FS19 simulator running = True 

if recorded: 

    latitude = dataRetrieve(11,"float32")
    lat = latitude.retrieve()

    longitude = dataRetrieve(12,"float32")
    longD = longitude.retrieve()

    data = dataRetrieve(0,0)
    dataset = data.completeData()
    plots = plotRecorded(dataset)
   
else: 
    plots = plotLive(Fs19_connection, False)
    plots.show()
     
    


