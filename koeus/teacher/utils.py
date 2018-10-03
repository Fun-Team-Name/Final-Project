import datetime

def utcNowTimestamp():
	return str(int(datetime.datetime.utcnow().timestamp()))
