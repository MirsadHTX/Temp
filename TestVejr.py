from weather import Weather, Unit
weather = Weather(unit=Unit.CELSIUS)

# Lookup WOEID via http://weather.yahoo.com.

##lookup = weather.lookup(560743)
#condition = lookup.condition
#print(condition.text)

# Lookup via location name.
#Mirsad
location = weather.lookup_by_location('aarhus')
condition = location.condition
print(condition.text)
print(condition.date)
print(condition.temp)
#print(condition.code)



# Get weather forecasts for the upcoming days.

#forecasts = location.forecast
#for forecast in forecasts:
#    print(forecast.text)
#    print(forecast.date)
#    print(forecast.high)
#    print(forecast.low)


# Lookup via latitude and longitude

#w = Weather(Unit.CELSIUS)
#lookup = w.lookup_by_latlng(53.3494,-6.2601)
#condition = lookup.condition
#print(condition.text)