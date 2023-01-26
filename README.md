# Real-Estate-Price-Prediction:

## Description : 

This is a project about price prediction on the website Immoweb with help of AI.<br>

It's going to be in 4 steps : Scrapping, to get the data from Immoweb -> Data analyse, to understand the data set -> data modeling, to get the best model -> Deployement, heu I'll know later

#### Scrapping part<br>

In the project, the folder named "data_acquisition" contains all the Python scripts related to the scraping process. Scraping refers to the process of extracting data from websites or other sources. The scripts in the data_acquisition folder are used to collect and process the data needed for the project.<br>

You'll find differents python file : <br>
- Scrapper.py is used to get all the link of properties in immoweb
- scrapper_thread.py is used to get all the links of properties in immoweb but faster because of the threads
- data_analyse_pandas.py is used to scrape information from a website, specifically immoweb, related to properties. The script extracts data such as the 'locality','Price','Type_property' ,'Sale_type','number_bedrooms','Living_area','fully_equipped_kitchen','Furnished','terrace','garden','surface_land','surface_area_plot','facades_number','Swimming_pool','building_state' ,'fire_place' and converts them into a pandas data frame. The data is then saved in a CSV file for further analysis. This script allows you to collect the data you need and put it in a structured format that is easy to work with.
 - data_refactoring.py is used to clean and organize the data acquired through scraping. It removes any unnecessary HTML elements and special characters, as well as any excess whitespace. The script is also used to standardize and improve the names of the columns in the data set, making it more readable and usable for further analysis. The goal is to get a 'cleaned' data that is ready for further processing and analysis.

#### data analyse<br>

After acquiring the data set, it is important to understand it by cleaning the data and asking specific questions to gain insights. Data cleaning is the process of removing or modifying data that is incorrect, incomplete, irrelevant or duplicated. Once the data is cleaned, you can start asking questions to the data set, such as finding the average price of properties in a certain area or the number of properties with a certain number of bedrooms. These questions can be answered using various data analysis techniques such as filtering, sorting, and aggregation. Finally, you can make interpretations of the data by using visualization techniques such as charts and graphs to help identify patterns, trends and outliers in the data. With a cleaned, organized and well-understood data set, you can make informed decisions and insights.<br>

You'll find differents python file : <br>
- data_cleaning.py is used to create a cleaned version of the data set. In this case, cleaning the data means converting all string values to integers and creating a dictionary to match the integers with the corresponding string values. This is similar to how a zip code is matched to the name of a city. The script also addresses any issues with the pricing data, such as correcting any instances where prices were listed as double the actual value (ex : 200K where listed as 200 000 200 000). This script allows for the data to be in a more consistent and usable format for further analysis.
- data_analysis.py and data_interpretation.py are used to understand the data set and ask specific questions. These scripts can be used to perform various data analysis techniques such as filtering, sorting and aggregation. The data analysis script can be used to answer questions about the data, such as finding the average price of properties in a certain area or the number of properties with a certain number of bedrooms. The data interpretation script is used to make sense of the data, by using visualization techniques such as charts and graphs to help identify patterns, trends, and outliers in the data. These scripts allow you to understand the data set and gain valuable insights.
- presentation.py is used to create two graphs that are presented in the results part. 

#### data modeling<br>

After understanding the data set, the next step is to predict prices on Belgium's real estate sales using machine learning. The process typically involves the following steps:

- Selecting a model, such as linear regression, decision tree, lasso, elastic net, or ridge, that best fits the data set.
- Training the model on the data set.
- Testing the model using a separate set of data, called the test set, to evaluate its performance.
- Evaluating the model using metrics such as mean squared error, mean absolute error, and score. <br>

The "results" section of the README contains the testing and evaluation of different models, showing the performance of each one. It is important to keep in mind that the choice of model and the parameters used may have an effect on the performance of the prediction. Therefore, it is important to compare the performance of different models and choose the one that performs the best.
### main.py info <br>
The main file in the project contains a lot of commented parts because it is optimized for speed by saving different information in CSV files. This way, the data does not have to be scrapped, refactored, and cleaned every time a test is run. The main file is also divided into different sections, each of which launches a specific part of the project. This allows for easy navigation and execution of individual parts of the project, rather than having to run the entire project every time. The use of CSV files also allows for the data to be stored and used for future analysis without having to re-scrap and clean the data again.

