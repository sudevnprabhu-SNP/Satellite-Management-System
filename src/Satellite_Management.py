# Satellite Management System v1.0
# You have joined the Mission Planning Division of ISRO as a Software Development Intern.

# The engineers currently maintain satellite information in Excel sheets.

# Your task is to develop a console-based application to manage satellite information efficiently.

from datetime import datetime

current_year = datetime.now().year

satellite ={
    1001 : {
        "name": "Cartosat-3",
        "country":"India",
        "agency":"ISRO",
        "mission":"Earth Observation",
        "orbit":"LEO",
        "launch": 2019,
        "status":"Active",
        "fuel": 78
    }
}

status_list = [
    "Active",
    "Inactive",
    "Maintenance",
    "Decommissioned"
]

country = "India"
agency = "ISRO"

mission_type = [
    "Communication",
    "Navigation",
    "Earth Observation",
    "Scientific",
    "Astronomy",
    "Weather",
    "Planetary Exploration"
]

orbit_list = [
    "LEO",
    "MEO",
    "GEO",
    "HEO",
    "Polar",
    "L1",
    "Lunar Orbit",
    "Mars Orbit"
]

def check_launchYear(year):
    if year > current_year :
        print("The year entered is invalid")
        print("event can only be present or past")
        return False
    
    if year < 1975:
        print("Before 1975 ISRO never launched a satellite")
        return False
    
    return True

def check_fuel(fuel):
    if fuel > 100 :
        print("Fuel cannot exceet the tank")
        return False
    
    if fuel < 0:
        print("Fuel cannot be negative.")
        return False
    
    if fuel == 0:
        print("Warning: The satellite has no fuel.")

    return True

def check_fuel_limit():
    for id in satellite:
        if satellite[id]['fuel'] < 20:
            print("⚠️ LOW FUEL WARNING")

def check_old_satellite():
    for id in satellite:
        if satellite[id]['launch'] < 2015:
            print("⚠️ OLD SATELLITE WARNING")

def generate_satellite_id():
    if not satellite:
        return 1001      # First satellite ID
    return max(satellite) + 1


def menu():
    print("========== SATELLITE MANAGEMENT SYSTEM ==========")
    print("1. Add Satellite")
    print("2. View Satellites")
    print("3. Search Satellite")
    print("4. Update Satellite")
    print("5. Refuel Satellite")
    print("6. Consume Fuel")
    print("7. Change Status")
    print("8. Delete Satellite")
    print("9. Satellite Statistics")
    print("10. Exit")

    try:
        menu_selected = int(input("Select the index from the menu: "))
        return menu_selected

    except ValueError:
        print("Invalid input! Please enter only numbers.")

def add_sattellite(name, country, agency, mission, orbit, launch, status, fuel):
    satellite_id = generate_satellite_id()

    if satellite_id in satellite:
        print("The satellite already exists")
    else:
        satellite[satellite_id] = {
            "name": name,
            "country":country,
            "agency":agency,
            "mission":mission,
            "orbit":orbit,
            "launch":launch,
            "status":status,
            "fuel":fuel
        }
        print("Satellite added successfully.")
        print("Generated Satellite ID:", satellite_id)


