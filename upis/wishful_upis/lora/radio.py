from wishful_upis.meta_models import Attribute, Measurement, Event, Action

__author__ = "Qasim Lone"
__copyright__ = "Copyright (c) 2016, Grenoble INP, IMAG, LIG LAB"
__version__ = "0.1.0"
__email__ = "qasim.lone@univ-grenoble-alpes.fr"

'''LoRaWAN protocol family

The protocol-specific definition of the WiSHFUL radio control interface, UPI_R,
for configuration/monitoring of the lower layers of the network protocol stack
(lower MAC and PHY).

'''


# ATTRIBUTES

LORA_PHY_CURRENTCHANNEL = Attribute("LORA_phyCurrentChannel", type=int, isReadOnly=False)  #: LORA channel number.
LORA_TXPOWER = Attribute("LORA_phyTXPower", type=int, isReadOnly=False)  #: The transmit power of the device.
LORA_ADR = Attribute("LORA_adrEnabled", type=bool, isReadOnly=False)  #: Set the ADR on/off
LORA_CODERATE = Attribute("LORA_codeRate", type=int, isReadOnly=False)  #: The transmit power of the device.



# Functions
def set_dr(datarate):
    """This function sets the data rate for LoRa Mote.


    Args:
        datarate (int): the values can be from 0 to 6.

    Returns:

    """
    return
s
def get_dr():
    """This function sets the data rate for LoRa Mote.
    Args:

    Returns:
         datarate (int): the values can be from 0 to 6.

    """
    return

def set_cr(coderate):
    """This function sets the code rate for LoRa Mote.
    Args:
        coderate (int): the values can be from 1 to 4.

    Returns:

    """
    return


def get_cr():
    """This function sets the code rate for LoRa Mote.
    Args: 
    Returns:
    coderate (int): the values can be from 1 to 4.
    1 is 4/5 2 is 4/6 3 is 4/7 and 4 is 4/8

    """
    return

