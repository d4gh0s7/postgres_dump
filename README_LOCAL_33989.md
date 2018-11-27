# postgres_dump

Ansible role to run a full postgresql database dump.

## Requirements

Minimum required ansible version **2.5.0**

## Role Variables

Variables set in `defaults/main.yml`:

```yaml
# defaults file for postgres_dump

# The base postgresql path;
# This variable will be used to determine the backup storage path.
postgresql_base_folder: /var/lib/pgsql

# Set the user that will execute the backup;
# Before changing this value, verify that the authentication methods are compatible with your strategy.
# This variable will be overruled when postgresql_provision_temporary_user is set to Yes.
postgresql_backup_executor: postgres

# Set the user that will own the backup.
postgresql_backup_owner: postgres

# Flag to Yes in order to provision a temporay unprivileged user and run the pg_dumpall with it;
# The user will be deleted immediately after the backup execution;
# The username will be logged to the file system in a .log file archived with the backup.
# This feature is still experimental, though currently stable.
postgresql_provision_temporary_user: Yes

# Set to No to skip the service postgresql state task
postgresql_check_service_state: Yes

# The options passed to the pg_dumpall command
# For a full list check the postgresql documentation at:
# https://www.postgresql.org/docs/11/app-pg-dumpall.html
postgresql_dumpall_params:
  - --clean
  - --if-exists

# Set cleanup_after_backup to No, to store the backup files along with the compressed version.
postgresql_cleanup_after_backup: Yes
```

Variables set in `vars/main.yml`:

```yaml
# Dynamically determined within the main task.
# The postgresql version is stored in format: Major.Minor
# This variable is used merely to determine the path to the postgresql backups folder;
# Set the value manually only if you know what you are doing.
postgresql_version: 0

# Set the backup file name. The dump will be created in the postgresql default backups folder.
postgresql_dump_filename: "full_dump-{{ ansible_date_time.iso8601_basic_short }}.sql"
```

## Example Playbook

The role can be uesed, for instance, as follow:

```yaml
- hosts:
    - postgresql_databases
  become: True
  gather_facts: True

  roles:
    - postgres_dump
      postgresql_provision_temporary_user: No
      postgresql_cleanup_after_backup: Yes
 ```

## License

**CC0 1.0**

## Author Information

[Francesco Cosentino](https://www.linkedin.com/in/francesco-cosentino/) <fc@hyperd.sh>