### branch info <br>
The main branch will be used as the final branch, while the data_modeling branch will be used to keep track of the development of the data modeling process. In the data_modeling branch, you can find the data sets such as link.csv or immo_data.csv, the cleaned data (data_cleaned.csv), as well as the .png files for the graphs. This branch contains all the intermediate files that were generated during the data modeling process and allows for access to the data at different stages of the project. (Please only look at the CSV file, the code will make you cry. :cry:)<br>
 The main branch, on the other hand, contains the final version of the project that is ready for use or presentation.
## State of the project : 
- [x] Scrapping
- [x] Data analyse
- [x] Data modeling
- [ ] Deployement (TBC)
## Results : 
### Data Scrapped : 
We have arround 60K rows, for each rows we have those columns : <br>

<style>
table {
  word-break: keep-all; /* prevent line breaks within cells */
}
</style>

<table>
  <thead>
    <tr>
      <th>Locality</th>
      <th>Price</th>
      <th>Type_property</th>
      <th>Sale_type</th>
      <th>Number_bedrooms</th>
      <th>Living_area</th>
      <th>Fully_equipped_kitchen</th>
      <th>Furnished</th>
      <th>Terrace</th>
      <th>Garden</th>
      <th>Surface_land</th>
      <th>Surface_area_plot</th>
      <th>Facades_number</th>
      <th>Swimming_pool</th>
      <th>Building_state</th>
      <th>Fire_place</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Int (Zip Code)</td>
      <td>Int</td>
      <td>Str (House, flat, ...)</td>
      <td>Rent or sale</td>
      <td>Int</td>
      <td>Float</td>
      <td>Str (Semi, full, No, ...)</td>
      <td>Boolean</td>
      <td>Float (Surface of the terrace)</td>
      <td>Float (Surface of the Garden)</td>
      <td>Float</td>
      <td>Float</td>
      <td>Int</td>
      <td>Boolean</td>
      <td>Str (New, to renovate, ...)</td>
      <td>Boolean</td>
    </tr>
  </tbody>
</table>

When **cleaning the data** all the str and boolean are converted to int ! 

### Presentation : 
The data suggests that the presence of a fire place has the most significant impact on the price of a property. However, it may be due to a lack of data on the topic. To improve the accuracy and completeness of the data, it would be beneficial to make it mandatory for property owners or real estate agents to provide information about the presence of a fire place when listing a property. This would also be beneficial for potential buyers as it would help them make better decisions based on the features they are looking for. The two graphs presented in the analysis aim to demonstrate the importance of collecting data about the presence of a fire place and the potential benefits of implementing this requirement on the platform.
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
- Test score: The test score is a measure of how well the model fits the test data. It is a value between -1 and 1, with higher values indicating a better fit.
- Test MAE (Mean Absolute Error): The test MAE is a measure of the average difference between the predicted values and the actual values. The lower the value, the better the model is at predicting the test data. 
- Test MSE (Mean Squared Error): The test MSE is a measure of the average of the square of the errors. The lower the value, the better the model is at predicting the test data.<br>

**linear_regression model**<br>
Test score: 0.57 <br>
Test Mean Absolute Error: 72333.11 <br>
Test Mean Squared Error: 9319215038.32<br>

**ridge model**<br>
Test score: 0.57 <br>
Test Mean Absolute Error: 72333.05 <br>
Test Mean Squared Error: 9319214776.91 <br>

**elastic_net model** <br>
Test score: 0.52 <br>
Test Mean Absolute Error: 76916.42 <br>
Test Mean Squared Error: 10329782560.707<br>

**lasso model**<br>
Test score: 0.57<br>
Test Mean Absolute Error: 72333.10 <br>
Test Mean Squared Error: 9319209940.24<br>

**decision_tree model**<br>
Test score: 0.13 <br>
Test Mean Absolute Error: 101784.48 <br>
Test Mean Squared Error: 18796478598.45 <br>

Going to choose models that have a test score higher than 0.50
## Installation and how to use:

pip install -r requirements.txt <br>
Requirements.txt file is available !<br>

To use the project, launch the main.py from the main branch. <br>
If you already have some of the CSV file you can comment some part of the main code to make it faster. (The code is well commented, it's easy to find wich part to comment.)
## Usage:

The data recolted are not used for any commercial activities. <br>
This is done for the purpose of the training only.

## Visuals:

Matplotlib graphs <br>
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
