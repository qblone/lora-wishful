"""The WiSHFUL radio control interface, UPI_R.
Used for configuration/monitoring of the lower
layers of the network protocol stack (lower MAC and PHY).

Note, here all generic functions are defined, i.e. those which can be
supported by any wireless networking node (IEEE 802.11, LTE, ZigBee).

All protocol-dependent functions are defined in separate folder,
e.g. ``wifi/``, ``lowpan/`` or ``lte/``.
"""
from .lte.radio import *
from .wifi.radio import *
from .lowpan.radio import *


__author__ = "Piotr Gawlowicz, Mikolaj Chwalisz, Anatolij Zubow, Peter Ruckebusch, Domenico Garlisi"
__copyright__ = "Copyright (c) 2016, Technische Universitat Berlin, iMinds, CNIT"
__version__ = "0.1.0"
__email__ = "{gawlowicz, chwalisz, zubow}@tkn.tu-berlin.de, peter.ruckebusch@intec.ugent.be, domenico.garlisi@cnit.it"

from wishful_upis.meta_models import Attribute, Measurement, Event, Action, ValueDoc


# ATTRIBUTES
TX_POWER = Attribute(key='TX_POWER', type=int, isReadOnly=False) #:Transmission power in dBm
TX_ANTENNA = Attribute(key='TX_ANTENNA', type=int, isReadOnly=False) #:Antenna number selected for transmission
RX_ANTENNA = Attribute(key='RX_ANTENNA', type=int, isReadOnly=False) #:Antenna number selected for reception

NETWORK_INTERFACE_HW_ADDRESS = Attribute(key='NETWORK_INTERFACE_HW_ADDRESS', type=int, isReadOnly=False) #:MAC address of wireless network interface card

TDMA_SUPER_FRAME_SIZE = Attribute(key='TDMA_SUPER_FRAME_SIZE', type=int, isReadOnly=False) #:TDMA protocol. Duration of periodic frames used for slot allocations in us
TDMA_NUMBER_OF_SYNC_SLOT = Attribute(key='TDMA_NUMBER_OF_SYNC_SLOT', type=int, isReadOnly=False) #:TDMA protocol. Number of slots included in a super frame
TDMA_ALLOCATED_SLOT = Attribute(key='TDMA_ALLOCATED_SLOT', type=int, isReadOnly=False) #:TDMA protocol. Assigned slot in a super frame
TDMA_MAC_PRIORITY_CLASS = Attribute(key='TDMA_MAC_PRIORITY_CLASS', type=int, isReadOnly=False) #:TDMA protocol. QUEUE class service associated with TDMA radio program

CSMA_BACKOFF_VALUE = Attribute(key='CSMA_BACKOFF_VALUE', type=int, isReadOnly=False) #:CSMA protocol. Backoff value
CSMA_CW = Attribute(key='CSMA_CW', type=int, isReadOnly=False) #:CSMA protocol.current value of the Contention Window
CSMA_CW_MIN = Attribute(key='CSMA_CW_MIN', type=int, isReadOnly=False) #:CSMA protocol. Minimum value of the Contention Window
CSMA_CW_MAX = Attribute(key='CSMA_CW_MAX', type=int, isReadOnly=False) #:CSMA protocol. Maximum value of the Contention Window
CSMA_TIMESLOT = Attribute(key='CSMA_TIMESLOT', type=int, isReadOnly=False) #:CSMA protocol.Duration of the backoff slot
CSMA_EIFS = Attribute(key='CSMA_EIFS', type=int, isReadOnly=False) #:CSMA protocol.Duration of the EIFS time
CSMA_DIFS = Attribute(key='CSMA_DIFS', type=int, isReadOnly=False) #:CSMA protocol.Duration of the DIFS time
CSMA_SIFS = Attribute(key='CSMA_SIFS', type=int, isReadOnly=False) #:CSMA protocol.Duration of the SIFS time
CSMA_MAC_PRIORITY_CLASS = Attribute(key='CSMA_MAC_PRIORITY_CLASS', type=int, isReadOnly=False) #:CSMA protocol.QUEUE class service associated with CSMA radio program
CSMA_NUM_FREEZING_COUNT = Attribute(key='CSMA_NUM_FREEZING_COUNT', type=int, isReadOnly=True) #:CSMA protocol.Total number of freezing during the backoff phase


