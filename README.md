# Robotic-Arm
3rd year semester project made by 3D printing and AI on python.

The stl files are open sorce, we made a coustom AI to read out the color in the frame and evaluate the most common color for 10 sec(can be re-adjusted), 

The data is then sent to the Arduino via a serial connection .
<h1> Computer Visions </h1>

<h5>For this project computer vision is helpfull in the following ways:</h5> <br>

<li>Localization-determine robot location automatically</li>
<li>Navigation</li>
<li>Obstacles avoidance</li>
<li>Assembly (peg-in-hole, welding, painting)</li>
<li>Manipulation (e.g. PUMA robot manipulator)</li>
<li>Human Robot Interaction (HRI): Intelligent robotics to interact with and serve people</li>
<br><br>

The Arduino performs the specific function according to the color (Functions are yet to be coded).<br><br>
The expected functionality of the arm is as follows :

<img src=  "https://user-images.githubusercontent.com/66710785/211758973-24a84a45-ef91-4524-9c28-406a2655b9c7.mp4"  width="200px">  


## Current Drawbacks <br>
The arduino code is just hard coded to pick object from a specific point and drop to a specific point . _No automation involved (As of now)_
<br>
## ToDo:
<li>Add revese kinematics to move to any position and detect the object from anywhere on the frame.</l1>
<li>Improve on the Computer vision code in python</li>
<li>Use pyfirmata istead of pyserial to drive the python code</li>

### PPT Video link :
https://drive.google.com/drive/folders/1pHB9iqaUcThfxiqsn59udMkkbB08ejvl

## Images :
### Orignal image : 
<img src="https://github.com/karanS08/Robotic-Arm/blob/main/assets/1672864126047.jpeg"  width="400px">

### 3d Modeled Images :
<br>
<img src = "https://github.com/karanS08/Robotic-Arm/blob/main/assets/Screenshot%20from%202022-10-16%2013-05-28.png" width="175px" align="left" >
<img src = "https://github.com/karanS08/Robotic-Arm/blob/main/assets/Screenshot%20from%202022-10-16%2013-31-06.png" width="175px"align="left" >
<img src="https://github.com/karanS08/Robotic-Arm/blob/main/assets/Screenshot%20from%202022-10-16%2013-31-23.png" width="175px"align="left" >
<img src="https://github.com/karanS08/Robotic-Arm/blob/main/assets/Screenshot%20from%202022-10-16%2013-31-43.png"width="175px"align="left" >
<img src="https://github.com/karanS08/Robotic-Arm/blob/main/assets/Screenshot%20from%202022-10-16%2013-32-50.png"width="175px"align="left" >