def view_satellite(sort_by="id", filter_by=None, filter_value=None):
    if not satellite:
        print("No satellites available.")
        return

    filtered_satellites = []

    for satellite_id, sat in satellite.items():

        if filter_by is None:
            filtered_satellites.append((satellite_id, sat))

        elif filter_by == "status":
            if sat["status"].lower() == filter_value.lower():
                filtered_satellites.append((satellite_id, sat))

        elif filter_by == "fuel":
            if sat["fuel"] <= filter_value:
                filtered_satellites.append((satellite_id, sat))

        elif filter_by == "mission":
            if sat["mission"].lower() == filter_value.lower():
                filtered_satellites.append((satellite_id, sat))

        elif filter_by == "orbit":
            if sat["orbit"].lower() == filter_value.lower():
                filtered_satellites.append((satellite_id, sat))

        elif filter_by == "agency":
            if sat["agency"].lower() == filter_value.lower():
                filtered_satellites.append((satellite_id, sat))

        elif filter_by == "launch":
            if sat["launch"] == filter_value:
                filtered_satellites.append((satellite_id, sat))

    if not filtered_satellites:
        print("No satellites found for the selected filter.")
        return

    if sort_by == "id":
        sorted_satellites = sorted(
            filtered_satellites,
            key=lambda item: item[0]
        )

    elif sort_by == "name":
        sorted_satellites = sorted(
            filtered_satellites,
            key=lambda item: item[1]["name"].lower()
        )

    elif sort_by == "launch":
        sorted_satellites = sorted(
            filtered_satellites,
            key=lambda item: item[1]["launch"]
        )

    elif sort_by == "status":
        sorted_satellites = sorted(
            filtered_satellites,
            key=lambda item: item[1]["status"].lower()
        )

    elif sort_by == "fuel":
        sorted_satellites = sorted(
            filtered_satellites,
            key=lambda item: item[1]["fuel"]
        )

    elif sort_by == "mission":
        sorted_satellites = sorted(
            filtered_satellites,
            key=lambda item: item[1]["mission"].lower()
        )

    elif sort_by == "orbit":
        sorted_satellites = sorted(
            filtered_satellites,
            key=lambda item: item[1]["orbit"].lower()
        )

    else:
        sorted_satellites = sorted(
            filtered_satellites,
            key=lambda item: item[0]
        )

    print("=" * 135)
    print(
        f"{'Satellite ID':<15}"
        f"{'Name':<20}"
        f"{'Country':<12}"
        f"{'Agency':<12}"
        f"{'Mission':<25}"
        f"{'Orbit':<15}"
        f"{'Launch':<10}"
        f"{'Status':<18}"
        f"{'Fuel':<8}"
    )
    print("=" * 135)

    for satellite_id, sat in sorted_satellites:
        print(
            f"{satellite_id:<15}"
            f"{sat['name']:<20}"
            f"{sat['country']:<12}"
            f"{sat['agency']:<12}"
            f"{sat['mission']:<25}"
            f"{sat['orbit']:<15}"
            f"{sat['launch']:<10}"
            f"{sat['status']:<18}"
            f"{sat['fuel']:<8}"
        )

    print("=" * 135)


def search_satellite(satellite_id):
    if satellite_id in satellite:
        sat = satellite[satellite_id]

        print("=" * 70)
        print("Satellite ID       :", satellite_id)
        print("Satellite Name     :", sat["name"])
        print("Satellite Country  :", sat["country"])
        print("Satellite Agency   :", sat["agency"])
        print("Satellite Mission  :", sat["mission"])
        print("Satellite Orbit    :", sat["orbit"])
        print("Satellite Launch   :", sat["launch"])
        print("Satellite Status   :", sat["status"])
        print("Satellite Fuel     :", sat["fuel"], "%")
        print("=" * 70)
    else:
        print("Satellite not found.")

def search_by_field(field, value):
    found = False

    for satellite_id, sat in satellite.items():

        if str(sat[field]).lower() == str(value).lower():
            search_satellite(satellite_id)
            found = True

    if not found:
        print("No satellites found.")

