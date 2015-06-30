## Find default loans & save money 

#### Kush Patel, June 2015

The app is live at [defaultFinder](http://www.defaultfinder.info).  

The aim of this project is allow kiva lender or kiva organization to predict potential default loans to save money using machine learning. Using cost benifit matrix and profit curve, translate machine learning to business impact.

## Install
You'll need a few things to run the script. This was built using Python 2.7 

- Download the JSON data snapshot from kiva: http://s3.kiva.org/snapshots/kiva_ds_json.zip
- Checkout the code: 'git clone git://github.com/kush99993s/defaultfinder' 
* cd predict-kiva && pip install -r requirements.txt

### Example:
Average Loan Value: $ 416
Average Interest Rate: 36%

Best model is gradient boosting classifier with recall rate of 0.8. 
Cost benefit matrix:
True Positive: 575 
	Benefit associated with predicting default loan as default
	Benefit: Loan + Interest


False Negative: 607
	cost associated with predicting default loan as non-default
	cost: Loan + Interest + churn of lander (Assume 10%)

False Positive : 0
	cost associated with predicting non-default loan as default
	Since, number of borrower are higher than number of landers. There will not be negative impact classifying some non default loan as default loan

True Negative: 0
	Benefit associated with predicting non-default loan as non-default loan
	benefit will not increase.

Using this cost benefit matrix, I compute profit cure, which shows that there will be maximum profit of $ 3.32 per loan.

Number of Loans are nine hundred thousand. Therefore, total profit is around 3 million dollar. 

### How it works:




##### Caveats:
Geo location and partners are most critical features predicting default loans. There are some cases where few loans given through some partners therefore, it will not good model for predicting loans given borrower through partner. There are few borrowers from some country, therefore, it will be difficult to predict for that country.


### Project Pipeline
1. KIVA API -> JSON
- clean data, input missing value into data
- transform data in numerical value
- split data into training and testing for cross validation
- trained multiple models on 500k loans
- predict status of loans on 300k loans from test data set
- using cross validation, compute model performance and select best model
- build cost benefit matrix, and profit curve
- compute profit for kiva 



#### Packages used
- sklearn
- numpy
- pandas
- javascript
- mapbox

### Background Resources
- [Kiva](https://kiva.org/), 
- [KIVA API](https://build.kiva.org/)
- [mapbox maps](http://leafletjs.com/)