class Country:
    #class variable lists and dictionaries where instance variable values can be collected to determine the maximum value and maximum index.
    _country_name_list=[]
    _country_areas_list=[]
    _country_population_list=[]
    _country_density_list=[]

    _country_areas_dict={}
    _country_population_dict={}
    _country_density_dict={}


    # In the constructor we create the selected instance variables: name, area and population
    #Moreover we add these values to the class variable lists and dictionaries
    #@params name - name of the country, area - area of the country in million square kms, population - population of the country in millions

    def __init__(self, name, area, population):
        self._name=name
        self._area=area
        self._population=population
        density=round(population/area,2)

        Country._country_areas_list.append(self._area)
        Country._country_population_list.append(self._population)
        Country._country_density_list.append(density)
        Country._country_name_list.append(self._name)

        Country._country_areas_dict[self._name]=self._area
        Country._country_population_dict[self._name]=self._population
        Country._country_density_dict[self._name]=density

    #To get the country with maximum area, population and density I defined class methods to get the value of the class variables
    #The first 3 class methods represent the list based solution the last 3 class methods use the class dictionaries.
    #These methods print both the name of the country and the maximum value
    @classmethod
    def getLargestAreaList(cls):
        maxvalue=max(Country._country_areas_list)
        idx=Country._country_areas_list.index(maxvalue)
        country_name=Country._country_name_list[idx]
        print(f"{country_name} has the largest area with {maxvalue} million square kilometers.")

    @classmethod
    def getLargestPopulationList(cls):
        maxvalue=max(Country._country_population_list)
        idx=Country._country_population_list.index(maxvalue)
        country_name=Country._country_name_list[idx]
        print(f"{country_name} has the largest population with {maxvalue} million people.") 
        
    @classmethod
    def getLargestDensityList(cls):
        maxvalue=max(Country._country_density_list)
        idx=Country._country_density_list.index(maxvalue)
        country_name=Country._country_name_list[idx]
        print(f"{country_name} has the largest population density with {maxvalue} person per square kilometer.") 



    #these class methods use the class dictionaries to get the maximum
    @classmethod
    def getLargestAreaDict(cls):
        country_name=max(Country._country_areas_dict, key=Country._country_areas_dict.get)
        maxvalue=max(Country._country_areas_dict.values())
        print(f"{country_name} has the largest area with {maxvalue} million square kilometers.")

    @classmethod
    def getLargestPopulationDict(cls):
        country_name=max(Country._country_population_dict, key=Country._country_population_dict.get)
        maxvalue=max(Country._country_population_dict.values())
        print(f"{country_name} has the largest population with {maxvalue} million people.") 
        
    @classmethod
    def getLargestDensityDict(cls):
        country_name=max(Country._country_density_dict, key=Country._country_density_dict.get)
        maxvalue=max(Country._country_density_dict.values())
        print(f"{country_name} has the largest population density with {maxvalue} person per square kilometer.") 






        