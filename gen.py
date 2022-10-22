def crea_config(smtp, port, username, password, subject, victim_addr, fake_addr, att_website, body, to):
    stringasussy=f'''
		"sending_server": ("{smtp}", {port}),  
		"username": b"{username}",
		"password": b"{password}",
		'''
    stringasussy2='"client_mode": {'+stringasussy+'},'
    stringasussy3=f'''
		"attacker_site": b"{att_website}",
		"legitimate_site_address": b"{fake_addr}",
		"victim_address": b"{victim_addr}",
		"case_id": b"client_a1",


		{stringasussy2}
		
		# Optional. You can leave them empty or customize the email message header or body here
		"subject_header": b"Subject: {subject}",  # Subject: Test espoofer\r\n
		"to_header": b"To: {to}", # To: <alice@example.com>\r\n
		"body": b"{body}", # Test Body.

		# Optional. Set the raw email message you want to sent. It's usually used for replay attacks
		"raw_email": b"", 
		'''
    crea_config2(stringasussy3)

def crea_config2(stringasussy3):
	stringafinale='config = {'+stringasussy3+'}'
	with open('config.py', 'w') as f:
		f.write(stringafinale)
