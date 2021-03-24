# <img src="./resources/GA.png" width="25" height="25" />   <span style="color:Purple">DSI Capstone:  MTB Trail Recommender Engine</span> 
---


#### Ryan McDonald- General Assembly 

---
### Problem Statement
For anyone new to mountain biking, or new to a specific trail area, the task can be daunting:

“Which trail should I ride?”

“How am I going to get back to the car?”

“Which trails will offer the best training?”

“Am I going to get hurt riding this particular trail?”

The wrong choice can set a rider up for failure, or even worse… injury.  In hopes of providing new-to-the-area riders an alternative to blind guesses, a trail recommender system has been developed to better guide riders to more enjoyable riding experiences!
This project will provide two, value-added resources to riders!

-	A rider will be able to select certain attributes they want to experience on the trail.  Adjusting distance, climbing, descent and trail difficulty will provide the user with trails to ride based on the requirements given.
-	Based on other trail users, the recommender system will provide the target user with trails to ride based on others experiences.  The user may elect to ride trails that have been ridden most in the area.

---
 
### This section is for Capstone Check-in 3

   - Specific metrics will be determined throughout week 9 of DSI Program. Recommender systems are still quite new to me.
    - The project appears to be scoped appropriately, based on feedback. However, I'm happy to take additional criticisms/ insights.
   - Does anyone care about this?!  You betcha!  One of the more challenging frustrations to riders in new areas, especially if they don’t have a local to ride with, is choosing the right trail to ride! The results of this recommender system will quickly provide the confidence riders need to be safe, and enjoy the ride.

**Timeline**

**Week 9**: Complete data retrieval.  Scrapper is still running on user data.  Unfortunately, the site I’m pulling data from has strict/long time requirements between pulls, and, since I’ve been an active user on that site since 2013, I don’t want to risk being banned!

**Week 10**: ALL data to be cleaned/formatted/and EDA completed.

   * The data is, unfortunately, a bit of a mess.  Also, the data is not retrieved in one large CSV.  IT comes in many that need to be combined.

   * Start on recommender system!

**Week 11**:  Complete recommender system (potential StreamLit app to be generated, time allowing)

   * Prepare presentation/ documentation for project submission

**Week 12**: Solicit feedback from peers prior to submission.  

   * Make any necessary last-minute updates! 

---

## Executive Summary
**Summary of methodolgy, production model**
   
   -  various attributes of discussion for model 
        
        -  other models tried...
        
        - something else
        
**streamlit/ tabluea thingy?**

![a picture](./resources/gui_pic.PNG) 
           
---
### Data Description
Data utilized for the project analysis was obtained through utilization of the OctoParse web scrapper API tool.  Data was pulled from 6 unique pages within the TrailForks webpage (the leading organization for trail and user data within the mountain biking community).

Data was collect on all, nearly 10,000, registered mountain bike trails in MA.  This project will likely be continued nationwide (an additional 80,000 trails) post-course.

User data is still being scrapped from the web. I'm only able to pull North America user data, so with over 1.5 million user 'checkins' pulled so far, I should, statistically (based on percentage of trails in MA vs North America) have several 10,000's of user checkin data.

Trail feature data along with user data collected is described, below:

**Data Dictionary created for datasets utilized in this analysis**

| Feature     | dType | Description                |
|-------------|-------|----------------------------|
| trail_URL   | str   | URL to specific trail      |
| trail       | str   | trail name                 |
| riding_area | str   | trail system               |
| distance    | int   | trail distance             |
| descent     | int   | total trail descent        |
| climb       | int   | total trail climb          |
| difficulty  | obj   | trail difficulty rating    |
| coordinates | float | trailhead GPS location     |
| popularity  | int   | trail rating (0-100)       |
| user_URL    | str   | users trail log page       |
| user_name   | str   | user name                  |
| city        | str   | user hometown              |
| trails      | str   | trails logged by user ride |
| dist        | int   | length of user ride        |
 
**(TO BE UPDATED) The following databases were utilized in analysis:**

| Database Utilized            | Features Within Database                                         |
|------------------------------|------------------------------------------------------------------|
| Pandas                       |                                                                  |
| Numpy                        |                                                                  |
| matplotlib                   | pyplot                                                           |
| pickle                       |                                                                  |
| nltk - tokenize              | sent-tokenizer, Regexp                                           |
| nltk - sentiment             | SetimentIntensityAnalyzer                                        |
| time                         |                                                                  |
| xgboost                      | XGBClassifier                                                    |
| SKLearn - Model Selection    | train_test_split, GridSearchCV, corr_val_score                   |
| SKLearn - Pipeline           | Pipeline                                                         |
| SKLearn - Naive-bayes        | MultinomialNB, BernoulliNB                                       |
| SKLearn - Linear Model       | LogisticRegression, LogisticRegressionCV                         |
| SKLearn - Feature Extraction | CountVectorizer, TfidfVectorizer                                 |
| SKLearn - Ensemble           | RandomForestClassifier, ExtraTreesClassifier, AdaBoostClassifier |
| SKLearn - Tree               | export_text, DecisionTreeClassifier, plot_tree                   |
| SKLearn - SVM                | LinearSVC                                                        |
| SKLearn - Metrics            | confusion_matrix, plot_confusion_matrix                          |
| tkinter                      | simpledialog                                                     |

---      
### Analysis - TO BE UPDATED!

1. typical numbered things
2. mroe numbered things, maybe.. who knows
  
  -  wicked interesting point
  
      ![another pic](./resources/sentiment_table.JPG)
  
  -  cough, sneeze, burp
  
      ![another pic](./resources/model_params.JPG)

   - blah blah blah
   
      ![another pic](./resources/follow_up_performance.PNG) 



3.  Additional supporting analysis is provided in the code notebook for review, as well as additional insights. Indepth and detailed processing and review are featured throughout the code notebook within markdown and code- formatted lines. 

---
### Conclusions and Recommendations- TO BE UPDATED!!!
   
  Fingers crossed there are some!