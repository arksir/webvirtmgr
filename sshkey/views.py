import os, stat

from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.template import RequestContext
from django.core.urlresolvers import reverse

from sshkey.models import SSHKey


def update(request):
    """

    Update SSH Key value.

    """
    if not request.user.is_authenticated():
        return HttpResponseRedirect(reverse('login'))
    else:
        # import pdb; pdb.set_trace()
        if request.method == 'POST':
            new_key = request.POST.get('sshkey_content')
            if new_key:
                home_dir = os.environ['HOME']
                ssh_key_dir = os.path.join(home_dir, '.ssh')
                if not os.path.exists(ssh_key_dir):
                    print("ssh key dir not exist, creating it now.")
                    os.mkdir(ssh_key_dir)
                key_file_path = os.path.join(ssh_key_dir, 'is_rsa')
                key_file_obj = open(key_file_path, 'w')
                key_file_obj.write(new_key)
                key_file_obj.close()
                os.chmod(key_file_path, stat.S_IRUSR | stat.S_IWUSR)
                update_result = u"Update success."

        return render_to_response('sshkey.html', locals(), context_instance=RequestContext(request))



