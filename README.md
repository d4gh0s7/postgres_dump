# Ansible role: postgres_dump

Ansible role designed to run a full postgresql database dump leveraging the pg_dumpall command.

## Requirements

Minimum required ansible version **2.5.0**

### Pre-conditions

This role assumes that the **peer authentication** is enabled for the user `postgres` (or for the role set through the `postgresql_backup_owner` variable). Different scenarios and detections of authentication strategies will be progressively implemented.

## Features

- `postgresql_install_requirements`:
This role relies on the ansible modules (postgresql_user)[https://docs.ansible.com/ansible/latest/modules/postgresql_user_module.html], (postgresql_privs)[https://docs.ansible.com/ansible/latest/modules/postgresql_privs_module.html] and (expect)[https://docs.ansible.com/ansible/latest/modules/expect_module.html] to provision the temporary user when `postgresql_provision_temporary_user` is set to Yes.
To setup the target system and meet the role's requirements, the variable `postgresql_install_requirements` may be set to Yes and the necessary dependencies will be checked and eventually installed, preventing a failure of the database dump.

- `postgresql_provision_temporary_user`:
This role can conditionally, when `postgresql_provision_temporary_user: Yes`, provision a **read only** user with a minimum set of privileges in order to execute the `pg_dumpall` command. This is a temporary user that will be dropped immediately after the database dump execution. It is flagged to **expire in 1d** in order to be inactive in a scenario where the database dump will be restored. The username is randomized and stored in a log file archived along with the database dump, to facilitate the deletion after the restore procedure.
**This feature increases the security and may prevent any accidental or malicious data alteration during the database dump procedure.**

- `postgresql_dumpall_params`:
The database dump command can be customized providing a list of options. Refer to the role variables set in `defaults/main.yml`, and documented below, for the correct implementation of it

## Role Variables

Variables set in `defaults/main.yml`:

```yaml
# defaults file for postgres_dump

# Mark to Yes when postgresql_provision_temporary_user
# and the remote system does not meet the following requirements:
# psycopg2
# pexpect
postgresql_install_requirements: No

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

# Set to No to skip the service postgresql state task;
# The task will be executed in any case when postgresql_provision_temporary_user is flagged to Yes
postgresql_check_service_state: Yes

# Do NOT set the following options, these flags are set during the main task executions and cannot be overruled
# --host
# --username
# --[no]-password
# --file
# Refer to the official documentation for further settings: 
# https://www.postgresql.org/docs/<your_postgresql_version>/app-pg-dumpall.html
postgresql_dumpall_params:
  - --clean
  - --if-exists

# Set cleanup_after_backup to No, to store the backup files along with the compressed version.
postgresql_cleanup_after_backup: Yes
```

## Example Playbook

The role can be uesed, for instance, as follow:

```yaml
- hosts:
    - postgresql_databases
  become: True
  gather_facts: True

  roles:
    - role: postgres_dump
      postgresql_provision_temporary_user: Yes
      postgresql_cleanup_after_backup: Yes
 ```

## License

**CC0 1.0**

## Author Information

[Francesco Cosentino](https://www.linkedin.com/in/francesco-cosentino/) <fc@hyperd.sh>
