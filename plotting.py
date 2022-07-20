import matplotlib.pyplot as plt 
import numpy as np 
from matplotlib.animation import FuncAnimation
import pandas as pd 
import pyproj

class plotRecorded: 

    def __init__(self, dataset): 

        self.dataSet = dataset #np.loadtxt(r"C:\Users\M. Tilocca\Documents\My Games\FarmingSimulator2019\dataToCan.txt", delimiter=",")
        self.time = np.dot(self.dataSet[:, [4]], 0.0167) 
        self.xlabelname = "time [s]"

   
   
    def steerAngles(self, save=False):

        alphaFR = self.dataSet[:, [0]]
        alphaFL = self.dataSet[:, [1]]

        titlename = "Steering Angles"

        self.figSTA = plt.figure(titlename)
        self.figSTA = self.figSTA.gca()
    
        self.figSTA.plot(self.time, alphaFR, color='r',
            label="alphaFR")

        self.figSTA.plot(self.time, alphaFL, color='b',
            label="alphaFL")

        self.figSTA.set_title(titlename)
        self.figSTA.set_xlabel(self.xlabelname)
        self.figSTA.set_ylabel("Steering Angles")
        self.figSTA.legend()
        self.figSTA.grid(True)

        
        if save:
            self.save_fig(self.figSTA, titlename)









    def speed(self, save=False):


        
        x = self.time 
        y = self.dataSet[:, [2]]

        titlename = "Vehicle Speed"
        xaxisname = self.xlabelname
        yname = "velocity"
        yaxisname = "velocity [m/s]"


        self.figSPD = plt.figure(titlename)

        self.figSPD = self.figSPD.gca()
        self.figSPD.plot(x, y, color='r',
            label=yname )

        self.figSPD.set_title(titlename)
        self.figSPD.set_xlabel(xaxisname)
        self.figSPD.set_ylabel(yaxisname)

        self.figSPD.legend()
        self.figSPD.grid(True)

        
        if save:
            self.save_fig(self.figSPD, titlename)

    def CoG(self, cog, save = False):

        x = self.time
        # delete last element 
        x = x[:-1]
        y = cog 

        titlename = "Course Over Ground"
        xaxisname = self.xlabelname
        yname = "CoG"
        yaxisname = "course over ground"


        self.FigCoG = plt.figure(titlename)

        self.FigCoG = self.FigCoG.gca()
        self.FigCoG.plot(x, y, color='r',
            label=yname )

        self.FigCoG.set_title(titlename)
        self.FigCoG.set_xlabel(xaxisname)
        self.FigCoG.set_ylabel(yaxisname)

        self.FigCoG.legend()
        self.FigCoG.grid(True)

        
        if save:
            self.save_fig(self.FigCoG, titlename)

    def traveledD(self, dis, save = False):

        x = self.time
       # delete last element 
        x = x[:-1]
        y = dis
        y = list(y)


        for i in range(len(y)):
            y[i] = y[i-1] + abs(y[i])

        titlename = "Traveled Distance"
        xaxisname = self.xlabelname
        yname = "distance"
        yaxisname = "[m]"


        self.FigCoGD = plt.figure(titlename)

        self.FigCoGD = self.FigCoGD.gca()
        self.FigCoGD.plot(x, y, color='r',
            label=yname )

        self.FigCoGD.set_title(titlename)
        self.FigCoGD.set_xlabel(xaxisname)
        self.FigCoGD.set_ylabel(yaxisname)

        self.FigCoGD.legend()
        self.FigCoGD.grid(True)

        
        if save:
            self.save_fig(self.FigCoGD, titlename)


    def RPM(self, save=False):


        
        x = self.time 
        y = self.dataSet[:, [3]]

        titlename = "Motor RPM"
        xaxisname = self.xlabelname
        yname = "rpm"
        yaxisname = "rpm [rev/min]"


        self.figRPM = plt.figure(titlename)

        self.figRPM = self.figRPM.gca()
        self.figRPM.plot(x, y, color='r',
            label=yname )

        self.figRPM.set_title(titlename)
        self.figRPM.set_xlabel(xaxisname)
        self.figRPM.set_ylabel(yaxisname)

        self.figRPM.legend()
        self.figRPM.grid(True)

        
        if save:
            self.save_fig(self.figRPM, titlename)



    

    def GearRatio(self, save=False):


        
        x = self.time 
        y = self.dataSet[:, [5]]

        titlename = "Gear Ratio"
        xaxisname = self.xlabelname
        yname = "gear ratio"
        yaxisname = "Gear Ratio"


        self.figGR = plt.figure(titlename)

        self.figGR = self.figGR.gca()
        self.figGR.plot(x, y, color='r',
            label=yname )

        self.figGR.set_title(titlename)
        self.figGR.set_xlabel(xaxisname)
        self.figGR.set_ylabel(yaxisname)

        self.figGR.legend()
        self.figGR.grid(True)

        if save:
            self.save_fig(self.figGR, titlename)


    def YPR(self, save=False):


        x = self.time 
        xlabelname = self.xlabelname

        yaw =  self.dataSet[:, [15]]
        pitch =  self.dataSet[:, [14]]
        roll =  self.dataSet[:, [16]]

        titlename = "3D Angle Rates"

        self.fig3DA, (ax1, ax2, ax3) = plt.subplots(3, sharex=True)
        self.fig3DA.suptitle(titlename)

        ax1.plot(x, yaw, label = "yaw [rad/s]")
        ax1.grid(True)

        ax2.plot(x, pitch,label = "pitch [rad/s]")
        ax2.grid(True)

        ax3.plot(x, roll, label = "roll [rad/s]")
        ax3.grid(True)

        ax3.set(xlabel=xlabelname)
        self.fig3DA.text(0.04, 0.5, 'radians', va='center', rotation='vertical')

        if save: 
            self.save_fig(self.fig3DA, titlename)


    
    def wheels(self, save=False):

        omFR = self.dataSet[:, [8]]
        omFL =self.dataSet[:, [7]]

        omRR = self.dataSet[:, [10]]
        omRL = self.dataSet[:, [9]]

        x = self.time
        xlabelname = self.xlabelname

        titlename = "Wheels Angular Velocity"

        self.figWAV = plt.figure(titlename)
        self.figWAV = self.figWAV.gca()

        self.figWAV.plot(x, omFR, color='r',
            label="Omega FR")

        self.figWAV.plot(x, omFL, color='b',
            label="Omega FL")


        self.figWAV.plot(x, omRR, color='m',
            label="Omega RR")


        self.figWAV.plot(x, omRL, color='k',
            label="Omega RL")


    #TODO: find how it can be shared the y-axis label for all the 3 subplots ----- IMPORTANT -----

        self.figWAV.set_title(titlename)
        self.figWAV.set_xlabel(xlabelname)
        self.figWAV.set_ylabel("Angular Velocity [rad/s]")
        self.figWAV.legend()
        self.figWAV.grid(True)

        if save:
            self.save_fig(self.figWAV, titlename)

       
    def WGS84(self, save=False):

        x1 = self.time  # definition of time array which will be used for all 3 subplots 
        x1= np.delete(x1, 0, 0)
       
        y1 = self.dataSet[:, [11]] # latitude 
        y1 = np.delete(y1, 0, 0) 

        y2 = self.dataSet[:, [12]] # longitude 
        y2 = np.delete(y2, 0, 0)

        y3 = self.dataSet[:, [13]] # altitude 
        y3 = np.delete(y3, 0, 0)



        y1 = np.rad2deg(y1) # conversion from rad to deg 
        y2 = np.rad2deg(y2)

        titlename = "WGS84 Positioning"
        self.figWGS, (ax1, ax2, ax3) = plt.subplots(3, sharex=True)
        self.figWGS.suptitle(titlename)

        ax1.plot(x1, y1, label = "latitude")
        ax1.grid(True)
        ax1.legend()
        ax1.set(ylabel= "degrees [deg]")

        ax2.plot(x1, y2,label = "longitude")
        ax2.grid(True)
        ax2.legend()
        ax2.set(ylabel= "degrees [deg]")


        ax3.plot(x1, y3, label = "height")
        ax3.grid(True)
        ax3.legend()
        ax3.set(ylabel= "altitude [m]")


        ax3.set(xlabel="time [s]")

        if save: 
            self.save_fig(self.figWGS, titlename)

        
    
    def show_all(self, cog, dis):  # so first we need to calculate the CoG and Traveled Distance with the other module 

        self.steerAngles()
        self.YPR()
        self.GearRatio()
        self.RPM()
        self.speed()
        self.wheels()
        self.WGS84()
        self.CoG(cog)
        self.traveledD(dis)

        plt.show()


    def show_selected(self):

        plt.show() # to be tested --> create figures singularly and then call this function 

    def save_all(self):

        self.steerAngles(save = True)
        self.GearRatio(save = True)

        self.RPM(save = True)
        self.speed(save = True)
        self.YPR(save = True)

        self.WGS84(save = True)
        self.wheels(save = True)



    def save_fig(fig, title):
        # called internally once the function flag save != False
      fig.savefig(title, format='eps')



