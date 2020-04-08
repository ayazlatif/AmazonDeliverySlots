from selenium import webdriver
import time
import getpass
from text import send_text

def get_delivery_slots(browser):
    slots = browser.find_elements_by_class_name("ufss-date-select-toggle-text-availability")

    slots_text = list(map(lambda s: (s, s.text), slots))
    slots_text = list(filter(lambda s: s[1] != 'Not available', slots_text))
    return slots_text

def navigate_to_sign_in(browser):
    browser.get("https://amazon.com")
    browser.find_element_by_id("nav-link-accountList").click()

def get_phone_info():
    email = input("Please enter your email address: ")
    password = getpass.getpass(prompt="Please enter email password: ")
    phone = input("Please enter phone number to recieve texts: ")
    carrier = input("Which carrier do you have?\
        \n1) AT&T\n2) Sprint\n3) T-Mobile\n4) Verizon\n5) Boost\n6) Cricket\
        \n7) Metro PCS\n8) Tracfone\n9)U.S. Cellular\n10) Virgin Mobile\
        \nPlease enter number: ")
    print()

    return email, password, phone, int(carrier) - 1


response = input("Would you like to recieve text updates on delivery slot availability (y/n)? ")
phone_info = ()
if response == 'y':
    phone_info = get_phone_info()

browser = webdriver.Chrome()
browser.implicitly_wait(60)

navigate_to_sign_in(browser)

print("Please sign in to your account")
input("Press enter once signed in...")
print()

# Opens cart
browser.find_element_by_id("nav-cart-count").click()

print("Please select cart you wish to check delivery slots for and navigate to")
print("schedule delivery screen")
input("Press enter to when you are on the delivery screen...")
print()

print("Finding slots for you now!")
delivery_slots = get_delivery_slots(browser)

while len(delivery_slots) == 0:
    print("refreshing page! " + str(delivery_slots))
    browser.refresh()
    delivery_slots = get_delivery_slots(browser)
    time.sleep(30)


print("Found time slots!")
if len(phone_info) > 0:
    send_text(phone_info)
