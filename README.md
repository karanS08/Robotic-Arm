# Robotic-Arm
3rd year semester project made by 3D printing and AI on python.

The stl files are open sorce, we made a coustom AI to read out the color in the frame and evaluate the most common color for 10 sec(can be re-adjusted), 

The data is then sent to the Arduino via a serial connection .

The Arduino performs the specific function according to the color (Functions are yet to be coded).

The arduino code is just hard coded to pick object from a specific point and drop to a specific point . _No automation involved_
## ToDo:

Add revese kinematics to move to any position and detect the object from anywhere on the frame .
