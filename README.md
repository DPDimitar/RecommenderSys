# MOVIES RECOMMENDER SYSTEM

## Setup development environment
1. Create environment (e.g. venv, conda, ...)
   - https://docs.python.org/3/library/venv.html

## Data
- You can use datasets from https://grouplens.org/datasets/movielens/
- Store them in root /

## Project structure
- \main.py
  - Entrypoint to configure and execute the system
- read.py
  - Reading Ratings
  ![img_1.png](readme_images/img_1.png)
- movies.py
  - Reading Movies
  ![img_2.png](readme_images/img_2.png)
- predictor.py
  - Random Predictor
  ![img_3.png](readme_images/img_3.png)
- recommendation.py
  - Recommendation
  ![img_4.png](readme_images/img_4.png)
- average.py
  - Average Predictor
  ![img_5.png](readme_images/img_5.png)
- viewsPredictor.py
  - Recommending the most watched movies
  ![img_6.png](readme_images/img_6.png)
- IBPredictor.py
  - Predicting scores with similarity between products
  ![img_7.png](readme_images/img_7.png)
  - Recommendation based on the currently viewed content
  ![img_8.png](readme_images/img_8.png)

## Recommendation for Yourself
![img_9.png](readme_images/img_9.png)
  

## Execution
1. Comment or uncomment the tasks in `main.py` which you choose to run
2. Execute `python main.py`