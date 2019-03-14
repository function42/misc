import logging, os, shutil, json, time

def weiboLogin(driver, username, password):
    driver.get('https://www.weibo.com/Login.php')
    driver.find_element_by_id('loginname').send_keys(username)
    driver.find_element_by_xpath('/html/body/div[1]/div[1]/div/div[2]/div[1]/div[2]/div/div[2]/div[1]/div[2]/div[1]/div/div/div/div[3]/div[2]/div/input').send_keys(password)
    time.sleep(10)
    driver.find_element_by_css_selector('div.info_list:nth-child(6) > a:nth-child(1)').click()
    time.sleep(20)
    cookies = driver.get_cookies()
    json.dump(cookies, open('cookies.json', 'w'))

def copyFile(ori_file, dest_folder):
	_, filename = os.path.split(ori_file)

	dest_file = os.path.join(dest_folder, filename)
	print('copy %s into %s' % (ori_file, dest_file))
	shutil.copy(ori_file, dest_file)

def showTimeDuration(time_length):
	re_time = ''

	if time_length > 5:  # above 5 seconds
		days = int(time_length // (24 * 60 * 60))
		time_length = time_length - days * 24 * 60 * 60
		hours = int(time_length // (60 * 60))
		time_length = time_length - hours * 60 * 60
		mins = int(time_length // 60)
		secs = time_length - mins * 60

		if days:
			re_time += '{}d '.format(days)
		if hours:
			re_time += '{}h '.format(hours)
		if mins:
			re_time += '{}m '.format(mins)
		re_time += '{:.0f}s'.format(secs)
	else:
		re_time += '{:.3f}s'.format(time_length)

	return re_time


class WatchLogger():
	"""WatchLogger"""
	def __init__(self, write_console=True, write_file=None):
		super(WatchLogger, self).__init__()

		self.watch_logger = logging.getLogger(__name__)
		self.watch_logger.setLevel(logging.INFO)
		formatter = logging.Formatter(
			fmt="%(asctime)s - %(message)s",
			datefmt="%y/%m/%d %H:%M:%S")

		if write_console:  # whether print on console
			console_logging = logging.StreamHandler()
			console_logging.setLevel(logging.INFO)
			console_logging.setFormatter(formatter)
			self.watch_logger.addHandler(console_logging)

		if write_file:  # whether print on file
			file_logging = logging.FileHandler(write_file)
			file_logging.setLevel(logging.INFO)
			file_logging.setFormatter(formatter)
			self.watch_logger.addHandler(file_logging)

	def __call__(self, message):
		# default is info
		self.watch_logger.info(message)

	def debug(self, message):
		self.watch_logger.debug(message)

	def info(self, message):
		self.watch_logger.info(message)

	def warning(self, message):
		self.watch_logger.warning(message)
