"""
Created on Fri Nov 19 16:11:38 2021

@author: Marcos Herrera
"""

""" SCOPING YOUR PROJECT
A- Analyze the data inside the dataset “insurance.csv” and gain insight by looking and finding relationships between the different variable, this analysis should help us respond the following questions:
   1- What is the age-sex distribution? 
   2- How is BMI average distributed by age? 
   3- Number of smokers grouped by age, and what percentage of it are female or male?
   4- How are males and females distributed in each region?
   5- Are smoker’s BMI average above or below non-smoker’s BMI average?
   6- Do people from a certain region have a higher BMI average than people from another region?
   7- Do people with a greater number of children have greater BMI average?
   8- Do older people have more kids?
   9- Do people that smoke have more children that those who don’t smoke?
   10- What is the children-region distribution?
   11- What is the smoker-region distribution?
   12- What is the age-region distribution?
   13- If we group charges by age which pays more in terms of totals and percentage?
   14- Which region pays more charges in terms of totals and percentage?
   15- If we group smokers and non-smokers who pays more charges in terms of totals and percentage?
   16- Do people that have more children pays more charges?
   17- Do people with BMI higher than average pay more that those with BMI lower than average?

B- Draw conclusions and make recommendation

"""
#Import csv library / numpy library / matplotlib library
import csv
import numpy as np
import matplotlib.pyplot as plt

#Import dataset from insurance.csv into your Python file and inspect the contents.
age_list = []
sex_list = []
bmi_list = []
children_list = []
smoker_list = []
region_list = []
charges_list = []

def import_dataset_to_lists(csv_file):
    with open(csv_file, newline='') as  data_set_csv:
        data_set_dict = csv.DictReader(data_set_csv)
        for row in data_set_dict: # Iterate through each row of the csv file dataset turned into a dictionary by the csv.Dictreader method
            age_list.append(int(row['age'])) # Create lists that later will be used for analysis
            sex_list.append(row['sex'])
            bmi_list.append(float(row['bmi']))
            children_list.append(int(row['children']))
            smoker_list.append(row['smoker'])
            region_list.append(row['region'])
            charges_list.append(float(row['charges']))
        return 
import_dataset_to_lists('insurance.csv')       

sum_males_dataset = sex_list.count('male') # variable to sum all females in the data set (Global variable)
sum_females_dataset = sex_list.count('female') # variable to sum all males in the data set (Global variable)
total_population_dataset = len(age_list) # variable with the total population of the dataset (Global variable)
average_age = round((sum(age_list) / total_population_dataset), 2) # Average age
sum_smokers = smoker_list.count('yes') # Sum of all smokers within the dataset
sum_nonsmokers = smoker_list.count('no') # Sum of all non-smokers within the dataset
average_bmi = round((sum(bmi_list) / total_population_dataset), 2) # Average BMI of all the population
total_children = sum(children_list)
sum_total_charges = sum(charges_list)
average_charges = round((sum_total_charges / total_population_dataset),2)
#------------------------------------------------------------------------------
"""  1- What is the age-sex distribution? """

#  Create a dictionary that groups female and male population within each age ===> {'Age': [Σ of population of the same age, Σ males,  Σ females]}
age_sex_dict = {}
def age_sex_dictionary(age_list, sex_list): # Funtion that creates the age_sex dictionary
    for age, sex in zip(age_list, sex_list): # Iterate through the list containing age and sex data
        if age not in age_sex_dict:
            age_sex_dict[age] = {'Total specific age population': 0, 'Males': 0, 'females': 0}
        if age in age_sex_dict and sex == 'male':
            age_sex_dict[age]['Total specific age population'] += 1
            age_sex_dict[age]['Males'] += 1
        elif age in age_sex_dict and sex == 'female':
            age_sex_dict[age]['Total specific age population'] += 1
            age_sex_dict[age]['females'] += 1
    return age_sex_dict
age_sex_dictionary(age_list, sex_list)
#print(age_sex_dictionary(age_list, sex_list))

#------------------------------------------------
sorted_age_sex_dict = {}
def sort_dictionary_by_key(age_sex_dictionary):# This funtion sorts the age_sex_dict and returns a sorted dictionary
    sort = sorted(age_sex_dict.items(), key = lambda t: t[0])# Here we sort the dictionary passed as a parameter to the funtion
    sorted_age_sex_dict.update(sort)
    return sorted_age_sex_dict
sort_dictionary_by_key(age_sex_dict)
#print(sort_dictionary_by_key(age_sex_dict)) 

#------------------------------------------------
x_axis_age = []# Empty list that will contain the sorted ages of age_sex_dcitionary
y_axis_population = []# Empty list that will contain the total population of each age of age_sex_dictionary
y_axis_male = [] # Empty list that will contain the male count of each age of age_sex_dictionary
y_axis_female = [] # Empty list that will contain the female count of each age of age_sex_dictionary
def fill_list_to_plot(sorted_age_sex__dictionary):# This funtion fills the lists to plot the age-population chart
    for key in sorted_age_sex_dict.keys():# Iterates through the age_sex_dictionary and fills the lists that will be used to plot age_population barchart
        x_axis_age.append(key)
        y_axis_population.append(sorted_age_sex_dict[key]['Total specific age population'])
        y_axis_male.append(sorted_age_sex_dict[key]['Males'])
        y_axis_female.append(sorted_age_sex_dict[key]['females'])
    return x_axis_age, y_axis_population
fill_list_to_plot(sorted_age_sex_dict)
#print(fill_list_to_plot(sorted_age_sex_dict))

#------------------------------------------------
def stacked_barchart_age_vs_population(x_axis_age_list, y_axis_population_list):# This funtion plots a stacked bar chart of age vs population
    plt.figure(num = 1,dpi = 600, figsize = (15, 11))
    p1 = plt.bar(x_axis_age, y_axis_male, width = 0.5, label='Male') # ec = 'black' parameter to enclose the bars if desired
    p2 = plt.bar(x_axis_age, y_axis_female,width = 0.5, bottom = y_axis_male,  label='Female')
    p3 = plt.bar(x_axis_age, y_axis_population, width = 0.5, label='', ec = 'white', alpha = 0)# Using parameter alpha to make p3 transparent
    plt.xticks(x_axis_age, color='black', fontsize=5)
    #plt.grid()
    plt.title('01- Age Vs Population size (gender)')
    plt.xlabel('Age')
    plt.ylabel('Population size (gender)')
    plt.legend()
    plt.bar_label(p1, label_type = 'center', fontsize = 6)
    plt.bar_label(p2, label_type = 'center', fontsize = 6)
    plt.bar_label(p3, label_type = 'edge', fontsize = 7)
    return plt.show
#stacked_barchart_age_vs_population(x_axis_age, y_axis_population)

#------------------------------------------------------------------------------
"""  2- How is BMI average distributed by age? """

#  Create a dictionary that groups BMI average (the mean) within each age ===> {'Age': {'Total specific age population': , 'Σ BMI': , 'BMI average': }
age_bmi_average_dict = {}
def age_bmi_dictionary(age_list, bmi_list): # Funtion that creates a key = age and a value BMI average for age_bmi_average_dict
    for age, bmi in zip(age_list, bmi_list): # Iterate through the list containing age data
        if age not in age_bmi_average_dict:
            age_bmi_average_dict[age] = {'Total specific age population': 0, 'Σ BMI': 0}
        if age in age_bmi_average_dict:
            age_bmi_average_dict[age]['Total specific age population'] += 1
            age_bmi_average_dict[age]['Σ BMI'] += bmi
    for age in age_bmi_average_dict.keys(): # Itarate through the age_bmi_average_dict to add the BMI average key and its value
        age_bmi_average_dict[age]['Σ BMI'] = round(age_bmi_average_dict[age]['Σ BMI'],2) # rounds up Σ BMI
        age_bmi_average_dict[age]['BMI average'] = round(age_bmi_average_dict[age]['Σ BMI'] / age_bmi_average_dict[age]['Total specific age population'], 2)
    return age_bmi_average_dict
age_bmi_dictionary(age_list, bmi_list)
#print(age_bmi_dictionary(age_list, bmi_list))

#------------------------------------------------
sorted_age_bmi_average_dict = {}
def sort_dictionary_by_key(age_bmi_dictionary):# This funtion sorts the age_bmi_average_dict and returns a sorted dictionary
    sort = sorted(age_bmi_average_dict.items(), key = lambda t: t[0])# Here we sort the dictionary passed as a parameter to the funtion
    sorted_age_bmi_average_dict.update(sort)
    return sorted_age_bmi_average_dict
sort_dictionary_by_key(age_bmi_average_dict)
#print(sort_dictionary_by_key(age_bmi_average_dict))

#------------------------------------------------
y_axis_bmi_average = [] # Empty list that will contain the female count of each age of age_sex_dictionary
def fill_list_to_plot(sorted_age_bmi_average_dictionary):# This funtion fills the lists to plot the age-population chart
    for key in sorted_age_bmi_average_dict.keys():# Iterates through the age_sex_dictionary and fills the lists that will be used to plot age_population barchart
        y_axis_bmi_average.append(sorted_age_bmi_average_dict[key]['BMI average'])
    return y_axis_bmi_average
