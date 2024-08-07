---

# Kali GNOME Toolkit

This Python script customizes a Kali Linux installation by updating the system, installing GNOME, configuring settings, and more. It includes features like interactive menus, logging, and post-installation scripts.

## Features

- **System Update**: Updates and upgrades the system packages.
- **GNOME Installation**: Installs the GNOME desktop environment and sets it as default.
- **Additional Software Installation**: Installs extra software based on user preferences.
- **GNOME Configuration**: Configures GNOME settings like themes and terminal preferences.
- **Network Configuration**: Configures network settings if specified.
- **Backup Creation**: Creates a backup of critical directories.
- **Post-Install Script**: Executes a custom post-installation script.
- **System Health Checks**: Performs basic system health checks.
- **Logging**: Logs actions and outputs for troubleshooting.

## Requirements

- Python 3
- Root (sudo) privileges

## Configuration

Create a `customization_config.json` file to specify additional software, GNOME settings, and network configurations. An example configuration file is provided below.

**Example `customization_config.json`:**
```json
{
    "additional_software": [
        "vim",
        "htop",
        "git",
        "gnome-shell-extensions",
        "gnome-system-monitor"
    ],
    "gnome_settings": {
        "org.gnome.desktop.interface gtk-theme": "'Adwaita-dark'",
        "org.gnome.desktop.interface icon-theme": "'Adwaita'",
        "org.gnome.Terminal.Legacy.Settings default-show-menubar": "false"
    },
    "network_config": {
        "my-connection": "ipv4.addresses 192.168.1.100/24"
    }
}
```

Create a `post_install.sh` script if you need to run custom commands after installation.

**Example `post_install.sh`:**
```bash
#!/bin/bash
# Custom post-installation script
echo "Running custom post-installation configurations..."
# Add your custom commands here
```

## Usage

1. **Save the Script**: Save the script to a file, e.g., `customize_kali.py`.
2. **Make Executable**: Make the script executable:
   ```bash
   chmod +x kalignometoolkit.py
   ```
3. **Run the Script**: Execute the script with root privileges:
   ```bash
   sudo python3 kalignometoolkit.py
   ```

4. **Follow the Menu**: Choose the desired actions from the interactive menu.

## Logging

The script logs actions and outputs to `/var/log/kali_customization.log`. Check this log file for details about what was changed and if any errors occurred.

## Notes

- **Backup**: Always ensure you have recent backups before running the script.
- **Root Privileges**: The script requires root privileges to make system-wide changes.
- **Testing**: Test the script in a safe environment before deploying it to production systems.

## License

This script is provided as-is with no warranty. Use it at your own risk.

---
