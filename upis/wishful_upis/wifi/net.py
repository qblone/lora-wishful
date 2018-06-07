__author__ = "Piotr Gawlowicz, Mikolaj Chwalisz, Zubow"
__copyright__ = "Copyright (c) 2015, Technische Universitat Berlin"
__version__ = "0.1.0"
__email__ = "{gawlowicz, chwalisz, zubow}@tkn.tu-berlin.de"


from wishful_upis.meta_models import Attribute, Measurement, Event, Action

# The protocol-specific definition of the WiSHFUL network control interface, UPI_N, for configuration/monitoring of the higher
# layers of the network protocol stack (upper MAC and higher).
# IEEE 802.11 protocol family

# ATTRIBUTES
DOT_80211_MODE = Attribute(key='DOT_80211_MODE', type=int, isReadOnly=False) #: Mode of device: STA, AP, P2P, MESH, AD-HOC
DOT_80211_STA_BLACKLIST = Attribute(key='DOT_80211_STA_BLACKLIST', type=str, isReadOnly=False) #: List of MAC addressed of blacklisted STAs
DOT_80211_STA_TX_POWER = Attribute(key='DOT_80211_STA_TX_POWER', type=int, isReadOnly=False) #: Per STA TX power


# MEASUREMENTS
DOT_80211_AP_NUMBER = Measurement(key='DOT_80211_STA_NUMBER', type=int) #: Number of APs in communication range
DOT_80211_STA_NUMBER = Measurement(key='DOT_80211_STA_NUMBER', type=int) #: Number of STAs in communication range
DOT_80211_SEEN_SSIDS = Measurement(key='DOT_80211_SEEN_SSIDS', type=str) #: List of SSIDs seen in communication range
DOT_80211_CONNECTED_STA_NUMBER = Measurement(key='DOT_80211_CONNECTED_STA_NUMBER', type=int) #: Number of connected STAs to AP
DOT_80211_STA_RSSI = Measurement(key='DOT_80211_STA_RSSI', type=str) #: Per-STA RSSI
DOT_80211_STA_TX_BITRATE = Measurement(key='DOT_80211_STA_TX_BITRATE', type=str) #: Per-STA bitrate
DOT_80211_STA_TX_BYTES = Measurement(key='DOT_80211_STA_TX_BYTES', type=str) #: Per-STA TX bytes
DOT_80211_STA_TX_PKTS = Measurement(key='DOT_80211_STA_TX_PKTS', type=str) #: Per-STA TX packets
DOT_80211_STA_RX_BYTES = Measurement(key='DOT_80211_STA_RX_BYTES', type=str) #: Per-STA RX bytes
DOT_80211_STA_RX_PKTS = Measurement(key='DOT_80211_STA_RX_PKTS', type=str) #: Per-STA RX packets
DOT_80211_STA_INACTIVE_TIME = Measurement(key='DOT_80211_STA_INACTIVE_TIME', type=str) #: Per-STA inactivity time
DOT_80211_STA_RETRY_NUM = Measurement(key='DOT_80211_STA_RETRY_NUM', type=str) #: Per-STA TX retries number
DOT_80211_STA_TX_FAILED = Measurement(key='DOT_80211_STA_TX_FAILED', type=str) #: Per-STA number of failed transmissions

# EVENTS
DOT_80211_PROBE_REQUEST = Event(key='DOT_80211_PROBE_REQUEST', type=None) #: Event triggered on Probe Request reception
DOT_80211_STA_CONNECTED = Event(key='DOT_80211_STA_CONNECTED', type=None) #: Event triggered on STA connection to AP
DOT_80211_STA_DISCONNECTED = Event(key='DOT_80211_STA_DISCONNECTED', type=None) #: Event triggered on STA disconnection from AP
DOT_80211_STA_LOSS = Event(key='DOT_80211_STA_LOSS', type=None) #: Event triggered when STA lost connection with AP

# ACTIONS
DOT_80211_SCAN = Action(key='DOT_80211_SCAN', args_types=int, return_type=bool) #: Perform scanning
DOT_80211_CONNECT = Action(key='DOT_80211_CONNECT', args_types=str, return_type=bool) #: Connect to network by SSID
DOT_80211_DISCONNECT = Action(key='DOT_80211_DISCONNECT', args_types=str, return_type=bool) #: Disconnect from network




# Upper MAC layer
def set_hostapd_conf(iface, file_path, channel, essid):
    '''Set hostapd configuration, provide functionality to setting Access Point station
    '''
    pass


def start_hostapd(file_path):
    '''Start hostapd, provide functionality to run Access Point
    '''
    pass


