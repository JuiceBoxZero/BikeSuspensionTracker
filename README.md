# BikeSuspensionTracker
This project lets you track the performance of your bike suspension by logging the G forces.

## Usage
To install this software without having to manually create the file and copy/paste the code, do the following:
This is assuming you have set up your Raspberry Pi with a monitor, internet connection(Ethernet or WIFI), keyboard and mouse connected directly. 

Open a terminal and type the following to make sure your Pi is updated (This could take a few minutes):
```
sudo apt-get update
sudo apt-get upgrade
```
You'll need to make sure you have the Adafruit GPIO Python library installed.
Follow the instructions here to install it:

https://github.com/adafruit/Adafruit_Python_GPIO

Then type the following to download the supporting files (huge thanks to mattdy!):
```
git clone https://github.com/mattdy/python-lis3dh.git
```
Enter the python-lis3dh folder that was just made:
```
cd python-lis3dh
```
Now download the JuiceBox Zero example code:
```
git clone https://github.com/JuiceBoxZero/BikeSuspensionTracker.git
```
This should be all you need to get running. Now test out your accelerometers by running the testLIS3DH.py script by typing:
```
sudo python testLIS3DH.py
```
(press Ctrl-c to kill the program)
This will test the accelerometer that is set to address 0x18 (the default in the code)
See here for more details on how to change the address: 

https://learn.adafruit.com/adafruit-lis3dh-triple-axis-accelerometer-breakout?view=all

Now test out your dual accelerometer setup by running the suspension.py script:
```
sudo python suspension.py
```

Once you verify that both accelerometers are outputting the correct magnitude reading, you can change the 
```degug = True``` to ```debug = False```

Then, to make sure the code runs in the background, you'll create a crontab.
Do this by typing:
```
sudo crontab -e
```
(select a text editor, usually "Nano" is the default option)
At the bottom of the file add the line:
```
@reboot python /home/pi/python-lis3dh/suspension.py &
```
Now save and exit.
Then, reboot your Pi with:
```
sudo reboot -n
```
That's it!
The next time you reboot your Pi, you will automatically start logging data! 
Once you are done with logging your ride connect your Pi HDMI and a keyboard. 
You'll need to stop your datalogging gracefully, but I haven't implemented anything to do that yet..
