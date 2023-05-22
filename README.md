
# The BCG Data Science &amp; Advanced Analytics Virtual Experience Program


BCG GAMMA is transforming the businesses of today through data science and advanced analytics initiatives and the company's goal is to help companies generate competitive advantage through these initiatives. .

## Tasks

## 1: Business Understanding & Problem Framing

**Background information on task 1**

PowerCo is a major gas and electricity utility that supplies to corporate, SME (Small & Medium Enterprise), and residential customers. The power-liberalization of the energy market in Europe has led to significant customer churn, especially in the SME segment. They have partnered with BCG to help diagnose the source of churning SME customers.

One of the hypotheses under consideration is that churn is driven by the customers’ price sensitivities and that it is possible to predict customers likely to churn using a predictive model. The client also wants to try a discounting strategy, with the head of the SME division suggesting that offering customers at high propensity to churn a 20% discount might be effective.

The Lead Data Scientist (LDS) held an initial team meeting to discuss various hypotheses, including churn due to price sensitivity. After discussion with your team, you have been asked to go deeper on the hypothesis that the churn is driven by the customers’ price sensitivities. 

Your LDS wants an email with your thoughts on how the team should go about to test this hypothesis.


**Objectives:**

The first task is to understand what is going on at the client and think about how you would approach a problem like this to test this specific hypothesis.

Formulate the hypothesis as a data science problem and lay out the major steps needed to test this hypothesis. Communicate your thoughts and findings in an email to your LDS, focusing on the potential data that would be needed from the client and analytical models you would use to test such a hypothesis.

---

## 2: Exploratory Data Analysis & Data Cleaning
Understanding business through data

**Background information on task 2**

The BCG project team thinks that building a churn model to understand whether price sensitivity is the largest driver of churn has potential. The client has sent over some data and the LDS wants you to perform some exploratory data analysis and data cleaning.

The data that was sent over includes:

* Historical customer data: Customer data such as usage, sign up date, forecasted usage etc
* Historical pricing data: variable and fixed pricing data etc
* Churn indicator: whether each customer has churned or not

These datasets are otherwise identical and have historical price data and customer data (including churn status for the customers in the training data).


**Objectives:**

* **Sub-Task 1:** Clean the data – you might have to address missing values, duplicates, data type conversions, transformations, and multicolinearity, as well as outliers.

* **Sub-Task 2:** Perform some exploratory data analysis. Look into the data types, data statistics, and identify any missing data or null values, and how often they appear in the data. Visualize specific parameters as well as variable distributions.

---

## 3: Feature Engineering
Uncovering signals with data

The team now has a good understanding of the data and feels confident to use the data to further understand the business problem. The team now needs to brainstorm and build out features to uncover signals in the data that could inform the churn model.

Feature engineering is one of the keys to unlocking predictive insight through mathematical modeling. Based on the data that is available and was cleaned, identify what you think could be drivers of churn for our client and build those features to later use in your model.

**Objectives:**

We’ve included some pre-written functions to help you focus on your analysis as opposed to programming syntax.

* **Sub-task 1:** Think through what key drivers of churn could be for our client

* **Sub-task 2:** Build the features in order to get ready to model

---

## 4: Modeling & Evaluation
Modeling the problem and evaluating the model

**Background information on task 4**

Recall that one of the hypotheses under consideration is that churn is driven by the customers’ price sensitivities and that it would be possible to predict customers likely to churn using a predictive model.

The client also wants to try a discounting strategy, with the head of the SME division suggesting that offering customers at high propensity to churn a 20% discount might be effective.

Build your models and test them while keeping in mind you would need data to prove/disprove the hypotheses, as well as to test the effect of a 20% discount on customers at high propensity to churn.

**Objectives:**

* <b>Sub-Task 1:</b> Build churn model(s) to try to predict the churn probability of any customer, taking into account all the explanatory variables you have constructed in the feature engineering process.

* <b>Sub-Task 2:</b> Evaluate your model, using a holdout set, and with metrics of your choosing. Be sure to pick a metric that would make sense for this business case.

* <b>Sub-Task 3:</b> Interpret the results and use them to formulate your answers to the client’s hypotheses and questions. You will be asked to form these answers into coherent thoughts and recommendations in the next module.