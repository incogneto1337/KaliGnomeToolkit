import subprocess
import sys
import os
import json
import time
from datetime import datetime

LOG_FILE = '/var/log/kali_customization.log'
BACKUP_DIR = '/root/kali_backup/'
CONFIG_FILE = 'customization_config.json'
POST_INSTALL_SCRIPT = '/root/post_install.sh'

def run_command(command, log=True, show_progress=False):
    try:
        if show_progress:
            print(f"Running: {command}")
        result = subprocess.run(command, shell=True, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output = result.stdout.decode('utf-8').strip()
        if log:
            log_action(command, output)
        return output
    except subprocess.CalledProcessError as e:
        log_action(command, e.stderr.decode('utf-8').strip())
        print(f"Error: {e.stderr.decode('utf-8').strip()}")
        sys.exit(1)

def log_action(command, output):
    with open(LOG_FILE, 'a') as log_file:
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        log_file.write(f"{timestamp} - Command: {command}\n")
        log_file.write(f"{timestamp} - Output: {output}\n\n")

def create_backup():
    if not os.path.exists(BACKUP_DIR):
        os.makedirs(BACKUP_DIR)
    print("Creating system backup...")
    run_command(f"tar -czf {BACKUP_DIR}backup_{datetime.now().strftime('%Y%m%d_%H%M%S')}.tar.gz /home /etc /var", log=False)

def update_system():
    print("Updating system...")
    run_command("apt-get update && apt-get upgrade -y", show_progress=True)

def install_gnome():
    print("Installing GNOME...")
    run_command("apt-get install -y gnome-core gnome-terminal gnome-tweak-tool", show_progress=True)

def set_gnome_as_default():
    print("Setting GNOME as default...")
    run_command("update-alternatives --set x-session-manager /usr/bin/gnome-session", show_progress=True)

def install_additional_software(software_list):
    print("Installing additional software...")
    for package in software_list:
        run_command(f"apt-get install -y {package}", show_progress=True)

def configure_gnome(gnome_settings):
    print("Configuring GNOME...")
    for setting, value in gnome_settings.items():
        run_command(f"gsettings set {setting} {value}", show_progress=True)

def configure_network(network_config):
    if network_config:
        print("Configuring network settings...")
        for setting, value in network_config.items():
            run_command(f"nmcli connection modify {setting} {value}", show_progress=True)

def run_post_install_script():
    if os.path.exists(POST_INSTALL_SCRIPT):
        print("Running post-install script...")
        run_command(f"bash {POST_INSTALL_SCRIPT}", show_progress=True)
    else:
        print(f"Post-install script {POST_INSTALL_SCRIPT} not found.")

def clean_up():
    print("Cleaning up...")
    run_command("apt-get autoremove -y && apt-get autoclean -y", show_progress=True)

def check_system_health():
    print("Checking system health...")
    run_command("df -h")
    run_command("free -h")
    run_command("uptime")

def display_menu():
    print("\nMenu:")
    print("1. Update System")
    print("2. Install GNOME")
    print("3. Set GNOME as Default")
    print("4. Install Additional Software")
    print("5. Configure GNOME")
    print("6. Configure Network Settings")
    print("7. Create Backup")
    print("8. Run Post-Install Script")
    print("9. Clean Up")
    print("10. Check System Health")
    print("11. Exit")

def main():
    if os.geteuid() != 0:
        print("This script must be run as root.")
        sys.exit(1)

    with open(CONFIG_FILE, 'r') as config_file:
        config = json.load(config_file)
    
    while True:
        display_menu()
        choice = input("Select an option: ")

        if choice == '1':
            update_system()
        elif choice == '2':
            install_gnome()
        elif choice == '3':
            set_gnome_as_default()
        elif choice == '4':
            additional_software = config.get('additional_software', [])
            install_additional_software(additional_software)
        elif choice == '5':
            gnome_settings = config.get('gnome_settings', {})
            configure_gnome(gnome_settings)
        elif choice == '6':
            network_config = config.get('network_config', {})
            configure_network(network_config)
        elif choice == '7':
            create_backup()
        elif choice == '8':
            run_post_install_script()
        elif choice == '9':
            clean_up()
        elif choice == '10':
            check_system_health()
        elif choice == '11':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please select a valid option.")

    print("Customization complete. Please restart your system to apply changes.")

if __name__ == "__main__":
    main()
