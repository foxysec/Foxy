# Foxy ![](https://visitor-badge.glitch.me/badge?page_id=foxysec.foxy)  [Developing...]

<div> 
  <p align="center">
    <img src="_assets/b_foxy.svg" width="400"> 
  </p>
</div>

**Foxy** is open source CLI application that allows you to use pentester payloads. Foxy App working on Linux and Mac Os X perfectly. You can use it on windows , but there might be some bugs. We will solve these type of problems soon. For any bugs you can write us [issues](https://github.com/foxysec/Foxy/issues). Dont forget to leave star if you like project. You are also free to change code && upgrade code...

## Installation

Copy and paste this script to terminal...

```
git clone https://github.com/foxysec/Foxy
cd Foxy
pip install -r requirements.txt
python foxy.py # Start Foxy
```

## Payloads :
Avaliable Payloads :

```cpp
Payload                         Name             Platform
------------------------------  ---------------  ---------------
foxy::discord::webhook-spammer  Webhook Spammer  Win/Linux/MacOs
foxy::net::port-scanner         Port Scanner     Win/Linux/MacOs
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