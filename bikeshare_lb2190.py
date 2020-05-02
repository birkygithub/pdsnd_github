# File:: Bikeshare_lb2190.py
#  Program for Data Science with Python  - 2nd Project - Bikeshare data
#  Lisa Birkenberger  lb2190@att.com
#  4/18/2020
#
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
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    #while loop to get city name and handle exceptions or incorrect string entry
    while True:
        try:
            city_input = input("Enter city to explore data from: Chicago, New York City, Washington> ")
            if city_input.lower() in ['chicago','new york city','washington']:
                break  # correct city was inputted
            else:    # incorrect string entry
                 print("Input didn't match the city name expected.  Please try again.")
        
        except KeyboardInterrupt:  # CTRL-c or other interrupt to stop app
            city_input = 'exit'  # setup up some keyword to return and indicate stop app
            print('KeyboardInterrupt exception')
            break
        except:      # exception occurred with input
            print("   Error occurred with city input.  Please try again.")
            
        # Outside try/except block, go back to get city_input, as While is True
    # Outside while block for city name
    
    # TO DO: get user input for month (all, january, february, ... , june)
    #while loop to get month and handle exceptions or incorrect string entry
    while True and city_input != 'exit':
        try:
            month_input = input("Enter month in 2017 to use: January, February, March, April, May, June OR All>  ")
            if month_input.lower() in ['january', 'february', 'march', 'april', 'may', 'june', 'all']:
                break  # correct month was inputted
            else:    # incorrect string entry
                 print("Input didn't match the month expected.  Please try again.")
                    
        except KeyboardInterrupt:  # CTRL-c or other interrupt to stop app
            city_input = 'exit'  # setup up some keyword to return and indicate stop app
            print('KeyboardInterrupt exception')
            break
        except:      # exception occurred with input
            print("  Error occurred with month input.  Please try again.")
            
        # Outside try/except block, go back to get month_input, as While is True
    # Outside while block for month name

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    #while loop to get month and handle exceptions or incorrect string entry
    while True and city_input != 'exit':
        try:
            day_input = input("Select a day of the week: Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday OR All>  ")
            if day_input.lower() in ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday', 'all']:
                break  # correct day was inputted
            else:    # incorrect string entry
                 print("Input didn't match the day expected.  Please try again.")
                    
        except KeyboardInterrupt:  # CTRL-c or other interrupt to stop app
            city_input = 'exit'  # setup up some keyword to return and indicate stop app
            print('KeyboardInterrupt exception')
            break
        except:      # exception occurred with input
            print("  Error occurred with day input.  Please try again.")
            
        # Outside try/except block, go back to get day_input, as While is True
    # Outside while block for day name
    
        
    print('-'*40)
    return city_input.lower(), month_input.lower(), day_input.lower()

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
  
    filename = str(CITY_DATA.get(city))

    # load data file into a dataframe
    df = pd.read_csv(filename)

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name


    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month_int = months.index(month) +1

        # filter by month to create the new dataframe
        df = df[df['month'] == month_int] 

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]
    
    return df


