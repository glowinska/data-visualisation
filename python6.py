# -*- coding: utf-8 -*-
"""

Imagine an Ecommerce company based in New York City that sells clothing online but they also have in-store style and clothing advice sessions. Customers come in to the store, have sessions/meetings with a personal stylist, then they can go home and order either on a mobile app or website for the clothes they want.

The company is trying to decide whether to focus their efforts on their mobile app experience or their website.

Just follow the steps below to analyze the customer data.

Imports
** Import pandas, numpy, matplotlib,and seaborn. Then set %matplotlib inline
(You'll import sklearn as you need it.)**
"""



"""Get the Data
We'll work with the L06_Ecommerce_Customers.csv file attached to the exrecise. It has Customer info, such as Email, Address, and their color Avatar. Then it also has numerical value columns:

Avg. Session Length: Average session of in-store style advice sessions.
Time on App: Average time spent on App in minutes
Time on Website: Average time spent on Website in minutes
Length of Membership: How many years the customer has been a member.
** Read in the Ecommerce Customers csv file as a DataFrame called customers.**
"""



"""
Check the head of customers, and check out its info() and describe() methods.

...
<div> <table border="1" class="dataframe"> <thead> <tr style="text-align: right;"> <th></th> <th>Email</th> <th>Address</th> <th>Avatar</th> <th>Avg. Session Length</th> <th>Time on App</th> <th>Time on Website</th> <th>Length of Membership</th> <th>Yearly Amount Spent</th> </tr> </thead> <tbody> <tr> <th>0</th> <td>mstephenson@fernandez.com</td> <td>835 Frank Tunnel\nWrightmouth, MI 82180-9605</td> <td>Violet</td> <td>34.497268</td> <td>12.655651</td> <td>39.577668</td> <td>4.082621</td> <td>587.951054</td> </tr> <tr> <th>1</th> <td>hduke@hotmail.com</td> <td>4547 Archer Common\nDiazchester, CA 06566-8576</td> <td>DarkGreen</td> <td>31.926272</td> <td>11.109461</td> <td>37.268959</td> <td>2.664034</td> <td>392.204933</td> </tr> <tr> <th>2</th> <td>pallen@yahoo.com</td> <td>24645 Valerie Unions Suite 582\nCobbborough, D...</td> <td>Bisque</td> <td>33.000915</td> <td>11.330278</td> <td>37.110597</td> <td>4.104543</td> <td>487.547505</td> </tr> <tr> <th>3</th> <td>riverarebecca@gmail.com</td> <td>1414 David Throughway\nPort Jason, OH 22070-1220</td> <td>SaddleBrown</td> <td>34.305557</td> <td>13.717514</td> <td>36.721283</td> <td>3.120179</td> <td>581.852344</td> </tr> <tr> <th>4</th> <td>mstephens@davidson-herman.com</td> <td>14023 Rodriguez Passage\nPort Jacobville, PR 3...</td> <td>MediumAquaMarine</td> <td>33.330673</td> <td>12.795189</td> <td>37.536653</td> <td>4.446308</td> <td>599.406092</td> </tr> </tbody> </table> </div>

...
<div> <table border="1" class="dataframe"> <thead> <tr style="text-align: right;"> <th></th> <th>Avg. Session Length</th> <th>Time on App</th> <th>Time on Website</th> <th>Length of Membership</th> <th>Yearly Amount Spent</th> </tr> </thead> <tbody> <tr> <th>count</th> <td>500.000000</td> <td>500.000000</td> <td>500.000000</td> <td>500.000000</td> <td>500.000000</td> </tr> <tr> <th>mean</th> <td>33.053194</td> <td>12.052488</td> <td>37.060445</td> <td>3.533462</td> <td>499.314038</td> </tr> <tr> <th>std</th> <td>0.992563</td> <td>0.994216</td> <td>1.010489</td> <td>0.999278</td> <td>79.314782</td> </tr> <tr> <th>min</th> <td>29.532429</td> <td>8.508152</td> <td>33.913847</td> <td>0.269901</td> <td>256.670582</td> </tr> <tr> <th>25%</th> <td>32.341822</td> <td>11.388153</td> <td>36.349257</td> <td>2.930450</td> <td>445.038277</td> </tr> <tr> <th>50%</th> <td>33.082008</td> <td>11.983231</td> <td>37.069367</td> <td>3.533975</td> <td>498.887875</td> </tr> <tr> <th>75%</th> <td>33.711985</td> <td>12.753850</td> <td>37.716432</td> <td>4.126502</td> <td>549.313828</td> </tr> <tr> <th>max</th> <td>36.139662</td> <td>15.126994</td> <td>40.005182</td> <td>6.922689</td> <td>765.518462</td> </tr> </tbody> </table> </div>

...
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 500 entries, 0 to 499
Data columns (total 8 columns):
Email                   500 non-null object
Address                 500 non-null object
Avatar                  500 non-null object
Avg. Session Length     500 non-null float64
Time on App             500 non-null float64
Time on Website         500 non-null float64
Length of Membership    500 non-null float64
Yearly Amount Spent     500 non-null float64
dtypes: float64(5), object(3)
memory usage: 31.3+ KB"""



