import requests
import time

def main():
	previous_ip = None
	while True:
		try:
			current_ip = get_public_ip()
			if current_ip != previous_ip:
				print(f"{current_ip}")
				previous_ip = current_ip
			# else:
				# print(f"{current_ip}")

		except Exception as e:
			print(e)
			previous_ip = None

		time.sleep(360)

def get_public_ip():
	try:
		url = "https://ifconfig.me"
		response = requests.get(url, timeout=10)
		public_ip = response.text
		return public_ip

	except requests.ConnectionError:
		raise Exception("No connection")

	except requests.Timeout:
		raise Exception("Request timed out")

if __name__ == "__main__":
	main()