def satellite_search_menu():
    print("\n========= SEARCH SATELLITE =========")
    print("1. Search by ID")
    print("2. Search by Mission")
    print("3. Search by Orbit")
    print("4. Search by Status")
    print("5. Search by Launch Year")
    print("6. Search by Agency")

    try:
        choice = int(input("Enter your choice: "))

        if choice == 1:
            satellite_id = int(input("Enter satellite ID: "))
            search_satellite(satellite_id)

        elif choice == 2:
            selected_mission = select_from_list(
                "Select Mission",
                mission_type
            )

            search_by_field(
                "mission",
                selected_mission
            )

        elif choice == 3:
            selected_orbit = select_from_list(
                "Select Orbit",
                orbit_list
            )

            search_by_field(
                "orbit",
                selected_orbit
            )

        elif choice == 4:
            selected_status = select_from_list(
                "Select Status",
                status_list
            )

            search_by_field(
                "status",
                selected_status
            )

        elif choice == 5:
            launch_year = int(
                input("Enter launch year: ")
            )

            if check_launchYear(launch_year):
                search_by_field(
                    "launch",
                    launch_year
                )

        elif choice == 6:
            agency_name = input(
                "Enter agency name: "
            ).strip()

            search_by_field(
                "agency",
                agency_name
            )

        else:
            print("Invalid choice! Enter a number from 1 to 6.")

    except ValueError:
        print("Invalid input! Please enter only numbers.")

def update_satellite(id, name, mission, orbit, launch, status, fuel):
    if id in satellite:
        satellite[id]["name"] = name
        satellite[id]["mission"] = mission
        satellite[id]["orbit"] = orbit
        satellite[id]["launch"] = launch
        satellite[id]["status"] = status
        satellite[id]["fuel"] = fuel
        print("The satellite data is updated")
        search_satellite(id)
    else:
        print("No satellite found")

def refuel_satellite(id,fuel):
    if id in satellite:
        if check_fuel(fuel):
            new_fuel = satellite[id]["fuel"] + fuel

        if check_fuel(new_fuel):
            satellite[id]["fuel"] = new_fuel
            print("Satellite refuelled successfully.")
            print("Current Fuel:", satellite[id]["fuel"], "%")
    else:
        print("No satellite found")

def consume_satellite(id,fuel):
    if id in satellite:
        if check_fuel(fuel):
             new_fuel = satellite[id]["fuel"] - fuel

        if check_fuel(new_fuel):
            satellite[id]["fuel"] = new_fuel
            print("Satellite consumed successfully.")
            print("Current Fuel:", satellite[id]["fuel"], "%")
    else:
        print("No satellite found")
 
def change_status(id, status):
    if id in satellite:
        satellite[id]["status"] = status
        print("The status has been updated")
        search_satellite(id)
    else:
        print("The satellite not found")

def delete_satellite(id, reid, name):
    if id in satellite:
        if id == reid and satellite[id]["name"] == name:
            del satellite[id]
            print("The satellite removed successfully")
            view_satellite()

def satellite_statistics():
    if not satellite:
        print("No satellite data available.")
        return

    total_satellites = len(satellite)
    active_count = 0
    inactive_count = 0
    maintenance_count = 0
    decommissioned_count = 0

    fuel_values = []

    for satellite_id, details in satellite.items():
        status = details["status"]
        fuel = details["fuel"]

        if status == "Active":
            active_count += 1
        elif status == "Inactive":
            inactive_count += 1
        elif status == "Maintenance":
            maintenance_count += 1
        elif status == "Decommissioned":
            decommissioned_count += 1

        fuel_values.append(fuel)

    total_fuel = sum(fuel_values)
    average_fuel = total_fuel / total_satellites
    highest_fuel = max(fuel_values)
    lowest_fuel = min(fuel_values)

    print("=" * 60)
    print("SATELLITE STATISTICS")
    print("=" * 60)
    print("Total Satellites       :", total_satellites)
    print("Active Satellites      :", active_count)
    print("Inactive Satellites    :", inactive_count)
    print("Maintenance Satellites :", maintenance_count)
    print("Decommissioned         :", decommissioned_count)
    print("Average Fuel           :", round(average_fuel, 2), "%")
    print("Highest Fuel           :", highest_fuel, "%")
    print("Lowest Fuel            :", lowest_fuel, "%")
    print("=" * 60)

def select_from_list(title, options):
    while True:
        print(f"\n{title}")

        for index, option in enumerate(options, start=1):
            print(f"{index}. {option}")

        try:
            choice = int(input("Enter your choice: "))

            if 1 <= choice <= len(options):
                return options[choice - 1]

            print(
                f"Invalid choice! Enter a number from "
                f"1 to {len(options)}."
            )

        except ValueError:
            print("Invalid input! Please enter only numbers.")

