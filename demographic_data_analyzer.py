import pandas as pd

def calculate_demographic_data(print_data=True):
    df = pd.read_csv('adult.data.csv')

    race_count = df['race'].value_counts()

    average_age_men = round(df[df['sex'] == 'Male']['age'].mean(), 1)

    percentage_bachelors = round((df['education'] == 'Bachelors').mean() * 100, 1)

    higher_edu = df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])
    lower_edu = ~higher_edu

    higher_education_rich = round(
        (df[higher_edu]['salary'] == '>50K').mean() * 100, 1)

    lower_education_rich = round(
        (df[lower_edu]['salary'] == '>50K').mean() * 100, 1)

    min_work_hours = df['hours-per-week'].min()

    min_workers = df[df['hours-per-week'] == min_work_hours]

    rich_percentage = round(
        (min_workers['salary'] == '>50K').mean() * 100, 1)

    country_group = df.groupby('native-country')

    country_stats = (country_group['salary']
                 .apply(lambda x: (x == '>50K').mean()))

    highest_earning_country = country_stats.idxmax()

    highest_earning_country_percentage = round(country_stats.max() * 100, 1)  

    highest_earning_country = country_stats.idxmax()

    highest_earning_country_percentage = round(country_stats.max() * 100, 1)

    top_IN_occupation = df[
        (df['native-country'] == 'India') & (df['salary'] == '>50K')
    ]['occupation'].value_counts().idxmax()

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage': highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }