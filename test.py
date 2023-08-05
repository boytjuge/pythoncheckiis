import subprocess

def check_remote_pool_status(server_ip, pool_name):
    try:
        # Construct the remote PowerShell command
        command = f"Invoke-Command -ComputerName {server_ip} -ScriptBlock {{ Import-Module WebAdministration; (Get-WebAppPoolState -Name '{pool_name}').Value }}"
        
        # Run the command on the remote server using PowerShell
        result = subprocess.run(['powershell', '-Command', command], capture_output=True, text=True, check=True)
        
        # Check the output for the state (it should be "Started" if the pool is running)
        state = result.stdout.strip()
        return state == "Started"
    except subprocess.CalledProcessError as e:
        print(f"Error checking pool status on {server_ip}: {e}")
        return False

# Replace 'remote_server_ip' with the IP address of the remote server
remote_server_ip = 'remote_server_ip'

# Replace 'YourAppPoolName' with the actual name of the application pool you want to check
app_pool_name = 'YourAppPoolName'

if check_remote_pool_status(remote_server_ip, app_pool_name):
    print(f"Application pool {app_pool_name} is running on {remote_server_ip}.")
else:
    print(f"Application pool {app_pool_name} is not running on {remote_server_ip}.")
