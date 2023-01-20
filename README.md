# Real-Estate-Price-Prediction:

## Description : 

This is a project about price prediction on the website Immoweb.<br>

In the first part, I obtained the data by scraping them from Immoweb. More information can be found in the "data_acquisition" folder.<br>

Once I had the data set, I needed to understand it. So, I had to clean the data, ask some questions to my dataset, and then make interpretations. More information can be found in the "data_analyze" folder. In this folder, you will find the "presentation.py" file, where you can find the code to create the two graphs presented in the "results." <br>

Then, I had to predict prices on Belgium's real estate sales. So, I had to use machine learning. Here are the steps: select a model, train, test, and evaluate it using my dataset. In the "results," you will find the test and evaluation of different models.<br>
This project uses **linear regression**,**neural network**,**decision_tree**,**lasso**,**elastic_net**, and **ridge** models<br>

If you want to find the data set link.csv or immo_data.csv, the cleaned data (data_cleaned.csv) or the .png for the graph you can go in the **data_modeling branch**.
## results : 
### Presentation : 
<table>
  <tr>
    <td>
        <img src="https://github.com/chipsi44/real-estate-price-prediction-cyril/blob/data_modeling/Figure_1.png" width="400" height="200">
    </td>
    <td>
        <img src="https://github.com/chipsi44/real-estate-price-prediction-cyril/blob/data_modeling/Figure_2.png" width="400" height="200">
    </td>
  </tr>
</table>
(I need to remake the graphs, I know! I'll do it later.)

### Model results
**linear_regression model** <br>
Mean Squared Error:  8847171.593386266<br>
Mean Absolute Error:  2643.302809255087<br>

**Neural network model** <br>
Mean Squared Error:  8033030.594039319<br>
Mean Absolute Error:  2423.54099132909<br>

**ridge model**<br>
Mean Squared Error:  8847171.700932445<br>
Mean Absolute Error:  2643.3036503188905<br>

**elastic_net model**<br>
Mean Squared Error:  8862750.543392384<br>
Mean Absolute Error:  2653.112158454532<br>

**lasso model**<br>
Mean Squared Error:  8847178.330258686 <br>
Mean Absolute Error:  2643.4207911561834<br>

**decision_tree model**<br>
Mean Squared Error:  12167048.02336584<br>
Mean Absolute Error:  2432.6872378055973<br>

Seems pretty clear that taking the **Neural network** model is the more optimize
## Installation:

pip install -r requirements.txt <br>
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
first week (5 days) : **Data acquisition** <br>

Second week (7 days) : **Data analyse** <br>

Third week (6 days) : **Data modeling** <br>
