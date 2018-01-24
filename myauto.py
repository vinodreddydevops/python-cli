import yaml
import os
import csv
import click


@click.group()
def cli():
    pass

@click.command()
@click.option('--input', help="Enter Yaml file")
@click.option('--sourcefile', help="Enter repository file name")
def gensources(input,sourcefile):
	stream = open(input, "r")
	repos = yaml.load_all(stream)
	for repo in repos:
		for i,j in repo.items():
			output = []
			output.append(j)
	# 			print output
	for k in output:
		for y in k.items():
			if y[0] == "repos":
				z = y[1]
				repo1 = z[0]
				repo2 = z[1]

	sourcefile = open(sourcefile, "w+")
	#print '{0} {1} {2} {3}'.format(repo1['type'], repo1['uri'], repo1['suite'], repo1['section'])
	#print '{0} {1} {2} {3}'.format(repo2['type'], repo2['uri'], repo2['suite'], repo2['section'])
	repo1_url = repo1['type'] + ' ' + repo1['uri'] +  ' '+ repo1['suite']+ ' '+ repo1['section']
	repo2_url = repo2['type'] + ' ' + repo2['uri'] +  ' '+ repo2['suite']+ ' '+ repo2['section']
	sourcefile.write(repo1_url)
	sourcefile.write("\n")
	sourcefile.write(repo2_url)

@click.command()
@click.option('--input', help="Enter csv file")
@click.option('--output', help="Enter output file name with yaml extension")
def gennodes(input,output):	
	#input_file = open(input, 'r')
	#output_file = open(output, 'w+')
	items = []
	def csv_to_yaml(line,counter):
		item = {
		'name' : line[0],
		'pxe' : line[1],
	    'public' : line[2],
		'management' : line[3],
		'storage' : line[4]
				}
		items.append(item) 
	#try:
	with open(input, 'r') as input_file, open(output, 'w+') as output_file:
		reader = csv.reader(input_file)
		next(reader)
		for counter, line in enumerate(reader):
			csv_to_yaml(line, counter)
		output_file.write(yaml.dump(items,default_flow_style=False))
	#finally:
	#	input_file.close()
	#s	output_file.close()


@click.command()
@click.option('--input_file', help="Which file you want to convert")
@click.option('--extensiontype', help="enter extensiontype for converting given file extension type")
def convert(input_file, extensiontype):
#	print extensiontype
    if os.path.exists(input_file):
    	converted_file = os.path.splitext(input_file)[0] + '.' + extensiontype
    	os.rename(input_file, converted_file)
    else:
    	print "Given file is not exists"


cli.add_command(gennodes)
cli.add_command(gensources)
cli.add_command(convert)