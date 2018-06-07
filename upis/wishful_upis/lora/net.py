from wishful_upis.meta_models import Attribute, Measurement, Event, Action
from ipaddress import IPv6Address


__author__ = "Peter Ruckebusch"
__copyright__ = "Copyright (c) 2016, Ghent University, IMEC, IDLab"
__version__ = "0.1.0"
__email__ = "peter.ruckebusch@intec.ugent.be"

'''IEEE 802.15.4 protocol family

The protocol-specific definition of the WiSHFUL network control interface,
UPI_N, for configuration/monitoring of the higher layers of the network
protocol stack (upper MAC and higher).

'''


class LowPanRouteTableEntry(object):
    def __init__(self, dest_ipv6_addr, num_hops, nexthop_ipv6_addr):
        self.dest_ipv6_addr = dest_ipv6_addr
        self.num_hops = num_hops
        self.nexthop_ipv6_addr = nexthop_ipv6_addr


# Attributes
"""
The value used to configure lmin for the DIO Trickle timer.
The default value is 3.
This configuration results in Imin of 8 ms.
"""
LOWPAN_NET_RPL_DIO_INTERVAL_MIN = Attribute("rpl_dio_interval_min", type=int, isReadOnly=False)
"""
The value used to configure Imax for the DIO Trickle timer.
The default value is 20.
This configuration results in a maximum interval of 2.33 hours.
"""
LOWPAN_NET_RPL_DIO_INTERVAL_DOUBLINGS = Attribute("rpl_dio_interval_doublings", type=int, isReadOnly=False)  #:
"""
The value used to configure k for the DIO Trickle timer.
The default value is 10.
This configuration is a conservative value for Trickle suppression mechanism.
"""
LOWPAN_NET_RPL_DIO_REDUNDANCY = Attribute("rpl_dio_redundancy", type=int, isReadOnly=False)  #:
"""
Default route lifetime as a multiple of the lifetime unit.
The lifetime unit is the granularity of time used in RPL lifetime values, in seconds.
"""
LOWPAN_NET_RPL_DEFAULT_LIFETIME = Attribute("rpl_default_lifetime", type=int, isReadOnly=False)  #:
"""
Updates the objective function used to for link estimation and path cost calculation.
"""
LOWPAN_NET_RPL_OBJECTIVE_FUNCTION = Attribute("rpl_objective_function", type=int, isReadOnly=False)  #:

# MEASUREMENTS
LOWPAN_NET_RPL_STATISTICS = Measurement("rpl_stats", type=list)  #: Cumulative statics gathered during RPL operation.

# ACTION
"""
This function configures a node as RPL border router.
"""
LOWPAN_NET_RPL_SET_BORDER_ROUTER = Action("rpl_set_border_router", args_types=(list,), return_type=int)
"""
This function returns all route entries in the route table.
"""
LOWPAN_NET_IPV6_GET_ROUTE_TABLE = Action("get_route_table", args_types=(), return_type=list)
"""
Clears all route entries from the route table.
"""
LOWPAN_NET_IPV6_CLEAR_ROUTE_TABLE = Action("clear_route_table", args_types=(), return_type=int)
"""
Adds a route entry towards the destination IPv6 address given as argument.
"""
LOWPAN_NET_IPV6_ADD_ROUTE = Action("add_route", args_types=(IPv6Address, int, IPv6Address,), return_type=int)
"""
Removes the route entry towards the destination IPv6 address given as argument.
"""
LOWPAN_NET_IPV6_REMOVE_ROUTE = Action("remove_route", args_types=(list,), return_type=int)
"""
This function retuns a list with the IPv6 addresses of all connected neighbors.
"""
LOWPAN_NET_ND6_GET_NEIGHBOR_TABLE = Action("get_neighbor_table", args_types=(), return_type=list)
"""
Add a neigbor to the ND6 neighbor table.
"""
LOWPAN_NET_ND6_ADD_NEIGHBOR = Action("add_neighbor", args_types=(IPv6Address, int, list), return_type=int)


def rpl_set_border_router(rpl_prefix):
    """This function configures a node as RPL border router.
    The function requires an IPv6 rpl prefix as argument.

    Args:
        rpl_prefix (list): array with 8 bytes used as the IPv6 RPL prefix in the DODAG.

    Returns:
        int: Error value 0 = SUCCESS; -1 = FAIL
    """
    return


def ipv6_get_route_table():
    """This function returns all route entries in the route table.
    Each route entry contains the destination IPv6 address,
    the number of hops towards the destination and
    the IPv6 address of the nexthop.

    Returns:
        list: list of LowPanRouteTableEntry objects.
    """
    return


def ipv6_clear_route_table():
    """Clears all route entries from the route table.

    Returns:
        int: Error value 0 = SUCCESS; -1 = FAIL
    """
    return


def ipv6_route_add(dest_ipv6_addr, num_hops, nexthop_ipv6_addr):
    """Adds a route entry towards the destination IPv6 address given as argument.
    The number of hops and nexthop IPv6 address are also required.

    Args:
        dest_ipv6_addr (IPv6Address): IPv6 address of the destination.
        num_hops (int): Number of hops between source and destination.
        nexthop_ipv6_addr (IPv6Address): Next hop towards destination.

    Returns:
        int: Error value 0 = SUCCESS; -1 = FAIL
    """
    return


def ipv6_route_remove(dest_ipv6_addr):
    """Removes the route entry towards the destination IPv6 address given as argument.

    Args:
        dest_ipv6_addr (IPv6Address): IPv6 address of the destination.

    Returns:
        int: Error value 0 = SUCCESS; -1 = FAIL
    """
    return


def nd6_get_neighbor_table():
    """This function retuns a list with the IPv6 addresses of all connected neighbors.

    Returns:
        list: the IPv6 addresses of all connected neighbors.
    """
    return


def nd6_add_neighbor(neighbor_ipv6_addr, neighbor_mac_addr, is_router):
    """Add a neigbor to the ND6 neighbor table.
    This function takes the IPv6 address, the extended MAC address and the role of the neighbor as arguments.

    Args:
        neighbor_ipv6_addr (IPv6Address): Neighbor IPv6 address.
        neighbor_mac_addr (list): Neighbor extended MAC address (64-bit).
        is_router (bool): Indicates if the neighbor has routing capabilities enabled.

    Returns:
        int: Error value 0 = SUCCESS; -1 = FAIL
    """
    return