def stop_hostapd():
    '''Stop hostapd, provide functionality to stop Access Point
    '''
    pass


def connect_to_network(iface, ssid):
    '''Connects a given interface to some network

    e.g. WiFi network identified by SSID.
    '''
    return


def network_dump(iface):
    '''Return the connection information a given interface to some network

    '''
    return


def add_device_to_blacklist(iface, device_mac_addr):
    '''Add the given device to the blacklist

    - 802.11 AP: the device is a client and the result of blacklisting is that the client cannot associate with this node.
    - Other??
    '''
    return


def remove_device_from_blacklist(iface, device_mac_addr):
    '''Remove the given device from the blacklist

    - 802.11 AP: the device is a client and the result of unblacklisting is that the client can associate with this node.
    - Other??
    '''
    return


def disconnect_device(iface, device_mac_addr):
    '''Disconnects the given device from this node

    - 802.11 AP: send dissassociation request to client device
    - 802.11 adhoc: no meaning
    - Other?
    '''
    return


def register_new_device(iface, sta_mac_addr):
    '''Register the given device

    - 802.11 AP: the device is associated with this AP.
    - Other??
    '''
    return


def trigger_channel_switch_in_device(iface, device_mac_addr, target_channel, serving_channel, **kwargs):
    '''Trigger a channel switch in the device connected to this node

    - 802.11 AP: send channel switch announcement to client STA,
    - other??
    '''
    return

def get_info_of_connected_devices():
    '''Returns information about associated devices

    - 802.11 AP: info about the associated client devices of that AP.
    - Other??
    '''
    return


def get_inactivity_time_of_connected_devices():
    '''Returns information about associated devices - inactivity time

    - 802.11 AP: info about the associated client devices of that AP.
    - Other??
    '''
    return


def get_avg_sigpower_of_connected_devices():
    '''Returns information about associated devices - link average signal power

    - 802.11 AP: info about the associated client devices of that AP.
    - Other??
    '''
    return


def get_sigpower_of_connected_devices():
    '''Returns information about associated devices - link signal power

    - 802.11 AP: info about the associated client devices of that AP.
    - Other??
    '''
    return


def get_tx_retries_of_connected_devices():
    '''Returns information about associated devices - tx retries

    - 802.11 AP: info about the associated client devices of that AP.
    - Other??
    '''
    return


def get_tx_packets_of_connected_devices():
    '''Returns information about associated devices - tx packets

    - 802.11 AP: info about the associated client devices of that AP.
    - Other??
    '''
    return


def get_tx_failed_of_connected_devices():
    '''Returns information about associated devices - tx failed

    - 802.11 AP: info about the associated client devices of that AP.
    - Other??
    '''
    return


def get_tx_bytes_of_connected_devices():
    '''Returns information about associated devices - tx bytes

    - 802.11 AP: info about the associated client devices of that AP.
    - Other??
    '''
    return


def get_tx_bitrate_of_connected_devices():
    '''Returns information about associated devices - tx bitrate

    - 802.11 AP: info about the associated client devices of that AP.
    - Other??
    '''
    return


def get_rx_bytes_of_connected_devices():
    '''Returns information about associated devices - rx bytes

    - 802.11 AP: info about the associated client devices of that AP.
    - Other??
    '''
    return


def get_rx_packets_of_connected_devices():
    '''Returns information about associated devices - rx packets

    - 802.11 AP: info about the associated client devices of that AP.
    - Other??
    '''
    return


def get_authorized_connected_device():
    '''Returns information about associated devices - is authorized

    - 802.11 AP: info about the associated client devices of that AP.
    - Other??
    '''
    return


def get_authenticated_connected_device():
    '''Returns information about associated devices - is authenticated

    - 802.11 AP: info about the associated client devices of that AP.
    - Other??
    '''
    return


def get_used_preamble_connected_device():
    '''Returns information about associated devices - preamble used

    - 802.11 AP: info about the associated client devices of that AP.
    - Other??
    '''
    return


def get_mfp_connected_device():
    '''Returns information about associated devices - MFP

    - 802.11 AP: info about the associated client devices of that AP.
    - Other??
    '''
    return


def get_wmm_wme_connected_device():
    '''Returns information about associated devices - WMM/WME

    - 802.11 AP: info about the associated client devices of that AP.
    - Other??
    '''
    return


def get_tdls_peer_connected_device():
    '''Returns information about associated devices - TDLS peer

    - 802.11 AP: info about the associated client devices of that AP.
    - Other??
    '''
    return


def start_monitor():
    '''
    Start Monitor Interface for WiFi Traffice
    '''
    return


def start_adhoc():
    '''
    Start Ad-hoc mode on WiFi interface
    '''
    return
