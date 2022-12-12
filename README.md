# british-airways-intern-project  
Analyzing Customer Feedback - Internship Project in British Airways

---
**Project status** = Done  
**Final Presentation** [Presentation in pptx](https://github.com/IchfanKurniawan/british-airways-intern-project/tree/main/presentation)  
**Source of dataset** https://www.airlinequality.com/airline-reviews/british-airways/  

### Project Context  
British Airways (BA) is the flag carrier airline of the United Kingdom (UK). Every day, thousands of BA flights arrive to and depart from the UK, carrying customers across the world. Whether it’s for holidays, work or any other reason, the end-to-end process of scheduling, planning, boarding, fuelling, transporting, landing, and continuously running flights on time, efficiently and with top-class customer service is a huge task with many highly important responsibilities.  

As a data scientist at BA, it will be your job to apply your analytical skills to influence real life multi-million-pound decisions from day one, making a tangible impact on the business as your recommendations, tools and models drive key business decisions, reduce costs and increase revenue.  

Customers who book a flight with BA will experience many interaction points with the BA brand. Understanding a customer's feelings, needs, and feedback is crucial for any business, including BA.  

### Project Requirement  
1. Scraping and collecting customer feedback and reviewing data from a third-party source   
2. Cleaning the collected dataset  
3. Analysing this data to present any insights, through:
    - Descriptive statistic
    - Topic Modeling
    - Sentiment Analysis
4. Presenting the findings

### Project Planning
1. Scraping & collecting customer feedback data has already done in `scrape_script.py` inside `code` folder
2. Exploratory Data Analysis
    - Data Structure
    - Data Quality
    - Content
3. Data Cleaning
4. Feature Engineering
5. Modeling  


### Dataset Column  
The full dataset is inside `dataset` folder.  


The columns are:  
`id`, `review`, `rating`, `header`, `sub_header`, `author`, `time_published`, `aircraft`, `type_of_traveller`, `seat_type`, `route`, `date_flown`, `seat_comfort`, `cabin_staff_service`, `food_&_beverages`, `ground_service`, `value_for_money`, `recommended`, `inflight_entertainment`, `wifi_&_connectivity`, `verified`, `rating_only`, `city`, `type_aircraft`
