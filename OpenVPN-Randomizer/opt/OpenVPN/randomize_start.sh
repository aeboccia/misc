#!/bin/bash
#Select a Random VPN config to use from dir script resides in

conf_sel=`find /opt/OpenVPN/ -name "*.ovpn" | shuf -n 1`
/usr/bin/openvpn --log-append /var/log/vpn_connection --config $conf_sel &
