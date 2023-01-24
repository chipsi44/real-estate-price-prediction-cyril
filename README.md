# Real-Estate-Price-Prediction:

## Description : 

This is a project about price prediction on the website Immoweb with help of AI.<br>

It's going to be in 4 steps : Scrapping, to get the data from Immoweb -> Data analyse, to understand the data set -> data modeling, to get the best model -> Deployement, heu I'll know later

#### In the first part, I obtained the data by scraping them from Immoweb.<br>

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
Test score: -6.09 <br>
Test MAE: 193230.63 <br>
Test MSE: 1548087208187.92 <br>

**ridge model**<br>
Test score: -6.07 <br>
Test MAE: 193210.83 <br>
Test MSE: 1544861136180.71 <br>

**elastic_net model**<br>
Test score: 0.23   <br>
Test MAE: 192366.58 <br>
Test MSE: 167438793285.93 <br>

**lasso model**<br>
Test score: -6.08 <br>
Test MAE: 193229.37 <br>
Test MSE: 1547891047219.70 <br>

**decision_tree model**<br>
Test score: 0.42 <br>
Test MAE: 145703.60 <br>
Test MSE: 126690476526.32 <br>

Those are pretty bad results trying to figure out why
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
