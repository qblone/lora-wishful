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
	def __init__(self, dev):
		super(LoraModule, self).__init__()
		self.log = logging.getLogger('LoraModule')
		dev = serial.Serial(comm_port, baudrate=115200,
			 bytesize= serial.EIGHTBITS,parity = serial.PARITY_NONE,
			 stopbits=serial.STOPBITS_ONE, timeout=10)
		self.node = dev
	

	@wishful_module.bind_function(upis.radio.set_parameters)
	def set_parameters(self, params):
        DR = 0
        if 0 <= params['DR'] <= 7:
        	input =''
        	while ((data != input)):
        		dev.write(data.encode('utf-8'))
        		dev.flush()
        		input =  dev.readline().strip()
        		input = input.decode('utf-8',errors='ignore').strip()
        		print(input,data)
        		time.sleep(0.2)# wait
        		


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




