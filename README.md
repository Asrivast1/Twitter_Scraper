# Twitter Keyword Scraper
This Python script is designed to scrape tweets from Twitter based on specific keywords and save them to a CSV file. It uses the Tweepy library for accessing Twitter's API.

## Prerequisites
Before using this script, you need to have Twitter's developer account to obtain the following API keys from Twitter:

* Twitter API Consumer Key (consumer_key)
* Twitter API Consumer Secret Key (consumer_secret)
* Twitter API Access Token (access_token)
* Twitter API Access Token Secret (access_token_secret)
* Make sure to replace the placeholder values in the script with your actual API keys.

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/your-repo.git

3. Create a virtual environment to isolate the project dependencies:
   ```bash
   python -m venv myenv

5. Activate the virtual environment:
     - On Windows:
       ```bash

       myenv\Scripts\activate
     - On macOS and Linux:
       ```bash
       source myenv/bin/activate
6. Install the required libraries from the requirements.txt file:
   ```bash
   pip install -r requirements.txt
1. Replace the placeholders in the script with your Twitter API keys.

## Usage
Modify the **keywords** list with the specific keywords you want to scrape. You can add or remove keywords as needed.

Set the **no_of_tweets** variable to the maximum number of tweets you want to retrieve for each keyword.

## Run the script:
     > python scraper.py
The script will search for tweets based on the specified keywords and store the collected data in a CSV file named ***"tweet.csv."***

## Disclaimer
Please be mindful of Twitter's terms of service and rate limits. This script is for educational purposes and should be used responsibly and in compliance with Twitter's API usage policies.

#### Do consider to star this project if you find it useful ⭐
