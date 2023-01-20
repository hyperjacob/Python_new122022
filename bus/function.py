def read_data_from_file(name):
    result = []
    with open(name, 'r', encoding='utf8') as datafile:
        for line in datafile:
            result.append(line.strip('\n').split(", "))
        return result


def save_data_to_file(name, data_list):
    data = name[:-4] + str(len(read_data_from_file(name))+1) + ', ' + data_list + '\n'
    with open(name, 'a', encoding='utf8') as datafile:
        datafile.write(data)
    print(f"Data was saved successfully: {data}")


def print_buses():
    bus_list = read_data_from_file("bus.txt")
    print('List of buses:')
    for num, el in enumerate(bus_list):
        print(f"{num + 1} - Bus with number: {el[1]}")
    print()


def add_bus():
    save_data_to_file("bus.txt", input("Enter bus number: "))


def print_drivers():
    driver_list = read_data_from_file("driver.txt")
    print('List of drivers:')
    for num, el in enumerate(driver_list):
        print(f"{num + 1} - Last name driver: {el[1]}")
    print()


def add_driver():
    save_data_to_file("driver.txt", input("Enter drivers surname: "))


def print_routes():
    driver_list = read_data_from_file("driver.txt")
    bus_list = read_data_from_file("bus.txt")
    route_list = read_data_from_file("route.txt")
    print('List of routes:')
    num_route = ""
    num_bus = ""
    sur_driver = ""
    for num, route in enumerate(route_list):
        num_route = route[1]
        for bus in bus_list:
            if bus[0] == route[2]:
                num_bus = bus[1]
        for driver in driver_list:
            if driver[0] == route[3]:
                sur_driver = driver[1]
        print(f"{num + 1} Number of route: {num_route}, Number of bus: {num_bus}, Last name driver: {sur_driver}")
    print()


def add_route():
    num_route = input("Enter number of route: ")
    bus = ""
    driver = ""
    print_buses()
    try:
        num_bus = int(input("Select number of bus: "))
    except:
        return print("Wrong number")
    bus_list = read_data_from_file("bus.txt")
    if num_bus > len(bus_list):
        return print("Wrong number")
    print_drivers()
    try:
        num_driver = int(input("Select number of driver: "))
    except:
        return print("Wrong number")
    driver_list = read_data_from_file("driver.txt")
    if num_driver > len(driver_list):
        return print("Wrong number")
    for i in range(len(bus_list)):
        if i + 1 == num_bus:
            bus = bus_list[i][0]
    for j in range(len(driver_list)):
        if j + 1 == num_driver:
            driver = driver_list[j][0]
    save_data_to_file("route.txt", num_route + ", " + bus + ", " + driver)
