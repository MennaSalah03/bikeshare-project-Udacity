##used outside sources to find suitable and easier ways to do some things
##used sources:stackoverflow,tutorials point,the panda documentation site,geeks for geeks,datacarpentry

import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv','new york city': 'new_york_city.csv','washington': 'washington.csv' }

###################################################
def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter

    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    """

    sp_day='';sp_month=''

    while(1):
        city= input("enter the name of the city you want from chicago, new york city or washington").lower()

        if city not in CITY_DATA.keys():
            print("no matches, please try again")
        else:break

    print(city)
    print("you chose {}".format(city))

    fltr = input("would you like to filter data by month, day, both or overall statistics?").lower() #filteration of data
    while fltr not in ["month","day","both","overall statistics"]:
            fltr = input("try again please.the input you sent wasn't recognizable").lower()


    #############################################
    months={"january":1,"february":2,"march":3,"april":4,"may":5,"june":6,"july":7,"august":8,"september":9,"october":10,"november":11,"december":12}
    days = {"monday":0,"tuesday":1,"wednesday":2,"thursday":3,"friday":4,"saturday":5,"sunday":6}
    #############################################

    if fltr=="month":
        while 1:
            sp_month =input("please enter the month you want").lower() #user chooses a specific month
            if sp_month not in months.keys():
                print("try again")

            else:break


    elif fltr=="day":
        while 1:
            sp_day=input("please enter the day of the week you want").lower() #user chooses a specific day
            if sp_day not in days.keys():
                print("please try again")
            else:break


    elif fltr=="both":
        while 1:
            sp_day =input("please enter the day of the week you want").lower() #user chooses a specific day
            if sp_day not in days.keys():
                print("please try again")
            else:break
        while 1:
            sp_month =input("please enter the month you want").lower() #user chooses a specific month
            if sp_month not in months.keys():
                print("please try again")
            else:break

    print('-'*40)
    return city, sp_month, sp_day




def load_data(city, sp_month, sp_day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "" to apply no month filter
        (str) day - name of the day of week to filter by, or "" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    #######################
    months={"january":1,"february":2,"march":3,"april":4,"may":5,"june":6,"july":7,"august":8,"september":9,"october":10,"november":11,"december":12}
    days = {"monday":0,"tuesday":1,"wednesday":2,"thursday":3,"friday":4,"saturday":5,"sunday":6}
    ########################
    df = pd.read_csv(CITY_DATA[city])
    ########################

        ######################################3
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df["month"]=df["Start Time"].dt.month
    df["day"]=df["Start Time"].dt.dayofweek


       ###########################
    if not(sp_month or sp_day):
        print("overall statistics coming your way :)...")
        print(df)
    elif (sp_month and sp_day):
        print("statistics filtered by both months and days coming your way:)...")

        df_dayandmonth=df[(df['month']==months[sp_month]) & (df['day']==days[sp_day])]
        df_y=df_dayandmonth
        print("data filtered by month and say coming your way :)...")

    elif sp_day:
        df_day=df.loc[(df["day"]==days[sp_day])]
        df_y=df_day
        print("statistics filtered by days coming your way:)....")
    else:
        df_month=df.loc[(df["month"]==months[sp_month])]
        df_y=df_month
        print("statistics filtered by month coming your way:)...")
        ###################################
    while 1:
        next_rows = input("do you want to view the next 5 rows of data? [yes-no]").lower()

        if (next_rows=='yes') and not(df.empty):
            print('next 5 columns of code coming your way')
            print(df_y.head(5))
            df_y = df_y.drop(df_y.index[0:5])

        elif (next_rows=='no') or (df.empty):
            print("that's all for the filtered data")
            break



    return df

#############################################################################################################
#NESTED FUNCTION HERE
def diplay_data_by_row(df_y):
    """
        displays filtered data a few columns (5) a time on user demand
    """

#######################################################################################
def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    df["month"]=df["Start Time"].dt.month
    common_month=df["month"].mode()[0]
    print("the most common month is{}".format(common_month))


    # TO DO: display the most common day of week
    df["day of week"]=df["Start Time"].dt.dayofweek
    common_day=df["day of week"].mode()[0]
    print("the most common day is{}".format(common_day))

    # TO DO: display the most common start hour
    df["hour"]=df["Start Time"].dt.hour
    common_hour=df["hour"].mode()[0]
    print("the most common hour is{}".format(common_hour))
    #########################################


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


################################################################################################################
def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    start_station_mode=df["Start Station"].mode()[0]
    print("the most common starting station is {}".format(start_station_mode))

    # TO DO: display most commonly used end station
    end_station_mode=df["End Station"].mode()[0]
    print("the most common ending station is {} ".format(end_station_mode))


    # TO DO: display most frequent combination of start station and end station trip
    df["Route"]=df["Start Station"]+df["End Station"]
    route_mode=df["Route"].mode()[0]
    print("the most common route is {}".format(route_mode))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    travel_time=df["Trip Duration"].sum()
    print("total time of trips is {}".format(travel_time))

    # TO DO: display mean travel time
    av_travel_time=df["Trip Duration"].mean()
    print("average time to travel was {}".format(av_travel_time))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    while 1 :
        Q=input("do you want to know individual statistics? [yes-no]").lower()
        if Q=="yes":
            print("user statistics coming your way")
            break
        elif Q=="no":
            print("ok then :)")
            break
        else:
            print("didn't recognize that please answer with yes or no")






    # TO DO: Display counts of user types
    count_usertype=df['User Type'].value_counts() #counts the amount of subscribers and non-subscribers
    print("the user type data: {}".format(count_usertype))

    # TO DO: Display counts of gender
    try:
        count_usergend=df['Gender'].value_counts() #counts the amount of males and females
        print("data for gender of users: {}".format(count_usergend))
    except:
        print("we're sorry. there's no avilable data for user gender")
    try:
        earliest_YOB=df['Birth Year'].min() #value of earliest date of birth
        recent_YOB=df['Birth Year'].max() #value of most recent day pf birth
        common_YOB=df['Birth Year'].mode()[0] #value of the most common year of birth
        print("earliest year of birth:{}","most recent birth year {}","most common birth year{}".format(earliest_YOB,recent_YOB,common_YOB),sep='\n')
    except:
        print("sorry. No data for Birth year, too")


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, sp_month, sp_day = get_filters()
        df = load_data(city, sp_month, sp_day)
        months={"january":1,"february":2,"march":3,"april":4,"may":5,"june":6,"july":7,"august":8,"september":9,"october":10,"november":11,"december":12}
        days = {"monday":0,"tuesday":1,"wednesday":2,"thursday":3,"friday":4,"saturday":5,"sunday":6}
        print(months, days,sep='\n')

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\n all the data you wanted was shown Would you like to restart? Enter yes if you want to restart.\n')
        if restart.lower() != 'yes':
            break



if __name__ == "__main__":
	main()
