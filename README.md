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

# Set the user that will execute the backup;
# Before changing this value, verify that the authentication methods are compatible with your strategy.
# This variable will be overruled when provision_temporary_user is set to Yes.
postgresql_backup_executor: postgres

# Set the user that will own the backup.
postgresql_backup_owner: postgres

# Flag to Yes in order to provision a temporay unprivileged user and run the pg_dumpall with it;
# The user will be deleted immediately after the backup execution;
# The username will be logged to the file system in a .log file archived with the backup.
# This feature is still experimental, though currently stable.
provision_temporary_user: Yes

# Set to No to skip the service postgresql status task
ensure_postgresql_is_running: Yes

# The options passed to the pg_dumpall command
# For a full list check the postgresql documentation at:
# https://www.postgresql.org/docs/11/app-pg-dumpall.html
postgresql_dumpall_params:
  - --clean
  - --if-exists

# Set cleanup_after_backup to No, to store the backup files along with the compressed version
cleanup_after_backup: Yes
```

Variables set in `vars/main.yml`:

```yaml
# Dynamically determined within the main task.
# The postgresql version is stored in format: Major.Minor
# This variable is used merely to determine the path to the postgresql backups folder;
# Set the value manually only if you know what you are doing.
postgresql_version: 0

# List the commands to run in order to grant the necessary privileges to the temporary user.
provision_temporary_user_grant_privileges_commands:
  - GRANT SELECT ON ALL TABLES IN SCHEMA pg_catalog TO {{ postgresql_backup_executor }}
  - GRANT SELECT, USAGE ON ALL SEQUENCES IN SCHEMA pg_catalog TO {{ postgresql_backup_executor }}

# List the commands to run in order to revoke the assigned privileges from the temporary user
# and allow the dropuser command.
provision_temporary_user_revoke_privileges_commands:
  - REVOKE ALL PRIVILEGES ON ALL TABLES IN SCHEMA pg_catalog FROM {{ postgresql_backup_executor }}
  - REVOKE ALL PRIVILEGES ON ALL SEQUENCES IN SCHEMA pg_catalog FROM {{ postgresql_backup_executor }}
```

## Example Playbook

Use the role as follow:

```yaml
- hosts:
    - postgresql_databases
  become: True
  gather_facts: True

  roles:
    - postgres_dump
      provision_temporary_user: Yes
      postgresql_dumpall_params:
        - --clean
        - --if-exists
 ```

## License

**CC0 1.0**

## Author Information

[Francesco Cosentino](https://www.linkedin.com/in/francesco-cosentino/) <fc@hyperd.sh>
