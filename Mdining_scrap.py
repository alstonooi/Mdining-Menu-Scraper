from selenium import webdriver
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--window-size=1920x1080")
driver = webdriver.Chrome('/mnt/g/Mini Projects/Mdining Menu Scrapper/env/chromedriver.exe', chrome_options=chrome_options)


while True:
	diningHall = input("Which dining hall are you looking for?\n 1 : Bursley \t2: East Quad \t3: Markley \t4: Mosher-Jordan\n 5:North Quad \t6:South Quad \t7:Twigs at Oxford\n")
	try:
		if(int(diningHall) > 0 and int(diningHall) < 8):
			break
	except:
		print("Choose value between 1-7")

diningHall_option = {
	1 : "bursley",
	2 : "east-quad",
	3 : "markley",
	4 : "mosher-jordan",
	5 : "north-quad",
	6 : "south-quad",
	7 : "twigs-at-oxford"
}

diningHall_url = "https://dining.umich.edu/menus-locations/dining-halls/" + diningHall_option.get(int(diningHall))

meal_type = []
driver.get(diningHall_url)
meals = driver.find_element_by_id("mdining-items").text
meal_type = meals.split("\n")

menu_by_meal = {}
for i in range(2, len(meal_type) + 2):
	link = '//*[@id="mdining-items"]/div[' + str(i) +']/ul/li'
	num_type_per_meal = len(driver.find_elements_by_xpath(link))
	food_type = {}
	for j in range(1, num_type_per_meal + 1):
		type_meal = ''
		type_meal = driver.find_element_by_xpath(link + '[' + str(j) + ']/h4').get_attribute("textContent")
		num_2 = len(driver.find_elements_by_xpath(link + '[' + str(j) + ']/ul/li'))
		food = []
		for k in range(1, num_2 + 1):
			item = driver.find_element_by_xpath(link + '[' + str(j) + ']/ul/li[' + str(k) + ']/a/h5/div').get_attribute("textContent")
			food.append(item)
		food_type[type_meal] = food
	menu_by_meal[meal_type[i - 2]] = food_type
