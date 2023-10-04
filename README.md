
# Terror Attack Prediction

Predicting if the Attack predicted is major or minor

Note: 'terror_data_final' dataset contain vast amount of misspell 




## Description



- prediction system: Function to check whether the model is working 

- prediction_features: Excel file to take input for models

-  Project_Terror: ipynb(Jupter) file of project

- Project_Terror_Attack: Information regarding project

- terror_data_final: original dataset

- trained_model: saved model for deployment

- Handel_spells: ipynb(Jupter) file of dataset cleaning

- clean_terror_data_final: Corrected version of dataset

- app.py: deployment file


## Roadmap

1. Use 'Handel_spells' file to create dataset without misspell

2. Load 'Project_Terror' file in jupyter or colab & use 'clean_terror_data_final' dataset

3. Save model for deploymment part 'trained_model.pkl', We have used catboost for model deploymment

4. Use 'prediction system' to check if model is working properly 


## Deployment

To deploy this project open anaconda prompt 

paste your project directory
```bash
  cd your project directory
```
run 
```bash
  streamlit run app.py
```

