import pandas as pd

def demographic_data_analyzer():
    # read the file.
    df = pd.read_csv('adult.csv')
    
    # number of people of each race in the dataset.
    race_count= df['race'].value_counts()
    
    # average age of men.
    average_age_men= round(df[df['gender']=='Male']['age'].mean(), 1)

    # the percentage of people who have a Bachelor's degree?
    percentage_bachelors=round((len(df[df['education']=='Bachelors'])/len(df))*100, 1)

    
    #percentage of people with advanced education (Bachelors, Masters, or Doctorate) make more than 50K.
    advanced_education = ['Bachelors', 'Masters', 'Doctorate']
    df_advanced_education=df[df['education'].isin(advanced_education)]
    rich_advanced_education= df_advanced_education[df_advanced_education['income']=='>50K']
    higher_education_rich_percentage= round(len(rich_advanced_education)/len(df_advanced_education)*100, 1)
    
    # percentage of people without advanced education make more than 50K.
    without_advanced_edu = df[~df['education'].isin(advanced_education)]
    rich_without_advanced_edu=without_advanced_edu[without_advanced_edu['income']=='>50K']
    non_higher_education_rich_percentage= round(len(rich_without_advanced_edu)/len(without_advanced_edu)*100, 1)

    # the minimum number of hours a person works per week
    min_hrs_per_week= df['hours-per-week'].min()

    # percentage of the people who work the minimum number of hours per week have a salary of more than 50K.
    min_worker= df[df['hours-per-week']==min_hrs_per_week]
    rich_min_worker= min_worker['income']=='>50K'
    rich_min_worker_percentage=round(rich_min_worker.sum()/len(min_worker)*100, 1)

    # The country which has the highest percentage of people that earn >50K and the percentage
    
    country_count=df[df['income']=='>50K']['native-country'].value_counts()/df['native-country'].value_counts()*100
    highest_earning_country=country_count.idxmax()
    highest_earning_country_percentage= round(country_count.max(), 1)

    # the most popular occupation for those who earn >50K in India.
    top_India_high_income_occupation=df[(df['native-country']== 'India')&(df['income']=='>50K')]['occupation'].mode()[0]

    return {
    "Race Count": race_count,
    "Average Age of Men": average_age_men,
    "Percentage with Bachelors": percentage_bachelors,
    "Higher Ed Rich %": higher_education_rich_percentage,
    "Non-Higher Ed Rich %": non_higher_education_rich_percentage,
    "Min Hours per Week": min_hrs_per_week,
    "Rich % Among Min Workers": rich_min_worker_percentage,
    "Highest Earning Country": highest_earning_country,
    "Highest Earning Country %": highest_earning_country_percentage,
    "Top India High Income Occupation": top_India_high_income_occupation
}
