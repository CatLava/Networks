"# Networks" 
These documents help to enumarate URLs to define webpages and open ports.
The nslook.py is essentially a python coded NSLookup for URLS only, will convert URL to assocaited IPs
The nslook.py file then calls on geol.py for geolocation of IPs.
Shogit.py is integrated with shodan API for more indepth enumaration of IPs, This can search for open ports and what not. However, when integrating with nslook.py, shodan can't process multiple IPs so an enterprise license is required.
Shogit can be run by itself but need to modify code for ideal IP.
nslook uses geol for running.
PM for questions or improvements.
