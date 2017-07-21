# predictDramaRating
## Abstract
Predict Korean drama tv rate by users behavior in social network by python

Nationality : South Korea

TV rating - http://www.nielsenkorea.co.kr/
Drama Clip(comment data) - http://tv.naver.com/
       
## Body
The South Korea have two ideal envrionment about studying that something is influence tv rating.
First, the KR is small country, that is why Korean measure compareatively accurate tv rating.
Second, the Korean converge on NAVER.com for search STH or social behavior.

Then, I formulate a hypothesis that naver user's behaviors in drama clip have relation with TV rate.
To prove my hypothesis, i will use 
statistical method : multi linear regression
Artificial intelligence : Support Vector Machine, Deep Learning

## Step
1. Parse DATA
Make schema about DATA.
Make spider parsing Nielsen and Naver by python.

Libs : Selenium.chromedriver (virtual browser)
       ODBC manager
       
2. Data Cleansing
Check data description/validation and Cleansing.

3. Data retrieval
Join DATA by SQL.
Draw graphs - scatter, linear.... by MS Excel.
Calculate correlation between variables by MS Excel or python.

4. Linear Regression
Multi Lnear Regression for predicting tv rating by Naver data.

Libs : numpy, pandas, scikit-learn.linear_model -> develop linear regression
       matplotlib.pyplot, seaborn -> data visualization

5. Support Vector Machine                            <============= NOW proceeding!!
The correlationship between tv rating and NAVER comment data can be thought of as a none linear model.
And comment data is 7-dimensions.
So I predict tv rating by SVM(kernel : 'rbf'=gaussian)
Referrence : https://tensorflow.blog/%ED%8C%8C%EC%9D%B4%EC%8D%AC-%EB%A8%B8%EC%8B%A0%EB%9F%AC%EB%8B%9D/

6. Neural Network
TBD...

## Develop environment
1. python 3.6
Anaconda3 4.3.1
(matplotlib 2.0.0
numpy 1.11.3
scikit-learn 0.18.1
seaborn 0.7.1)
Source IDE : Wing IDE 101
Visualize IDE : Jupyter notebook

2. MySQL 5.7.11 (local server)

3. MS Excel 2010

## Problem
Adequate data is severely lacking. But, Time will solve them.
