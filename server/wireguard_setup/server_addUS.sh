#!/usr/bin/env bash

if [ "$EUID" -ne 0 ]; then
 echo "Please, run the script as root."
 exit 1
fi

if [[ -z $1 ]] || [[ -z $2 ]];
then
  echo "Not found arguments"
  exit 0
fi

user_name=$1
local_address_client=$2

wg genkey | tee "${user_name}_privatekey" | wg pubkey | tee "${user_name}_publickey"

private_key=$(cat "${user_name}_privatekey")
public_key=$(cat "${user_name}_publickey")

cat << EOF >> /etc/wireguard/wg0.conf

[Peer]
PublicKey = ${public_key}
AllowedIPs = ${local_address_client}/32
EOF

systemctl restart wg-quick@wg0

exit 0

### THE END ###