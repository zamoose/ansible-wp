#!/usr/bin/python
# -*- coding: utf-8 -*-

ANSIBLE_METADATA = {'metadata_version': '0.1',
                    'status': ['preview'],
                    'supported_by': 'community'}

def core(module):
    theme = module.params['theme']
    plugin = module.params['plugin']
    args = []

    module.exit_json(msg="WPCLI Rocks!", changed=True)

def main():
    module = AnsibleModule( argument_spec = dict(
            theme = dict(required=False),
            plugin = dict(required=False),
            ),
        )

    if not os.path.exists("/usr/local/bin/wp"):
        module.fail_json(msg="You must have a working WP-CLI install in order to execute this module.")

    try:
        core(module)
    except Exception as e:
        module.fail_json(msg=str(e))

# import module snippets
from subprocess import call
from distutils import spawn
from ansible.module_utils.basic import *
if __name__ == '__main__':
    main()
