import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    
    print("WELCOME TO THE BIKESHARE DATA SCIENCE PROJECT")
    print("Valid names for city are chicago , new york city and washington" )
    print("Valid names for month are all, january, february, ... , june" )
    print("Valid names for day are all, monday, tuesday, ... sunday" )
    
    valid_cities = ['chicago' , 'new york city', 'washington']
    valid_months = ['all','january','febuary','march','april','may','june']
    valid_days = ['all','monday','tuesday','wednesday','thursday','friday','saturday','sunday']
    
    city = ""
    month = ""
    day = ""
    success = False
    
    while success == False:
        city = input("What is the name of the city ?")
        month = input("What is the name of the month ?")
        day = input("What is the day of the week ?")
        
        if city.lower() in valid_cities and month.lower() in valid_months and day.lower() in valid_days:
            success = True
        else:
            print("XXX--*   ERROR!!!  *--XXX")
            print("XXX--*YOUR INPUTS ARE INCORRECT*--XXX")
            print("***PLEASE READ THE INSTRUCTIONS ABOVE***")
        
    
    print('Hello! Let\'s explore some US bikeshare data!')
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    print(city)

    # get user input for month (all, january, february, ... , june)
    print(month)

    # get user input for day of week (all, monday, tuesday, ... sunday)
    print(day)

    print('-'*40)
    return city.lower(), month.lower(), day.lower()


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()
    
    # extract hour from the Start Time column to create an hour column
    df['hour'] = df['Start Time'].dt.hour

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    print(df["month"].mode()[0])

    # display the most common day of week
    print(df["day_of_week"].value_counts().idxmax())

    # display the most common start hour
    print(df["hour"].mode()[0])
    


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    print(df['Start Station'].value_counts().idxmax())


    # display most commonly used end station
    df['End Station'].value_counts().idxmax()


    # display most frequent combination of start station and end station trip


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    print(df["Trip Duration"].sum())


    # display mean travel time
    print(df["Trip Duration"].mean())

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    user_types = df['User Type'].value_counts()
    print(user_types)


    # Display counts of gender
    try:
        gender = df['Gender'].value_counts()
        print(gender)
    except KeyError:
        print("Error : Column [Gender] Does not exist in this Dataframe")


    # Display earliest, most recent, and most common year of birth
    try:
        print(df["Birth Year"].min())
        print(df["Birth Year"].max())
        print(df["Birth Year"].mode()[0])
    except KeyError:
        print("Error : Column [Birth Year] Does not exist in this Dataframe")
    
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
