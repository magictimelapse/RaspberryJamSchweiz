
prototype setup:

- Add empty ssh file to /boo/
- raspi-config -> enable I2C

Install software for motor hat:

```
sudo apt-get install -y python-smbus git
mkdir motor_hat
cd motor_hat
git clone https://github.com/adafruit/Adafruit-Motor-HAT-Python-Library.git
cd Adafruit-Motor-HAT-Python-Library
sudo apt-get -y install python-dev
sudo python setup.py install
sudo apt-get -y install ipython
```

Using stepper motor:

```

```