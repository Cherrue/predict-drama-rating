# predictDramaRating
## Abstract
Predict korean drama tv rate by users behavior in social network by python

Nationality : South Korea

TV rating - http://www.nielsenkorea.co.kr/
Drama Clip(comment data) - http://tv.naver.com/
       
## body
The South Korea have two ideal envrionment about studying that something is influence tv rating.
First, the KR is small country, that is why Korean measure compareatively accurate tv rating.
Second, the KR converge Korean on NAVER.com for search STH or social behavior.

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

5. Support Vector Machine
The correlationship between tv rating and NAVER comment data can be thought of as a none linear model.
And because comment data 7-dimensionsrfdec
So, I predict tv rating by SVM(kernel : 'rbf'=gaussian)

6. Neural Network

## Develop environment

## 개선점
1. 데이터가적음
2. 
