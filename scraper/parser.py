import re


def ProxyParser(text):
    # The ProxyParser func takes a string of data and returns a list of IP addresses.
    # Regex String to parse IP:PORT for example 65.253.152.100:52532
    regex_string = r'[0-9]+(?:\.[0-9]+){3}\:[0-9]{2,5}'
    ipaddress_list = re.findall(regex_string,text)
    return ipaddress_list

