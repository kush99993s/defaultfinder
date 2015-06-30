## Find default loans & save money 



#### Kush Patel, June 2015


The app is live at [defaultFinder](http://www.defaultfinder.info).  

The aim of this project is allow kiva lender or kiva organization to predict potential default loans to save money using machine learning. Using cost benifit matrix and profit curve, translate machine learning to business impact.



### Example

The maps are built using terms extracted from San Francisco Yelp restaurant reviews from December 2014. The size of the hexagons is proportional to the number of reviews in the area and gives a representation of the density of restaurant activity. The colors indicate the share of the reviews in that cell that contain the search term or words related to it.

The GREEN-RED color scale goes from a very low to a very high share of reviews in that hex-cell containing the relevant terms.
SIZE is proportional to the total number of reviews and does not change between searches.

### How it works


##### Caveats:
Geolocation and partnerid are most critical feature in machine learning alogritham, there are some cases where few loans given to partner therefore, it will not good model for predicting loans given borrower through partner

### Project Pipeline
1. KIVA API -> JSON
- clean data, input missing value into data
- transform data in numberical value
- split data into training and testing for cross validationn
- trained multiple models on 500k loans
- predict status of loans on 300k loans from test data set
- using cross validation, comput model performance
- build cost benifit matrix, and profit curve
- compute profit for kiva 



#### Packages used
- sklearn
- numpy
- pandas
- javascript
- mapbox

### Background Resources
- [word2vec](https://code.google.com/p/word2vec/), [technical details](https://docs.google.com/file/d/0B7XkCwpI5KDYRWRnd1RzWXQ2TWc/edit)
- [hexbin maps](http://www.delimited.io/blog/2013/12/1/hexbins-with-d3-and-leaflet-maps)
- [Yelp API](https://www.yelp.com/developers/documentation)