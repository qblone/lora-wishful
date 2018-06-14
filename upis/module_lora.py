import logging
import random
import wishful_upis as upis
import wishful_framework as wishful_module
from wishful_framework.classes import exceptions
import serial
import sys
import time
import errno
import os
import signal

@wishful_module.build_module
class LoraModule(wishful_module.AgentModule):
    node = None
    pwr = 6
    def __init__(self):
        super(LoraModule, self).__init__()
        self.log = logging.getLogger('LoraModule')
        #dev = serial.Serial('/dev/ttyACM0', baudrate=115200,
        #        bytesize= serial.EIGHTBITS,parity = serial.PARITY_NONE,
        #        stopbits=serial.STOPBITS_ONE, timeout=10)
        #self.node = dev
	

    @wishful_module.bind_function(upis.lora.radio.set_dr)
    def set_dr(self,dr):
        self.log.info("Set Parameters called".format())
        #DR = 0
        if 0 <= dr <= 7:
            # Open serial connection
            dev = serial.Serial('/dev/ttyACM0', baudrate=115200,
                    bytesize= serial.EIGHTBITS,parity = serial.PARITY_NONE,
                    stopbits=serial.STOPBITS_ONE, timeout=10)
            
            #Adding start and end char to ensure data is recieved properly
            data ='^dr0{}$'.format(dr)
            # Writing data on serial prot
            self.log.info("Data sent by controller is: {}".format(data)) 
            dev.write(data.encode('utf-8'))
            dev.flush()
                
            rec_data = dev.readline().strip().decode('utf-8',errors='ignore')
            
            #while rec_data !='txDone': # wait for tx of packet
            #    rec_data = self.node.readline().strip().decode('utf-8',errors='ignore')
            
            #self.log.info("len {}".format(len(rec_data)))
            
            self.log.info("Recieved data from Lora {}:  Data sent to Lora Board{}".format(rec_data,data))
            time.sleep(0.2)# wait
            dev.close()
            return 1
        else:
            return 0
    
    @wishful_module.bind_function(upis.lora.radio.set_cr)
    def set_cr(self,cr):
        self.log.info("Set Parameters called".format())
        #DR = 0
        if 1 <= cr <= 4:
            # Open serial connection
            dev = serial.Serial('/dev/ttyACM0', baudrate=115200,
                    bytesize= serial.EIGHTBITS,parity = serial.PARITY_NONE,
                    stopbits=serial.STOPBITS_ONE, timeout=10)

            #Adding start and end char to ensure data is recieved properly
            data ='^cr0{}$'.format(cr)
            # Writing data on serial prot
            self.log.info("Data sent by controller is: {}".format(data)) 
            dev.write(data.encode('utf-8'))
            dev.flush()
                
            rec_data = dev.readline().strip().decode('utf-8',errors='ignore')
            
            #while rec_data !='txDone': # wait for tx of packet
            #    rec_data = self.node.readline().strip().decode('utf-8',errors='ignore')
            
            #self.log.info("len {}".format(len(rec_data)))
            
            self.log.info("Recieved data from Lora {}:  Data sent to Lora Board{}".format(rec_data,data))
            time.sleep(0.2)# wait
            dev.close()
            return 1
        else:
            return 0
    
    
    
    @wishful_module.bind_function(upis.radio.set_tx_power)
    def set_tx_power(self, power):
        if 2 <= power <= 14:
            data ='^tx{}$'.format(str(power).zfill(2))
            self.log.info("Data sent by controller is: {}".format(data))

            return 1
        else:
            return 0





#    @wishful_module.bind_function(upis.radio.set_parameters)
#    def set_parameters(self, params):
#        self.log.info("Set Parameters called".format())
#        #DR = 0
#        if 0 <= params['DR'] <= 7:
#            ctr_dt = params['DR']
#            data ='^dr0{}$'.format(ctr_dt)
#            self.log.info("Data sent by controller is: {}".format(data)) 
#            rec_data = ''
#            #while ((data != rec_data)):
#            self.node.write(data.encode('utf-8'))
#            self.node.flush()
#                
#            rec_data = self.node.readline().strip().decode('utf-8',errors='ignore')
#            self.log.info("len {}".format(len(rec_data)))
#            self.log.info("Recieved data from Lora {}:  Data sent to Lora Board{}".format(rec_data,data))
#            time.sleep(0.2)# wait







    @wishful_module.on_start()
    def myFunc_1(self):
        self.log.info("This function is executed on agent start".format())


    @wishful_module.on_exit()
    def myFunc_2(self):
        self.log.info("This function is executed on agent exit".format())


    @wishful_module.on_connected()
    def myFunc_3(self):
        self.log.info("This function is executed on connection to global controller".format())


    @wishful_module.on_disconnected()
    def myFunc_4(self):
        self.log.info("This function is executed after connection with global controller was lost".format())


    @wishful_module.on_first_call_to_module()
    def myFunc_5(self):
        self.log.info("This function is executed before first UPI call to module".format())




