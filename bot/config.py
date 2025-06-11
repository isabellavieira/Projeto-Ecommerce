#!/usr/bin/env python3
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.

import os

class DefaultConfig:
    """ Bot Configuration """

    PORT = 3978
    APP_ID = os.environ.get("MicrosoftAppId", "")
    APP_PASSWORD = os.environ.get("MicrosoftAppPassword", "")
    URL_PREFIX = os.environ.get("URL_PREFIX", "http://localhost:8080")
    COSMOS_URI = "https://ecommerce-isa-bia-fab-cosmosdb.documents.azure.com:443/"
    COSMOS_KEY = "GkZaTbJzjKs9jO5UgSnyPcGmH0ryjxo3LRFIo9FI9q1RM6udZnhkQ11YovPWMlcOVTLwLwIBIww5ACDbaOhR0A=="
    DATABASE_NAME = "ecommerce"
    CONTAINER_NAME = "produtos"