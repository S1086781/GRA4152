def Country_test():
    from Country import Country
    import argparse

    parser=argparse.ArgumentParser(description="""The Country class is created to add and store the parameters of countries such as name, area, population and density. The user can get the country with the largest area, population, density by both list and dictionary based solution.
                                   
                                   This class only includes class methods:
                                   Constructor - creates name, area, population instance variables and appends variables to class lists and dictionaries.
                                   Method 1-3 - getLargestAreaList, getLargestPopulationList, getLargestDensityList - these methods print the country name and the largest value from the class variable list.
                                   Method 4-6 -  getLargestAreaDict, getLargestPopulationDict, getLargestDensityDict - these methods print the country name and the largest value from the class variable dictionary.

                                   Input parameters: name - name of the country, area - area of the country in million square kms, population - population of the country in millionsname - name of the country, area - area of the country in million square kms, population - population of the country in millions
                                   """)
    
    parser.parse_args()
    

    Norway=Country('Norway', 0.385, 5.5 )
    Sweden=Country('Sweden', 0.447, 10.5)
    Netherlands=Country('Netherlands', 0.041, 17.9)

    Country.getLargestAreaList()
    Country.getLargestPopulationList()
    Country.getLargestDensityList()
    print("\n\nExpected:Sweden has the largest area with 0.447 million square kilometers.\nNetherlands has the largest population with 17.9 million people.\nNetherlands has the largest population density with 436.59 person per square kilometer.\n\n")

    Country.getLargestAreaDict()
    Country.getLargestPopulationDict()
    Country.getLargestDensityDict()
    print("\n\nExpected:Sweden has the largest area with 0.447 million square kilometers.\nNetherlands has the largest population with 17.9 million people.\nNetherlands has the largest population density with 436.59 person per square kilometer.\n\n")

Country_test()