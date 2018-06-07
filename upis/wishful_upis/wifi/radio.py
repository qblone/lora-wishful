__author__ = "Piotr Gawlowicz, Mikolaj Chwalisz, Zubow"
__copyright__ = "Copyright (c) 2015, Technische Universitat Berlin"
__version__ = "0.1.0"
__email__ = "{gawlowicz, chwalisz, zubow}@tkn.tu-berlin.de"


from wishful_upis.meta_models import Attribute, Measurement, Event, Action, ValueDoc


'''
    The protocol-specific definition of the WiSHFUL radio control interface,
    UPI_R, for configuration/monitoring of the
    lower layers of the network protocol stack (lower MAC and PHY).
    IEEE 802.11 protocol family
'''


# ATTRIBUTES
DOT_80211_PHY_ANI = Attribute(key='DOT_80211_PHY_ANI', type=int, isReadOnly=False) #: Adaptive Noise Immunity (ANI)
DOT_80211_STANDARDS = Attribute(key='DOT_80211_STANDARDS', type=int, isReadOnly=False) #: Supported 802.11 standards
DOT_80211_PHY_CHANNEL = Attribute(key='DOT_80211_PHY_CHANNEL', type=int, isReadOnly=False) #: PHY channel
DOT_80211_PHY_RATE = Attribute(key='DOT_80211_PHY_RATE', type=int, isReadOnly=False) #: Rate index value
DOT_80211_PHY_MCS = Attribute(key='DOT_80211_PHY_MCS', type=int, isReadOnly=False) #: Modulation and Coding Scheme (MCS) index value
DOT_80211_PHY_CCA = Attribute(key='DOT_80211_PHY_CCA', type=int, isReadOnly=False) #: Clear channel assessment (CCA) threshold
DOT_80211_RTS_CTS_THRESHOLD = Attribute(key='DOT_80211_RTS_CTS_THRESHOLD', type=int, isReadOnly=False) #:
DOT_80211_FRAGMENTATION_THRESHOLD = Attribute(key='DOT_80211_RTS_CTS_THRESHOLD', type=int, isReadOnly=False) #:
DOT_80211_RETRY_SHORT = Attribute(key='DOT_80211_RETRY_SHORT', type=int, isReadOnly=False) #:Retry short is the number of transmission attempts before change the modulation rate
DOT_80211_RETRY_LONG = Attribute(key='DOT_80211_RETRY_LONG', type=int, isReadOnly=False) #:Retry short is the number of transmission attempts after change the modulation rate
DOT_80211_MAC_STATE_SAMPLING_INTERVAL = Attribute(key='DOT_80211_MAC_STATE_SAMPLING_INTERVAL', type=int, isReadOnly=False) #: MAC state sampling interval in ms
DOT_80211_MAC_EDCA_AIFS = Attribute(key='DOT_80211_MAC_EDCA_AIFS', type=int, isReadOnly=False) #: EDCA Arbitrated Interframe Space value
DOT_80211_MAC_EDCA_CW_MIN =Attribute(key='DOT_80211_MAC_EDCA_CW_MIN', type=int, isReadOnly=False) #: EDCA Contention Window Min value
DOT_80211_MAC_EDCA_CW_MAX =Attribute(key='DOT_80211_MAC_EDCA_CW_MAX', type=int, isReadOnly=False) #: EDCA Contention Window Max value
DOT_80211_MAC_EDCA_TX_OP =Attribute(key='DOT_80211_MAC_EDCA_TX_OP', type=int, isReadOnly=False) #: EDCA Transmit Opportunity value
DOT_80211_PHY_REGURATORY_DOMAIN =Attribute(key='DOT_80211_PHY_REGURATORY_DOMAIN', type=str, isReadOnly=False) #: Reguratory domain information
DOT_80211_POWER_MANAGEMENT = Attribute(key='DOT_80211_POWER_MANAGEMENT', type=int, isReadOnly=False) #: Power Managemenet Scheme: Fixed, Auto

