import sys, os

if __name__ == "__main__":

    # This script requires an app name.
    if len(sys.argv)!=2:
        print("Please use one argument stating the app path.")
        exit()
    app_name = sys.argv[1]
    
    # Check if path exists; otherwise exit.
    if not os.path.exists(app_name):
        print("Flask app does not exist.")
        exit()

    # Create controllers, models and components directories.
    controllers = create_directory(app_name, "controllers")
    models = create_directory(app_name, "models")
    components = create_directory(app_name, "components")

    object_name = input("Object name: ")
    
    creating_columns = True
    while creating_columns:
        column_name = input("Column name: ")
        
    