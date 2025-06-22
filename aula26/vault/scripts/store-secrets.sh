#!/bin/bash
export VAULT_ADDR='http://127.0.0.1:8200'
export VAULT_TOKEN='root'
vault kv put secret/devsecops db_user=admin db_pass=Sup3rS3cr3t
vault kv get secret/devsecops
