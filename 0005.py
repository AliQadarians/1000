wind_speed = float(input('Enter wind spead(km/s): '))
temperatur = float(input('Enter temperatur(celsius): '))
wind_childe = 13.12 + 0.6215 * temperatur - 11.37 * (wind_speed ** 0.16) + 0.3965 * temperatur * (wind_speed ** 0.16)

print('The wind spead index is {} .'.format(round(wind_childe,1)))