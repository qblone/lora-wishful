__author__ = "Piotr Gawlowicz, Mikolaj Chwalisz, Zubow"
__copyright__ = "Copyright (c) 2015, Technische Universitat Berlin"
__version__ = "0.1.0"
__email__ = "{gawlowicz, chwalisz, zubow}@tkn.tu-berlin.de"

'''
    The WiSHFUL management interface.
'''

''' Wishful rule-matching engine '''
def add_rule(rule):
    '''Add new rule to rule-matching engine
    '''
    pass


def delete_rule(rule_id):
    '''Remove rule to rule-matching engine
    '''
    pass

'''
    Framework functionality
'''

def start_local_control_program(program_name, program_code):
    '''Install and execute a given control program on a local node remotely.
    
    Args:
        program_name (string): The name of the local CP.
        program_code (function): A python function containing the local CP control logic. 
    '''
    pass


def stop_local_control_program(program_id):
    '''Stops execution of a given control program on loca/remote node.
    '''
    pass


def send_msg_to_local_control_program(program_id, msg):
    '''Hierarchical control function allows the global control program to send messages to local control programs.
    '''
    pass

def transaction_begin():
    '''Start a transaction

    i.e. all subsequent UPI calls are executed in transactional scope.
    '''
    pass


def transaction_abort():
    '''Aborts a running transaction

    i.e. all changes are roll backed.
    '''
    pass


def transaction_commit():
    '''Commit an open transaction.
    '''
    pass


def disseminate_radio_program(radio_program_id, radio_program, nodes, source_node=0):
    """This function allows to disseminate radio programs to one or more nodes.
    Optionally, a source node can be selected that manages the dissemination process.

    Args:
        radio_program_id (int): Radio program identifier.
        radio_program (file): Binary file containing radio program.
        nodes (list[int]): List of node IDs that need to receive the update.
        source_node (int, optional): ID of the node that manages the dissemination process.

    Returns:
        int: Error value 0 = SUCCESS; -1 = FAIL
    """
    return


def inject_radio_program(radio_program_id, nodes, source_node=0):
    """This function allows to inject a previously disseminated radio programs in one or more nodes.
    Optionally, a source node can be selected that manages the injection process.

    Args:
        radio_program_id (int): Radio program identifier.
        nodes (list[int]): List of node IDs that need to inject the radio program.
        source_node (int, optional): ID of the node that manages the injection process.

    Returns:
        int: Error value 0 = SUCCESS; -1 = FAIL
    """
    return


def allocate_memory(module_id, elf_file_size, rom_size, ram_size, nodes=[]):
    """This function allocates memory on one or more nodes.
    The allocated memory will be used to store the software module and/or radio program.
    This step is required when using an offline ELF linker because the exact memory location must be known upfront.

    Args:
        elf_file_size (int): Size of the ELF file that needs to be stored.
        rom_size (int): ROM usage of the code contained in the ELF file.
        ram_size (int): RAM usage of the code contained in the ELF file.
        nodes (list[int]): List of node IDs that need to allocate_memory.

    Returns:
        AllocatedMemoryBlock: Returns the allocated ROM and RAM addressess, repeats the sizes.
    """
    return


def store_file(module_id, is_last_block, block_size, block_offset, block_data):
    return


def disseminate_software_module(module_id, nodes=[]):
    """This function allows disseminating a software module (i.e. ELF object file) to one or more nodes.

    Args:
        elf_object_file_id (int): ELF object file identifier
        elf_object_file (file): ELF object file
        nodes (list[int]): List of node IDs that need to receive the ELF file.
        source_node (int, optional): ID of the node that manages the dissemination process.

    Returns:
        int: Error value 0 = SUCCESS; -1 = FAIL
    """
    return


def install_software_module(module_id, nodes=[]):
    """This function allows installing a previously disseminated software module on one or more nodes.

    Args:
        elf_object_file_id (int): ELF object file identifier
        nodes (list[int]): List of node IDs that need to install the ELF file.
        source_node (int, optional): ID of the node that manages the installation process.

    Returns:
        int: Error value 0 = SUCCESS; -1 = FAIL
    """
    return


def activate_software_module(module_id, nodes=[]):
    """This function allows activating a previously installed software module on one or more nodes.

    Args:
        elf_object_file_id (int): ELF object file identifier
        nodes (list[int]): List of node IDs that need to activate the ELF file.
        source_node (int, optional): ID of the node that manages the activation process.

    Returns:
        int: Error value 0 = SUCCESS; -1 = FAIL
    """
    return


def init_energy_harvester():
    return


def start_energy_harvester():
    return


def stop_energy_harvester():
    return


def update_energy_harvester():
    return
