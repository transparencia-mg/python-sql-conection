import pymysql
import os

def connect():
	result = pymysql.connect(host=os.environ.get('DB_HOST'),
	                     user=os.environ.get('DB_USER'),
	                     password=os.environ.get('DB_PASSWORD'),
	                     database=os.environ.get('DB_DATABASE'),
	                     cursorclass=pymysql.cursors.DictCursor,
	                     read_timeout=30)
	return result

def test_connection(resources):
	rows = ''
	connection = connect()
	with connection.cursor() as cursor:
		cursor.execute(f"select * from evento_etl_carga order by 2 desc;")
		rows = cursor.fetchall()
	return rows

if __name__ == '__main__':
	print(test_connection())