# MEASUREMENTS
DOT_80211_MAC_STATE_IDLE_TIME = Measurement(key='DOT_80211_MAC_STATE_IDLE_TIME', type=int) #: Time MAC spent in idle state in last sampling interval
DOT_80211_MAC_STATE_IDLE_RATIO = Measurement(key='DOT_80211_MAC_STATE_IDLE_RATIO', type=float) #: Ratio of time that MAC spent in idle state in last sampling interval
DOT_80211_MAC_STATE_BUSY_TIME = Measurement(key='DOT_80211_MAC_STATE_BUSY_TIME', type=int) #: Time MAC spent in busy state in last sampling interval
DOT_80211_MAC_STATE_BUSY_RATIO = Measurement(key='DOT_80211_MAC_STATE_BUSY_RATIO', type=float) #: Ratio of time that MAC spent in busy state in last sampling interval
DOT_80211_MAC_STATE_TX_TIME = Measurement(key='DOT_80211_MAC_STATE_TX_TIME', type=int) #: Time MAC spent in TX state in last sampling interval
DOT_80211_MAC_STATE_TX_RATIO = Measurement(key='DOT_80211_MAC_STATE_TX_RATIO', type=float) #: Ratio of time that MAC spent in TX state in last sampling interval
DOT_80211_MAC_STATE_RX_TIME = Measurement(key='DOT_80211_MAC_STATE_RX_TIME', type=int) #: Time MAC spent in RX state in last sampling interval
DOT_80211_MAC_STATE_RX_RATIO = Measurement(key='DOT_80211_MAC_STATE_RX_RATIO', type=float) #: Ratio of time that MAC spent in RX state in last sampling interval
DOT_80211_MAC_STATE_ED_TIME = Measurement(key='DOT_80211_MAC_STATE_ED_TIME', type=int) #: Time MAC spent in energy detection state in last sampling interval
DOT_80211_MAC_STATE_ED_RATIO = Measurement(key='DOT_80211_MAC_STATE_ED_RATIO', type=float) #: Ratio of time that MAC spent in energy detection state in last sampling interval

DOT_80211_MAC_STA_AIR_TIME = Measurement(key='DOT_80211_MAC_STA_AIR_TIME', type=float) #: Per STA air-time statistics
DOT_80211_PHY_LINK_INFO = Measurement(key='DOT_80211_PHY_LINK_INFO', type=float) #: Per STA link informations

# EVENTS
DOT_80211_DATA_FRAME_LOSS = Event(key='DOT_80211_DATA_FRAME_LOSS', type=None) #: Notify about data frame loss
DOT_80211_CONTROL_FRAME_LOSS = Event(key='DOT_80211_CONTROL_FRAME_LOSS', type=None) #: Notify about control frame loss
DOT_80211_MGMT_FRAME_LOSS = Event(key='DOT_80211_MGMT_FRAME_LOSS', type=None) #: Notify about management frame loss

# ACTIONS
DOT_80211_SWITCH_CHANNEL = Action(key='DOT_80211_SWITCH_CHANNEL', args_types=int, return_type=bool) #: Trigger channel switch to new channel
DOT_80211_INJECT_L2_FRAME = Action(key='DOT_80211_INJECT_MGMT_FRAME', args_types=str, return_type=bool) #: Inject L2 frame in hex format
DOT_80211_SNIFF_L2_FRAMES = Action(key='DOT_80211_SNIFF_L2_FRAMES', args_types=int, return_type=bool) #: Sniff N L2 frames


#######################################################
# MAC layer

def set_mac_access_parameters(queueId, qParam):
    '''MAC access parameters in 802.11e: the configuration of the access categories
    '''
    pass


def get_mac_access_parameters(queueId):
    '''MAC access parameters: in 802.11e: the configuration of the access categories
    '''
    pass


'''
    PHY layer
'''


def get_airtime_utilization():
    '''Returns the relative time the spectrum is empty.
    '''
    pass


def perform_spectral_scanning(iface, freq_list, mode):
    '''Perform spectral scanning.

    Returns:
        Power value for each frequency bin.
    '''
    pass


def set_channel(channel):
    '''Set channel, i.e. center frequency of the primary band.

    Args:
        channel: channel to set
    '''
    pass


def get_channel():
    '''Get channel, i.e. center frequency of the primary band.
    '''
    pass


def set_modulation_rate(rate_Mbps):
    '''Set rate modulation
    '''
    pass


def configure_radio_sensitivity(phy_dev, **kwargs):
    '''Configuring the receiving sensitivity of the IEEE 802.11 radio.
    '''
    pass


''' Per flow transmit power control '''

def set_per_flow_tx_power(flowId, txPower):
    """Sets for a flow identified by an 5-tuple (IP header) the transmit power to be used.
    """
    return


def clean_per_flow_tx_power_table():
    """Remove any entries in the transmit power table.
    """
    return


def get_per_flow_tx_power(flowId):
    """Return the transmit power level used for the given flow.
    """
    return


def get_per_flow_tx_power_table():
    """Return the whole transmit power table.
    """
    return


def install_mac_processor(interface, mac_profile):
    """
    Install new WiFi MAC Processor
    """
    return


def update_mac_processor(interface, mac_profile):
    """
    Update WiFi MAC Processor
    """
    pass


def uninstall_mac_processor(interface, mac_profile):
    """
    Uninstall WiFi MAC Processor
    """
    pass


'''
    Channel state information and spectrum scanning capabilities.
'''

def receive_csi(runt):
    '''Receives CSI samples from the ath9k driver.
    '''
    pass


def scan_psd(runt):
    '''Receives PSD samples from the ath9k driver.
    '''
    pass

def set_rts_threshold():
    '''
    Set RTS packet size threshold
    '''
    pass
