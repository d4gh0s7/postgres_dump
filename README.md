# postgres_dump
=========

Ansible role to run a full postgresql database dump.

Requirements
------------

Minimum ansible version **2.5.0**

Role Variables
--------------

Variables set in `defaults/main.yml`:

```yaml
# defaults file for postgres_dump

# The base path for the postgres dump storage.
postgres_base_dump_folder: /var/lib/pgsql

# The user that will execute and own the backup.
postgresql_backup_owner: postgres
```

Variables set in `vars/main.yml`:

```yaml
# Variable used to store the postgresql version in Major.Minor format.
postgresql_version: 0
```

Example Playbook
----------------

Including an example of how to use your role (for instance, with variables passed in as parameters) is always nice for users too:

    - hosts: servers
      roles:
         - { role: username.rolename, x: 42 }

License
-------

BSD

Author Information
------------------

[Francesco Cosentino](https://www.linkedin.com/in/francesco-cosentino/) <fc@hyperd.io>
