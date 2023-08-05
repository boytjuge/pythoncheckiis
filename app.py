import subprocess
import time
def is_application_pool_running(pool_name):
    try:
        # Run a PowerShell command to check the status of the application pool
        command = f"Import-Module WebAdministration; (Get-WebAppPoolState -Name '{pool_name}').Value"
        result = subprocess.run(["powershell", "-Command", command], capture_output=True, text=True, check=True)
        # Check the output for the state (it should be "Started" if the pool is running)
        state = result.stdout.strip()
        return state == "Started"
    except subprocess.CalledProcessError as e:
        print(f"Error checking the status of application pool {pool_name}: {e}")
        return False

# List of application pool names you want to check
app_pool_names = ['test', 'dotnetreact']
datalog = set()
while(True) :
    print("Starting...")
      # Pause for 3 seconds

    for app_pool_name in app_pool_names:
        if is_application_pool_running(app_pool_name):
            for item in datalog:
                if item == app_pool_name:
                    print(f'Pool: {app_pool_name} Working At ')
                    print(datalog.remove(app_pool_name))
                    break
            print(f"Application pool {app_pool_name} is running.")
        else:
            datalog.add(app_pool_name)
            print(f"Application pool {app_pool_name} is not running.")
    print("...Finished")
    time.sleep(5)