# MEASUREMENTS
NOISE = Measurement(key='NOISE', type=int) #: Level of noise in dBm
CSI = Measurement(key='CSA', type=int) #: Channel State Information' last measured value
RSSI = Measurement(key='RSSI', type=int) #:Received Signal Strength Indication (RSSI); it refers to the last received frame in dBm.
SNR = Measurement(key='SNR', type=int) #:Signal-to-noise ratio (SNR) of the last received frame in dB.
LQI = Measurement(key='LQI', type=int) #:Link Quality Indicator (LQI)
FER = Measurement(key='FER', type=int) #:Frame Erasure Rate (FER)
BER = Measurement(key='BER', type=int) #:Bit Error Rate (BER)
BUSY_TYME = Measurement(key='BUSY_TYME', type=int) #:Time interval in which the transceiver has been active (including reception, transmission and carrier sense)
TX_ACTIVITY = Measurement(key='TX_ACTIVITY', type=int) #:Time interval in which the transceiver has been involved in transmission.
LOW_LEVEL_TIME = Measurement(key='LOW LEVEL TIME', type=int) #:Time provided by platform chipset

NUM_GOOD_PREAMBLE = Measurement(key='NUM_GOOD_PREAMBLE', type=int) #:Number of preambles correctly synchronized by the receiver.
NUM_BAD_PREAMBLE = Measurement(key='NUM_BAD_PREAMBLE', type=int) #:Number of receiver errors in synchronizing a valid preamble.
NUM_GOOD_PLCP = Measurement(key='NUM_GOOD_PLCP', type=int) #:Number of valid PLCP synchronized by the receiver
NUM_BAD_PLCP = Measurement(key='NUM_BAD_PLCP', type=int) #:Number of wrong PLCP errors triggered by the receiver
NUM_GOOD_CRC = Measurement(key='NUM_GOOD_CRC', type=int) #:Number of success of CRC checks
NUM_BAD_CRC = Measurement(key='NUM_BAD_CRC', type=int) #:Number of failures of CRC checks
NUM_TX = Measurement(key='NUM_TX', type=int) #:Total number of transmitted frames measured since the interface has been started
NUM_TX_DATA_FRAME = Measurement(key='NUM_TX_DATA_FRAME', type=int) #:Total number of transmitted frames measured since the interface has been started
NUM_TX_SUCCESS = Measurement(key='NUM_TX_SUCCESS', type=int) #:Total number of successfully transmitted frame measured since the interface has been started
NUM_RX = Measurement(key='NUM_RX', type=int) #:Total number of received frames since the interface has been started
NUM_RX_ACK_RAMATCH = Measurement(key='NUM_RX_ACK_RAMATCH', type=int) #:Total number of received frames addressed to the node since the interface has been started. This measurement traces the number of received frame in which the receiver address field matches with the network interface card MAC address
NUM_RX_ACK = Measurement(key='NUM_RX_ACK', type=int) #:Total receive ack frame measured since the interface has been started
NUM_RX_SUCCESS = Measurement(key='NUM_RX_SUCCESS', type=int) #:Total number of successfully transmitted frame measured since the interface has been started

# EVENTS
CHANNEL_UP = Event(key='CHANNEL_UP', type=None) #:Triggered when the wireless channel switches from idle to busy
CHANNEL_DOWN = Event(key='CHANNEL_DOWN', type=None) #:Triggered when the wireless channel switches from busy to idle
QUEUE_OUT_UP = Event(key='QUEUE_OUT_UP', type=None) #:Triggered when the frame is injected into the physical queue of the platform from the upper MAC
RX_END = Event(key='RX_END', type=None) #:Triggered when that receiver operation is finished
RX_PLCP_END = Event(key='RX_PLCP_END', type=None) #:Triggered at the end of PLCP reception
RX_ERROR_BAD_PLCP = Event(key='RX_ERROR_BAD_PLCP', type=None) #:Triggered at the occurrence of a receiver error due a PLCP check failure
RX_ERROR_BAD_CRC = Event(key='RX_ERROR_BAD_CRC', type=None) #:Triggered at the occurrence of a receiver error due a CRC failure
TDMA_SLOT_START = Event(key='TDMA_SLOT_START', type=None) #:Triggered at the beginning of a TDMA slot
TDMA_SLOT_END = Event(key='TDMA_SLOT_END', type=None) #:Triggered at the end of a TDMA slot