fill_list_to_plot(sorted_age_bmi_average_dict)
#print(fill_list_to_plot(sorted_age_sex_dict))

#------------------------------------------------
def barchart_age_vs_BMI_average(x_axis_age, y_axis_bmi_list):# This funtion plots a bar chart of age vs BMI average
    plt.figure(num = 2,dpi = 600, figsize = (15, 11)) # figsize(width, height) to change the size of the plot
    p1 = plt.bar(x_axis_age, y_axis_bmi_average, width = 0.5, align = 'center', label='BMI average')
    plt.xticks(x_axis_age, color='black', fontsize=5)
    plt.ylim(0, 35)
    plt.title('02- Age Vs BMI average', fontsize = 12)
    plt.xlabel('Age', fontsize = 12)
    plt.ylabel('BMI average', fontsize = 12)
    plt.legend()
    plt.bar_label(p1, label_type = 'edge', fontsize = 5)
    return plt.show
#barchart_age_vs_BMI_average(x_axis_age, y_axis_bmi_average)

#------------------------------------------------------------------------------
"""  3- Number of smokers grouped by age, and what percentage of it are female or male? """
#  Create a dictionary that groups smokers and non-smokers and if they males or females within each age ===> {'Age': ['total_smokers': , 'male_smokers': , 'female_smokers': , '%_total': , '%_males': , '%_females': ]}
age_smoker_dict = {}
def age_smoker_dictionary(age_list, smoker_list, sex_list): # Funtion that creates the age_smoker dictionary
    for age, smoker, sex in zip(age_list, smoker_list, sex_list): # Iterate through the list containing age and smoke data
        if age not in age_smoker_dict:
            age_smoker_dict[age] = {'total_smokers': 0, 'male_smokers': 0, 'female_smokers': 0, '%_total': 0, '%_males': 0, '%_females': 0}
        if age in age_smoker_dict and smoker == 'yes' and sex == 'male':
            age_smoker_dict[age]['total_smokers'] += 1
            age_smoker_dict[age]['male_smokers'] += 1
        elif age in age_smoker_dict and smoker == 'yes' and sex == 'female':
            age_smoker_dict[age]['total_smokers'] += 1
            age_smoker_dict[age]['female_smokers'] += 1
    for age in age_smoker_dict.keys(): # Itarate through the age_smoker_dict to add the percentages
        age_smoker_dict[age]['%_total'] = round((age_smoker_dict[age]['total_smokers'] / sum_smokers) * 100, 3)
        age_smoker_dict[age]['%_males'] = round((age_smoker_dict[age]['male_smokers'] / sum_smokers) * 100,2)
        age_smoker_dict[age]['%_females'] = round((age_smoker_dict[age]['female_smokers'] / sum_smokers) * 100,2)
    return age_smoker_dict
age_smoker_dictionary(age_list, smoker_list, sex_list)
#print(age_smoker_dictionary(age_list, smoker_list, sex_list))
""" #To test if %_total is equal to 100%
add = 0
for key in age_smoker_dict.keys():
    add += age_smoker_dict[key]['%_total']
print(add)""" 

#------------------------------------------------
sorted_age_smoker_dict = {}
def sort_dictionary_by_key(age_smoker_dictionary):# This funtion sorts the age_bmi_average_dict and returns a sorted dictionary
    sort = sorted(age_smoker_dict.items(), key = lambda t: t[0])# Here we sort the dictionary passed as a parameter to the funtion
    sorted_age_smoker_dict.update(sort)
    return sorted_age_smoker_dict
sort_dictionary_by_key(age_smoker_dict)
#print(sort_dictionary_by_key(age_smoker_dict))

#------------------------------------------------
y_total_smoker_percentage = [] # Empty list that will contain the total percentage of smokers in sorted_age_smoker_dict
y_male_smoker_percentage = [] # Empty list that will contain the total percentage of male smokers in sorted_age_smoker_dict
y_female_smoker_percentage = [] # Empty list that will contain the total percentage of female smokers in sorted_age_smoker_dict  
def fill_list_to_plot(sorted_age_smoker_dictionary):# This funtion fills the lists to plot the age-smoker chart
    for key in sorted_age_smoker_dict.keys():# Iterates through the sorted_age_smoker_dict and fills the lists that will be used to plot age Vs smoker barchart
        y_total_smoker_percentage.append(sorted_age_smoker_dict[key]['%_total'])
        y_male_smoker_percentage.append(sorted_age_smoker_dict[key]['%_males'])
        y_female_smoker_percentage.append(sorted_age_smoker_dict[key]['%_females'])
    return y_total_smoker_percentage
fill_list_to_plot(sorted_age_smoker_dict)
#print(fill_list_to_plot(sorted_age_smoker_dict))
 
#------------------------------------------------   
def stacked_barchart_age_vs_smoker(x_axis_age_list, y_total_smoker_percentage, y_male_smoker_percentage, y_female_smoker_percentage ):# This funtion plots a stacked bar chart of age vs smoker
    plt.figure(num = 3,dpi = 600, figsize = (20, 11))# figsize(width, height) to change the size of the plot
    p1 = plt.bar(x_axis_age, y_male_smoker_percentage, width = 0.5, label='Male') # ec = 'black' parameter to enclose the bars if desired
    p2 = plt.bar(x_axis_age, y_female_smoker_percentage, width = 0.5, bottom = y_male_smoker_percentage,  label='Female')
    p3 = plt.bar(x_axis_age, y_total_smoker_percentage, width = 0.5, label='', ec = 'white', alpha = 0)# Using parameter alpha to make p3 transparent
    plt.xticks(x_axis_age, color='black', fontsize=5)
    #plt.grid()
    plt.title('03- Age Vs Smokers', fontsize = 12)
    plt.xlabel('Age', fontsize = 12)
    plt.ylabel('% of Smokers', fontsize = 12)
    plt.legend()
    plt.bar_label(p1, label_type = 'center', fontsize = 6)
    plt.bar_label(p2, label_type = 'center', fontsize = 6)
    plt.bar_label(p3, label_type = 'edge', fontsize = 7)
    return plt.show
#stacked_barchart_age_vs_smoker(x_axis_age, y_total_smoker_percentage, y_male_smoker_percentage, y_female_smoker_percentage )

#------------------------------------------------------------------------------
""" 4- How are males and females distributed in each region? """
#  Create a dictionary of population gropuped in regions and if they are males or females ===> {'Age': [Σ of population of the region, Σ males,  Σ females]}
region_population_dict = {}
def region_population_dictionary(region_list, sex_list): # Funtion that creates the age_smoker dictionary
    for region, sex in zip(region_list, sex_list): # Iterate through the list containing region and sex data
        if region not in region_population_dict:
            region_population_dict[region] = {'total_population': 0, 'male_population': 0, 'female_population': 0}
        if region in region_population_dict and sex == 'male':
            region_population_dict[region]['male_population'] += 1
            region_population_dict[region]['total_population'] += 1
        elif region in region_population_dict and sex == 'female':
            region_population_dict[region]['female_population'] += 1
            region_population_dict[region]['total_population'] += 1
    return region_population_dict
region_population_dictionary(region_list, sex_list)
#print(region_population_dictionary(region_list, sex_list))

#------------------------------------------------
x_axis_regions = []
y_region_total_population = [] # Empty list that will contain the total population of each region
y_region_male_population = [] # Empty list that will contain the male population of each region
y_region_female_population = [] # Empty list that will contain the female population of each region
def fill_list_to_plot(region_population_dict):# This funtion fills the lists to plot the region-population chart
    for key in region_population_dict.keys():# Iterates through the sorted_region_population_dict and fills the lists that will be used to plot region Vs population barchart
        x_axis_regions.append(key)
        y_region_total_population.append(region_population_dict[key]['total_population'])
        y_region_male_population.append(region_population_dict[key]['male_population'])
        y_region_female_population.append(region_population_dict[key]['female_population'])
    return x_axis_regions, y_region_total_population, y_region_male_population, y_region_female_population
fill_list_to_plot(region_population_dict)
#print(fill_list_to_plot(region_population_dict))

#------------------------------------------------   
def multiple_barchart_region_vs_population(x_axis_regions, y_region_male_population, y_region_female_population): # This funtion plots a multiple bar chart of region vs population
    plt.figure(num = 4,dpi = 600, figsize = (20, 11))# figsize(width, height) to change the size of the plot
    w = 0.4
    bar1 = np.arange(len(x_axis_regions))
    bar2 = [i+w for i in bar1]
    bar3 = [i+(w/2) for i in bar1]
    p1 = plt.bar(bar1, y_region_male_population, w, label='Male') # ec = 'black' parameter to enclose the bars if desired
    p2 = plt.bar(bar2, y_region_female_population, w, label='Female')
    p3 = plt.bar(bar3, y_region_total_population, w, label='Total population', ec = 'white', alpha = 0.3)# Using parameter alpha to make p3 transparent
    plt.xticks(bar1 + w/2, x_axis_regions, color='black', fontsize=5)
    #plt.grid()
    plt.title('04- Region Vs Population', fontsize = 12)
    plt.xlabel('Region', fontsize = 12)
    plt.ylabel('Population', fontsize = 12)
    plt.legend()
    plt.bar_label(p1, label_type = 'center', fontsize = 10)
    plt.bar_label(p2, label_type = 'center', fontsize = 10)
    plt.bar_label(p3, label_type = 'edge', fontsize = 10)
    return plt.show
