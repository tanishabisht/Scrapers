# Scrapers
This repo contains web scrapers, build using selenium.

## Research Gate Downloads
To download all the research papers given the key word by the user, and save in ResearchGate Downloads folder

## QS World Ranking
To extract all the indicators in from the website and save as an excel file. The column headings are:
```
['Rank', 'University', 'Overall Score', 'International Students Ratio', 'International Faculty Ratio', 'Faculty Student Ratio', 'Citations per Faculty', 'Academic Reputation', 'Employer Reputation']
```

## Devfolio Scraper
This will scrape all the required fields (name, desc, devfolioLink, githubLinks, longDesc) and create a json object in the DatabaseDevfolio folder
```
{
    "idNo": 0, 
    "name": "SheWalksSafe - A Women Safety Application", 
    "desc": "A women safetd for safety", 
    "devfolioLink": "https://devfolio.co/submissions/shewalkssafe", 
    "githubLinks": ["https://drive.google.com/file", "https://github.com/rakulvm/SheWalksSafe"], 
    "special_mention": "10th", 
    "stacksUsed": ["Flutter", "Google Maps API", "Crimeometer API"], 
    "longDesc": "<...>"}
```