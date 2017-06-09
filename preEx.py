'''
<PreEx - Intelligence Gathering Program>

Currently has the following capabilities:
    * Organization email addresses
    * Organization hostnames-IPs
    * Target Phone numbers
    * Employee social media profiles
    * Target Social media profiles
    * Current and past addresses
    * DNS information
    * Registered domain holder information
    * SNMP device enumeration
    * Samba device enumeration

Currently working on adding:
    * 

Planning to work on:
    * Relevant contacts (Facebook friends; following on Twitter; manually enter)
    * Events to attend
    * Locations visited
    * Interests
    * Operating System used
    * Software used


PreEx is powered in part by laramies's TheHarvester. 

'''


import sys
# Imports all the scripts in the research folder
from research import *
from subprocess import call
import time


def emails():

    target = raw_input("Enter the target domain: ")

    engine = raw_input("Enter the search engine to use (Google, Baidu, Yandex, or All)\n: ")

    save = raw_input("Do you want to save the information found?\n[?] Enter 1 for yes and 0 for no: ")


    if engine == "Google" or engine == "google":
	search_limit = raw_input("Enter the limit for results in segments of 100: ")

	start = raw_input("Enter the result number to begin searching from (Default: 0): ")

	print "[*] Searching in Google: "
	search = google.google_search(target, search_limit, start)
	search.process()
	emails = search.find_emails()

    if engine == "Baidu" or engine == "baidu":
	search_limit = raw_input("Enter the limit for results in segments of 10: ")

	print "[*] Searching in Baidu: "
	search = baidu.baidu_search(target, search_limit)
	search.process()
	emails = search.find_emails()

    if engine == "Yandex" or engine == "yandex":
	search_limit = raw_input("Enter the limit for results in segments of 50: ")

	print "[*] Searching in Yandex: "
	search = yandex.yandex_search(target, search_limit)
	search.process()
	emails = search.find_emails()

    if save == '0':
        print "\n\n[*] Emails found:"
        print "----------------------"
        if emails == []:
    	    print "[!] No emails found"
        else:
    	    print "\n".join(emails)
    	    print

    else:
        print "\n\n[*] Saving data to file..."
        print "----------------------------"
        try:
    	    t = time.localtime()
    	    timestamp = time.strftime('%b-%d-%Y_%H%M', t)

    	    if engine == engine == "Google" or engine == "google":
    	        filename = "emails_google_" + timestamp

    	    if engine == "Baidu" or engine == "baidu":
    	        filename = "emails_baidu_" + timestamp

    	    if engine == "Yandex" or engine == "yandex":
    	        filename = "emails_yandex_" + timestamp

    	    with open(filename, 'a+') as f:
    	        f.write("\n".join(emails))

    	    print "[+] File saved as: " + filename
    	    print

        except Exception as e:
    	    print e