#multiple_barchart_region_vs_population(x_axis_regions, y_region_male_population, y_region_female_population) 

#------------------------------------------------------------------------------
""" 5- Are smoker’s BMI average above or below non-smoker’s BMI average? """
smoker_nonsmoker_bmi_dict = {'Σ_bmi_smokers': 0, 'average_bmi_smokers': 0, 'Σ_bmi_nonsmokers': 0, 'average_bmi_nonsmokers': 0}
def smoker_nonsmoker_bmi_dictionary(smoker_list, bmi_list): # Funtion that creates the smoker_nonsmoker_bmi average dictionary
    for smoker, bmi in zip(smoker_list, bmi_list): # Iterate through the list containing smoker and bmi data
        if smoker == 'yes':
            smoker_nonsmoker_bmi_dict['Σ_bmi_smokers'] += bmi
        elif smoker == 'no':
            smoker_nonsmoker_bmi_dict['Σ_bmi_nonsmokers'] += bmi
    for key in smoker_nonsmoker_bmi_dict.keys():
        smoker_nonsmoker_bmi_dict['Σ_bmi_smokers'] = round(smoker_nonsmoker_bmi_dict['Σ_bmi_smokers'], 2)
        smoker_nonsmoker_bmi_dict['average_bmi_smokers'] = round((smoker_nonsmoker_bmi_dict['Σ_bmi_smokers'] / sum_smokers), 2)
        smoker_nonsmoker_bmi_dict['Σ_bmi_nonsmokers'] = round(smoker_nonsmoker_bmi_dict['Σ_bmi_nonsmokers'], 2)
        smoker_nonsmoker_bmi_dict['average_bmi_nonsmokers'] = round((smoker_nonsmoker_bmi_dict['Σ_bmi_nonsmokers'] / sum_nonsmokers), 2)
    return smoker_nonsmoker_bmi_dict
smoker_nonsmoker_bmi_dictionary(smoker_list, bmi_list)
#print(smoker_nonsmoker_bmi_dictionary(smoker_list, bmi_list))

#------------------------------------------------
x_axis_smokers = ['smokers', 'non smokers']
y_axis_average_bmi_smoker_non_smoker = [smoker_nonsmoker_bmi_dict['average_bmi_smokers'],smoker_nonsmoker_bmi_dict['average_bmi_nonsmokers']]
#y_average_bmi_smokers = smoker_nonsmoker_bmi_dict['average_bmi_smokers'] # Empty list that will contain the average bmi of smokers
#y_average_bmi_nonsmokers = smoker_nonsmoker_bmi_dict['average_bmi_nonsmokers'] # Empty list that will contain the average bmi of nonsmokers
def barchart_smoker_vs_average_bmi(x_axis_smokers): # This funtion plots a bar chart of region vs population
    plt.figure(num = 5,dpi = 600, figsize = (20, 11))# figsize(width, height) to change the size of the plot
    w = 0.4
    p1 = plt.bar(x_axis_smokers[0], y_axis_average_bmi_smoker_non_smoker[0], w, label='Smoker') # ec = 'black' parameter to enclose the bars if desired
    p2 = plt.bar(x_axis_smokers[1], y_axis_average_bmi_smoker_non_smoker[1], w, label='Non-Smoker')
    #p3 = plt.bar(bar3, y_region_total_population, w, label='Total population', ec = 'white', alpha = 0.3)# Using parameter alpha to make p3 transparent
    plt.xticks(x_axis_smokers, color='black', fontsize=12)
    #plt.grid()
    plt.title('05- Smoker-Non-Smoker Vs Average BMI', fontsize = 14)
    plt.xlabel('Smoker-Non-Smoker', fontsize = 14)
    plt.ylabel('Average BMI', fontsize = 14)
    plt.legend()
    plt.bar_label(p1, label_type = 'center', fontsize = 10)
    plt.bar_label(p2, label_type = 'center', fontsize = 10)
    #plt.bar_label(p3, label_type = 'edge', fontsize = 10)
    return plt.show
#barchart_smoker_vs_average_bmi(x_axis_smokers) 

#------------------------------------------------------------------------------
""" 6- Do people from a certain region have a higher BMI average than people from another region? """
#  Create a dictionary that groups BMI average (the mean) within each region ===> {'Region': BMI average}
region_bmi_average_dict = {}
def region_bmi_dictionary(region_list, bmi_list): # Funtion that creates a key = region and a value BMI average for each region
    for region, bmi in zip(region_list, bmi_list): # Iterate through the lists containing region and bmi data
        if region not in region_bmi_average_dict:
            region_bmi_average_dict[region] = {'Σ_bmi': 0 , 'average_bmi': 0}
        if region in region_bmi_average_dict:
            region_bmi_average_dict[region]['Σ_bmi'] += bmi
    for region in region_bmi_average_dict.keys(): # Itarate through the region_bmi_average_dictt to add the average BMI value
        region_bmi_average_dict[region]['Σ_bmi'] = round(region_bmi_average_dict[region]['Σ_bmi'], 2)
        region_bmi_average_dict[region]['average_bmi'] = round(region_bmi_average_dict[region]['Σ_bmi'] / region_population_dict[region]['total_population'] ,2) # rounds up Σ BMI
    return region_bmi_average_dict
region_bmi_dictionary(region_list, bmi_list)
#print( region_bmi_dictionary(region_list, bmi_list))

#------------------------------------------------
y_axis_average_bmi_region = [] # Empty list that will contain the average BMI of each region
def fill_list_to_plot(region_bmi_average_dict):# This funtion fills the lists to plot the region-Average BMI chart
    for key in region_bmi_average_dict.keys():# Iterates through the region_bmi_average_dict and fills the lists that will be used to plot region Vs Average BMI barchart
        y_axis_average_bmi_region.append(region_bmi_average_dict[key]['average_bmi'])
    return y_axis_average_bmi_region
fill_list_to_plot(region_bmi_average_dict)
#print(fill_list_to_plot(region_bmi_average_dict))

#------------------------------------------------   
def barchart_region_vs_bmi(x_axis_regions, y_axis_average_bmi_region): # This funtion plots bar chart of region vs Average BMI
    plt.figure(num = 6,dpi = 600, figsize = (20, 11))# figsize(width, height) to change the size of the plot
    w = 0.4
    p1 = plt.bar(x_axis_regions, y_axis_average_bmi_region, w) # ec = 'black' parameter to enclose the bars if desired
    #p2 = plt.bar(bar2, y_region_female_population, w, label='Female')
    #p3 = plt.bar(bar3, y_region_total_population, w, label='Total population', ec = 'white', alpha = 0.3)# Using parameter alpha to make p3 transparent
    plt.xticks(x_axis_regions, color='black', fontsize = 12)
    #plt.grid()
    plt.title('06- Region Vs Average BMI (Body mass index)', fontsize = 14)
    plt.xlabel('Region', fontsize = 14)
    plt.ylabel('Average BMI', fontsize = 14)
    #plt.legend()
    plt.bar_label(p1, label_type = 'center', fontsize = 10)
    #plt.bar_label(p2, label_type = 'center', fontsize = 10)
    #plt.bar_label(p3, label_type = 'edge', fontsize = 10)
    return plt.show
#barchart_region_vs_bmi(x_axis_regions, y_axis_average_bmi_region)

#------------------------------------------------------------------------------
""" 7- Do people with a greater number of children have greater BMI average?"""
#  Create a dictionary that groups BMI average (the mean) within each number of children
num_children_average_bmi_dict = {}
def num_children_bmi_dictionary(children_list, bmi_list): # Funtion that creates a key = number of children and a value BMI average for each number of children
    for num, bmi in zip(children_list, bmi_list): # Iterate through the lists containing number of children and bmi data
        if num not in num_children_average_bmi_dict:
            num_children_average_bmi_dict[num] = {'times_repeated': 0, 'Σ_bmi': 0, 'average_bmi': 0, '%_of_total_population': 0}
        if num in num_children_average_bmi_dict:
            num_children_average_bmi_dict[num]['Σ_bmi'] += bmi
            num_children_average_bmi_dict[num]['times_repeated'] += 1
    for num in num_children_average_bmi_dict.keys(): # Itarate through the num_children_average_bmi_dict to add the average BMI value
        num_children_average_bmi_dict[num]['Σ_bmi'] = round(num_children_average_bmi_dict[num]['Σ_bmi'], 2) # rounds up Σ BMI
        num_children_average_bmi_dict[num]['average_bmi'] = round((num_children_average_bmi_dict[num]['Σ_bmi'] / num_children_average_bmi_dict[num]['times_repeated']) ,2) # Calculates average BMI for the especific age
        num_children_average_bmi_dict[num]['%_of_total_population'] = round((num_children_average_bmi_dict[num]['times_repeated'] / total_population_dataset) * 100 ,2) # Calculates average BMI for the especific age
    return num_children_average_bmi_dict
