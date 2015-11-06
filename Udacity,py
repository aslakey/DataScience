import pandas
import pandasql


def num_rainy_days(filename):
    '''
    Function returning various sql statements regarding this weather data:
    https://www.dropbox.com/s/7sf0yqc9ykpq3w8/weather_underground.csv
    '''
    weather_data = pandas.read_csv(filename)
    
    rain_count = """
    SELECT count(rain) FROM weather_data WHERE rain = 1;
    """
    maxTemp_fog = """
    SELECT fog, max(maxtempi) FROM weather_data WHERE fog = 0
    UNION
    SELECT fog, max(maxtempi) FROM weather_data WHERE fog = 1;
    """
    meanTemp_weekend = """
    select avg(cast (meantempi as integer)) from weather_data
    where cast (strftime('%w', date) as integer) in (0, 6);
    """
    avgMinTemp_rain = """
    select avg(mintempi) from weather_data where rain = 1 and mintempi > 55;
    """
    
    #Execute one of the SQL command against the pandas frame
    rainy_count = pandasql.sqldf(q1.lower(), locals())
    return rainy_count