# Generic API to control the lower layers, i.e. key-value configuration.
def set_parameters(param_key_values_dict):
    """The UPI_R interface is able to configure the radio and MAC behavior by changing parameters.
    Parameters correspond to the configuration registers of the hardware platform and to the variables used in
    the radio programs. This function (re)set the value(s) of the parameters specified in
    the dictionary argument. The list of available parameters supported by all platforms are defined in this module.
    Parameters specific to a subgroup of platforms are defined in the corresponding submodules.
    A list of supported parameters can be dynamically obtained using the get_radio_info function.

    Example:
        .. code-block:: python

            >> param_key_values = {CSMA_CW : 15, CSMA_CW_MIN : 15, CSMA_CW_MAX : 15}
            >> result = control_engine.radio.iface("wlan0").set_parameters(param_key_values)
            >> print result
            {CSMA_CW : 0, CSMA_CW_MIN : 0, CSMA_CW_MAX : 0}

    Args:
        param_key_values_dict (dict): dictionary containing the key (string) value (any) pairs for each parameter.
            An example is {CSMA_CW : 15, CSMA_CW_MIN : 15, CSMA_CW_MAX : 15}

    Returns:
        dict: A dictionary containing key (string name) error (0 = success, 1=fail, +1=error code) pairs for each parameter.
    """
    return


def get_parameters(param_key_list):
    """The UPI_R interface is able to obtain the current radio and MAC configuration by getting parameter values.
    Parameters correspond to the configuration registers of the hardware platform and to the variables used in the
    radio programs. This function get(s) the value(s) of the parameters specified in the list argument.
    The list of available parameters supported by all platforms are defined in this module.
    Parameters specific to a subgroup of platforms are defined in the corresponding submodules.
    A list of supported parameters can be dynamically obtained using the get_radio_info function.

    Example:
        .. code-block:: python

            >> param_keys = [CSMA_CW,CSMA_CWMIN]
            >> result = control_engine.radio.iface("wlan0").get_parameters(param_keys)
            >> print result
            {CSMA_CW : 15, CSMA_CWMIN : 15}

    Args:
        param_key_list (list): list of parameter names, an example is [UPI_RN.CSMA_CW, UPI_RN.CSMA_CW_MIN, UPI_RN.CSMA_CW_MAX].

    Returns:
        dict: A dictionary containing key (string name) and values of the requested parameters.
     """
    return


def get_measurements(measurement_key_list):
    """The UPI_R interface is able to get the radio measurements in a pull based manner.
    The low-level measurements are continuously monitored by the hardware platform and by the radio programs.
    They can be used to get information and statistics about the state of the physical links or the internal state of the node.
    This function gets the measurements specified in the list argument and returns a dictionary with their values.
    The list of available measurements supported by all platforms are defined in this module.
    Measurements specific to a subgroup of platforms are defined in the corresponding submodules.
    A list of supported measurements can be dynamically obtained using the get_radio_info function.

    Example:
        .. code-block:: python

            >> measurement_keys = [NUM_FREEZING_COUNT]
            >> result = control_engine.radio.iface("wlan0").get_measurements(measurement_keys)
            >> print result
            {UPI_RN.NUM_FREEZING_COUNT : 150}

    Args:
        measurement_key_list (list): list of requested measurements, an example of is [NUM_FREEZING_COUNT, TX_ACTIVITY].

    Returns:
        dict: A dictionary containing key (string name) and values of the requested measurements.
    """
    return


def get_measurements_periodic(measurement_key_list, collect_period, report_period, num_iterations, report_callback):
    """The UPI_R interface is able to get the radio measurements in a pull based manner periodically.
    This function works similarly to  get_measurements, it gets the value(s) specified in the list argument and returns a dictionary with their values, but in cycling mode.
    The function gets the measurements every collect_period and stores them on node memory. Every report_period all measurements are reported to the controller.
    This operation is performed a number of times specified by num_iterations. A callback function is used to receive the measurements results.
    The list of available measurements supported by all platforms are defined in this module. Measurements specific to a subgroup of platforms are defined in the corresponding submodules.
    A list of supported measurements can be dynamically obtained using the get_radio_info function.

    Example:
        .. code-block:: python

            >> def my_cb(report):
            >>     for key in report.keys():
            >>         for measurement in report[key]:
            >>             print measurement
            >> measurement_keys = [NUM_FREEZING_COUNT, TX_ACTIVITY]
            >> result = control_engine.radio.iface("wlan0").get_measurements_periodic(measurement_keys,1000000,5000000,10,my_cb)
            >> print result
            {UPI_RN.NUM_FREEZING_COUNT : 150}

    Args:
        measurement_key_list (list): list of measurement keys. The keys are measurement names defined in this module.
        collect_period (int): defines the time between two consecutive measurement readings, in microsecond.
        report_period (int): defines the time between two consecutive reports to the control program, in microseconds.
        num_iterations (int): defines how many times the measurement collection has to be repeated.
        report_callback (function): the local callback that is invoked every report period.

    Returns:
        int:
            - 0 if the parameter setting call was successfully performed
            - 1 partial success
            - 2 error.
    """
    return