"""Exploratory Data Analysis
Use seaborn to create a jointplot to compare the Time on Website and Yearly Amount Spent columns. Does the correlation make sense?
"""



"""** Do the same but with the Time on App column instead. **"""



"""** Use jointplot to create a 2D hex bin plot comparing Time on App and Length of Membership.**"""



"""Let's explore these types of relationships across the entire data set. Use pairplot to recreate the plot below.(Don't worry about the the colors)"""



"""Based off this plot what looks to be the most correlated feature with Yearly Amount Spent?

**Create a linear model plot (using seaborn's lmplot) of Yearly Amount Spent vs. Length of Membership. **
"""



"""Training and Testing Data
** Set a variable X equal to the numerical features of the customers and a variable y equal to the "Yearly Amount Spent" column. **

** Use model_selection.train_test_split from sklearn to split the data into training and testing sets. Set test_size=0.3 and random_state=101**

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=101)
"""



"""Training the Model
Now its time to train our model on our training data!

** Import LinearRegression from sklearn.linear_model **

from sklearn.linear_model import LinearRegression
Create an instance of a LinearRegression() model named lm.

lm = LinearRegression()

"""



"""** Train/fit lm on the training data.**

lm.fit(X_train,y_train)

Print out the coefficients of the model

# The coefficients
print('Coefficients: \n', lm.coef_)
    Coefficients:
     [ 25.98154972  38.59015875   0.19040528  61.27909654]
"""



"""Predicting Test Data
Now that we have fit our model, let's evaluate its performance by predicting off the test values!

** Use lm.predict() to predict off the X_test set of the data.**

predictions = lm.predict( X_test)
"""



"""** Create a scatterplot of the real test values versus the predicted values. **"""



"""Evaluating the Model
Let's evaluate our model performance by calculating the residual sum of squares and the explained variance score (R^2).

** Calculate the Mean Absolute Error, Mean Squared Error, and the Root Mean Squared Error. Refer to the lecture or to Wikipedia for the formulas**

# calculate these metrics by hand!
from sklearn import metrics
print('MAE:', metrics.mean_absolute_error(y_test, predictions))
print('MSE:', metrics.mean_squared_error(y_test, predictions))
print('RMSE:', np.sqrt(metrics.mean_squared_error(y_test, predictions)))
    MAE: 7.22814865343
    MSE: 79.813051651
    RMSE: 8.93381506698
"""



"""Residuals
Plot a histogram of the residuals and make sure it looks normally distributed. Use either seaborn distplot, or just plt.hist().
"""



"""Conclusion
We still want to figure out the answer to the original question, do we focus our efforts on mobile app or website development? Or maybe that doesn't even really matter, and Membership Time is what is really important. Let's see if we can interpret the coefficients at all to get an idea.

** Recreate the dataframe below. **

coeffecients = pd.DataFrame(lm.coef_,X.columns)
coeffecients.columns = ['Coeffecient']
coeffecients

<div> <table border="1" class="dataframe"> <thead> <tr style="text-align: right;"> <th></th> <th>Coeffecient</th> </tr> </thead> <tbody> <tr> <th>Avg. Session Length</th> <td>25.981550</td> </tr> <tr> <th>Time on App</th> <td>38.590159</td> </tr> <tr> <th>Time on Website</th> <td>0.190405</td> </tr> <tr> <th>Length of Membership</th> <td>61.279097</td> </tr> </tbody> </table> </div>
"""



"""** How can you interpret these coefficients? **

Example:

Interpreting the coefficients:

Holding all other features fixed, a 1 unit increase in Avg. Session Length is associated with an increase of 25.98 total dollars spent.
Holding all other features fixed, a 1 unit increase in Time on App is associated with an increase of 38.59 total dollars spent.
Holding all other features fixed, a 1 unit increase in Time on Website is associated with an increase of 0.19 total dollars spent.
Holding all other features fixed, a 1 unit increase in Length of Membership is associated with an increase of 61.27 total dollars spent.
Do you think the company should focus more on their mobile app or on their website?

Answer?
"""





