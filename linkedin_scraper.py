import time
from time import sleep
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from webdriver_manager.chrome import ChromeDriverManager


def scrape(urls: list[str], config: dict, write=False, path=""):
	"""
	Inputs: 
		urls - List of urls
		config: Dictionary containing Linkedin login credentials in the form {"user":"", "pass":""}
		write: Bool to indicate
		path: location to write to, if write == True
	Outputs:

	Usage: e.g. scrape(["https://www.linkedin.com/company/lsesu-data-science-society"])

	"""

	driver = webdriver.Chrome(ChromeDriverManager().install())

	# driver = webdriver.Chrome(executable_path='chromedriver',options=chromeOptions)
	for i, url in enumerate(urls):
		print(f"Current URL: {url}")
		driver.get(url)
		if i == 0:
			# need to close GDPR
			try:
				value = WebDriverWait(driver,3).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'artdeco-global-alert-action')))
				driver.switch_to.frame(value)
				WebDriverWait(driver, 3).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'artdeco-global-alert-action'))).click()
				driver.switch_to.default_content()
				print("Closed GDPR")
			except:
				print("Failed to close GDPR")
			
			# Need to sign in 
			try:
				pass
			except:
				print("Failed to sign in")

		# save webpage, or write to disk

		try:
			pass
		except:
			print("Failed to save webpage")

	return pages