num_children_bmi_dictionary(children_list, bmi_list)
#print( num_children_bmi_dictionary(children_list, bmi_list))
   
#------------------------------------------------
sorted_num_children_average_bmi_dict = {}
def sort_dictionary_by_key(num_children_average_bmi_dictionary):# This funtion sorts the num_children_average_bmi_dict and returns a sorted dictionary
    sort = sorted(num_children_average_bmi_dict.items(), key = lambda t: t[0])# Here we sort the dictionary passed as a parameter to the funtion
    sorted_num_children_average_bmi_dict.update(sort)
    return sorted_num_children_average_bmi_dict 
sort_dictionary_by_key(num_children_average_bmi_dict)
#print(sort_dictionary_by_key(num_children_average_bmi_dict))      

#------------------------------------------------
x_axis_num_children = []# Empty list that will contain the sorted ages of age_sex_dcitionary
y_axis_average_bmi_num_children = []# Empty list that will contain the total population of each age of age_sex_dictionary
y_axis_percentage_of_total_population = [] # Empty list that will contain the male count of each age of age_sex_dictionary
y_axis_times_repeated = [] # Empty list that will contain the female count of each age of age_sex_dictionary
def fill_list_to_plot(sorted_num_children_average_bmi_dictionary):# This funtion fills the lists to plot the age-population chart
    for key in sorted_num_children_average_bmi_dict.keys():# Iterates through the age_sex_dictionary and fills the lists that will be used to plot age_population barchart
        x_axis_num_children.append(key)
        y_axis_times_repeated.append(sorted_num_children_average_bmi_dict[key]['times_repeated'])
        y_axis_average_bmi_num_children.append(sorted_num_children_average_bmi_dict[key]['average_bmi'])
        y_axis_percentage_of_total_population.append(sorted_num_children_average_bmi_dict[key]['%_of_total_population'])
    return x_axis_num_children, y_axis_average_bmi_num_children, y_axis_percentage_of_total_population, y_axis_times_repeated
fill_list_to_plot(sorted_num_children_average_bmi_dict)
#print(fill_list_to_plot(sorted_num_children_average_bmi_dict))

#------------------------------------------------
def barchart_num_chilcren_vs_average_bmi(x_axis_num_children, y_axis_average_bmi_num_children): # This funtion plots a bar chart of number of children vs average bmi
    plt.figure(num = 7,dpi = 600, figsize = (20, 11))# figsize(width, height) to change the size of the plot
    w = 0.4
    p1 = plt.bar(x_axis_num_children, y_axis_average_bmi_num_children, w) # ec = 'black' parameter to enclose the bars if desired
    #p2 = plt.bar(x_axis_smokers[1], y_axis_average_bmi_smoker_non_smoker[1], w, label='Non-Smoker')
    #p3 = plt.bar(bar3, y_region_total_population, w, label='Total population', ec = 'white', alpha = 0.3)# Using parameter alpha to make p3 transparent
    plt.xticks(x_axis_num_children, color='black', fontsize=12)
    #plt.grid()
    plt.title('07- Number of children Vs Average BMI', fontsize = 14)
    plt.xlabel('Number of children', fontsize = 14)
    plt.ylabel('Average BMI', fontsize = 14)
    #plt.legend()
    plt.bar_label(p1, label_type = 'center', fontsize = 10)
    #plt.bar_label(p2, label_type = 'center', fontsize = 10)
    #plt.bar_label(p3, label_type = 'edge', fontsize = 10)
    return plt.show
#barchart_num_chilcren_vs_average_bmi(x_axis_num_children, y_axis_average_bmi_num_children)

#------------------------------------------------------------------------------
""" 8- Do older people have more kids?"""
#  Create a dictionary that groups number of children within each age
age_num_children_dict = {}
def age_num_children_dictionary(age_list, children_list): # Funtion that creates the age_num_of_children dictionary
    for age, num in zip(age_list, children_list): # Iterate through the lists containing age and children data
        if age not in age_num_children_dict:
            age_num_children_dict[age] = {'Σ_children': 0}
        elif age in age_num_children_dict:
            age_num_children_dict[age]['Σ_children'] += num
    return age_num_children_dict
age_num_children_dictionary(age_list, children_list)
#print(age_num_children_dictionary(age_list, children_list))

#------------------------------------------------
sorted_age_num_children_dict = {}
def sort_dictionary_by_key(age_num_children_dictionary):# This funtion sorts the age_num_children_dict and returns a sorted dictionary
    sort = sorted(age_num_children_dict.items(), key = lambda t: t[0])# Here we sort the dictionary passed as a parameter to the funtion
    sorted_age_num_children_dict.update(sort)
    return sorted_age_num_children_dict 
sort_dictionary_by_key(age_num_children_dict)
#print(sort_dictionary_by_key(num_children_average_bmi_dict))

#------------------------------------------------
y_axis_num_of_children_by_age = []
def fill_list_to_plot(sorted_age_num_children_dict):# This funtion fills the lists to plot the age-number_of_children chart
    for key in sorted_age_num_children_dict.keys():# Iterates through the age_num_children_dictionary and fills the lists that will be used to plot age_number_of_children barchart
        y_axis_num_of_children_by_age.append(sorted_age_num_children_dict[key]['Σ_children'])
    return y_axis_num_of_children_by_age 
fill_list_to_plot(sorted_age_num_children_dict)
#print(fill_list_to_plot(sorted_age_num_children_dict))

#------------------------------------------------
def barchart_age_num_chilcren(x_axis_age, y_axis_num_of_children_by_age): # This funtion plots a bar chart of number of children vs average bmi
    plt.figure(num = 8,dpi = 600, figsize = (20, 11))# figsize(width, height) to change the size of the plot
    w = 0.4
    p1 = plt.bar(x_axis_age, y_axis_num_of_children_by_age, w) # ec = 'black' parameter to enclose the bars if desired
    #p2 = plt.bar(x_axis_smokers[1], y_axis_average_bmi_smoker_non_smoker[1], w, label='Non-Smoker')
    #p3 = plt.bar(bar3, y_region_total_population, w, label='Total population', ec = 'white', alpha = 0.3)# Using parameter alpha to make p3 transparent
    plt.xticks(x_axis_age, color='black', fontsize=12)
    #plt.grid()
    plt.title('08- Age Vs Number of children', fontsize = 14)
    plt.xlabel('Age', fontsize = 14)
    plt.ylabel('Number of children', fontsize = 14)
    #plt.legend()
    plt.bar_label(p1, label_type = 'center', fontsize = 8)
    #plt.bar_label(p2, label_type = 'center', fontsize = 10)
    #plt.bar_label(p3, label_type = 'edge', fontsize = 10)
    return plt.show
#barchart_age_num_chilcren(x_axis_age, y_axis_num_of_children_by_age)

#------------------------------------------------------------------------------
""" 9- Do people that smoke have more children that those who don’t smoke?"""
smoker_nonsmoker_children_dict = {}
def smoker_children_dictionary(smoker_list, children_list): # This funtion willuse the lists smoker_list, children_list and add the number of chuldren to children_smokers and children_nonsmokers.
    children_smoker = 0 # This variable will count all the children whose parents smoke
    children_nonsmoker = 0 # This variable will count all the children whose parents dont smoke
    for smoker, children in zip(smoker_list, children_list):
        if smoker == 'yes':
                 children_smoker += int(children)
        elif smoker == 'no':
            children_nonsmoker += int(children)
    smoker_nonsmoker_children_dict['Σ_children_smoker'] = children_smoker
    smoker_nonsmoker_children_dict['Σ_children_nonsmoker'] = children_nonsmoker
    return smoker_nonsmoker_children_dict
smoker_children_dictionary(smoker_list, children_list)
#print(smoker_children_dictionary(smoker_list, children_list))

