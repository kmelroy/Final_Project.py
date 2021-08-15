print ("Welcome to my Final Project")
print ("---------------------------")
import requests

#API Key Information
def get_weather_data (zip=None, city=None):
    siteUrl = "http://api.openweathermap.org/data/2.5/weather?units=imperial"
    apiid = "e2feddb3d6d51d0b53960cc9851c14dc"

    if zip is not None:
      siteUrl += "&zip="+str(zip)+",us"
    else:
      siteUrl += "&q="+str(city)+",us"
    siteUrl += "&appid="+str(apiid)
    r = requests.get(siteUrl)
    return r
#Displaying results
def display(response):
    if response.status_code == 200:
        data = response.json()
        print("")
        #Tell information from host avaliable
        print("Connection to Weather Server Successful: ")
        print("")
        print ((f"""{data['name']} Weather Forecast:
        Condition Type: {data['weather'][0]['description']}
        Wind Speed : {data['wind']['speed']} mph
        Min Temp : {data['main']['temp_min']} F
        Max Temp : {data['main']['temp_max']} F
        """))
    #Creating a loop
    else:
        print("Connection to Weather Server NOT successful:")
        print("Request Failed, Error : ", response.status_code),
        print("Please Try Again")
        print("---------------------------")
        print("")

#Main menu function
def menu():
    while True:
        choice = int(
        input("Enter one of the following numbers to search weather data :\n1. Zip Code\n2. City Name\n3. Exit\n"))

        if choice == 1:
          print("")
          try:
            zipCode = int(input("Enter a valid 5 digit zip code : "))
            response = get_weather_data(zipCode, None)
            print("-----------------------------------------")
            display(response)
          except Exception as ex:
            print("Error : ", ex)
        elif choice == 2:
          print("")
          try:
            cityname = input("Enter a valid city name : ")
            response = get_weather_data(None, cityname)
            print("-----------------------------------------")
            display(response)
          except Exception as ex:
            print("Error : ", ex)
        elif choice == 3:
          break
        else:
          print("")
          print("Invalid Selection, please try again...\n")
          print("===================================")
          print("")

#Run Function
if __name__ == "__main__":
    menu()
