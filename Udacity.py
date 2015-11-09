import pandas
import pandasql
import csv


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
def fix_turnstile_data(filenames):
    '''
    Filenames is a list of MTA Subway turnstile text files. A link to an example
    MTA Subway turnstile text file can be seen at the URL below:
    http://web.mta.info/developers/data/nyct/turnstile/turnstile_110507.txt
    In addition, here is a CSV reader/writer introductory tutorial:
    http://goo.gl/HBbvyy
    You can see a sample of the turnstile text file that's passed into this function
    and the the corresponding updated file in the links below:
    Sample input file:
    https://www.dropbox.com/s/mpin5zv4hgrx244/turnstile_110528.txt
    Sample updated file:
    https://www.dropbox.com/s/074xbgio4c39b7h/solution_turnstile_110528.txt
    '''
    for name in filenames:
        f_in = open(name,'r')
        f_out = open("updated_"+name, 'w')

        reader_in = csv.reader(f_in, delimiter=",")
        writer_out = csv.writer(f_out,delimiter=",")
        
        # your code here
        for line in reader_in:
            first_el=line[0]
            second_el=line[1]
            third_el=line[2]
            for element in range(0,len(line)):
                if (element-2)%5==0:
                    new_line = [first_el,second_el,third_el,line[element-4],line[element-3],line[element-2],line[element-1],line[element]]
                    writer_out.writerow(new_line)