def subscribe_events(event_key_list, event_callback, event_duration):
    """The UPI_R interface is able to monitor the radio and mac behavior asynchronously through events.
    This function subscribes an event listener for one or more events for the specified event duration (0 = infinite).
    The event callback is called each time on of the event is posted.
    The list of available events supported by all platforms are defined in this module.
    Events specific to a subgroup of platforms are defined in the corresponding submodules.
    A list of supported events can be dynamically obtained using the get_radio_info function.

    Example:
        .. code-block:: python

            >> event_keys = ["MAC_RX_EVENT","MAC_COLLISION_EVENT"]
            >> result = control_engine.radio.iface("wlan0").subscribe_events(event_keys, event_cb, 60)
            >> print result
            {"MAC_RX_EVENT" : 0, "MAC_COLLISION_EVENT":0}

    Args:
        event_key_list (list): List of events which should be monitored.
        event_callback (Callable): Callback called every time an event is posted.
        event_duration (int): Duration (in seconds) for which the event listener(s) should be active (0 = infinite)

    Returns:
        dict: A dictionary containing an error code for each event.
    """
    return

# Activation and deactivation of radio programs.


def activate_radio_program(name):
    """This function activates the specified radio program.
    When executed, this function stops the current radio program and enables the execution of the radio program specified in the parameter name.

    Example:
        .. code-block:: python

           >> result = control_engine.radio.iface("wlan0").activate_radio_program("CSMA")
           >> print result
           0

    Args:
        name (str): String identifier of the radio program (e.g. CSMA, TDMA, TSCH)

    Returns:
        int:
            - 0 if the parameter setting call was successfully performed
            - 1 partial success
            - 2 error.
    """
    return


def deactivate_radio_program(name):
    """When executed, this function stops the radio program specified in the parameter radio_program_name.

    Example:
        .. code-block:: python

           >> result = control_engine.radio.iface("wlan0").deactivate_radio_program("CSMA")
           >> print result
           0

    Args:
        name (str): String identifier of the radio program (e.g. CSMA, TDMA, TSCH)

    Returns:
        int:
            - 0 if the parameter setting call was successfully performed
            - 1 partial success
            - 2 error.
    """
    return


def get_running_radio_program():
    """Returns active radio program.

    Each radio program is associated with a name and an index. When executed,
    this function return the index of the radio program active.

    Example:
        .. code-block:: python

            >> args = {'interface' : 'wlan0'}
            >> result = control_engine.radio.iface("wlan0").getActive(args)
            >> print result
            CSMA

    Args:
        myargs:
            a dictionary data type (key: value) where the keys are:
            The key "interface" specify the network interface to use.

    Returns:
        the name of the active radio program
    """
    return

''' Transmission of radio waveform (no MAC) '''


def play_waveform(iface, freq, power_lvl, dict_args):
    """Starts transmitting a radio waveform on signal generator

    Example:
        .. code-block:: python

            >> iface = '192.168.200.35'
            >> freq = '5200'
            >> power_lvl = 0
            >> controller.radio.play_waveform(iface, freq, power_lvl)

    Args:
        iface (String): Address ip of the interface connected with the signal generator.
        freq (int): Frequency of the generated waveform.
        power_lvl (int): power level of the generated waveform.
        dict_args: Extra argumentes for the signal generator.

    Returns:
        int:
            - 0 if the  call was successfully performed
            - 1 partial success
            - 2 error.
    """
    return


def stop_waveform(iface, dict_args):
    """Stops the radio waveform transmitting on signal generator

    Example:
        .. code-block:: python

            >> iface = '192.168.200.35'
            >> controller.radio.stop_waveform(iface)

    Args:
        iface (String): Address ip of the interface connected with the signal generator.
        dict_args: Extra argumentes for the signal generator.

    Returns:
        int:
            - 0 if the  call was successfully performed
            - 1 partial success
            - 2 error.
    """
    return


