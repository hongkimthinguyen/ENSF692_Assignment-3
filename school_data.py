# school_data.py
# AUTHOR NAME: Kim Nguyen
#
# A terminal-based application for computing and printing statistics based on given input.
# You must include the main listed below. You may add your own additional classes, functions, variables, etc. 
# You may import any modules from the standard Python library.
# Remember to include docstrings and comments.

import numpy as np
from given_data import year_2013, year_2014, year_2015, year_2016, year_2017, year_2018, year_2019, year_2020, year_2021, year_2022

def combine_and_reshape_data(years):
    """
    Combine yearly data arrays into a single array and reshape into a 3D array.
    
    Parameters:
    years (list): List of numpy arrays containing yearly data.

    Returns:
    np.array: Reshaped 3D array with dimensions (10 years, 20 schools, 3 grades).
    """
    combined_data = np.concatenate(years, axis=0)  # Ensure concatenation along the correct axis
    reshaped_data = combined_data.reshape(10, 20, 3)
    return reshaped_data

# Initialize the data arrays
all_years = [year_2013, year_2014, year_2015, year_2016, year_2017, year_2018, year_2019, year_2020, year_2021, year_2022]

# Combine and reshape the data
reshaped_data = combine_and_reshape_data(all_years)

# Define school names and codes
school_names = [
    "Centennial High School", "Robert Thirsk School", "Louise Dean School",
    "Queen Elizabeth High School", "Forest Lawn High School", "Crescent Heights High School",
    "Western Canada High School", "Central Memorial High School", "James Fowler High School",
    "Ernest Manning High School", "William Aberhart High School", "National Sport School",
    "Henry Wise Wood High School", "Bowness High School", "Lord Beaverbrook High School",
    "Jack James High School", "Sir Winston Churchill High School", "Dr. E. P. Scarlett High School",
    "John G Diefenbaker High School", "Lester B. Pearson High School"
]

school_codes = [
    1224, 1679, 9626, 9806, 9813, 9815, 9816, 9823, 9825, 9826,
    9829, 9830, 9836, 9847, 9850, 9856, 9857, 9858, 9860, 9865
]

school_dict = {code: name for code, name in zip(school_codes, school_names)}

def get_school_index(school_input):
    """
    Get the index of the school based on the school names or codes.

    Parameters:
    school_input (str): The school name or code provided by the user.

    Returns:
    int: The index of the school in the list of schools.

    Raises:
    ValueError: If the school name or code is not valid.
    """
    if school_input.isdigit():
        school_code = int(school_input)
        if school_code in school_dict:
            return school_codes.index(school_code)
        else:
            raise ValueError("You must enter a valid school name or code.")
    else:
        if school_input in school_names:
            return school_names.index(school_input)
        else:
            raise ValueError("You must enter a valid school name or code.")

def calculate_school_stats(school_data):
    """
    Calculate statistics for a specific school based on its data.

    Parameters:
    school_data (np.array): Array containing the school's data for all years and grades.

    Returns:
    dict: Dictionary containing calculated statistics.
    """
    mean_enrollment_grade10 = np.floor(np.nanmean(school_data[:, 0])).astype(int)
    mean_enrollment_grade11 = np.floor(np.nanmean(school_data[:, 1])).astype(int)
    mean_enrollment_grade12 = np.floor(np.nanmean(school_data[:, 2])).astype(int)
    highest_enrollment = np.nanmax(school_data).astype(int)
    lowest_enrollment = np.nanmin(school_data).astype(int)
    total_enrollment_each_year = np.nansum(school_data, axis=1).astype(int)
    total_ten_year_enrollment = np.nansum(total_enrollment_each_year).astype(int)
    mean_total_yearly_enrollment = np.floor(np.nanmean(total_enrollment_each_year)).astype(int)
    over_500_enrollment = school_data[school_data > 500]
    over_500_median = np.nanmedian(over_500_enrollment).astype(int) if over_500_enrollment.size else "No enrollments over 500."

    return {
        "mean_enrollment_grade10": mean_enrollment_grade10,
        "mean_enrollment_grade11": mean_enrollment_grade11,
        "mean_enrollment_grade12": mean_enrollment_grade12,
        "highest_enrollment": highest_enrollment,
        "lowest_enrollment": lowest_enrollment,
        "total_enrollment_each_year": total_enrollment_each_year,
        "total_ten_year_enrollment": total_ten_year_enrollment,
        "mean_total_yearly_enrollment": mean_total_yearly_enrollment,
        "over_500_median": over_500_median
    }