def convert_24hr_12ampm(military_hr):
    """ Takes a 24 hour military time and converts to 12 hr using am/pm """
          
    if military_hr == 0:
        hour_ampm_str = "12am"
    elif military_hr == 12:
        hour_ampm_str = "12pm"
    elif military_hr > 12:
        hour_ampm_str = str(military_hr - 12) + "pm"
    else:
        hour_ampm_str = str(military_hr) + "am"
    # end of if block
   
    return hour_ampm_str


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...')
    start_time = time.time()

    
    # TO DO: display the most common month
    common_month = df['month'].mode() -1
    common_months = ['January', 'February', 'March', 'April', 'May', 'June']
                                      
    if common_month.size == 1: 
        print("From the data selected, most common month: {}".format(common_months[common_month[0]]))   
    else:
        print("From the data selected, most common month(s):", end = " ")
        for index in range(common_month.size):  # loop thru mult common values found
            if index == common_month.size -1:  # this is the last mult vlalue to show, end of print line
               print("{}".format(common_months[common_month[index]]))
            else: # mult values to show, add space and print on same line for Python3
                print("{},".format(common_months[common_month[index]]), end =" ")
            # end if block
        #end for loop
    #end if else block - more than than one month

    
    # TO DO: display the most common day of week
    common_day_of_week = df['day_of_week'].mode()[0:]
    if common_day_of_week.size >1: 
        print("                        most common day(s): {}".format(df['day_of_week'].mode().values))
    else:
        print("                        most common day: {}".format(df['day_of_week'].mode()[0]))
    # end if block for mult of singel day of week value
    
    
    # TO DO: display the most common start hour
    start_hour = df['Start Time'].dt.hour
    common_start_hour = start_hour.mode()  # [0] limits to 1st common hr, if more than 1
    
    
    if common_start_hour.size == 1: 
        start_hour_str = convert_24hr_12ampm(common_start_hour[0])      
        print("                        most common hour to start: " + start_hour_str)
    else:
        print("                        most common hour(s) to start:", end = " ")
        for index in range(common_start_hour.size):  # loop thru mult common values found
            if index == common_start_hour.size -1:  # this is the last mult vlalue to show, end of print line
               start_hour_str = convert_24hr_12ampm(common_start_hour[index])      
               print(start_hour_str)
            else: # mult values to show, add space and print on same line for Python3
                start_hour_str = convert_24hr_12ampm(common_start_hour[index])      
                print("{},".format(start_hour_str), end =" ")
            # end if block
        #end for loop
    #end if else block - more than than one month
   

    print("This took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...')
    start_time = time.time()

    # TO DO: display most commonly used start station
    common_start_st = df['Start Station'].mode()[0:]
    
    if common_start_st.size >1: 
        print("    Start Station(s): {}".format(common_start_st.values))
    else:
        print("    Start Station: {}".format(common_start_st[0]))
    # end if block for mult of start location values

    # TO DO: display most commonly used end station
    common_stop_st = df['End Station'].mode()[0:]
    
    if common_stop_st.size >1: 
        print("    End Station(s): {}".format(common_stop_st.values))
    else:
        print("    End Station: {}".format(common_stop_st[0]))
    # end if block for mult of stop location values

    # TO DO: display most frequent combination of start station and end station trip
    
    
    freq_combo = (df.groupby(['Start Station','End Station'])['End Station'].count())  
    print("    Most Popular trip(s){} ".format(freq_combo[freq_combo == freq_combo.max()]))        
      
 
    print("This took %s seconds." % (time.time() - start_time))
    print('-'*40)


def convert_seconds_days_hr_min_sec(seconds_duration):
    """ Takes duration in seconds and converts to string of Days, Hrs, Mins, Seconds """
          
    days = seconds_duration // (24 * 3600)
    remainder = seconds_duration % (24 * 3600)
    hours = remainder // 3600
    remainder = remainder % 3600
    mins = remainder // 60
    seconds = remainder % 60
    days_hrs_mins_sec_str = str("{} Day(s)  {} Hour(s) {} Mins {} Seconds".format(int(days), int(hours), int(mins), round(seconds,2)))
                                
    return days_hrs_mins_sec_str


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...')
    start_time = time.time()

    # TO DO: display total travel time
    total_duration = df['Trip Duration'].sum()
    total_duration_str = convert_seconds_days_hr_min_sec(total_duration)
    print('  Total rental time: ',total_duration_str)


    # TO DO: display mean travel time
    average_duration = df['Trip Duration'].mean()
    average_duration_str = convert_seconds_days_hr_min_sec(average_duration)
    print('Average rental time: ',average_duration_str)


    print("This took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df, selected_city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...')
    start_time = time.time()

    # TO DO: Display counts of user types
    rental_type = (df.groupby('User Type')['User Type'].count())  
    print("    Rental type by {} ".format(rental_type))
    

    # TO DO: Display counts of gender
    # TO DO: Display earliest, most recent, and most common year of birth
    # gender and year of birth not collected for washington
    if selected_city != 'washington':  #no user data to analyze for washington
        print('\nAnalysis on user...')
        # TO DO: Display counts of gender
        gender_grp = (df.groupby('Gender')['Gender'].count())  
        print("    Customer break-down by {} ".format(gender_grp))
  
        # TO DO: Display earliest, most recent, and most common year of birth
        print('\nCustomer age ranges...')
        earliest_YOB = df['Birth Year'].min()
        print('        Oldest renter: {}yrs old'.format(int(2020 - earliest_YOB)))
        
        oldest_YOB = df['Birth Year'].max()
        print('      Youngest renter: {}yrs old'.format(int(2020 - oldest_YOB)))

        average_YOB = df['Birth Year'].mode()[0:]
        if average_YOB.size == 1: 
            print('      Most common age: {}yrs old'.format(int(2020 - average_YOB[0])))  
        else:
            print("    Most common ages(s) were:", end = " ")
            for index in range(average_YOB.size):  # loop thru mult common values found
                if index == average_YOB.size -1:  # this is the last mult vlalue to show, end of print line
                    print("{}yrs old".format(int(2020 - average_YOB[index])))
                else: # mult values to show, add space and print on same line for Python3
                    print("{},".format(int(2020 - average_YOB[index])), end =" ")
                # end if block
            #end for loop
        #end if else block - more than than one month


    print("This took %s seconds." % (time.time() - start_time))
    print('-'*40)

    
def show_raw_data(df):
    """Displays 5 rows of raw data, based in user desire to see more."""

    review_data = input('\nWould you like review the raw data 20 at a time? Enter yes or no> ')
    if review_data.lower() == 'yes':
        pd.set_option('display.max_rows', 20)
        pd.set_option('display.max_columns', None)
        pd.set_option('display.width', None)
        df.pop('month')
        df.pop('day_of_week')
        #df.pop([0])  # 1st column of unlabel numbers
            
        for n in range(0,(len(df)),20): 
            print(df.iloc[n : n+20])
            if n+20 < len(df):
                review_more = input('\n    More? Enter yes or no> ')
                if review_more.lower() != 'yes':
                    break  # see no more data
                # End if  review more block
            #End if no more to loop thru
        #end For loop 
    # end see raw data
    # Nothing to return

    

def main():
    while True:
        city, month, day = get_filters()
        if city == 'exit':  # if user select CTRL-C or other KeyBoard Interrupt, set city to 'exit' and stop app
            break; 
            
        df = load_data(city, month, day)  
        
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df, city)
        show_raw_data(df)
        
        
        try:
            restart = input('\nWould you like to apply filters differently? Enter yes or no> ')
            if restart.lower() != 'yes':
                break  # exits While True loop

        except KeyboardInterrupt:  # CTRL-c or other interrupt to stop app
            break
        
if __name__ == "__main__":
	main()