def set_tx_power(power_dBm):
    """ Sets the transmit power in dBm. If W is the power in Watt, the power in dBm is P = 30 + 10.log(W).

    In addition auto and fixed enable and disable power control (if those features are available).

    Example:
        .. code-block:: python

            >> controller.radio.set_power("15")

    Args:
        power_dBm (String): Specify transmit power level in dBm and setting type

    Returns:
        int:
            - 0 if the  call was successfully performed
            - 1 partial success
            - 2 error.
    """
    return

def get_tx_power():
    """ Gets the current transmit power and the list of various Transmit Powers available on the device

    Example:
        .. code-block:: python

            >> power_information = controller.radio.get_power()
            >> print(power_information)
            current_tx_power:15
            available_tx_power:8,9,10,11,12,13,14,15,16,17,18

    Returns:
        dictionary: transmission power values in dBm

    """
    return

def get_noise():
    """  Background noise level (when no packet is transmitted). May be arbitrary units or dBm, this framework uses
    driver meta information to interpret the raw value given by interface and display it.

    Example:
        .. code-block:: python

            >> noise_information = controller.radio.get_noise()
            >> print(noise_information)
            -80dBm

    Returns:
        int: noise level value

    """
    return


def start_csi_measurements(callback):
    """ Start the thread to receive the channel state information. (amplitude + phase)

    When call, this UPI uses a separate thread to logs channel state estimation for each of the 56 ofdm subcarriers
    (HT20 case). The channel state info is the I and Q values for the subcarriers. When a burst of CSI information is
    ready, a callback is called.

    Args:
        callback (function): Specify the function to call when CSI information have been reported

    Returns:
        int:
            - 0 if the  call was successfully performed
            - 1 partial success
            - 2 error.

    """
    return


def stop_csi_measurements():
    """Stop the thread to receive the channel state information. (amplitude + phase)

    When call, this UPI uses a separate thread to logs channel state estimation for each of the 56 ofdm subcarriers
    (HT20 case). The channel state info is the I and Q values for the subcarriers. When a burst of CSI information is
    ready, a callback is called.

    Returns:
        int:
            - 0 if the  call was successfully performed
            - 1 partial success
            - 2 error.

    """
    return


def get_radio_platforms():
    """ Gets available radio platforms. The information elements used by the UPI_R
    interface, to manage parameters, measurements and radio program, are organized into data structures,
    which provide information on the platform type and radio capabilities.
    When executed, this function return information about available interfaces on node, the name or the identifier
    of the interface and the supported platform type.

    Example:
        .. code-block:: python

            >> radio_platform_list = radio_platform_t()
            >> current_NIC_list_string = control_engine.radio.iface("wlan0").get_radio_platforms()
            >> current_NIC_list.platform_info =  current_NIC_list_string[0]
            >> current_NIC_list.platform =  current_NIC_list_string[1]

    Returns:
        current_NIC_list:
            a list of pair value, the first value is the interface identifier and the second is the supported platforms.
    """
    return


def get_radio_info(platform_id):
    """Gets the radio capabilities of a given network card radio_platform_t in terms of supported measurement and supported
    parameter and list of supported radio program. The information elements used by the UPI_R interface, to manage
    parameters, measurements and radio program, are organized into data structures, which provide information
    on the platform type and radio capabilities. When executed, this function return information about available
    radio capabilities (measurements and parameters) of each interface (radio_platform_t) on the available radio programs
    (radio_prg_t) available for transmissions over the radio interface.

    Example:
        .. code-block:: python

            >> current_platform_info = radio_info_t()
            >> current_platform_info_str = control_engine.radio.iface("wlan0").getRadioInfo(platform_id)
            >> current_platform_info.platform_info.platform_id = current_platform_info_str['radio_info'][0]
            >> current_platform_info.platform_info.platform = current_platform_info_str['radio_info'][1]
            >> current_platform_info.monitor_list = current_platform_info_str['monitor_list']
            >> current_platform_info.param_list = current_platform_info_str['param_list']
            >> current_platform_info.execution_engine_list_name = current_platform_info_str['exec_engine_list_name']
            >> current_platform_info.execution_engine_list_pointer = current_platform_info_str['exec_engine_list_pointer']
            >> current_platform_info.radio_program_list_name = current_platform_info_str['radio_prg_list_name']
            >> current_platform_info.radio_program_list_path = current_platform_info_str['radio_prg_list_pointer']


    Args:
     interface:
        network interfaces to use

    :Returns
        result:
            return a list in term of a dictionary data type (list of key: value). in which are present the key showed below:
            'radio_info' --> a list of pair value, the first value is the interface identifier and the second is the supported platforms.
            'monitor_list' --> a list of supported measurements between the attribute of the class UPI_R
            'param_list' --> a list of supported Parameters between the attribute of the class UPI_R
            'exec_engine_list_name' --> a list of supported execution environment name
            'exec_engine_list_pointer' --> a list of supported execution environment path
            'radio_prg_list_name'--> a list of supported radio program name
            'radio_prg_list_pointer' --> a list of supported radio program path
    """
    return


