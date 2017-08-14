#!/usr/bin/python
# -*- coding: utf-8 -*-

ANSIBLE_METADATA = {'metadata_version': '0.1',
                    'status': ['preview'],
                    'supported_by': 'community'}

DOCUMENTATION = '''
---
module: ansible_wp
version_added: "post 2.3"
author: Doug Stewart
short_description: Install and manage WordPress sites
description:
   - WordPress installations can be installed, removed, and managed using the WP-CLI command line tool
'''

# import module snippets
from subprocess import call
from distutils.spawn import *
from ansible.module_utils.basic import *

def core(path, wp, module):
    args = []

    rc, wpversion, wperr = module.run_command("{} core version --path={}".format(wp, path))

    if not rc:
        module.exit_json(msg=wpversion, changed=True)
    else:
        module.fail_json(msg=wperr)

def plugin(module, wp):
    path = module.params['path']

def theme(module, wp):
    path = module.params['path']

def main():
    module = AnsibleModule(
        argument_spec = {
            "path": {'required': True, 'type': 'str'},
            'download': {
                'required': False,
                'default': 'no',
                'choices': ['no','yes'],
                'type': 'str'
            },
            'plugins': {'required': False, 'type': 'list'},
            'themes': {'required': False, 'type': 'list'},
            'users': {'required': False, 'type': 'list'},
            'cache': {
                'required': False,
                'type': 'str'
            },
        },
        mutually_exclusive = [
        ],
        supports_check_mode = True
    )

    path = module.params['path']
    themes = module.params['themes']
    plugins = module.params['plugins']
    users = module.params['users']
    download = module.params['download']

    wp_cli_exe = find_executable('wp')

    if not wp_cli_exe:
        module.fail_json(msg="`wp` not found! You must have a working WP-CLI install in order to execute this module. '{}' '{}'".format(type(wp_cli_exe), wp_cli_exe))

    try:
        core(path, wp_cli_exe, module)
    except Exception as e:
        module.fail_json(msg=str(e))

if __name__ == '__main__':
    main()
