import os
import time
import numpy as np
import pandas as pd

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def clear_screen():
    '''Clearing the screen
    '''
    os.system('cls' if os.name == 'nt' else 'clear')


def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city_menu = "\t1. Chicago\n\t2. New York City\n\t3. Washington"
    while True:
        clear_screen()
        print('Hello! Let\'s explore some US bikeshare data!')
        print("\nPick a city. Enter city's number or name from items below:")
        print(city_menu)
        city_input = input("\n\tYour choice please: ")
        if city_input == "1" or city_input.lower() == "chicago":
            city = "chicago"
            break
        elif city_input == "2" or city_input.lower() == "new york city":
            city = "new york city"
            break
        elif city_input == "3" or city_input.lower() == "washington":
            city = "washington"
            break

    # get user input for month (all, january, february, ... , june)
    month_menu = "\n\t1. All\n\t2. January\n\t3. February\n\t4. March\n\t5. April\n\t6. May\n\t7. June"
    while True:
        clear_screen()
        print("\nPick a month. Enter month's number or name from items below:")
        print(month_menu)
        month_input = input("\n\tYour choice please: ")
        if month_input == "1" or month_input.lower() == "all":
            month = 'all'
            break
        elif month_input == "2" or month_input.lower() == "january":
            month = 'january'
            break
        elif month_input == "3" or month_input.lower() == "february":
            month = 'february'
            break
        elif month_input == "4" or month_input.lower() == "march":
            month = 'march'
            break
        elif month_input == "5" or month_input.lower() == "april":
            month = 'april'
            break
        elif month_input == "6" or month_input.lower() == "may":
            month = 'may'
            break
        elif month_input == "7" or month_input.lower() == "june":
            month = 'june'
            break

    # get user input for day of week (all, monday, tuesday, ... sunday)
    day_menu = "\n\t1. All\n\t2. Sunday\n\t3. Monday\n\t4. Tuesday\n\t5. Wednesday\n\t6. Thursday\n\t7. Friday\n\t8. Saturday"
    while True:
        clear_screen()
        print("\nPick a day. Enter day's number or name form items below:")
        print(day_menu)
        day_input = input("\n\tYour choice please: ")
        if day_input == "1" or day_input.lower() == "all":
            day = 'all'
            break
        if day_input == "2" or day_input.lower() == "sunday":
            day = 'sunday'
            break
        if day_input == "3" or day_input.lower() == "monday":
            day = 'monday'
            break
        if day_input == "4" or day_input.lower() == "tuesday":
            day = 'tuesday'
            break
        if day_input == "5" or day_input.lower() == "wednesday":
            day = 'wednesday'
            break
        if day_input == "6" or day_input.lower() == "thursday":
            day = 'thursday'
            break
        if day_input == "7" or day_input.lower() == "friday":
            day = 'friday'
            break
        if day_input == "8" or day_input.lower() == "saturday":
            day = 'saturday'
            break
    print('-'*40)
    return city, month, day


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
    clear_screen()
    df = pd.read_csv(CITY_DATA[city])
    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

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
    clear_screen()
    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    months = ['january', 'february', 'march', 'april', 'may', 'june']
    popular_month = df['month'].mode()[0]
    print('Most common month:', months[popular_month - 1].title())

    # display the most common day of week
    popular_day = df['day_of_week'].mode()[0]
    print('Most common day of the week:', popular_day)

    # extract hour from the Start Time column to create an hour column
    df['hour'] = df['Start Time'].dt.hour

    # display the most common start hour
    popular_hour = df['hour'].mode()[0]
    print('Most Popular Start Hour:', popular_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    popular_start_station = df['Start Station'].mode()[0]
    print('Most commonly used start station:', popular_start_station)

    # display most commonly used end station
    popular_end_station = df['End Station'].mode()[0]
    print('Most commonly used end station:', popular_end_station)

    # display most frequent combination of start station and end station trip
    df['Trip'] = 'From "' + df['Start Station'] + '" to "' + df['End Station'] + '"'
    popular_trip = df['Trip'].mode()[0]
    print('Most frequent combination of start station and end station trip is:\n\t', popular_trip)


    print("\n\t\tThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print('Total travel time:', total_travel_time)

    # display mean travel time
    average_travel_time = df['Trip Duration'].mean()
    print('Average travel time:', average_travel_time)

    print("\n\t\tThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    user_types = df['User Type'].value_counts()
    print("Type of users:")
    print (user_types.to_string())

    # Display counts of gender
    try:
        user_gender = df['Gender'].value_counts()
        print("\n\nGender of users:")
        print (user_gender.to_string())
    except:
        print("\n\nGender data not available!")

    # Display earliest, most recent, and most common year of birth
    try:
        earliest_birth_year = df['Birth Year'].min()
        recent_birth_year = df['Birth Year'].max()
        common_birth_year = df['Birth Year'].mode()[0]
        print("\n\nEarliest year of birth: ", int(earliest_birth_year))
        print("Most recent year of birth: ", int(recent_birth_year))
        print("Most common year of birth: ", int(common_birth_year))
    except:
        print("\n\nYear of birth not available!")

    print("\n\t\tThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        print("City: {}, Month: {}, Day: {}".format(city.title(), month.title(), day.title()))
        raw_data_view = input('\n\nWould you like to view row data? Enter yes or no: ')
        if raw_data_view.lower() == 'yes':
            print('Print out of the first five records:')
            df = df.head()
            lst = df.to_dict('records')
            for item in lst:
                print('\nStart Time: ', item['Start Time'])
                print('End Time: ', item['End Time'])
                print('Trip Duration: ', item['Trip Duration'])
                print('Start Station: ', item['Start Station'])
                print('End Station: ', item['End Station'])
                print('User Type: ', item['User Type'])
                print()
        restart = input('\n\nWould you like to restart? Enter yes or no: ')
        if restart.lower() != 'yes':
            break

if __name__ == "__main__":
    main()