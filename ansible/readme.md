# Prepare a SD card for RaspberryJam

1. Download, verify and extract the full Raspian image: https://www.raspberrypi.org/downloads/raspbian/
2. dd if=your.img of=/dev/YOURSDCARD
3. mount /dev/yoursdcard1 (first partition on the card)
4. ```touch ssh``` on the boot partition to create an empty file which enables SSH server at boot.
5. Boot the raspberry Pi
6. ssh-copy-id pi@RPIIP
7. SSH into your RapsberryPi (check if keybased/passwordless login is possible)

On the RaspberryPi

1. ```vi /etc/ssh/sshd_config``` -> uncomment PermitRootLogin ...
2. Add additional administrator SSH keys to /home/pi/.ssh/authorized_keys
3. ```sudo mkdir /root/.ssh```
4. ```cp /home/pi/.ssh/authorized_keys /root/.ssh/authorized_keys```
5. Define a new user password as pi user: ```passwd```
6. ```cat /etc/shadow``` copy the hashed password for pi user into ansible/playbooks/prepare_for_raspberryjam.yml
7. ```reboot```

After the RaspberyPi was rebooted

1. Add the RaspberryPi's IP address to ansible/hosts/raspberrjam.
2. cd into the ansible directory
3. ```ansible-playbook -l RASPBERRYPIIP prepare_for_raspberryjam.yml```

This will take more than 5 minutes.

1. SSH into the RaspberryPi and perform a clean shutdown ```shutdown -h now```