def advanced_filter_menu():
    print("\n========= CUSTOM FILTER =========")
    print("1. Filter by Status")
    print("2. Filter by Mission")
    print("3. Filter by Orbit")
    print("4. Filter by Agency")
    print("5. Filter by Launch Year")
    print("6. Filter by Maximum Fuel")

    try:
        choice = int(input("Enter your choice: "))

        if choice == 1:
            selected_status = select_from_list(
                "Select Status",
                status_list
            )

            view_satellite(
                sort_by="name",
                filter_by="status",
                filter_value=selected_status
            )

        elif choice == 2:
            selected_mission = select_from_list(
                "Select Mission",
                mission_type
            )

            view_satellite(
                sort_by="name",
                filter_by="mission",
                filter_value=selected_mission
            )

        elif choice == 3:
            selected_orbit = select_from_list(
                "Select Orbit",
                orbit_list
            )

            view_satellite(
                sort_by="name",
                filter_by="orbit",
                filter_value=selected_orbit
            )

        elif choice == 4:
            agency_value = input(
                "Enter agency name: "
            ).strip()

            view_satellite(
                sort_by="name",
                filter_by="agency",
                filter_value=agency_value
            )

        elif choice == 5:
            launch_year = int(
                input("Enter launch year: ")
            )

            view_satellite(
                sort_by="name",
                filter_by="launch",
                filter_value=launch_year
            )

        elif choice == 6:
            maximum_fuel = int(
                input("Show satellites with fuel less than or equal to: ")
            )

            if 0 <= maximum_fuel <= 100:
                view_satellite(
                    sort_by="fuel",
                    filter_by="fuel",
                    filter_value=maximum_fuel
                )
            else:
                print("Fuel must be between 0 and 100.")

        else:
            print("Invalid choice.")

    except ValueError:
        print("Invalid input! Please enter only numbers.")


