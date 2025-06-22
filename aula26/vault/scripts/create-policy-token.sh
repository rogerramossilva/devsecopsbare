#!/bin/bash
export VAULT_ADDR='http://127.0.0.1:8200'
export VAULT_TOKEN='root'
vault policy write gitlab-pipeline - <<EOF
path "secret/data/devsecops" {
  capabilities = ["read"]
}
EOF
vault token create -policy="gitlab-pipeline" -ttl=1h
