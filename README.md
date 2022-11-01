# Foxy ![](https://visitor-badge.glitch.me/badge?page_id=foxysec.foxy)  [Developing...]

<div> 
  <p align="center">
    <img src="_assets/b_foxy.svg" width="400"> 
  </p>
</div>

Foxy is CLI application that allows you to create trojans,rat virusses and more...\
Here is the installation script.
```
git clone https://github.com/foxysec/Foxy
cd Foxy
pip install -r requirements.txt
python foxy.py # Start Foxy
```

## Payloads :
Avaliable Payloads inside of Foxy App.

```cpp
Payload                         Name             Status
------------------------------  ---------------  ---------
foxy::discord::webhook-spammer  Webhook Spammer  Avaliable
foxy::net::port-scanner         Port Scanner     Avaliable
```

# Guide & Usage
* To get help type 'help' and press enter. You Will get this result :
```
● [Basic]: 

    clear          : clear cmd
    history        : show Foxy command history
    ls             : list files in current directory
    pwd            : print current directory
    cd <dir>       : open folder
    ping <host>    : ping host

● [Advanced]:
    list                : list avaliable payloads
    set payload <pn>    : set payload to start 
    back                : back to Foxy
```
* Setting payload : Setting payload will run setted payload script. 


#### **Developed by Foxy Security Team** :
* [@Thesaderror](https://github.com/Thesaderror)
