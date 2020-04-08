# Amazon Delivery Time Slots

With increased demand for grocery delivery due to COVID 19, it can be difficult to find a time slot. Use this script to get text notifications when a time slot opens up for an Amazon Delivery time slot
(for Whole Foods or Amazon Fresh delivery).

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

python3

selenium

chrome webdriver

gmail account to get text notifications

### Installing

To get selenium use:
pip install selenium

To get chrome webdriver go to following webiste:
https://chromedriver.chromium.org/ 


## Running the script

Run with:
python3 get_time_slots.py

The program will walk you through how to use it. The idea is you will navigate to the schedule delivery
page and will leave the script running on that page. It will periodically refresh the page and send 
you a text notification once a time slot is open!