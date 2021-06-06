<<<<<<< HEAD
#Title: Analyse bike share data in cities
||||||| cdb7100
import os,time
=======
#Description: Bikeshare project used for course
import os,time
>>>>>>> refactoring
import pandas as pd
import numpy as np

# First we copy the directory where we store all the data
#path_data = r"C:\DATA_SCIENCE_Course\Git\pdsnd_github\"
# Change directory to the path_data
os.chdir(path_data)


CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

MONTH_DATA = ['january','february','march','april','may','june','all']

DAY_DATA = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday','all']

##################################################################################################
def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')

    city = 'rabbit'
    while city not in CITY_DATA.keys():
        print("\n Please choose a city you would like to explore:")
        print("\n1. Chicago 2. New York City 3. Washington")
        print("\nAccepted input:\nFull name of city; not case sensitive (e.g. chicago or CHICAGO).\nFull name in title case (e.g. Chicago).")

        city = input().lower()
        if city not in CITY_DATA.keys():
            print("\nPlease check your input, it doesn\'t appear to be conforming to any of the accepted input formats.")
            print("\nRestarting...")
    print(f"\nYou have chosen {city.title()} as your city.")

    month = 'rabbit'
    while month not in MONTH_DATA:
        print("\nPlease enter the month, between January to June, for which you're seeking the data:")
        print("\nAccepted input:\nFull month name; not case sensitive (e.g. january or JANUARY).\nFull month name in title case (e.g. April).")
        print("\n(You may also opt to view data for all months, please type 'all' or 'All' or 'ALL' for that.)")
        month = input().lower()
        if month not in MONTH_DATA:
            print("\nInvalid input. Please try again in the accepted input format.")
            print("\nRestarting...")
    print(f"\nYou have chosen {month.title()} as your month.")


    day = 'rabbit'
    while day not in DAY_DATA:
        print("\nPlease enter a day in the week of your choice for which you're seeking the data:")
        print("\nAccepted input:\nDay name; not case sensitive (e.g. monday or MONDAY).\nDay name in title case (e.g. Monday).")
        print("\n(You can also put 'all' or 'All' to view data for all days in a week.)")
        day = input().lower()
        if day not in DAY_DATA:
            print("\nInvalid input. Please try again in one of the accepted input formats.")
            print("\nRestarting...")
    print(f"\nYou have chosen {day.title()} as your day.")

    print(f"\nYou have chosen to view data for city: {city.upper()}, month/s: {month.upper()} and day/s: {day.upper()}.")
    print('-'*80)
    #Returning the city, month and day selections
    return city, month, day
###########################################################################
def load_data(city, month, day):
    """Load data for the specified filters of city(ies), month(s) and
          day(s) whenever applicable.
       Args:
           (str) city - name of the city(ies) to analyze
           (str) month - name of the month(s) to filter
           (str) day - name of the day(s) of week to filter
       Returns:
           df - Pandas DataFrame containing filtered data
    """
    # load the csv
    which_csv = CITY_DATA.get(city)
    df = pd.read_csv(which_csv)
    # The current Start Time format is not recognisable for python
    # we need to convert the Start Time column to datetime format so we could extract the month and day
    # we convert the Start Time column to datetime format and add it as a new column 'datetime' to df
    df['datetime'] = pd.to_datetime(df['Start Time'])
    # extract the month and add it as a new column 'MONTH'
    df['MONTH'] = df['datetime'].dt.month
    # extract the day and add it as a new column 'DAY'
    df['DAY'] = df['datetime'].dt.day_name() # NOTE: if your pandas package is <=0.22 you should use dt.weekday_name
    df['HOUR'] = df['datetime'].dt.hour                                     #      my pandas package is >0.22 so I am using dt.day_name()

    # filter by month
    if month.lower() =='all':
        df_month =df
    elif month.lower() != 'all':
        month_num = MONTH_DATA.index(month.lower())+1
        df_month = df.loc[df['MONTH']==month_num]

    # filter by day
    if day.lower() =='all':
        df_month_day = df_month
    elif day.lower() != 'all':
        df_month_day = df_month.loc[df_month['DAY']==day.lower().title()]

    return (df_month_day)
