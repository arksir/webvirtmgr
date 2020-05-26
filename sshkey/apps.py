import os

from django.apps import AppConfig
from django.db.utils import OperationalError, ProgrammingError
from sshkey.models import SSHKey

from webvirtmgr.utils import file_handler

class SSHKeyConfig(AppConfig):
    name = 'sshkey'

    def ready(self):
        ssh_key = None
        try:
            ssh_key = SSHKey.objects.get(name='id_rsa')
        except SSHKey.DoesNotExist:
            print('SSH Key not found in database.')
        except OperationalError:
            print('OperationalError: maybe first startup.')
        except ProgrammingError:
            print('ProgrammingError: maybe first startup.')

        if ssh_key:
            print('Found SSH Key in databasek, will init it to filesystem')
            file_handler.save_ssh_key(ssh_key.value)

