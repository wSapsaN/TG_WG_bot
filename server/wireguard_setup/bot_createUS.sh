#!/usr/bin/env bash

user_name=$1
private_key=$2
local_address_client=$3

cat << EOF >> "${user_name}.conf"
[Interface]
PrivateKey = ${private_key}
Address = ${local_address_client}/32
DNS = 8.8.8.8

[Peer]
PublicKey = /JjRTRuWZvKn5KIOKuIYeuL0LvEz1N/dm6RHD5If3Gk=
Endpoint = 193.124.92.75:51820 
AllowedIPs = 0.0.0.0/0 
PersistentKeepalive = 20
EOF

exit 0

### THE END ###