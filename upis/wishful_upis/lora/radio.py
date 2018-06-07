from wishful_upis.meta_models import Attribute, Measurement, Event, Action

__author__ = "Peter Ruckebusch"
__copyright__ = "Copyright (c) 2016, Ghent University, IMEC, IDLab"
__version__ = "0.1.0"
__email__ = "peter.ruckebusch@intec.ugent.be"

'''IEEE 802.15.4 protocol family

The protocol-specific definition of the WiSHFUL radio control interface, UPI_R,
for configuration/monitoring of the lower layers of the network protocol stack
(lower MAC and PHY).

'''


class DOT_802154E_TimeSlot(object):
    def __init__(self, slot_index, slot_option, channel_offset):
        self.slot_index = slot_index
        self.slot_option = slot_option
        self.channel_offset = channel_offset


class DOT_802154E_SlotLink(object):
    def __init__(self, src_address, dst_address, slot_index, slot_type, channel_offset):
        self.slot_index = slot_index
        self.src_address = src_address
        self.dst_address = dst_address
        self.slot_type = slot_type
        self.channel_offset = channel_offset


class DOT_802154E_SlotFrame(object):
    def __init__(self, slot_offset=0, num_slots=0, slot_frame=None):
        self.slot_offset = slot_offset
        self.num_slots = num_slots
        self.slot_frame = slot_frame


class DOT_802154E_SlotList(object):
    def __init__(self, num_slots, slot_list=None):
        self.num_slots = num_slots
        self.slot_list = slot_list


# ATTRIBUTES
# derived from the IEEE-802.15.4-2012 standard
DOT_802154_PHY_CURRENTCHANNEL = Attribute("IEEE802154_phyCurrentChannel", type=int, isReadOnly=False)  #: IEEE-802.15.4 channel number.
DOT_802154_PHY_TXPOWER = Attribute("IEEE802154_phyTXPower", type=int, isReadOnly=False)  #: The transmit power of the device.
DOT_802154_MAC_EXTENDEDADDRESS = Attribute("IEEE802154_macExtendedAddress", type=list, isReadOnly=False)  #: The extended 64-bit IEEE address assigned to the device.
DOT_802154_MAC_SHORTADDRESS = Attribute("IEEE802154_macShortAddress", type=int, isReadOnly=False)  #: The short 16-bit address that the device uses to communicate in the PAN.
DOT_802154_MAC_PANID = Attribute("IEEE802154_macPANId", type=int, isReadOnly=False)  #: The 16-bit identifier of the PAN on which the device is operating.
DOT_802154_MAC_CW = Attribute("IEEE802154_macCW", type=int, isReadOnly=False)  #: IEEE-802.15.4 channel.
DOT_802154_MAC_MAX_BE = Attribute("IEEE802154_macMaxBE", type=int, isReadOnly=False)  #: The maximum value of the backoff exponent, BE, in the CSMA-CA algorithm, as defined in Section 5.1.1.4. of the IEEE-802.15.4 standard.
DOT_802154_MAC_MIN_BE = Attribute("IEEE802154_macMinBE", type=int, isReadOnly=False)  #: IEEE-802.15.4 channel.
DOT_802154_MAC_MAXCSMABACKOFFS = Attribute("IEEE802154_macMaxCSMABackoffs", type=int, isReadOnly=False)  #: IEEE-802.15.4 channel.
DOT_802154_MAC_MAXFRAMERETRIES = Attribute("IEEE802154_macMaxFrameRetries", type=int, isReadOnly=False)  #: IEEE-802.15.4 channel.
DOT_802154E_MAC_HOPPINGSEQUENCELENGTH = Attribute("IEEE802154e_macHoppingSequenceLength", type=int, isReadOnly=False)  #: IEEE-802.15.4 channel.
DOT_802154E_MAC_HOPPINGSEQUENCELIST = Attribute("IEEE802154e_macHoppingSequenceList", type=list, isReadOnly=False)  #: IEEE-802.15.4 channel.
DOT_802154E_MAC_SLOTFRAMESIZE = Attribute("IEEE802154e_macSlotframeSize", type=int, isReadOnly=False)  #: IEEE-802.15.4 channel.
DOT_802154E_MAC_TIMESLOT = Attribute("IEEE802154e_macTimeslot", type=DOT_802154E_TimeSlot, isReadOnly=False)  #: IEEE-802.15.4 channel.
DOT_802154E_MAC_TSTIMESLOTLENGTH = Attribute("IEEE802154e_macTsTimeslotLength", type=int, isReadOnly=False)  #: IEEE-802.15.4 channel.
DOT_802154E_MAC_SLOTLIST = Attribute("IEEE802154e_macSlotList", type=DOT_802154E_SlotList, isReadOnly=False)  #: IEEE-802.15.4 channel.
DOT_802154E_MAC_SLOTFRAME = Attribute("IEEE802154e_macSlotFrame", type=DOT_802154E_SlotFrame, isReadOnly=False)  #: IEEE-802.15.4 channel.
# protocol (LPL, e.g. contiki_mac specific attributes or TAISC SPECIFIC)
DOT_802154_MAC_LPL_CHANNELCHECKRATE = Attribute("IEEE802154_macLplChannelCheckRate", type=int, isReadOnly=False)  #: IEEE-802.15.4 channel.
DOT_802154_MAC_LPL_PHASEOPTIMIZATION = Attribute("IEEE802154_macLplPhaseOptimization", type=bool, isReadOnly=False)  #: IEEE-802.15.4 channel.
DOT_802154_MAC_TAISC_ACTIVE_RADIO_PROGRAM = Attribute("TAISCActiveRadioProgram", type=str, isReadOnly=False)  #: IEEE-802.15.4 channel.

# MEASUREMENTS
DOT_802154_MAC_STATISTICS = Measurement("IEEE802154_macStats", type=list)

# EVENTS
DOT_802154_MAC_STATISTICS_EVENT = Event("IEEE802154_macStatsEvent", type=list)


def blacklist_channels():
    return
