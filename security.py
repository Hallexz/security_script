import os
import subprocess

def check_updates():
    print("Проверка обновлений системы...")
    os.system('sudo apt-get update && sudo apt-get upgrade')  # Debian-based
    os.system('sudo dnf check-update && sudo dnf upgrade')  # Fedora
    os.system('sudo pacman -Syu')  # Arch Linux

def check_open_ports():
    print("Проверка открытых портов...")
    os.system('sudo ss -tuln')

def check_file_permissions():
    print("Проверка прав доступа к файлам...")
    insecure_files = subprocess.check_output('find / -perm -4000 -o -perm -2000 -type f', shell=True)
    print(insecure_files.decode())

def check_empty_passwords():
    print("Проверка пользователей без пароля...")
    empty_passwords = subprocess.check_output('sudo awk -F: \'($2 == "") {print $1}\' /etc/shadow', shell=True)
    print(empty_passwords.decode())

def check_failed_login_attempts():
    print("Проверка неудачных попыток входа...")
    os.system('sudo lastb')

def check_sudoers():
    print("Проверка пользователей с правами sudo...")
    os.system('sudo cat /etc/sudoers')

def check_ssh_config():
    print("Проверка конфигурации SSH...")
    os.system('sudo cat /etc/ssh/sshd_config')

def check_firewall_rules():
    print("Проверка правил брандмауэра...")
    os.system('sudo ufw status verbose')  # Ubuntu
    os.system('sudo firewall-cmd --list-all')  # Fedora
    os.system('sudo iptables -L')  # Arch Linux

def check_installed_packages():
    print("Проверка установленных пакетов...")
    os.system('dpkg --get-selections')  # Debian-based
    os.system('dnf list installed')  # Fedora
    os.system('pacman -Q')  # Arch Linux

def check_running_services():
    print("Проверка работающих служб...")
    os.system('systemctl list-units --type=service')

def check_cron_jobs():
    print("Проверка заданий cron...")
    os.system('crontab -l')

def check_user_accounts():
    print("Проверка учетных записей пользователей...")
    os.system('cat /etc/passwd')

def check_group_memberships():
    print("Проверка членства в группах...")
    os.system('cat /etc/group')

def check_security():
    check_updates()
    check_open_ports()
    check_file_permissions()
    check_empty_passwords()
    check_failed_login_attempts()
    check_sudoers()
    check_ssh_config()
    check_firewall_rules()
    check_installed_packages()
    check_running_services()
    check_cron_jobs()
    check_user_accounts()
    check_group_memberships()

# Вызываем функцию проверки безопасности
check_security()
