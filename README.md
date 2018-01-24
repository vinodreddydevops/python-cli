Python cli using click 

command: auto gensources

description: It will take a yaml file as input. Look for key "repos" and use the values within it to create debian sources.list file. Check plugins.yaml as sample input 


command: auto gennodes

Description: "It will take a csv file as input and a number representing number of machines to accomodate in rack. Each row in csv contains a rack name and cidr of different networks. Create a yaml file containing a list of machines"

command: auto convert 

Description: "It will take machines.yaml and an file extension. Task here is to convert machines.yaml to given extension."
