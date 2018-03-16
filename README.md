# Funding Circle Tools

Scripts to scrape information from Funding Circle and plot the data. 
(Also some scripts to automate login and navigation to desired pages.)

Using chromedriver and Python 3 with Selenium and Matplotlib.

### Installation instructions ###

* Install/check you have Python 3.6+ installed along with packages Selenium and Matplotlib.

* Download/clone this git repository.

* Install [chromedriver](https://sites.google.com/a/chromium.org/chromedriver/downloads).
  * If you're on Windows, take a note of the installation directory.
  * Otherwise, add chromedriver to PATH.

* Run generate_storage_files.py and follow the instructions.

### Usage instructions ###

* Run tracking.py to scrape information from Funding Circle website.

* Run graphing.py to generate an interactive plot of scraped data (also saves a picture to graph.pdf).

### Troubleshooting ###

* If you encounter an error, please **make sure you are using the latest version of [chromedriver](https://sites.google.com/a/chromium.org/chromedriver/downloads)**.

* If that doesn't fix it, let me know by logging the issue on Github.
