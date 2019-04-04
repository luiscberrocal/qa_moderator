import os
import re
import subprocess
import sys


def run_command(command):
    proc = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, shell=True)
    return_code = proc.returncode

    if return_code:
        raise Exception(proc.stdout, return_code)

    for line in proc.stdout.readlines():
        yield line.strip().decode('utf-8')


def run_backup_in_container(container):
    command = ['docker', 'container', 'exec', '-it', container, 'backup']
    return run_command(command)


def copy_backup_file(container, filename, destination_folder):
    command = ['docker', 'cp', '{}:/backups/{}'.format(container, filename), destination_folder]
    return run_command(command)


def copy_to_sharepoint(moved_file, share_point_folder):
    command = ['copy', moved_file, share_point_folder]
    print('Running command {}'.format(' '.join(command)))
    return run_command(command)


if __name__ == '__main__':
    """
    Script to backup the Postgres database.
    
    This Script:
        # Runs the backup process in the container.
        # Copies the backup file from the container to the ../backups directory.
        # Copies the backup file to OneDrive into the pmp_shield folder 
        
    To use:
        # cd to the scripts folder
        # Run::
            $ python backup.py
    """
    container = 'pmp_shield_postgres_1'
    reg_exp_for_filename = r'successfully\screated\sbackup\s(pmp_shield_backup_\d{8}_\d{6}\.sql\.gz)'
    share_point_environment_variable = 'OneDrive'
    share_point_folder = os.environ.get(share_point_environment_variable)
    share_point_backup_folder = os.path.join(share_point_folder, 'pmp_shield')
    download_folder = '../backups/'  # Linux
    regex = re.compile(reg_exp_for_filename)
    filename = None

    lines = run_backup_in_container(container)
    for line in lines:
        match = regex.match(line)
        if match:
            filename = match.group(1)
        if 'Error response from daemon' in line:
            print('Cannot run backup. It seems your postgres container is not up')
            sys.exit()
        #print(line)

    print('Filename: {}'.format(filename))
    print('--' * 30)

    lines = copy_backup_file(container, filename, download_folder)
    for line in lines:
        print(line)

    downloaded_file = os.path.join(download_folder.replace('/', '\\'), filename)
    if not os.path.exists(downloaded_file):
        print('Error file was not copied')
    # print('OneDrive: {}'.format(os.environ.get('OneDrive')))
    current_file = os.path.dirname(os.path.abspath(__file__))
    print('Current file: {}'.format(current_file))
    lines = copy_to_sharepoint(downloaded_file, share_point_backup_folder)
    for line in lines:
        print(line)
