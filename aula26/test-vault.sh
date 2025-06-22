#!/bin/bash
export VAULT_ADDR='http://127.0.0.1:8200'
export VAULT_TOKEN='root'
curl --silent --header "X-Vault-Token: $VAULT_TOKEN"  $VAULT_ADDR/v1/secret/data/devsecops | jq '.data.data'