def set_rxchannel(freq_Hz, bandwidth):
    """Set the operating reception frequency or channel.

    A value below 1000 indicates a channel number, a value greater than 1000 is a frequency in Hz. It is possible to use the suffix k, M or G to the value
    ("2.42G" for 2.42 GHz frequency). Channels are usually numbered starting at 1, it is possible to use get_rxchannel() UPI to get the total number of channels,
    list the available frequencies, and display the current channel.

    Example :
        .. code-block:: python

            >> control_engine.blocking(False).radio.iface("lowpan0").set_rxchannel(26)
            >> print(control_engine.blocking(False).radio.iface("lowpan0").get_rxchannel())
            26 channels in total; available frequencies :
            ...
            Channel 01 : 904 MHz
            Channel 02 : 906 MHz
            Channel 03 : 908 MHz
            ...
            Channel 25 : 2.478 GHz
            Channel 26 : 2.483 GHz
            Current Frequency:2.483 GHz (Channel 26)

    Args :
        freq_Hz(int): frequency in Hz or channel number
        bandwidth(int): bandwidth in Hz

    Returns:
        int:
            - 0 if the  call was successfully performed
            - 1 partial success
            - 2 error.
    """
    return


def get_rxchannel():
    """Return the list of available frequencies in the device and the number of defined channels for the reception module.
     Also return the current frequency/channel setted.

    Example :
        .. code-block:: python

            >> print(control_engine.blocking(False).radio.iface("lowpan0").get_rxchannel())
            26 channels in total; available frequencies :
            ...
            Channel 01 : 904 MHz
            Channel 02 : 906 MHz
            Channel 03 : 908 MHz
            ...
            Channel 25 : 2.478 GHz
            Channel 26 : 2.483 GHz
            Current Frequency:2.483 GHz (Channel 26)

    Returns:
        list: list of available frequencies/channels and current frequency/channel setted
    """
    return


def set_txchannel(freq_Hz, bandwidth):
    """Set the operating transmission frequency or channel.

    A value below 1000 indicates a channel number, a value greater than 1000 is a frequency in Hz. It is possible to use the suffix k, M or G to the value
    ("2.42G" for 2.42 GHz frequency). Channels are usually numbered starting at 1, it is possible to use get_rxchannel() UPI to get the total number of channels,
    list the available frequencies, and display the current channel.

    Example :
        .. code-block:: python

            >> control_engine.blocking(False).radio.iface("lowpan0").set_txchannel(26)
            >> print(control_engine.blocking(False).radio.iface("lowpan0").get_txchannel())
            26 channels in total; available frequencies :
            ...
            Channel 01 : 904 MHz
            Channel 02 : 906 MHz
            Channel 03 : 908 MHz
            ...
            Channel 25 : 2.478 GHz
            Channel 26 : 2.483 GHz
            Current Frequency:2.483 GHz (Channel 26)

    Args :
        freq_Hz(int): frequency in Hz or channel number
        bandwidth(int): bandwidth in Hz

    Returns:
        int:
            - 0 if the  call was successfully performed
            - 1 partial success
            - 2 error.
    """
    return


def get_txchannel():
    """ Return the list of available frequencies in the device and the number of defined channels for the transmission module.
     Also return the current frequency/channel setted.

    Example :
        .. code-block:: python

            >> print(control_engine.blocking(False).radio.iface("lowpan0").get_rxchannel())
            26 channels in total; available frequencies :
            ...
            Channel 01 : 904 MHz
            Channel 02 : 906 MHz
            Channel 03 : 908 MHz
            ...
            Channel 25 : 2.478 GHz
            Channel 26 : 2.483 GHz
            Current Frequency:2.483 GHz (Channel 26)

    Returns:
        list: list of available frequencies/channels and current frequency/channel setted

    """
    return


def get_hwaddr():
    """ Return the Hardware address of the device

    Example :
        .. code-block:: python

            >> mac_address = control_engine.blocking(False).radio.iface("lowpan0").get_hwaddr()
            >> print(mac_address)
            10:1f:74:54:62:f7

    Returns:
        String: HW address in the IEEE: MAC-48 format
    """
    return
