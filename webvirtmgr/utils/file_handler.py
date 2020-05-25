import os, stat
import getpass


def save_ssh_key(new_key):
    home_dir = os.path.expanduser('~' + getpass.getuser())
    ssh_key_dir = os.path.join(home_dir, '.ssh')
    if not os.path.exists(ssh_key_dir):
        print("ssh key dir not exist, creating it now.")
        os.mkdir(ssh_key_dir)
    key_file_path = os.path.join(ssh_key_dir, 'id_rsa')

    with open(key_file_path, 'w') as key_file_obj:
        key_file_obj.write(new_key)

    os.chmod(key_file_path, stat.S_IRUSR | stat.S_IWUSR)

