import boto3
import pandas as pd
import json

def clean_data(data):
	for d in data:
		d['S No'] = int(d['S No'])
	return data

def get_data(table_name, region_name, access_key, secret_key):
	db = boto3.resource(
			"dynamodb", 
			region_name=region_name,
			aws_access_key_id=access_key,
	        aws_secret_access_key= secret_key
	    )

	table = db.Table(table_name)

	items = table.scan().get('Items')
	items = clean_data(items)
	return items
