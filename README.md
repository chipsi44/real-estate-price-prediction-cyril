# Real-Estate-Price-Prediction:

## Description : 

This is a project about price prediction on the website Immoweb.<br>

In the first part, I obtained the data by scraping them from Immoweb. More information can be found in the "data_acquisition" folder.<br>

Once I had the data set, I needed to understand it. So, I had to clean the data, ask some questions to my dataset, and then make interpretations. More information can be found in the "data_analyze" folder. In this folder, you will find the "presentation.py" file, where you can find the code to create the two graphs presented in the "results." <br>

Then, I had to predict prices on Belgium's real estate sales. So, I had to use machine learning. Here are the steps: select a model, train, test, and evaluate it using my dataset. In the "results," you will find the test and evaluation of different models.<br>
This project uses **linear regression**, **logistic**, **random forest**, and **neural network** models<br>

If you want to find the data set (immo_data.csv), the cleaned data (data_cleaned.csv) or the .png for the graph you can go in the **data_modeling branch**.
## results : 
### Presentation : 
### Model results
**linear regression model** <br>
Mean Squared Error:  8847171.593386266 <br>
Mean Absolute Error:  2643.302809255087
                
**logistic model** <br>
Train score:  0.03636597275764585 <br>
Test score:  0.035670230263157895 

**random_forest model** <br>
Train score:  0.8721151374967875 <br>
Test score:  0.15758634868421054 

**nn model** <br>
Mean Squared Error:  8064819.722794194 <br>
Mean Absolute Error:  2443.128342451968

## Installation:

Install pandas, matplotlib, bs4, scikit-learn, numpy <br>
Requirements.txt file is available !
## Usage:

The data recolted are not used for any commercial activities. <br>
This is done for the purpose of the training only.

## Visuals:

matplotlib graphs <br>
Exported as PNG at some points

## Contributors:
**First week (Data acquisition) :** <br>
Andy Gilet <br>
Cyril Verwimp <br>
Ibrahim Mettioui <br>
**Second and third week (Data analyse + data modeling ) :** <br>
Cyril Verwimp
## Timeline:
first week (5 days): **Data acquisition** <br>

Second week (7 days): **Data analyse** <br>

Third week (6 days) : **Data modeling** <br>

