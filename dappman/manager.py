import base64
import datetime
import os

from algosdk.future import transaction, wait_for_confirmation
from algosdk import account, mnemonic
from algosdk.v2client import algod
from pyteal import compileTeal, Mode
from helpers import *
from ticket_smart_contract import approval_program, clear_state_program

def create(
        approval_program,
        clear_state_program,
        algod_address="",
        algod_token="",
        local_bytes=0
        local_ints=0,
        global_bytes=0,
        global_ints=0
    ):

    # user declared account mnemonics
    mnemonic = os.environ.get("MNEMONIC")
    address = os.environ.get("PUBLIC_KEY")
    if mnemonic == None:
        print("Could not find $MNEMONIC envirionment variable")
        return
    if address == None:
        print("Could not find $PUBLIC_KEY envirionment variable")
        return
    
    # define private keys
    creator_private_key = get_private_key_from_mnemonic(mnemonic)       

    # user declared algod connection parameters. Node must have EnableDeveloperAPI set to true in its config
    if algod_address == "":
        # Connect to Algorand Sandbox
        algod_address = "http://localhost:4001"
        algod_token = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
    
    # initialize an algodClient
    algod_client = algod.AlgodClient(algod_token, algod_address)
    
    account_info = algod_client.account_info(address)
    print("Account balance: {} microAlgos".format(account_info.get('amount')))
    if account_info.get('amount') < 1000:
        print("Please add funds before continuing")
        return

    # declare application state storage (immutable)
    global_schema = transaction.StateSchema(global_ints, global_bytes)
    local_schema = transaction.StateSchema(local_ints, local_bytes)
    
    # create list of bytes for app args
    app_args = []

    # create new application
    app_id = create_app(
        algod_client,
        creator_private_key,
        approval_program_compiled,
        clear_state_program_compiled,
        global_schema,
        local_schema,
        app_args,
    )
    
    # read global state of application
    print(
        "Global state:",
        read_global_state(
            algod_client, account.address_from_private_key(creator_private_key), app_id
        ),
    )
    return

def update():
    print("Called update")
    return


def delete():
    print("Called delete")
    return
