import db
import email_manager
import json
import pandas as pd

CREDENTIALS = json.loads(open('./config.json').read())


def run():
	data = db.get_data(
		region_name=CREDENTIALS['REGION_NAME'],
		table_name=CREDENTIALS['TABLE_NAME'],
		access_key=CREDENTIALS['ACCESS_KEY'],
		secret_key=CREDENTIALS['SECRET_KEY']
	)
	data = sorted(data, key=lambda x: x['S No'])
	
	headers = '''
		<th style="border: 1px solid; padding-left: 30px; padding-right: 30px;">S No</th>
	    <th style="border: 1px solid; padding-left: 30px; padding-right: 30px;">ProductName</th>
	    <th style="border: 1px solid; padding-left: 30px; padding-right: 30px;">Status</th>
	'''	
	rows = ""

	for d in data:
		rows += f"<tr style='border: 1px solid'><td style='border: 1px solid'>{d['S No']}</td><td style='border: 1px solid'>{d['ProductName']}</td><td style='border: 1px solid'>{d['Status']}</td></tr>"


	email_manager.send_email(
		sender_address=CREDENTIALS['SENDER_EMAIL_ADDRESS'],
		sender_password=CREDENTIALS['SENDER_PASSWORD'],
		receiver_address=CREDENTIALS['RECEIVER_EMAIL_ADDRESS'],
		body=f'''
		<html>
		<body>
			<table style="border: 1px solid;  border-collapse: collapse;">
			  <tr style="border: 1px solid; background-color: #D3D3D3">
			    {headers}
			  </tr>
			  {rows}
			</table>
		</body>
		</html>''',
		subject="DynamoDB Report"
	)

if __name__ == '__main__':
	run()