#------------------------------------------------
x_axis_smokers = ['smokers', 'non smokers']
y_axis_smoker_non_smoker_children = [smoker_nonsmoker_children_dict['Σ_children_smoker'], smoker_nonsmoker_children_dict['Σ_children_nonsmoker']]
def barchart_smoker_nonsmoker_vs_children(x_axis_smokers, y_axis_smoker_non_smoker_children): # This funtion plots a bar chart of region vs population
    plt.figure(num = 9,dpi = 600, figsize = (20, 11))# figsize(width, height) to change the size of the plot
    w = 0.4
    p1 = plt.bar(x_axis_smokers[0], y_axis_smoker_non_smoker_children [0], w, label='Smoker') # ec = 'black' parameter to enclose the bars if desired
    p2 = plt.bar(x_axis_smokers[1], y_axis_smoker_non_smoker_children [1], w, label='Non-Smoker')
    #p3 = plt.bar(bar3, y_region_total_population, w, label='Total population', ec = 'white', alpha = 0.3)# Using parameter alpha to make p3 transparent
    plt.xticks(x_axis_smokers, color='black', fontsize=12)
    #plt.grid()
    plt.title('09- Smoker-Non-Smoker Vs Σ_children', fontsize = 14)
    plt.xlabel('Smoker-Non-Smoker', fontsize = 14)
    plt.ylabel('Σ_children', fontsize = 14)
    plt.legend()
    plt.bar_label(p1, label_type = 'center', fontsize = 10)
    plt.bar_label(p2, label_type = 'center', fontsize = 10)
    #plt.bar_label(p3, label_type = 'edge', fontsize = 10)
    return plt.show
#barchart_smoker_nonsmoker_vs_children(x_axis_smokers, y_axis_smoker_non_smoker_children) 

#------------------------------------------------------------------------------
""" 10- What is the children-region distribution?"""
#  Create a dictionary of Σ_children for each in region ===> {'Region': {Σ_children}
region_num_of_children_dict = {}
def region_num_of_children_dictionary(region_list, children_list): # Funtion that creates the region_Σ_children dictionary
    for region, num in zip(region_list, children_list): # Iterate through the list containing region and children data
        if region not in region_num_of_children_dict:
            region_num_of_children_dict[region] = {'Σ_children': 0}
        if region in region_num_of_children_dict:
            region_num_of_children_dict[region]['Σ_children'] += num
    return region_num_of_children_dict
region_num_of_children_dictionary(region_list, children_list)
#print(region_num_of_children_dictionary(region_list, children_list))

#------------------------------------------------
y_axis_region_num_of_children = []
def fill_list_to_plot(region_num_of_children_dict):# This funtion fills the lists to plot the region-number_of_children chart
    for key in region_num_of_children_dict.keys():# Iterates through the region_num_children_dictionary and fills the lists that will be used to plot region_of_children barchart
        y_axis_region_num_of_children.append(region_num_of_children_dict[key]['Σ_children'])
    return y_axis_region_num_of_children 
fill_list_to_plot(region_num_of_children_dict)
#print(fill_list_to_plot(region_num_of_children_dict))

#------------------------------------------------
def barchart_region_vs_num_children(x_axis_regions, y_axis_region_num_of_children): # This funtion plots a bar chart of region vs population
    plt.figure(num = 10,dpi = 600, figsize = (20, 11))# figsize(width, height) to change the size of the plot
    w = 0.4
    p1 = plt.bar(x_axis_regions, y_axis_region_num_of_children, w, label='Smoker') # ec = 'black' parameter to enclose the bars if desired
    #p2 = plt.bar(x_axis_smokers[1], y_axis_smoker_non_smoker_children [1], w, label='Non-Smoker')
    #p3 = plt.bar(bar3, y_region_total_population, w, label='Total population', ec = 'white', alpha = 0.3)# Using parameter alpha to make p3 transparent
    plt.xticks(x_axis_regions, color='black', fontsize=12)
    #plt.grid()
    plt.title('10- Region Vs Σ_children', fontsize = 14)
    plt.xlabel('Region', fontsize = 14)
    plt.ylabel('Σ_children', fontsize = 14)
    #plt.legend()
    plt.bar_label(p1, label_type = 'center', fontsize = 10)
    #plt.bar_label(p2, label_type = 'center', fontsize = 10)
    #plt.bar_label(p3, label_type = 'edge', fontsize = 10)
    return plt.show
#barchart_region_vs_num_children(x_axis_regions, y_axis_region_num_of_children)

#------------------------------------------------------------------------------
""" 11- What is the smoker-region distribution?""" 
#  Create a dictionary of Σ_smokers for each in region ===> {'Region': {Σ_smokers}
region_smokers_dict = {}
def region_num_of_children_dictionary(region_list, smoker_list): # Funtion that creates the region_smoker dictionary
    for region, smoker in zip(region_list, smoker_list): # Iterate through the list containing region and smoker data
        if region not in region_smokers_dict:
            region_smokers_dict[region] = {'Σ_smokers': 0}
        if region in region_smokers_dict and smoker == 'yes':
            region_smokers_dict[region]['Σ_smokers'] += 1
    return region_smokers_dict
region_num_of_children_dictionary(region_list, smoker_list)
#print(region_num_of_children_dictionary(region_list, smoker_list))

#------------------------------------------------
y_axis_region_num_of_smokers = []
def fill_list_to_plot(region_smokers_dict):# This funtion fills the lists to plot the region-number_of_smokers
    for key in region_smokers_dict.keys():# Iterates through the region_smokers_dictionary and fills the lists that will be used to plot region_num_of_smokers
        y_axis_region_num_of_smokers.append(region_smokers_dict[key]['Σ_smokers'])
    return y_axis_region_num_of_smokers
fill_list_to_plot(region_smokers_dict)
#print(fill_list_to_plot(region_smokers_dict))

#------------------------------------------------
def barchart_region_vs_num_of_smokers(x_axis_regions, y_axis_region_num_of_smokers): # This funtion plots a bar chart of region vs population
    plt.figure(num = 11,dpi = 600, figsize = (20, 11))# figsize(width, height) to change the size of the plot
    w = 0.4
    p1 = plt.bar(x_axis_regions, y_axis_region_num_of_smokers, w, label='Smoker') # ec = 'black' parameter to enclose the bars if desired
    #p2 = plt.bar(x_axis_smokers[1], y_axis_smoker_non_smoker_children [1], w, label='Non-Smoker')
    #p3 = plt.bar(bar3, y_region_total_population, w, label='Total population', ec = 'white', alpha = 0.3)# Using parameter alpha to make p3 transparent
    plt.xticks(x_axis_regions, color='black', fontsize=12)
    #plt.grid()
    plt.title('11- Region Vs Σ_smokers', fontsize = 14)
    plt.xlabel('Region', fontsize = 14)
    plt.ylabel('Σ_smokers', fontsize = 14)
    #plt.legend()
    plt.bar_label(p1, label_type = 'center', fontsize = 10)
    #plt.bar_label(p2, label_type = 'center', fontsize = 10)
    #plt.bar_label(p3, label_type = 'edge', fontsize = 10)
    return plt.show
#barchart_region_vs_num_of_smokers(x_axis_regions, y_axis_region_num_of_smokers)

#------------------------------------------------------------------------------
""" 12- What is the age-region distribution?"""
region_age_percentage_dict = {}
def region_age_percentage_dictionary(age_list, region_list): # This funtion creates a dictioary that encloses all regions within an age and assigns a value of zero to each region
    for age, region in zip(age_list, region_list): # Iterate through the list containing age and region
        if age not in region_age_percentage_dict:
            region_age_percentage_dict[age] = {}
            region_age_percentage_dict[age] = {region : 0 for region in region_list if region not in region_age_percentage_dict[age]} # This comprehensive list adds the regions as keys within each internal dictionary
        if age in region_age_percentage_dict and region == 'southwest':
            region_age_percentage_dict[age]['southwest'] += 1
        if age in region_age_percentage_dict and region == 'southeast':
            region_age_percentage_dict[age]['southeast'] += 1
        if age in region_age_percentage_dict and region == 'northwest':
            region_age_percentage_dict[age]['northwest'] += 1
        if age in region_age_percentage_dict and region == 'northeast':
            region_age_percentage_dict[age]['northeast'] += 1
    return region_age_percentage_dict
region_age_percentage_dictionary(age_list, region_list)          
#print(region_age_percentage_dictionary(age_list, region_list))

#------------------------------------------------
sorted_region_age_percentage_dict = {}
def sort_dictionary_by_key(region_age_percentage_dictionary):# This funtion sorts the region_age_dict and returns a sorted dictionary
    sort = sorted(region_age_percentage_dict.items(), key = lambda t: t[0])# Here we sort the dictionary passed as a parameter to the funtion
    sorted_region_age_percentage_dict.update(sort)
    return sorted_region_age_percentage_dict
sort_dictionary_by_key(region_age_percentage_dict)
#print(sort_dictionary_by_key(region_age_percentage_dict))
  
#------------------------------------------------
y_axis_southwest = [] # Empty list that will contain the number of people of the southwest region
y_axis_southeast = [] # Empty list that will contain the number of people of the southeast region
y_axis_northwest = [] # Empty list that will contain the number of people of the northwest region
y_axis_northeast = [] # Empty list that will contain the number of people of the northeast region 
def fill_list_to_plot(sorted_region_age_percentage_dict):# This funtion fills the lists to plot the age-smoker chart
    for key in sorted_age_smoker_dict.keys():# Iterates through the sorted_age_smoker_dict and fills the lists that will be used to plot age Vs smoker barchart
        y_axis_southwest.append(sorted_region_age_percentage_dict[key]['southwest'])
        y_axis_southeast.append(sorted_region_age_percentage_dict[key]['southeast'])
        y_axis_northwest.append(sorted_region_age_percentage_dict[key]['northwest'])
        y_axis_northeast.append(sorted_region_age_percentage_dict[key]['northeast'])
    return y_axis_southwest, y_axis_southeast, y_axis_northwest, y_axis_northeast 