while True:
    check_fuel_limit()
    check_old_satellite()
    menu_selected = menu()

    if menu_selected == 1:
        try:
            name = input("Enter the satellite name: ").strip()

            mission_value = select_from_list(
                "Select Mission Type",
                mission_type
            )

            orbit_value = select_from_list(
                "Select Orbit Type",
                orbit_list
            )

            launch_year = int(
                input("Enter the launch year: ")
            )

            status_value = select_from_list(
                "Select Satellite Status",
                status_list
            )

            fuel_value = int(
                input("Enter the fuel percentage: ")
            )

            if not name:
                print("Satellite name cannot be empty.")

            elif not check_launchYear(launch_year):
                pass

            elif not check_fuel(fuel_value):
                pass

            else:
                add_sattellite(
                    name,
                    country,
                    agency,
                    mission_value,
                    orbit_value,
                    launch_year,
                    status_value,
                    fuel_value
                )

        except ValueError:
            print(
                "Launch year and fuel must be entered as numbers."
            )

    elif menu_selected == 2:
        print("\n========= VIEW SATELLITES =========")
        print("1. View All")
        print("2. Only Active")
        print("3. Only Inactive")
        print("4. Only Maintenance")
        print("5. Only Decommissioned")
        print("6. Only Low Fuel")
        print("7. Only Earth Observation")
        print("8. Only GEO")
        print("9. Only LEO")
        print("10. Custom Filter")

        try:
            choice = int(input("Enter your choice: "))

            if choice == 1:
                view_satellite()

            elif choice == 2:
                view_satellite(
                    sort_by="name",
                    filter_by="status",
                    filter_value="Active"
                )

            elif choice == 3:
                view_satellite(
                    sort_by="name",
                    filter_by="status",
                    filter_value="Inactive"
                )

            elif choice == 4:
                view_satellite(
                    sort_by="name",
                    filter_by="status",
                    filter_value="Maintenance"
                )

            elif choice == 5:
                view_satellite(
                    sort_by="name",
                    filter_by="status",
                    filter_value="Decommissioned"
                )

            elif choice == 6:
                view_satellite(
                    sort_by="fuel",
                    filter_by="fuel",
                    filter_value=20
                )

            elif choice == 7:
                view_satellite(
                    sort_by="name",
                    filter_by="mission",
                    filter_value="Earth Observation"
                )

            elif choice == 8:
                view_satellite(
                    sort_by="name",
                    filter_by="orbit",
                    filter_value="GEO"
                )

            elif choice == 9:
                view_satellite(
                    sort_by="name",
                    filter_by="orbit",
                    filter_value="LEO"
                )

            elif choice == 10:
                advanced_filter_menu()

            else:
                print("Invalid choice. Enter a number from 1 to 10.")

        except ValueError:
            print("Invalid input! Please enter only numbers.")

    elif menu_selected == 3:
       satellite_search_menu()
       
    elif menu_selected == 4:
        print("\nEnter the values to update the satellite completely")

        try:
            satellite_id = int(input("Enter the satellite ID: "))

            if satellite_id not in satellite:
                print("No satellite found.")

            else:
                name = input("Enter the updated satellite name: ").strip()

                mission_value = select_from_list(
                    "Select Updated Mission",
                    mission_type
                )

                orbit_value = select_from_list(
                    "Select Updated Orbit",
                    orbit_list
                )

                launch_year = int(
                    input("Enter the updated launch year: ")
                )

                status_value = select_from_list(
                    "Select Updated Status",
                    status_list
                )

                fuel_value = int(
                    input("Enter the updated fuel percentage: ")
                )

                if not name:
                    print("Satellite name cannot be empty.")

                elif not check_launchYear(launch_year):
                    pass

                elif not check_fuel(fuel_value):
                    pass

                else:
                    update_satellite(
                        satellite_id,
                        name,
                        mission_value,
                        orbit_value,
                        launch_year,
                        status_value,
                        fuel_value
                    )

        except ValueError:
            print(
                "Satellite ID, launch year and fuel must be entered as numbers."
            )

    elif menu_selected == 5:
        try:
            satellite_id = int(input("Enter the satellite ID: "))

            if satellite_id not in satellite:
                print("Satellite not found.")

            else:
                fuel_amount = int(
                    input("Enter the amount of fuel to add: ")
                )

                refuel_satellite(
                    satellite_id,
                    fuel_amount
                )

        except ValueError:
            print(
                "Satellite ID and fuel amount must be entered as numbers."
            )    

    elif menu_selected == 6:
        try:
            satellite_id = int(input("Enter the satellite ID: "))

            if satellite_id not in satellite:
                print("Satellite not found.")

            else:
                fuel_amount = int(
                    input("Enter the amount of fuel to consume: ")
                )

                consume_satellite(
                    satellite_id,
                    fuel_amount
                )

        except ValueError:
            print(
                "Satellite ID and fuel amount must be entered as numbers."
            )

    elif menu_selected == 7:
        try:
            satellite_id = int(input("Enter the satellite ID: "))

            if satellite_id not in satellite:
                print("Satellite not found.")

            else:
                new_status = select_from_list(
                    "Select New Satellite Status",
                    status_list
                )

                change_status(
                    satellite_id,
                    new_status
                )

        except ValueError:
            print("Satellite ID must be entered as a number.")

    elif menu_selected == 8:
        try:
            prd_id = int(input("Enter the Satellite id: "))
            reid = int(input("Contirm the satellite id: "))
            name = input("Enter the Name of the satellite: ")
 
            delete_satellite(prd_id,reid,name)
        
        except ValueError:
            print("Invalid input! Please enter only numbers.")

    elif menu_selected == 9:
        satellite_statistics()

    elif menu_selected == 10:
        print("Thank you for using our Satellite Management Application.")
        break

    else:
         print("Invalid Choice! Please try again.")