'''
Class to plot live data as it is received from the file written by FS19 
'''


class plotLive:

    def __init__(self, Fs19 = True, singular = False):
        
        self.Afr = 0
        self.seconds = 4
        self.Afl = 1

        self.Speed = 2
        self.Rpm = 3 
        self.GearRatio = 6

        self.Ofl = 7 
        self.Ofr = 8 
        self.Orl = 9 
        self.Orr = 10 

        self.latcol = 11
        self.longcol = 12 
        self.hcol = 13

        self.yaw = 15
        self.pitch = 14
        self.roll = 16

        self.Fs19 = Fs19
        self.singular = singular 



    def SteeringAngles(self):
        
        def animate(i):

            if self.Fs19:
                data = pd.read_csv(r'C:\Users\M. Tilocca\Documents\My Games\FarmingSimulator2019\dataToCan.txt', sep =",", header = None, usecols=[self.Afr, self.Afl, self.seconds])
            else: 
                data = pd.read_csv(r'C:\Users\M. Tilocca\Desktop\Work\Vehicle_Simulator\vehicle-simulator\CAN_data_connection\data.csv', sep =",", header = None, usecols=[self.Afr, self.Afl, self.seconds])
                
            time = data[self.seconds]*0.0167
            steerFR = data[self.Afr]
            steerFL = data[self.Afl]

            plt.cla()

            plt.plot(time, steerFR, color ='b', label ="alpha FR")
            plt.scatter(time[-1], steerFR[-1], color = 'b')
            plt.text(time[-1], steerFR[-1]+0.5, "{}".format(np.float16(steerFR[-1])))

            
            plt.plot(time, steerFL, color = 'r', label = "alpha FL")
            plt.scatter(time[-1], steerFL[-1], color = 'r')
            plt.text(time[-1], steerFL[-1]+0.5, "{}".format(np.float16(steerFL[-1])))

            plt.grid(True)
            plt.legend(loc ='upper left')
            plt.title('Front Wheels Steering Angles')
            plt.ylabel('Steering Angle [deg]')
            plt.xlabel('Time [s]')

        fig = plt.figure()
        self.aniST = FuncAnimation(fig, animate, interval = 200)
        if self.singular:
            plt.show()
            




    def Wheels(self):
         

         # C:\Users\M. Tilocca\Desktop\Work\Vehicle Simulator\vehicle-simulator\CAN data connection\data.csv
        def animate(i):

            if self.Fs19:
                data = pd.read_csv(r'C:\Users\M. Tilocca\Documents\My Games\FarmingSimulator2019\dataToCan.txt', sep =",", header = None, usecols=[self.seconds, self.Ofl, self.Ofr, self.Orl, self.Orr])
            else: 
                data = pd.read_csv(r'C:\Users\M. Tilocca\Desktop\Work\Vehicle_Simulator\vehicle-simulator\CAN_data_connection\data.csv', sep =",", header = None, usecols=[self.seconds, self.Ofl, self.Ofr, self.Orl, self.Orr])

            time = data[self.seconds]*0.0167
            Omfl= data[self.Ofl]
            Omfr = data[self.Ofr]
            Omrl = data[self.Orl]
            Omrr = data[self.Orr]

            plt.cla()

            plt.plot(time, Omfl, color ='b', label ="Omega FL")
            plt.scatter(time[-1], Omfl[-1], color ='b')
            plt.text(time[-1], Omfl[-1]+0.5, "{}".format(np.float16(Omfl[-1])))

            plt.plot(time, Omfr, color = 'r', label = "Omega FR")
            plt.scatter(time[-1], Omfr[-1], color ='r')
            plt.text(time[-1], Omfr[-1]+0.5, "{}".format(np.float16(Omfr[-1])))

            plt.plot(time, Omrl, color ='k', label ="Omega RL")
            plt.scatter(time[-1], Omrl[-1], color ='k')
            plt.text(time[-1], Omrl[-1]+0.5, "{}".format(np.float16(Omrl[-1])))

            plt.plot(time, Omrr, color ='m', label ="Omega RR")
            plt.scatter(time[-1], Omrr[-1], color ='m')
            plt.text(time[-1], Omrr[-1]+0.5, "{}".format(np.float16(Omrr[-1])))

            plt.grid(True)
            plt.legend(loc ='upper left')
            plt.title('Wheels Angular velocity')
            plt.ylabel('Angular Velocity [rad/s]')
            plt.xlabel('Time [s]')


        fig = plt.figure()
        self.aniWA = FuncAnimation(fig, animate, interval = 200)
        if self.singular:
            plt.show()
            




    def YPR(self):
       
        def animate(i):

            if self.Fs19:
                data = pd.read_csv(r'C:\Users\M. Tilocca\Documents\My Games\FarmingSimulator2019\dataToCan.txt', sep =",", header = None, usecols=[self.seconds, self.yaw, self.pitch, self.roll])
            else: 
                data = pd.read_csv(r'C:\Users\M. Tilocca\Desktop\Work\Vehicle_Simulator\vehicle-simulator\CAN_data_connection\data.csv', sep =",", header = None, usecols=[self.seconds, self.yaw, self.pitch, self.roll])

            time = data[self.seconds]*0.0167
            yaw= data[self.yaw]
            pitch = data[self.pitch]
            roll = data[self.roll]

            # clear the subplots -- 3 
            ax1.cla()
            ax2.cla()
            ax3.cla()

            ax1.plot(time, yaw, color ='b', label ="yaw [deg]")
            ax1.scatter(time[-1], yaw[-1], color ='b')
            ax1.text(time[-1], yaw[-1]+0.5, "{}".format(np.float16(yaw[-1])))
            ax1.grid(True)
            ax1.legend(loc='upper left')


            ax2.plot(time, pitch, color ='b', label ="longitude [deg]")
            ax2.scatter(time[-1], pitch[-1], color ='b')
            ax2.text(time[-1], pitch[-1]+0.5, "{}".format(np.float16(pitch[-1])))
            ax2.grid(True)
            ax2.legend(loc='upper left')
            ax2.set(ylabel = 'Angle [rad]')


            ax3.plot(time, roll, color ='b', label ="latitude [deg]")
            ax3.scatter(time[-1], roll[-1], color ='b')
            ax3.text(time[-1], roll[-1]+0.5, "{}".format(np.float16(roll[-1])))
            ax3.grid(True)
            ax3.legend(loc='upper left')
            ax3.set(xlabel='Time [s]')


        fig, (ax1, ax2, ax3) = plt.subplots(3, sharex=True)
        fig.suptitle('WGS84 positioning')
        self.Gr = FuncAnimation(fig, animate, interval = 200)
        if self.singular:
            plt.show()



    def WGS(self):

        def animate(i):


            if self.Fs19:
                data = pd.read_csv(r'C:\Users\M. Tilocca\Documents\My Games\FarmingSimulator2019\dataToCan.txt', sep =",", header = None, usecols=[self.seconds, self.latcol, self.longcol, self.hcol])
            else: 
                data = pd.read_csv(r'C:\Users\M. Tilocca\Desktop\Work\Vehicle_Simulator\vehicle-simulator\CAN_data_connection\data.csv', sep =",", header = None, usecols=[self.seconds, self.latcol, self.longcol, self.hcol])

            time = data[self.seconds]*0.0167
            lat= data[self.latcol]
            lon = data[self.longcol]
            h = data[self.hcol]

            # clear the subplots -- 3 
            ax1.cla()
            ax2.cla()
            ax3.cla()

            ax1.plot(time, lat, color ='b', label ="latitude [deg]")
            ax1.scatter(time[-1], lat[-1], color ='b')
            ax1.text(time[-1], lat[-1]+0.5, "{}".format(np.float16(lat[-1])))
            ax1.grid(True)
            ax1.legend(loc='upper left')


            ax2.plot(time, lon, color ='b', label ="longitude [deg]")
            ax2.scatter(time[-1], lon[-1], color ='b')
            ax2.text(time[-1], lon[-1]+0.5, "{}".format(np.float16(lon[-1])))
            ax2.grid(True)
            ax2.legend(loc='upper left')


            ax3.plot(time, lat, color ='b', label ="latitude [deg]")
            ax3.scatter(time[-1], lat[-1], color ='b')
            ax3.text(time[-1], lat[-1]+0.5, "{}".format(np.float16(lat[-1])))
            ax3.grid(True)
            ax3.legend(loc='upper left')
            ax3.set(xlabel='Time [s]')


        fig, (ax1, ax2, ax3) = plt.subplots(3, sharex=True)
        fig.suptitle('WGS84 positioning')
        self.Gr = FuncAnimation(fig, animate, interval = 200)
        if self.singular:
            plt.show()
  


    def gearRatio(self):

        def animate(i):
            
            if self.Fs19:
                data = pd.read_csv(r'C:\Users\M. Tilocca\Documents\My Games\FarmingSimulator2019\dataToCan.txt', sep =",", header = None, usecols=[self.seconds, self.GearRatio])
            else: 
                data = pd.read_csv(r'C:\Users\M. Tilocca\Desktop\Work\Vehicle_Simulator\vehicle-simulator\CAN_data_connection\data.csv', sep =",", header = None, usecols=[self.seconds, self.GearRatio])


            time = data[self.seconds]*0.0167
            Gear= data[self.GearRatio]
            
            plt.cla()

            plt.plot(time, Gear, color ='b', label ="Gear Ratio")
            plt.scatter(time[-1], Gear[-1], color ='b')
            plt.text(time[-1], Gear[-1]+0.5, "{}".format(np.float16(Gear[-1])))

            plt.grid(True)
            plt.legend(loc ='upper left')
            plt.title('Gear Ratio')
            plt.ylabel('Gear Ratio')
            plt.xlabel('Time [s]')


        fig = plt.figure()
        self.Gr = FuncAnimation(fig, animate, interval = 200)
        if self.singular:
            plt.show()



    def speed(self):
       
        def animate(i):
            if self.Fs19:
                data = pd.read_csv(r'C:\Users\M. Tilocca\Documents\My Games\FarmingSimulator2019\dataToCan.txt', sep =",", header = None, usecols=[self.seconds, self.Speed])
            else: 
                data = pd.read_csv(r'C:\Users\M. Tilocca\Desktop\Work\Vehicle_Simulator\vehicle-simulator\CAN_data_connection\data.csv', sep =",", header = None, usecols=[self.seconds, self.Speed])

            time = data[self.seconds]*0.0167
            Speed= data[self.Speed]
            
            plt.cla()

            plt.plot(time, Speed, color ='b', label ="Speed")
            plt.scatter(time[-1], Speed[-1], color ='b')
            plt.text(time[-1], Speed[-1]+0.5, "{}".format(np.float16(Speed[-1])))

            plt.grid(True)
            plt.legend(loc ='upper left')
            plt.title('Speed of the vehicle')
            plt.ylabel('Velocity [m/s]')
            plt.xlabel('Time [s]')
        
        fig = plt.figure()
        self.Sp= FuncAnimation(fig, animate, interval = 200)
        if self.singular:
            plt.show()




    def RPM(self):
        
        def animate(i):
            if self.Fs19:
                data = pd.read_csv(r'C:\Users\M. Tilocca\Documents\My Games\FarmingSimulator2019\dataToCan.txt', sep =",", header = None, usecols=[self.seconds, self.Rpm])
            else:
                data = pd.read_csv(r'C:\Users\M. Tilocca\Desktop\Work\Vehicle_Simulator\vehicle-simulator\CAN_data_connection\data.csv', sep =",", header = None, usecols=[self.seconds, self.Rpm])

            time = data[self.seconds]*0.0167
            RPm= data[self.Rpm]
            RPm = list(RPm)

            print(RPm[len(RPm)-1])
            print(time[len(time)-1])

            plt.cla()

            plt.plot(time, RPm, color ='b', label ="Speed")
            plt.scatter(time[len(time)-1], RPm[len(RPm)-1], color ='b')
            plt.text(time[len(time)-1], RPm[len(RPm)-1]+0.5, "{}".format(np.float16(RPm[len(RPm)-1])))

            plt.grid(True)
            plt.legend(loc ='upper left')
            plt.title('Motor RPM')
            plt.ylabel('rpm [rev/min]')
            plt.xlabel('Time [s]')

        fig = plt.figure()
        self.RpmF = FuncAnimation(fig, animate, interval = 200)
        if self.singular:
            plt.show()


    def CoG_travelD(self):
        
        def calcData(latL, lonL):

            longStart = lonL[0]
            longEnd = lonL[1]

            latStart = latL[0]
            latEnd = latL[1]

            GEOD = pyproj.Geod(ellps='WGS84')

    # inv returns azimuth, back azimuth and distance
            a,_,d = GEOD.inv(longStart, latStart,longEnd,latEnd) # start Longitude, start Latitude, end Longitude, end Latitude
                                               #it calculates , azimuth, back azimuth and distance between the two points 
            a = np.float16(a)
            d = np.float32(d) # as we have 60 fps the movement after each frame is small, thus an higher accuracy is needed. 
        
            return d,a 

        
        def animate(i):

            if self.Fs19:
                data = pd.read_csv(r'C:\Users\M. Tilocca\Documents\My Games\FarmingSimulator2019\dataToCan.txt', sep =",", header = None, usecols=[self.seconds, self.latcol, self.longcol, self.hcol])
            else:
                data = pd.read_csv(r'C:\Users\M. Tilocca\Desktop\Work\Vehicle_Simulator\vehicle-simulator\CAN_data_connection\data.csv', sep =",", header = None, usecols=[self.seconds, self.latcol, self.longcol, self.hcol])

            time = data[self.seconds]*0.0167
            lat= data[self.latcol]
            lon = data[self.longcol]
            
            d,a = calcData([lat[-2], lat[-1]] , [lon[-2], lon[-1]]) # calculate the latest data 

            # clear the subplots -- 3 
            ax1.cla()
            ax2.cla()
            
            ax1.plot(time, a, color ='b', label ="CoG")
            ax1.scatter(time[-1], a[-1], color ='b')
            ax1.text(time[-1], a[-1]+0.5, "{}".format(np.float16(a[-1])))
            ax1.grid(True)
            ax1.legend(loc='upper left')
            ax1.set(ylabel = 'CoG')


            ax2.plot(time, d, color ='b', label ="distance")
            ax2.scatter(time[-1], d[-1], color ='b')
            ax2.text(time[-1], d[-1]+0.5, "{}".format(np.float16(d[-1])))
            ax2.grid(True)
            ax2.legend(loc='upper left')
            ax2.set(ylabel = 'traveled distance [m]')
            ax2.set(xlabel='Time [s]')


        fig, (ax1, ax2) = plt.subplots(2, sharex=True)
        fig.suptitle('CoG & Traveled Distance')
        self.Gr = FuncAnimation(fig, animate, interval = 200)
        if self.singular:
            plt.show()
  




    def show(self):

        self.SteeringAngles()
        self.Wheels()
        self.WGS()
        self.CoG_travelD()
        self.YPR()
        self.speed()
        self.gearRatio()
        self.RPM()

        plt.show()


#TODO : create a script for CAN , send data only, create a script for plot recorded data only, create a script for live data plotting 
#TODO : create a script for creation of live data in csv format to simulate FS19 API 


''' 
The created data structure has 14 columns for N rows. 

each column represents: 

1] alpha front right 
2] alpha front left 

3] vehicle speed (m/s)
4] motor RPM 

5] frame number 
6] gear ratio 

7] alpha axle 
8] omega front left (rad/s)

9] omega front right (rad/s)
10] omega rear left (rad/s)

11] omega rear right (rad/s)
12] latitude (rad)

13] longitude (rad)
14] height (deg)

15] rotX -- pitch
16] rotY -- yaw 

17] rotZ -- roll 
18] traveled distance 

'''