fill_list_to_plot(sorted_region_age_percentage_dict)
#print(fill_list_to_plot(sorted_region_age_percentage_dict))

#------------------------------------------------
def stacked_barchart_region_population_vs_age(x_axis_age, y_axis_southwest, y_axis_southeast, y_axis_northwest, y_axis_northeast):# This funtion plots a stacked bar chart of age vs population
    plt.figure(num = 12,dpi = 600, figsize = (15, 11))
    bottom_northwest = [a+b for a,b in zip(y_axis_southwest, y_axis_southeast )]
    bottom_northeast = [a+b for a,b in zip(bottom_northwest, y_axis_northwest)]
    p1 = plt.bar(x_axis_age, y_axis_southwest, width = 0.5, label='southwest') # ec = 'black' parameter to enclose the bars if desired
    p2 = plt.bar(x_axis_age, y_axis_southeast, width = 0.5, bottom = y_axis_southwest,  label='southeast')
    p3 = plt.bar(x_axis_age, y_axis_northwest, width = 0.5, bottom = bottom_northwest,  label='northwest')
    p4 = plt.bar(x_axis_age, y_axis_northeast, width = 0.5, bottom = bottom_northeast,  label='northeast')
    p5 = plt.bar(x_axis_age, y_axis_population, width = 0.5, label='', ec = 'white', alpha = 0)# Using parameter alpha to make p3 transparent
    plt.xticks(x_axis_age, color='black', fontsize=8)
    #plt.grid()
    plt.title('12- Age Vs Population size (region)', fontsize = 12)
    plt.xlabel('Age', fontsize = 12)
    plt.ylabel( 'Population size (region)', fontsize = 12)
    plt.legend()
    plt.bar_label(p1, label_type = 'center', fontsize = 6)
    plt.bar_label(p2, label_type = 'center', fontsize = 6)
    plt.bar_label(p3, label_type = 'center', fontsize = 6)
    plt.bar_label(p4, label_type = 'center', fontsize = 6)
    plt.bar_label(p5, label_type = 'edge', fontsize = 8)
    return plt.show
#stacked_barchart_region_population_vs_age(x_axis_age, y_axis_southwest, y_axis_southeast, y_axis_northwest, y_axis_northeast)

#------------------------------------------------------------------------------
""" 13- If we group charges by age which pays more in terms of nominal value and percentage?"""
age_sum_charges_dict = {}
def age_sum_charges_dictionary(age_list, charges_list): # This funtion creates a dictioary that contains the sum of charges by age and the percentage that it represents from all charges
    for age, charge in zip(age_list, charges_list):
        if age not in age_sum_charges_dict:
            age_sum_charges_dict[age] = {'Σ_charges_by_age': 0, '%_of_total_charges_by_age': 0}
        elif age in age_sum_charges_dict:
            age_sum_charges_dict[age]['Σ_charges_by_age'] += charge
    for key in age_sum_charges_dict.keys():
        age_sum_charges_dict[key]['Σ_charges_by_age'] = round(age_sum_charges_dict[key]['Σ_charges_by_age'], 2)
        age_sum_charges_dict[key]['%_of_total_charges_by_age'] = round((age_sum_charges_dict[key]['Σ_charges_by_age'] / sum_total_charges) * 100, 2)
    return age_sum_charges_dict
age_sum_charges_dictionary(age_list, charges_list)
#print(age_sum_charges_dictionary(age_list, charges_list))

#------------------------------------------------
sorted_age_sum_charges_dict = {}
def sort_dictionary_by_key(age_sum_charges_dict):# This funtion sorts the age_sum_charges_dict and returns a sorted dictionary
    sort = sorted(age_sum_charges_dict.items(), key = lambda t: t[0])# Here we sort the dictionary passed as a parameter to the funtion
    sorted_age_sum_charges_dict.update(sort)
    return sorted_age_sum_charges_dict
sort_dictionary_by_key(age_sum_charges_dict)
#print(sort_dictionary_by_key(age_sum_charges_dict))

#------------------------------------------------
y_axis_sum_charges_by_age = []
y_axis_percentage_charges_by_age = []
def fill_list_to_plot(sorted_age_sum_charges_dict):# This funtion fills the lists to plot the region-number_of_smokers
    for key in sorted_age_sum_charges_dict.keys():# Iterates through the region_smokers_dictionary and fills the lists that will be used to plot region_num_of_smokers
        y_axis_sum_charges_by_age.append(sorted_age_sum_charges_dict[key]['Σ_charges_by_age'])
        y_axis_percentage_charges_by_age.append(sorted_age_sum_charges_dict[key]['%_of_total_charges_by_age'])
    return y_axis_sum_charges_by_age , y_axis_percentage_charges_by_age
fill_list_to_plot(sorted_age_sum_charges_dict)
#print(fill_list_to_plot(sorted_age_sum_charges_dict))

#------------------------------------------------
def barchart_age_sum_charges(x_axis_age, y_axis_percentage_charges_by_age, y_axis_sum_charges_by_age):# This funtion plots a bar chart of age vs BMI average
    plt.figure(num = 13,dpi = 600, figsize = (25, 11)) # figsize(width, height) to change the size of the plot
    p1 = plt.bar(x_axis_age, y_axis_percentage_charges_by_age, width = 0.5, align = 'center', label='% of total charges')
    #p2 = plt.bar(x_axis_age, y_axis_sum_charges_by_age, width = 0.5, align = 'center', label='Σ_charges', alpha = 0.5)
    plt.xticks(x_axis_age, color='black', fontsize=10)
    #plt.ylim(0, 35)
    plt.title('13- Age Vs % of total charges', fontsize = 14)
    plt.xlabel('Age', fontsize = 14)
    plt.ylabel('% of total charges', fontsize = 14)
    plt.legend()
    plt.bar_label(p1, label_type = 'edge', fontsize = 8)
    #plt.bar_label(p2, label_type = 'edge', fontsize = 8)
    return plt.show
#barchart_age_sum_charges(x_axis_age, y_axis_percentage_charges_by_age, y_axis_sum_charges_by_age)     

#------------------------------------------------------------------------------
""" 14- Which region pays more charges in terms of totals and percentage?"""       
region_sum_charges_dict = {}
def region_sum_charges_dictionary(region_list, charges_list): # This funtion creates a dictioary that contains the sum of charges by region and the percentage that it represents from all charges
    for region, charge in zip(region_list, charges_list):
        if region not in region_sum_charges_dict:
            region_sum_charges_dict[region] = {'Σ_charges_region': 0, '% of total charges': 0}
        elif region in region_sum_charges_dict:
            region_sum_charges_dict[region]['Σ_charges_region'] += charge
    for key in region_sum_charges_dict.keys():
        region_sum_charges_dict[key]['Σ_charges_region'] = round(region_sum_charges_dict[key]['Σ_charges_region'], 2)
        region_sum_charges_dict[key]['% of total charges'] = round((region_sum_charges_dict[key]['Σ_charges_region'] / sum_total_charges) * 100, 2)
    return region_sum_charges_dict
region_sum_charges_dictionary(region_list, charges_list)
#print(region_sum_charges_dictionary(region_list, charges_list))

#------------------------------------------------
y_axis_sum_charges_by_region = []
y_axis_percentage_charges_by_region = []
def fill_list_to_plot(region_sum_charges_dict):# This funtion fills the lists to plot the region_sum_charges_plot
    for key in region_sum_charges_dict.keys():# Iterates through the region_sum_charges_dictionary and fills the lists that will be used to plot region_sum_of_charges
        y_axis_sum_charges_by_region.append(region_sum_charges_dict[key]['Σ_charges_region'])
        y_axis_percentage_charges_by_region.append(region_sum_charges_dict[key]['% of total charges'])
    return y_axis_sum_charges_by_region , y_axis_percentage_charges_by_region
fill_list_to_plot(region_sum_charges_dict)
#print(fill_list_to_plot(region_sum_charges_dict))

#------------------------------------------------
def barchart_region_sum_charges(x_axis_regions, y_axis_percentage_charges_by_region, y_axis_sum_charges_by_region):# This funtion plots a bar chart of region vs % of total charges
    plt.figure(num = 14,dpi = 600, figsize = (25, 11)) # figsize(width, height) to change the size of the plot
    p1 = plt.bar(x_axis_regions, y_axis_percentage_charges_by_region, width = 0.5, align = 'center', label='% of total charges')
    #p2 = plt.bar(x_axis_regions, y_axis_sum_charges_by_region, width = 0.5, align = 'center', label='Σ_charges_Region', alpha = 0.5)
    plt.xticks(x_axis_regions, color='black', fontsize=10)
    #plt.ylim(0, 35)
    plt.title('14- Region Vs % of total charges', fontsize = 14)
    plt.xlabel('Region', fontsize = 14)
    plt.ylabel('% of total charges', fontsize = 14)
    plt.legend()
    plt.bar_label(p1, label_type = 'edge', fontsize = 14)
    #plt.bar_label(p2, label_type = 'edge', fontsize = 8)
    return plt.show
