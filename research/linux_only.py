'''
Reconnaisance tools available only in Linux devices.
'''

import subprocess


# Perform WhoIs lookups
def whois(target):
    try:
        bash_command = 'whois ' + target

        process = subprocess.Popen(bash_command.split(), stdout=subprocess.PIPE)
        output, error = process.communicate()
        print output

    except:
        print "\n[!] This functionality is only available in Unix and Linux systems.\n"


# Gather DNS information
def dns_recon(target):
    try:
        bash_command = 'dnsrecon -d ' + target

        process = subprocess.Popen(bash_command.split(), stdout=subprocess.PIPE)
        output, error = process.communicate()
        print output

    except:
        print "\n[!] This functionality is only available in Unix and Linux systems.\n"


# Enumerate Windows and Samba devices
def enum_samba(target):
    try:
        bash_command = 'enum4linux -a ' + target

        process = subprocess.Popen(bash_command.split(), stdout=subprocess.PIPE)
        output, error = process.communicate()
        print output

    except:
        print "\n[!] This functionality is only available in Unix and Linux systems.\n"


# Enumerate SNMP devices
def enum_snmp(target):
    try:
        bash_command = 'snmp-check ' + target

        process = subprocess.Popen(bash_command.split(), stdout=subprocess.PIPE)
        output, error = process.communicate()
        print output

    except:
        print "\n[!] This functionality is only available in Unix and Linux systems.\n"