def hosts():

    target = raw_input("Enter the target domain: ")

    engine = raw_input("Enter the search engine to use (Google, Baidu, Yandex, or All)\n: ")

    search_limit = raw_input("Enter the limit for results in segments of 100: ")

    start = raw_input("Enter the result number to begin searching from (Default: 0): ")

    save = raw_input("Do you want to save the information found?\n[?] Enter 1 for yes and 0 for no: ")


    if engine == "Google" or engine == "google":
        print "[*] Searching in Google: "
        search = google.google_search(target, search_limit, start)
        search.process()
        hosts = search.find_hostnames()

    if engine == "Baidu" or engine == "baidu":
        print "[*] Searching in Baidu: "
        search = baidu.baidu_search(target, search_limit, start)
        search.process()
        hosts = search.find_hostnames()

    if engine == "Yandex" or engine == "yandex":
        print "[*] Searching in Yandex: "
        search = yandex.yandex_search(target, search_limit, start)
        search.process()
        hosts = search.find_hostnames()

    if save == '0':
        print "\n\n[*] Hosts found:"
        print "----------------------"
        if hosts == []:
    	    print "[!] No hosts found"
        else:
    	    hosts = sorted(set(hosts))
    	    print "[*] Resolving hostnames to IPs...\n "

    	    check_hosts = host_confirm.Confirm(hosts)
    	    confirmed_hosts = check_hosts.check()

    	    for host in confirmed_hosts:
                ip = host.split(':')[0]
                print host

    	    print

    else:
        print "\n\n[*] Saving data to file..."
        print "----------------------------"
        try:
    	    t = time.localtime()
    	    timestamp = time.strftime('%b-%d-%Y_%H%M', t)

    	    if engine == engine == "Google" or engine == "google":
    	        filename = "hosts_google_" + timestamp

    	    if engine == "Baidu" or engine == "baidu":
    	        filename = "hosts_baidu_" + timestamp

    	    if engine == "Yandex" or engine == "yandex":
    	        filename = "hosts_yandex_" + timestamp

    	    with open(filename, 'a+') as f:
    	        hosts = sorted(set(hosts))

    	        check_hosts = host_confirm.Confirm(hosts)
    	        confirmed_hosts = check_hosts.check()

    	        for host in confirmed_hosts:
                    ip = host.split(':')[0]
                    f.write(host)
                    f.write("\n")

    	    print "[+] File saved as: " + filename
    	    print

        except Exception as e:
    	    print e


def phone_numbers():

    f_name = raw_input("Enter the target's first name: ")
    l_name = raw_input("Enter the target's last name: ")
    state = raw_input("Enter the target's state initials (Optional): ")
    city = raw_input("Enter the target's city (Optional): ")
    save = raw_input("Do you want to save the information found?\n[?] Enter 1 for yes and 0 for no: ")

    print "[*] Searching for phone numbers: "
    search = numbers.phone_search(f_name, l_name, state, city)
    search.search()
    nums = search.find_numbers()
	    
    if save == '0':
        print "\n\n[*] Phone numbers found:"
        print "----------------------"
        if nums == []:
    	    print "[!] No phone numbers found"
        else:
    	    print "\n".join(nums)
    	    print

    else:
        print "\n\n[*] Saving data to file..."
        print "----------------------------"
        try:
    	    t = time.localtime()
    	    timestamp = time.strftime('%b-%d-%Y_%H%M', t)

    	    filename = l_name + f_name[0] + "_phone_numbers_" + timestamp

    	    with open(filename, 'a+') as f:
    	        f.write(f_name + " " + l_name + " " + "Phone Numbers:\n")
    	        f.write("\n".join(nums))

    	    print "[+] File saved as: " + filename
    	    print

        except Exception as e:
    	    print e


def employees():

    target = raw_input("Enter the target organization: ")

    search_limit = raw_input("Enter the limit for results in segments of 100: ")

    save = raw_input("Do you want to save the information found?\n[?] Enter 1 for yes and 0 for no: ")

    print "[*] Searching in LinkedIn: "
    search = linkedin.linkedin_search(target, search_limit)
    search.process()
    people = search.find_people()
	    
    if save == '0':
        print "Users found in LinkedIn:"
        print "------------------------"
        for user in people:
            print user

    else:
        print "\n\n[*] Saving data to file..."
        print "----------------------------"
        try:
    	    t = time.localtime()
    	    timestamp = time.strftime('%b-%d-%Y_%H%M', t)

    	    filename = target + "_employees_LinkedIn_" + timestamp

    	    with open(filename, 'a+') as f:
    	        f.write(target + " employees:\n\n")
    	        for user in people:
                    f.write(user)
                    f.write("\n")

    	    print "[+] File saved as: " + filename
    	    print

        except Exception as e:
    	    print e