#barchart_region_sum_charges(x_axis_regions, y_axis_percentage_charges_by_region, y_axis_sum_charges_by_region)        

#------------------------------------------------------------------------------
""" 15- If we group smokers and non-smokers who pays more charges in terms of totals and percentage?"""         
smoker_sum_charges_dict = {'smoker': {'Σ_charges': 0, '% of total charges': 0, 'average_payment': 0}, 'non_smoker': {'Σ_charges': 0, '% of total charges': 0, 'average_payment': 0}}
def smoker_sum_charges_dictionary(smoker_list, charges_list): # This funtion creates a dictioary that contains the sum of charges by smokers and non smokers and the percentage that it represents from all charges
    for smoker, charges in zip(smoker_list, charges_list):
        if smoker  == 'yes':
            smoker_sum_charges_dict['smoker']['Σ_charges'] += charges
        if smoker  == 'no':
            smoker_sum_charges_dict['non_smoker']['Σ_charges'] += charges
    for key in smoker_sum_charges_dict.keys():
        smoker_sum_charges_dict[key]['Σ_charges'] = round(smoker_sum_charges_dict[key]['Σ_charges'], 2)
        smoker_sum_charges_dict[key]['% of total charges'] = round((smoker_sum_charges_dict[key]['Σ_charges'] / sum_total_charges) * 100, 2)
    smoker_sum_charges_dict['smoker']['average_payment'] = round((smoker_sum_charges_dict[key]['Σ_charges'] / sum_smokers), 2)
    smoker_sum_charges_dict['non_smoker']['average_payment'] = round((smoker_sum_charges_dict[key]['Σ_charges'] / sum_nonsmokers), 2)
    return smoker_sum_charges_dict
smoker_sum_charges_dictionary(smoker_list, charges_list)
#print(smoker_sum_charges_dictionary(smoker_list, charges_list))     
 
#------------------------------------------------
y_axis_sum_charges_by_smoker = []
y_axis_percentage_charges_by_smoker = []
y_axis_average_charges_smoker = []
def fill_list_to_plot(smoker_sum_charges_dict):# This funtion fills the lists to plot the smoker_% of total charges
    for key in smoker_sum_charges_dict.keys():# Iterates through the smoker_sum_charges_dictionary and fills the lists that will be used to plot Smoker / Non Smokers Vs % of total charges
        y_axis_sum_charges_by_smoker.append(smoker_sum_charges_dict[key]['Σ_charges'])
        y_axis_percentage_charges_by_smoker.append(smoker_sum_charges_dict[key]['% of total charges'])
        y_axis_average_charges_smoker.append(smoker_sum_charges_dict[key]['average_payment'])
    return y_axis_sum_charges_by_smoker , y_axis_percentage_charges_by_smoker, y_axis_average_charges_smoker 
fill_list_to_plot(smoker_sum_charges_dict)
#print(fill_list_to_plot(smoker_sum_charges_dict))       

#------------------------------------------------
def barchart_smoker_sum_charches(x_axis_smokers, y_axis_percentage_charges_by_smoker, y_axis_average_charges_smoker, y_axis_sum_charges_by_smoker):# This funtion plots a bar chart of Smoker / Non Smokers vs Average Payment
    plt.figure(num = 15,dpi = 600, figsize = (25, 11)) # figsize(width, height) to change the size of the plot
    #p1 = plt.bar(x_axis_smokers, y_axis_percentage_charges_by_smoker, width = 0.5, align = 'center', label='% of total charges')
    p2 = plt.bar(x_axis_smokers, y_axis_average_charges_smoker, width = 0.5, align = 'center', label='Average Payment')
    #p3 = plt.bar(x_axis_regions, y_axis_sum_charges_by_region, width = 0.5, align = 'center', label='Σ_charges_Region', alpha = 0.5)
    plt.xticks(x_axis_smokers, color='black', fontsize=10)
    #plt.ylim(0, 35)
    plt.title('15- Smoker / Non Smoker Vs Average Payment', fontsize = 14)
    plt.xlabel('Smoker / Non Smoker', fontsize = 14)
    plt.ylabel('Average Payment', fontsize = 14)
    plt.legend()
    #plt.bar_label(p1, label_type = 'edge', fontsize = 14)
    plt.bar_label(p2, label_type = 'edge', fontsize = 14)
    #plt.bar_label(p3, label_type = 'edge', fontsize = 8)
    return plt.show
#barchart_smoker_sum_charches(x_axis_smokers, y_axis_percentage_charges_by_smoker, y_axis_average_charges_smoker, y_axis_sum_charges_by_smoker)        

#------------------------------------------------------------------------------
""" 16- Do people that have more children pays more charges?"""         
#  Create a dictionary that groups average payment (the mean) within each number of children
num_children_average_payment_dict = {}
def num_children_average_payment_dictionary(children_list, charges_list): # Funtion that creates a key = number of children and a value average payment for each number of children
    for num, charges in zip(children_list, charges_list): # Iterate through the lists containing number of children and charges data
        if num not in num_children_average_payment_dict:
            num_children_average_payment_dict[num] = {'times_repeated': 0, 'Σ_charges': 0, 'average_payment': 0, '%_of_total_charges': 0}
        if num in num_children_average_payment_dict:
            num_children_average_payment_dict[num]['Σ_charges'] += charges
            num_children_average_payment_dict[num]['times_repeated'] += 1
    for num in num_children_average_payment_dict.keys(): # Itarate through the num_children_average_payment_dict to add the average payment value within each children age
        num_children_average_payment_dict[num]['Σ_charges'] = round(num_children_average_payment_dict[num]['Σ_charges'], 2) # rounds up Σ_charges
        num_children_average_payment_dict[num]['average_payment'] = round((num_children_average_payment_dict[num]['Σ_charges'] / num_children_average_payment_dict[num]['times_repeated']) ,2) # Calculates average payment for the especific age
        num_children_average_payment_dict[num]['%_of_total_charges'] = round((num_children_average_payment_dict[num]['Σ_charges'] / sum_total_charges) * 100 ,2) # Calculates the % of the total of the sum of all charges for the especific age
    return num_children_average_payment_dict
num_children_average_payment_dictionary(children_list, charges_list)
#print( num_children_average_payment_dictionary(children_list, charges_list))

#------------------------------------------------
sorted_num_children_average_payment_dict = {}
def sort_dictionary_by_key(num_children_average_payment_dict):# This funtion sorts the num_children_average_payment_dict and returns a sorted dictionary
    sort = sorted(num_children_average_payment_dict.items(), key = lambda t: t[0])# Here we sort the dictionary passed as a parameter to the funtion
    sorted_num_children_average_payment_dict.update(sort)
    return sorted_num_children_average_payment_dict 
sort_dictionary_by_key(num_children_average_payment_dict)
#print(sort_dictionary_by_key(num_children_average_payment_dict))  

#------------------------------------------------
y_axis_average_payment_num_children = []# Empty list that will contain the average payment of each age of chuldren_average_payment dictionary
y_axis_percentage_of_total_charges_num_children = [] # Empty list that will contain the totals in terms of percentage of each age of the chlldren_average_payment dictionary
def fill_list_to_plot(sorted_num_children_average_payment_dictionary):# This funtion fills the lists to plot the num_of_children vs average payment barchart
    for key in sorted_num_children_average_payment_dict.keys():# Iterates through the num_children_average_payment_dictionary and fills the lists that will be used to plot num_of_children vs average payment barchart
        y_axis_average_payment_num_children.append(sorted_num_children_average_payment_dict[key]['average_payment'])
        y_axis_percentage_of_total_charges_num_children.append(sorted_num_children_average_payment_dict[key]['%_of_total_charges'])
    return y_axis_average_payment_num_children, y_axis_percentage_of_total_charges_num_children
fill_list_to_plot(sorted_num_children_average_payment_dict)
#print(fill_list_to_plot(sorted_num_children_average_payment_dict))

#------------------------------------------------
def barchart_num_chilcren_vs_average_payment(x_axis_num_children, y_axis_average_payment_num_children): # This funtion plots a bar chart of number of children vs average payment
    plt.figure(num = 16,dpi = 600, figsize = (20, 11))# figsize(width, height) to change the size of the plot
    w = 0.4
    p1 = plt.bar(x_axis_num_children, y_axis_average_payment_num_children, w) # ec = 'black' parameter to enclose the bars if desired
    #p2 = plt.bar(x_axis_smokers[1], y_axis_average_bmi_smoker_non_smoker[1], w, label='Non-Smoker')
    #p3 = plt.bar(bar3, y_region_total_population, w, label='Total population', ec = 'white', alpha = 0.3)# Using parameter alpha to make p3 transparent
    plt.xticks(x_axis_num_children, color='black', fontsize=12)
    #plt.grid()
    plt.title('16- Number of children Vs Average Payment', fontsize = 14)
    plt.xlabel('Number of children', fontsize = 14)
    plt.ylabel('Average Payment', fontsize = 14)
    #plt.legend()
    plt.bar_label(p1, label_type = 'center', fontsize = 10)
    #plt.bar_label(p2, label_type = 'center', fontsize = 10)
    #plt.bar_label(p3, label_type = 'edge', fontsize = 10)
    return plt.show
