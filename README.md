# Bangalore Housing Price

## Aim

Our aim in the project was to make a model which can predict housing prices in Bangalore using a dataset from Kaggle to the nearest Lakh.

## Feature Engineering

1. Convert the values in total_sqft column such as 1100-1200 or 1100 sqft to a Avg float value so we can operate on it.

2. Find the Price/sqft for each area so we can identify the outliers easily.

3. Remove the spaces from the location words.

4. Find the total dataset in each Area.

5. Find the area which are less than 10 stats and keep them all together.

6. Finding the worth of the house, say each room is only 200sqft which is not nice, makes the room too small and suffocating.

## Outlier Removal

1. Remove which have very high Price/sqft. Filter out rows which are too far from the mean (Extreme Outliers).
2. Remove those values using numpy array where its like price of 3 BHK < 2 BHK, which is unrealistic.
3. Stats where there are too many baths, 4 BHK house and 7 baths. An Outlier.

## Training Model

Training the model using train_test_split from scikit-learn library.

- **Linear Regression**:
  - RMSE: 22.209067134017875
  - R2: 0.8672560791792229

- **Random Forest Regressor**:

  - RMSE: 23.168730307640438
  - R2: 0.8464476855697785

- **Cross-Validation**:

  - CV R2 score: [0.57545834, 0.76945633, 0.66584318, 0.6368459, 0.79098429]
  - Mean R2 score: 0.6877176069800204

## Final Prediction

HSR Layout, 2000sqft, 2 bath, 3 bhk = 1.68 Cr

Hebbal, 2000sqft, 3 bath, 3 bath = 1.71 Cr

Whitefield, 1500sqft, 2 bath, 2 bhk = 1.15 Cr