def social_media():

    social_media = raw_input("Enter the social media platform to search in (Facebook, LinkedIn, Twitter, or All)\n: ")

    f_name = raw_input("Enter the target's first name: ")
    l_name = raw_input("Enter the target's last name: ")
    company = raw_input("Enter the target's organization: ")
    state = raw_input("Enter the target's state: ")    


    if social_media == "Twitter" or social_media == "twitter":
        print "[*] Searching in Twitter... "
        print "[*] A web page will pop up with potential profiles."
        search = twitter.twitter_search(f_name, l_name, state)


    if social_media == "Facebook" or social_media == "facebook":
        print "[*] Searching in Facebook... "
        print "[*] A web page will pop up with potential profiles."
        search = facebook.facebook_search(f_name, l_name)


    if social_media == "LinkedIn" or social_media == "linkedin" or social_media == "Linkedin":
        print "[*] Searching in LinkedIn... "
        print "[*] A web page will pop up with potential profiles."
        search = linkedin.linkedin_search("",0).target_profile(f_name, l_name, company, state)


def addresses():
    f_name = raw_input("Enter the target's first name: ")
    m_name = raw_input("Enter the target's middle name (Optional): ")
    l_name = raw_input("Enter the target's last name: ")
    age = raw_input("Enter the target's age (Optional): ")
    state = raw_input("Enter the target's state initials: ")
    city = raw_input("Enter the target's city (Optional): ")

    print "[*] Searching for current and past addresses... "
    print "[*] A web page will open up in your browser with the target's profile."
    print "[*] Click on 'See Full Info >' to get detailed target information."
    print 

    search = "http://www.advancedbackgroundchecks.com/search/results.aspx?type=&fn=" + f_name + "&mi=" + m_name + "&ln=" + l_name + "&age=" + age + "&city=" + city + "&state=" + state

    return call(["x-www-browser", search])


def dnsrecon():
    target = raw_input("Enter the target domain: ")
    print
    search = linux_only.dns_recon(target)


def who():
    target = raw_input("Enter the target domain: ")
    print
    search = linux_only.whois(target)


def snmp_recon():
    target = raw_input("Enter the target IP address: ")
    print
    search = linux_only.enum_snmp(target)


def samba_recon():
    target = raw_input("Enter the target IP address: ")
    print
    search = linux_only.enum_samba(target)


def main():

    global target, wordlist_file, threads, resume, a_ip, a_port

    threads = 50

    if len(sys.argv[1:]) != 1:
        print '''
<PreEx version 0 - Intelligence Gathering Program>\n
Options:
-1   : Find organization email addresses.
-2   : Find organization hostnames-IPs.
-3   : Find phone numbers.
-4   : Find employees' LinkedIn profiles.
-5   : Find target's social media.
-6   : Find relevant contacts.				[Version 1]
-7   : Find current and past addresses.
-8   : Find events that will attend.			[Version 1]
-9   : Find locations visited.				[Version 1]
-10  : Find interests.					[Version 1]
-11  : Find Operating System used.			[Version 1]
-12  : Find software used.				[Version 1]
-13  : Find DNS information.				[Linux-Only]
-14  : Find registered domain holder information.	[Linux-Only]
-15  : Enumerate SNMP devices				[Linux-Only]
-16  : Enumerate Windows and Samba devices.		[Linux-Only]
-17  : View all saved data.				[Version 1]
-18  : Perform all.					[Version 1]
        '''
	sys.exit(0)

    option = sys.argv[1]
	

    # Emails
    if option == "-1":
	emails()

    # Hosts-IPs
    if option == "-2":
	hosts()

    # Phone numbers
    if option == "-3":
	phone_numbers()

    # Employees LinkedIn profiles
    if option == "-4":
	employees()

    # Target social media profiles
    if option == "-5":
	social_media()



    # Current and past addresses
    if option == "-7":
	addresses()


    # Gather DNS information
    if option == "-13":
	dnsrecon()

    # Perform WhoIs lookups
    if option == "-14":
	who()

    # Enumerate SNMP devices
    if option == "-15":
	snmp_recon()

    # Enumerate Windows and Samba devices
    if option == "-16":
	samba_recon()



main()

