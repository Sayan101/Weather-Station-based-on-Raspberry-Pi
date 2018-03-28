Use "git clone " to clone the libraries with the URLS given below.

https://github.com/adafruit/Adafruit_Python_BMP.git

https://github.com/adafruit/Adafruit_Python_DHT.git

Change the directory and get inside the respective directories and use 
sudo apt-get install build-essential python-dev
sudo python setup.py install

to use the BMP180 we need to enable the i2c interface , use the raspi-config command to enable it from the advanced options submenu.
Then rebot.
Then use this command.
sudo apt-get install -y python-smbus i2c-tools


lsmod | grep i2c_    use this command to check the i2c interface.

i2cdetect -y 1      use this command to check the hardware. 
