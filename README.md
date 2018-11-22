# postgres_dump

Ansible role to run a full postgresql database dump.

## Requirements

Minimum required ansible version **2.5.0**

## Role Variables

Variables set in `defaults/main.yml`:

```yaml
# defaults file for postgres_dump

# The base path for the postgres dump storage.
postgres_base_dump_folder: /var/lib/pgsql

# The user that will execute the backup.
postgresql_backup_executor: postgres

# The user that will own the backup.
postgresql_backup_owner: postgres

# The options passed to the pg_dumpall command
# For a full list check the postgresql documentation at:
# https://www.postgresql.org/docs/11/app-pg-dumpall.html
postgresql_dump_params:
  - --clean
  - --if-exists
```

Variables set in `vars/main.yml`:

```yaml
# Variable used to store the postgresql version in Major.Minor format.
postgresql_version: 0

# Set cleanup_after_backup to No, to store the backup files along with the compressed version
cleanup_after_backup: Yes

# Set to No to skip the service postgresql status task
ensure_postgresql_is_running: Yes
```

## Example Playbook

Use the role as follow:

```yaml
- hosts:
    - postgresql_databases
  become: True
  gather_facts: True
  vars_files:
    - ./group_vars/all.yml
  roles:
    - postgres_dump
      
 ```

## License

**CC0 1.0**

## Author Information

[Francesco Cosentino](https://www.linkedin.com/in/francesco-cosentino/) <fc@hyperd.sh>