def print_school_stats(school_name, school_code, stats):
    """
    Print the calculated statistics for a specific school.

    Parameters:
    school_name (str): Name of the school.
    school_code (int): Code of the school.
    stats (dict): Dictionary containing the calculated statistics.

    Returns:
    None
    """
    print(f"School Name: {school_name}, School Code: {school_code}")
    print(f"Mean enrollment for Grade 10: {stats['mean_enrollment_grade10']}")
    print(f"Mean enrollment for Grade 11: {stats['mean_enrollment_grade11']}")
    print(f"Mean enrollment for Grade 12: {stats['mean_enrollment_grade12']}")
    print(f"Highest enrollment for a single grade: {stats['highest_enrollment']}")
    print(f"Lowest enrollment for a single grade: {stats['lowest_enrollment']}")
    for year, enrollment in zip(range(2013, 2023), stats['total_enrollment_each_year']):
        print(f"Total enrollment for {year}: {enrollment}")
    print(f"Total ten year enrollment: {stats['total_ten_year_enrollment']}")
    print(f"Mean total enrollment over 10 years: {stats['mean_total_yearly_enrollment']}")
    print(f"For all enrollments over 500, the median value was: {stats['over_500_median']}")

def calculate_general_stats(data):
    """
    Calculate general statistics for all schools.

    Parameters:
    data (np.array): 3D array containing data for all schools, years, and grades.

    Returns:
    dict: Dictionary containing calculated general statistics.
    """
    mean_enrollment_2013 = np.floor(np.nanmean(data[0])).astype(int)
    mean_enrollment_2022 = np.floor(np.nanmean(data[-1])).astype(int)
    total_graduates_2022 = np.nansum(data[-1, :, 2]).astype(int)
    highest_enrollment_all_schools = np.nanmax(data).astype(int)
    lowest_enrollment_all_schools = np.nanmin(data).astype(int)

    return {
        "mean_enrollment_2013": mean_enrollment_2013,
        "mean_enrollment_2022": mean_enrollment_2022,
        "total_graduates_2022": total_graduates_2022,
        "highest_enrollment_all_schools": highest_enrollment_all_schools,
        "lowest_enrollment_all_schools": lowest_enrollment_all_schools
    }

def print_general_stats(stats):
    """
    Print the calculated general statistics for all schools.

    Parameters:
    stats (dict): Dictionary containing the calculated general statistics.

    Returns:
    None
    """
    print(f"Mean enrollment in 2013: {stats['mean_enrollment_2013']}")
    print(f"Mean enrollment in 2022: {stats['mean_enrollment_2022']}")
    print(f"Total graduating class of 2022: {stats['total_graduates_2022']}")
    print(f"Highest enrollment for a single grade: {stats['highest_enrollment_all_schools']}")
    print(f"Lowest enrollment for a single grade: {stats['lowest_enrollment_all_schools']}")

def main():
    print("ENSF 692 School Enrollment Statistics")

    # Print Stage 1 requirements here
    # Print the shape and dimensions of the reshaped data
    print("Shape of full data array: ", reshaped_data.shape)
    print("Dimensions of full data array: ", reshaped_data.ndim)

    # Prompt for user input
    # Handle user input for school name or code
    while True:
        school_input = input("Please enter the high school name or school code: ")
        try:
            school_index = get_school_index(school_input)
            break
        except ValueError as e:
            print(e)

    # Print Stage 2 requirements here 
    # Get and print school-specific statistics
    print("\n***Requested School Statistics***\n")
    school_data = reshaped_data[:, school_index, :]
    school_stats = calculate_school_stats(school_data)
    print_school_stats(school_names[school_index], school_codes[school_index], school_stats)

    # Print Stage 3 requirements here 
    # Get and print general statistics for all schools
    print("\n***General Statistics for All Schools***\n")
    general_stats = calculate_general_stats(reshaped_data)
    print_general_stats(general_stats)

if __name__ == '__main__':
    main()
