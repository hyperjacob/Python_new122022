from menu import Menu
import function as fn

if __name__ == "__main__":

    # основной блок
    menuitems = [
        ("1", "Show list of buses", fn.print_buses),
        ("2", "Add new bus", fn.add_bus),
        ("3", "Show list of drivers", fn.print_drivers),
        ("4", "Add new driver", fn.add_driver),
        ("5", "Show list of routes", fn.print_routes),
        ("6", "Add new route", fn.add_route),
        ("7", "Exit", lambda: exit())]
    
    menu = Menu(menuitems)
    menu.run('>:')


