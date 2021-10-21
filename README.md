# Mission To Mars

A web application using Flask that scrapes the NASA website for data related to the "Mission to Mars" and displays the information in a single HTML page. This data is always up-to-date whenever you click the "refresh" button on the homepage.


![Mars Screenshot](https://github.com/Jackelyneg/web-scraping-challenge/blob/main/mars%20screenshot.PNG)



### Technologies:
- Python
- Beautiful Soup
- Splinter
- Flask
- Pymongo
- MongoDB
- HTML
- CSS

### Websites Used:
- [Click Here for Mars News Site](https://redplanetscience.com/)
- [Click Here for Mars Featured Image](https://spaceimages-mars.com/)
- [Click Here for Mars Facts](https://galaxyfacts-mars.com/)

### web-scraping-challenge
- Scrape the Mars News Site and collect the latest News Title and Paragraph Text. 
- Use splinter to navigate the site and find the image url for the current Featured Mars Image 
- Visit the Mars Facts webpage here and use Pandas to scrape the table containing facts about the planet including Diameter, Mass, etc.
- Visit the astrogeology site here to obtain high resolution images for each of Mar's hemispheres.

### Flask:
Use MongoDB with Flask templating to create a new HTML page that displays all of the information that was scraped from the URLs above.

Start by converting your Jupyter notebook into a Python script called scrape_mars.py with a function called scrape that will execute all of your scraping code from above and return one Python dictionary containing all of the scraped data.

Next, create a route called /scrape that will import your scrape_mars.py script and call your scrape function.

Store the return value in Mongo as a Python dictionary.
Create a root route / that will query your Mongo database and pass the mars data into an HTML template to display the data.

Create a template HTML file called index.html that will take the mars data dictionary and display all of the data in the appropriate HTML elements. Use the following as a guide for what the final product should look like, but feel free to create your own design.


