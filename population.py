city_name = "Istanbul,Turkey"
pop_1927 = 691000
pop_2017 = 15029231
pop_change = pop_2017 - pop_1927
percentage_gr = (pop_change/pop_1927) * 100
annual_gr = percentage_gr/(2017-1927)
def population_growth(year_one=1927,year_two=2017,population_one=691000,population_two=15029231):
    growth_rate = annual_gr
    return growth_rate

print(annual_gr)    
set_one = population_growth()
print(set_one)