#barchart_num_chilcren_vs_average_payment(x_axis_num_children, y_axis_average_payment_num_children)     

#------------------------------------------------------------------------------
"""  17- Do people with BMI higher than average pay more that those with BMI lower than average?"""
#  Create a dictionary that groups average payment (the mean) within two gropus (BMI lower than average and BMI higher than average)
bmi_average_payment_average_dict = {'bmi_bellow_average':{'Σ_charges': 0, 'Σ_people': 0, 'average_payment': 0}, 'bmi_above_average':{'Σ_charges': 0, 'Σ_people': 0, 'average_payment': 0}}
def bmi_average_payment_average_dictionary(bmi_list, charges_list):
    for bmi, charges in zip(bmi_list, charges_list): # Iterate through the lists containing bmi and charges data
        if bmi < average_bmi:
            bmi_average_payment_average_dict['bmi_bellow_average']['Σ_charges'] += charges
            bmi_average_payment_average_dict['bmi_bellow_average']['Σ_people'] += 1
        if bmi > average_bmi:
           bmi_average_payment_average_dict['bmi_above_average']['Σ_charges'] += charges
           bmi_average_payment_average_dict['bmi_above_average']['Σ_people'] += 1
    for key in bmi_average_payment_average_dict.keys(): # Itarate through the bmi_average_payment_average_dict to add the average payment
        bmi_average_payment_average_dict[key]['Σ_charges'] = round(bmi_average_payment_average_dict[key]['Σ_charges'], 2) # rounds up Σ_charges
        bmi_average_payment_average_dict[key]['average_payment'] = round((bmi_average_payment_average_dict[key]['Σ_charges'] / bmi_average_payment_average_dict[key]['Σ_people']) ,2) # Calculates average payment each key
    return bmi_average_payment_average_dict
bmi_average_payment_average_dictionary(bmi_list, charges_list)
#print( bmi_average_payment_average_dictionary(bmi_list, charges_list))

#------------------------------------------------
x_axis_bmi_bellow_above_average = []
y_axis_average_payment_bmi_average = []# Empty list that will contain the average payment of people bellow and above average bmi
def fill_list_to_plot(bmi_average_payment_average_dict):# This funtion fills the lists to plot the bmi average vs average payment barchart
    for key in bmi_average_payment_average_dict.keys():# Iterates through the bmi_average_payment_average_dictionary and fills the lists that will be used to plot BMI average vs average payment
        x_axis_bmi_bellow_above_average.append(key)
        y_axis_average_payment_bmi_average.append(bmi_average_payment_average_dict[key]['average_payment'])
    return x_axis_bmi_bellow_above_average, y_axis_average_payment_bmi_average
fill_list_to_plot(bmi_average_payment_average_dict)
#print(fill_list_to_plot(bmi_average_payment_average_dict))       

#------------------------------------------------
def barchart_bmi_average_payment_average(x_axis_bmi_bellow_above_average, y_axis_average_payment_bmi_average): # This funtion plots a bar chart of number of children vs average payment
    plt.figure(num = 17,dpi = 600, figsize = (20, 11))# figsize(width, height) to change the size of the plot
    w = 0.4
    p1 = plt.bar(x_axis_bmi_bellow_above_average, y_axis_average_payment_bmi_average, w) # ec = 'black' parameter to enclose the bars if desired
    #p2 = plt.bar(x_axis_smokers[1], y_axis_average_bmi_smoker_non_smoker[1], w, label='Non-Smoker')
    #p3 = plt.bar(bar3, y_region_total_population, w, label='Total population', ec = 'white', alpha = 0.3)# Using parameter alpha to make p3 transparent
    plt.xticks(x_axis_bmi_bellow_above_average, color='black', fontsize=12)
    #plt.grid()
    plt.title('17- BMI Bellow/Above average Vs Average Payment', fontsize = 14)
    plt.xlabel('BMI Bellow/Above average', fontsize = 14)
    plt.ylabel('Average Payment', fontsize = 14)
    #plt.legend()
    plt.bar_label(p1, label_type = 'center', fontsize = 10)
    #plt.bar_label(p2, label_type = 'center', fontsize = 10)
    #plt.bar_label(p3, label_type = 'edge', fontsize = 10)
    return plt.show
#barchart_bmi_average_payment_average(x_axis_bmi_bellow_above_average, y_axis_average_payment_bmi_average)       
        
#------------------------------------------------------------------------------        
""" B- Draw conclusions and make recommendation"""
print("""     There are {} males and {} females, {} people in total, the overall average age is {};
     {} are smokers and {} are non-smokers, the largest percentage of smokers are {} old and represent {}% 
     of the total smokers followed by {} years old and {} years old with {}%, average BMI of smokers and
     non smokers have no relevant difference, the region with the gratest number of smokers is {} with 
     {} smokers, ages go from {} old to {} years old, please see barcharts 1, 2, 3, 5, and 11 for more detail.
     """.format(sum_males_dataset, sum_females_dataset, total_population_dataset, average_age, sum_smokers, sum_nonsmokers, x_axis_age[1], y_total_smoker_percentage[1], x_axis_age[0], x_axis_age[25], y_total_smoker_percentage[0], x_axis_regions[1], y_axis_region_num_of_smokers[1], x_axis_age[0], x_axis_age[46]  ))
     
print("""     Regarding population distribution, {} people live in the {} region, {} in the {} region,
     {} in the {} region and {} in the {} region, the bmi average is {}, the region with the 
     highest average BMI is {} with a BMI of {}, average BMI does not vary as people have more children, 
     the region with the highest number of children is {} with {} children, please see 
     barcharts 4, 6, 7, 8, 9, 10 and 12 for more detail. 
     """.format(y_region_total_population[0] ,x_axis_regions[0], y_region_total_population[1] , x_axis_regions[1], y_region_total_population[2], x_axis_regions[2], y_region_total_population[3], x_axis_regions[3],average_bmi, x_axis_regions[1], y_axis_average_bmi_region[1],x_axis_regions[1], y_axis_region_num_of_children[1] ))      

print("""     Since {} year old have the bigest number of smokers and the second highest population size {} people 
     in total, they also have the largest percentage of the sum of all charges, smoking and BMI are the 
     most influential for an individual’s medical insurance charges, The average yearly medical insurance
     charge per individual is {} USD, please see barcharts 13, 14, 15, 16 and 17.
     """.format(x_axis_age[1], y_axis_population[1], average_charges))        
        
        
#stacked_barchart_age_vs_population(x_axis_age, y_axis_population) # 01

#barchart_age_vs_BMI_average(x_axis_age, y_axis_bmi_average) # 02

#stacked_barchart_age_vs_smoker(x_axis_age, y_total_smoker_percentage, y_male_smoker_percentage, y_female_smoker_percentage ) # 03

#multiple_barchart_region_vs_population(x_axis_regions, y_region_male_population, y_region_female_population) # 04

#barchart_smoker_vs_average_bmi(x_axis_smokers) # 05

#barchart_region_vs_bmi(x_axis_regions, y_axis_average_bmi_region) # 06

#barchart_num_chilcren_vs_average_bmi(x_axis_num_children, y_axis_average_bmi_num_children) # 07

#barchart_age_num_chilcren(x_axis_age, y_axis_num_of_children_by_age) # 08

#barchart_smoker_nonsmoker_vs_children(x_axis_smokers, y_axis_smoker_non_smoker_children) # 09

#barchart_region_vs_num_children(x_axis_regions, y_axis_region_num_of_children) # 10

#barchart_region_vs_num_of_smokers(x_axis_regions, y_axis_region_num_of_smokers) # 11

#stacked_barchart_region_population_vs_age(x_axis_age, y_axis_southwest, y_axis_southeast, y_axis_northwest, y_axis_northeast) # 12

#barchart_age_sum_charges(x_axis_age, y_axis_percentage_charges_by_age, y_axis_sum_charges_by_age) # 13

#barchart_region_sum_charges(x_axis_regions, y_axis_percentage_charges_by_region, y_axis_sum_charges_by_region) # 14

#barchart_smoker_sum_charches(x_axis_smokers, y_axis_percentage_charges_by_smoker, y_axis_average_charges_smoker, y_axis_sum_charges_by_smoker) # 15

#print( num_children_average_payment_dictionary(children_list, charges_list)) # 16

#barchart_bmi_average_payment_average(x_axis_bmi_bellow_above_average, y_axis_average_payment_bmi_average) # 17





















