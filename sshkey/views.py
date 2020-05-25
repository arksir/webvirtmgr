import os, stat

from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.template import RequestContext
from django.core.urlresolvers import reverse

from sshkey.models import SSHKey
from webvirtmgr.utils import file_handler

def update(request):
    """

    Update SSH Key value.

    """
    if not request.user.is_authenticated():
        return HttpResponseRedirect(reverse('login'))
    else:
        if request.method == 'POST':
            new_key = request.POST.get('sshkey_content')
            if new_key:
                file_handler.save_ssh_key(new_key)

                old_ssh_key = None
                try:
                    old_ssh_key = SSHKey.objects.get(name='id_rsa')
                except SSHKey.DoesNotExist:
                    print('Old SSH Key not found in database.')

                if old_ssh_key:
                    print('Found old ssh key, delete it.')
                    old_ssh_key.delete()
                new_ssh_key = SSHKey(name="id_rsa", value=new_key)
                new_ssh_key.save()
                print('New ssh key saved.')

                update_result = u"Update success."

        return render_to_response('sshkey.html', locals(), context_instance=RequestContext(request))