##################################################################
def time_stats(df):
    """Display statistics on the most frequent times of travel."""

    # If we want to know how long it takes to run this function
    # we will first record the time we start run this code
    code_start_time = time.time() # This line gives us the current time
    # We use .mode() to get the most frequent observation from a column
    # However, after df['MONTH'].mode(), it returns a one value dataframe
    # But we only want the value not a dataframe.
    # we could use df['MONTH'].mode()[0] to get the value
    # or we can use what I usually use : df['MONTH'].mode().T.squeeze()
    common_month = df['MONTH'].mode()[0]
    print("The most common month from the given filtered data is: " + MONTH_DATA[common_month-1].title())
    # TO DO: display the most common day of week
    common_day_of_week = df['DAY'].mode()[0]
    print("The most common day of week from the given filtered data is: " + common_day_of_week)
    # TO DO: display the most common start hour
    common_start_hour = df['HOUR'].mode()[0]
    print("The most common start hour from the given filtered data is: " + str(common_start_hour))
    cost_time = round((time.time() - code_start_time),1)
    print("\nThis took %s seconds." % cost_time) # calculate the time used
    print('-'*60) # print - 60 times. so we get a dash line


#########################################################################################################################
def station_stats(df):
    """Display statistics on the most popular stations and trip."""
    print('\nCalculating The Most Popular Stations and Trip...\n')
    code_start_time = time.time()
    # TO DO: display most commonly used start station
    common_start_station = df['Start Station'].mode()[0]
    print("The most commonly used start station from the given fitered data is: " + common_start_station)
    # TO DO: display most commonly used end station
    common_end_station = df['End Station'].mode()[0]
    print("The most commonly used end station from the given filtered data is: " + common_end_station)
    # TO DO: display most frequent combination of start station and end station trip
    # We need to combine the two column 'Start Station' and 'End Station' together
    df_stations = df['Start Station'] + "->" + df['End Station'] # we can replace '->' with anything e.g.'rabbit'
                                                                 # only remember to later split it according to the same thing
    frequent_combination = df_stations.mode()[0]
    print("The most frequent combination of start station and end station trip is : " + str(frequent_combination.split("->")))
    cost_time = round((time.time() - code_start_time),1)
    print("\nThis took %s seconds." % cost_time)
    print('-'*40)

########################################################################
def trip_duration_stats(df):
    """Display statistics on the total and average trip duration."""
    print('\nCalculating Trip Duration...\n')
    code_start_time = time.time()
    # TO DO: display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print("The total travel time from the given filtered data is: " + str(total_travel_time))
    # TO DO: display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print("The mean travel time from the given filtered data is: " + str(mean_travel_time))
    cost_time = round((time.time() - code_start_time),1)
    print("\nThis took %s seconds." % cost_time)
    print('-'*40)
##########################################################################
def user_stats(df, city):
    """Display statistics on bikeshare users."""
    print('\nCalculating User Stats...\n')
    code_start_time = time.time()
    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts() # .value_counts() -> counts unique values in the df['User Type']
    print("The count of user types from the given filtered data is: \n" + str(user_types))
    if city == 'chicago' or city == 'new york city':
        # TO DO: Display counts of gender
        gender = df['Gender'].value_counts()
        print("The count of user gender from the given filtered data is: \n" + str(gender))
        # TO DO: Display earliest, most recent, and most common year of birth
        earliest_birth = df['Birth Year'].min()
        most_recent_birth = df['Birth Year'].max()
        most_common_birth = df['Birth Year'].mode()[0]
        print('Earliest birth from the given filtered data is: {}\n'.format(earliest_birth))
        print('Most recent birth from the given filtered data is: {}\n'.format(most_recent_birth))
        print('Most common birth from the given filtered data is: {}\n'.format(most_common_birth) )
    cost_time = round((time.time() - code_start_time),1)
    print("\nThis took %s seconds." % cost_time)
    print('-'*40)
#########################################################################
def display_raw_data(df):
    """Display 5 line of sorted raw data each time."""
    print(df.head())
    next = 0
    while True: # while true mean loop forever. The while statement takes an expression
                 # and executes the loop body while the expression evaluates to (boolean) "true".
        view_raw_data = input('\nWould you like to view next five row of raw data? Enter yes or no.\n')
        if view_raw_data.lower() != 'yes':
            return # loop from beginning, which is : while true:
        else:
            next = next + 5
            pd.set_option('display.max_columns',10) # only want to display 5 columns
            print(df.iloc[next:next+5])


#########################################################################
##### Finally, we define main which will call all the functions listed above ######
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df, city)
        while True:
            view_raw_data = input('\nWould you like to view first five row of raw data? Enter yes or no.\n')
            if view_raw_data.lower() != 'yes':
                break # if the above statement is true then break, if it is not true do below
            display_raw_data(df)
            break

        restart =''
        while restart not in ['yes','no']:
            print("\nWould you like to restart? Enter yes or no.\n")
            print("\nAccepted input:\n yes or no ; not case sensitive (e.g. Yes or yes).")

            restart = input().lower()
            if restart not in ['yes','no']:
                print('\nInvalid input. \nPlease check your input, it doesn\'t appear to be conforming to any of the accepted input formats."')

        if restart =='no':
            break



#############################################################
# Try to run main
main()
