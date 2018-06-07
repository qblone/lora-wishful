__author__ = "Francesco Giannone, Domenico Garlisi"
__copyright__ = "Copyright (c) 2017, Sant'Anna, CNIT"
__version__ = "0.1.0"
__email__ = "{francesco.giannone@santannapisa.it, domenico.garlisi@cnit.it}"

'''
The protocol-specific definition of the WiSHFUL network control interface, UPI_N, for configuration/monitoring of the higher
layers of the network protocol stack (upper MAC and higher).
LTE protocol family
'''

from wishful_upis.meta_models import Attribute, Measurement, Event, Action, ValueDoc

#********
#ENB Attribute
#********
LTE_ENB_DL_BW = Attribute(key='LTE_ENB_DL_BW', type=int, isReadOnly=False)  #: eNB Bandwidth DL
LTE_ENB_UL_BW = Attribute(key='LTE_ENB_UL_BW', type=int, isReadOnly=False)  #: eNB bandwidth UL
LTE_ENB_DL_FREQ = Attribute(key='LTE_ENB_DL_FREQ', type=int, isReadOnly=False)  #: eNB DL center frequency
LTE_ENB_UL_FREQ = Attribute(key='LTE_ENB_UL_FREQ', type=int, isReadOnly=False)  #: eNB UL center frequency
LTE_ENB_FREQ_BAND = Attribute(key='LTE_ENB_FREQ_BAND', type=int, isReadOnly=False)  #: 3GPP eNB Frequency band indicator
LTE_ENB_N_TX_ANT = Attribute(key='LTE_ENB_N_TX_ANT', type=int, isReadOnly=False)  #: eNB Number of TX antennas
LTE_ENB_N_RX_ANT = Attribute(key='LTE_ENB_N_RX_ANT', type=int, isReadOnly=False)  #: eNB Number of RX antennas
LTE_ENB_REF_SIG_POWER = Attribute(key='LTE_ENB_REF_SIG_POWER', type=int, isReadOnly=False)  #: eNB Reference signal power
LTE_ENB_TX_GAIN = Attribute(key='LTE_ENB_TX_GAIN', type=int, isReadOnly=False)  #: eNB TX gain
LTE_ENB_RX_GAIN = Attribute(key='LTE_ENB_RX_GAIN', type=int, isReadOnly=False)  #: eNB RX gain
LTE_ENB_DUPLEX_MODE = Attribute(key='LTE_ENB_DUPLEX_MODE', type=int, isReadOnly=False)  #: eNB Duplex Mode (TDD/FDD)
LTE_ENB_TDD_CONFIGURATION = Attribute(key='LTE_ENB_TDD_CONFIGURATION', type=int, isReadOnly=False)  #: 3GPP eNB TDD configuration mode

#********
#UE net Attribute
#********

LTE_UE_DL_FREQ = Attribute(key='LTE_UE_DL_FREQ', type=int, isReadOnly=False)  #: DL center frequency
LTE_UE_DL_BW = Attribute(key='LTE_UE_DL_BW', type=int, isReadOnly=False)  #: UL center frequency
LTE_UE_UL_BW = Attribute(key='LTE_UE_UL_BW', type=int, isReadOnly=False)  #: Bandwidth DL
LTE_UE_TX_GAIN = Attribute(key='LTE_UE_TX_GAIN', type=int, isReadOnly=False)  #: Bandwidth UL
LTE_UE_RX_GAIN = Attribute(key='LTE_UE_RX_GAIN', type=int, isReadOnly=False)  #: RRU RX gain
LTE_UE_N_TX_ANT = Attribute(key='LTE_UE_N_TX_ANT', type=int, isReadOnly=False)  #: Number of TX antennas
LTE_UE_N_RX_ANT = Attribute(key='LTE_UE_N_RX_ANT', type=int, isReadOnly=False)  #: Number of RX antennas
LTE_UE_RADIO_STATE = Attribute(key='LTE_UE_RADIO_STATE', type=bool, isReadOnly=False)  #: UE State



#********
#UPI
#********

# Generic API to control the lower layers, i.e. key-value configuration.
def set_parameters(param_key_values_dict):
    '''This function (re)set the value(s) of the parameters specified in the dictionary argument.
    The list of available parameters supported by all platforms/OS are defined in this module.
    Parameters specific to a subgroup of platforms/OS are defined in the corresponding submodules.
    A list of supported parameters can be dynamically obtained using the get_info function on each module.

    Examples:
        .. code-block:: python

            >> UPIargs_eNB = {radio.TX_GAIN_enb.key: 90}
            >> result = controller.node(enb_node).radio.set_parameters(UPIargs_eNB)
            >> print result
                    {TX_GAIN_enb.key: 90}

    Args:
        param_key_values_dict (dict): dictionary containing the key (string) value (any) pairs for each parameter.
        An example is {PUCCH_ENB : -96, MME_REALM : wishful_lte, TX_BANDWIDTH_enb : 25}

    Returns:
        dict: A dictionary containing key (string name) error (0 = success, 1=fail, +1=error code) pairs for each parameter.
    '''
    return


def get_parameters(param_key_list):
    '''This function get(s) the value(s) of the parameters specified in the list argument.
    The list of available parameters supported by all platforms are defined in this module.
    Parameters specific to a subgroup of platforms are defined in the corresponding submodules.

    Example:
        .. code-block:: python

            >> UPIargs_eNB = [TX_GAIN_enb]
            >> result = controller.node(enb_node).radio.get_parameters(UPIargs_eNB)
            >> print result
                {TX_GAIN_enb.key: 90}

    Args:
        param_key_list (list): list of parameter names, an example is [UPI_RN.CSMA_CW, UPI_RN.CSMA_CW_MIN, UPI_RN.CSMA_CW_MAX].

    Returns:
        dict: A dictionary containing key (string name) and values of the requested parameters.
    '''
    return