#!/usr/bin/env bash


SSH_USER_AND_HOST="pi@192.168.1.167"

scp stepper_motor_example.py ${SSH_USER_AND_HOST}:/home/pi/stepper_motor_example.py
ssh ${SSH_USER_AND_HOST} chmod 755 /home/pi/stepper_motor_example.py