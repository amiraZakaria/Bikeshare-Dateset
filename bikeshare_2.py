import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york': 'new_york_city.csv',
              'washington': 'washington.csv' }
months = ['january', 'february', 'march', 'april', 'may', 'june']

def get_filters():
        print('Hello! Lets explore some US bikeshare data!')
   
        city=input('Would you like to see data for Chicago, New York, or Washington?').lower()
    
    
        months=['january','february', 'march', 'april', 'may', 'june','all']
        days=['monday','tuesday','wednesday','thursday','friday', 'saturday','sunday','all']
        month=input('Which month - January, February, March, April, May, or June?').lower()
        day=input('Which day - Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, or Sunday?').lower()
        while (day not in days):
            day=input('Which day - Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, or Sunday?').lower()
        while (month not in months):
            month=input('Which month - January, February, March, April, May, or June?').lower()
        while (city not in CITY_DATA.keys()):
            city=input('Would you like to see data for Chicago, New York, or Washington?').lower()
       

            
        print('-'*40)
        return city, month, day


def load_data(city, month, day):
     
    df = pd.read_csv(CITY_DATA[city])
    
    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['day_of_week'] = df['Start Time'].dt.strftime("%A")
    df['month'] =  df['Start Time'].dt.month
    

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        
        month =  months.index(month)+1
    
        # filter by month to create the new dataframe
        df = df[df['month']==month] 

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df =  df[df['day_of_week']==day.title()] 
        

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    
    df['hour'] = df['Start Time'].dt.hour

# find the most popular hour
    print("MOST HOUR : ",  df['hour'].value_counts().idxmax())
    print("MOST DAY : " , df['day_of_week'].value_counts().idxmax())
    name_of_month =  months[df['month'].value_counts().idxmax()-1]
    print("MOST MONTH : ", name_of_month )


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    print("MOST STARTING : " ,df['Start Station'].value_counts().idxmax())
    print("MOST ENDING : ", df['End Station'].value_counts().idxmax())
    #print( df[df['Start Station'] and df['End Station']].value_counts().idxmax() )
    print("THE INTERSECTION BETWEEN THE START AND END : ",df.groupby(['Start Station','End Station']).size().idxmax())
    

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    print("THE TOTAL TRAVEL TIME",df["Trip Duration"].sum())

    # display mean travel time
    print("THE MEAN TIME OF THE TRAVEL",df["Trip Duration"].mean())

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    print(df['User Type'].value_counts())

    # Display counts of gender
    if ('Gender' in df.columns and 'Birth Year' in df.columns ):
        
        print(df['Gender'].value_counts())


        # Display earliest, most recent, and most common year of birth
        print("EARLIEST YEAR OF BIRTH  ",df['Birth Year'].min())
        print("MOST RECENT YEAR OF BIRTH  ",df['Birth Year'].max())
        print("MOST COMMON YEAR OF BIRTH  ",df['Birth Year'].value_counts().idxmax())



    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def raw_data (df):
    """Displays the data due filteration.
    5 rows will added in each press"""
    print('press enter to see row data, press no to skip')
    x = 0
    while (input()!= 'no' and x+5 < df.shape[0]):
        print(df.iloc[x:x+5])
        x = x+5
    
    
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        raw_data (df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
