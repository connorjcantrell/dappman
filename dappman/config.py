"""This module provides the dappman config functionality."""
# dappman/config.py

import os
import configparser
import yaml
from pathlib import Path

import typer

from dappman import (
    ALGOD_ERROR, ENV_ERROR, DIR_ERROR, SUCCESS, __app_name_
)


def init_app(app_directory) -> int:
    """Initialize the application."""
    passphrase = os.environ.get("PASSPHRASE")
    if passphrase == None:
        print("please set $PASSPHRASE environment variable")
        return ENV_ERROR
    algod_token = os.environ.get("ALGOD_TOKEN")
    if algod_token == None:
        print("please set $ALGOD_TOKEN environment variable")
        return ENV_ERROR
    config_code = _init_config_file()
    if config_code != SUCCESS:
        return config_code
    algod_client = _connect_node()
    if algod_client != SUCCESS:
        return algod_client
    return SUCCESS

def _init_config_file(app_directory) -> int:
    """Verify config.json is provided correctly """
    try:
        config = yaml.full_load(file(f"{app_directory}/config.yaml", 'rb').read())
        print(config)
    except OSError:
        return FILE_ERROR
    return SUCCESS

def _connect_node(algod_address: str, algod_token: str) -> int:
    """Connect to Algod Client and check status"""
    # initialize an algodClient
    algod_client = algod.AlgodClient(algod_token, algod_address)
    return SUCCESS
