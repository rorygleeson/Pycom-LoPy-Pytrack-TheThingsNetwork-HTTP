This folder contains the code for the Pycom LoPy.
Its uses the PyCom LoPy with the Pytracker board (for the GPS sensor).


Step 1: Ensure your Pycom Firmware Update tool is up to date, upgrade if required.

Step 2: Update the firmware on the PyTracker. The firmware on the Pytrack must be updated via the USB port using the terminal tool, DFU-util.  
        
Step 3: Update the LoPy firmware 

Step 4: Upload the files to the LopY, do not forget to upload the library files, and the pycoproc.py should go in main directory. 

Note: The file is used to configure TTN server HTTP integration, paste this into TTN HTTP payload formats custom decoder window. 
