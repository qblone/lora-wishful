WiSHFUL LoraWan Tutorial 
============================

In this tutorial, we will give a walk-through to setup LoRaWan B-L072Z-LRWAN1 LoRa mote and run an experiment using WiSHFUL framework. 

The objective of the tutorial is to configure LoRa motes to run LoRaWan protocol using wishful UPI's and change parameters dynamically. 


# Network Topology:
We installed WiSHFUL global controller program, on a PC connected through ethernet to a raspberry pi. The local controller (WiSHFUL agent) application is running on the raspberry pi. Finally, our LoRa mote is connected to raspberry pi using a serial interface. The global controller program performs following functions. It discovers network nodes, can configure the LoRa motes with application keys and device ids, and change radio transmission parameters (Spreading factor, tx power, code rate, etc.)



# Pre-requisites: 
1) Wishful Platform :
In our example, we install WiSHFUL Local Control program on the raspberry pi. The mote is connected to the raspberry pi on the serial interface. The WiSHFUL Global Program is installed on a physical machine. Please follow the guide here (http://www.wishful-project.eu/GettingStarted) to install WiSHFUL framework on machines running local control and global control program. Documentation about UPIs can be found here (https://wishful-project.github.io/wishful_upis/) 

2) LoRa Mote : 
We also need to flash mote with our custom bin file. The bin is located in folder mote-software. To flash it you simply need to copy the bin file on to the USB drive. If you do not have access to the graphical interface, please download the ST-link application (https://github.com/texane/stlink) and copy the flash your mote accordingly. 

3) The Things Network Gateways (TTN) : 
We will be using TTN public gateways. The Things network is a crowd-sourced platform which allows volunteers to register gateways and allows its access to the public. We can leverage these gateways and need not to set up our gateways to collect data. To get started create a free account at (https://account.thethingsnetwork.org/register). After that go to applications and add a new application using (https://console.thethingsnetwork.org/applications/add). Use 'ttn-exp' as application id. Finally, register a new device using https://console.thethingsnetwork.org/applications/ttn-exp/devices/register) this link. Type dev01 as device id and keep the other options as default. After successfully registering the device it will land on a new page with "Device EUI" , "Application EUI" and "App Key". We will use these shortly to register our device. 

# LoRaWan Application: 
We present a brief introduction about the LoRaWan and the current application. We have modified the iCube application to send data. The app is running in a continuous loop with class A implementation. It sends data until 1% duty cycle limitation is reached. It then backs off till next slot is available. The 1% duty cycle is an ETSI regulation on European 863-870MHz ISM band.  


# Motes configuration: 
The first step is to configure the mote with correct application keys, so they can activate and authenticate for the TTN servers, to receive data. Please use the keys from TTN account we configured earlier for the following steps. We will use Over-the-Air Activation (OTAA) method in our program. 

Modify the controller file and add the following code
<pre><code>

controller.node(nodes[0]).radio.iface("eth0").set_devEUI(YOURDEVEUI)
controller.node(nodes[0]).radio.iface("eth0").set_appEUI(YOURApplicationEUI)
controller.node(nodes[0]).radio.iface("eth0").set_ak(YOURAPPKEY)
</code></pre>

After running the above commands your device is now activated and you should be able to see incoming data at the following link

https://console.thethingsnetwork.org/applications/ttn-exp/devices/dev01/data

![Alt text](/imgs/connection.png)
Notice the first four messages are activation packets. The messages with blue arrows are actual data packets. 

