# Ansible Role: MongoDB

[![ci_v4](https://github.com/trfore/ansible-role-mongodb-install/actions/workflows/ci_v4.yml/badge.svg?branch=main)](https://github.com/trfore/ansible-role-mongodb-install/actions/workflows/ci_v4.yml)
[![cd](https://github.com/trfore/ansible-role-mongodb-install/actions/workflows/cd.yml/badge.svg?branch=main)](https://github.com/trfore/ansible-role-mongodb-install/actions/workflows/cd.yml)

This role installs the MongoDB Community edition server metapackage, `mongodb-org`, via the OS's package manager (default) or the server binaries via tar file. It currently defaults to installing the **latest release from version 4**, you can install a newer major version by setting `mongodb_version: 6.0.5`, see 'Tested Platforms and Versions' section for a compatibility matrix.

Alternatively, you can install the MongoDB server binaries - `mongo`, `mongod`, `mongos`, by setting `mongodb_pkg_install: false` and the role will download the **latest tarball from version 4** or a newer major version by setting `mongodb_version`. If you would like to install the binary from your local Ansible control host, download the appropriate tar file, `mongodb-linux-x86_64-{DISTRO}-{VERSION}.tgz`, to your `files` directory and set the following two variables in your playbook:

- `mongodb_tar_src: mongodb-linux-x86_64-{DISTRO}-{VERSION}.tgz`
- `mongodb_tar_src_remote: false`

See 'Example Playbooks' section for working examples. This role **does not configure the server**, it uses the default configuration values and minimal recommended `ulimit` settings. Its recommended to configure the server for production use, for details see: https://www.mongodb.com/docs/manual/administration/production-notes/

### Install the Role

You can install this role with the Ansible Galaxy CLI:

```bash
ansible-galaxy install trfore.mongodb_install
```

You can also include it in a `requirements.yml` file and install it with `ansible-galaxy role install -r requirements.yml`, using the format:

```yaml
---
roles:
  - trfore.mongodb_install
```

## Tested Platforms and Versions

### MongoDB Community `6.0.5`

- [![ci_v6](https://github.com/trfore/ansible-role-mongodb-install/actions/workflows/ci_v6.yml/badge.svg?branch=main)](https://github.com/trfore/ansible-role-mongodb-install/actions/workflows/ci_v6.yml)
- CentOS Stream 8
- Debian 10 & 11
- Ubuntu 20.04 & 22.04

### MongoDB Community `5.0.15`

- [![ci_v5](https://github.com/trfore/ansible-role-mongodb-install/actions/workflows/ci_v5.yml/badge.svg?branch=main)](https://github.com/trfore/ansible-role-mongodb-install/actions/workflows/ci_v5.yml)
- CentOS Stream 8
- Debian 10 & 11
- Ubuntu 20.04

### MongoDB Community `4.4.19`

- [![ci_v4](https://github.com/trfore/ansible-role-mongodb-install/actions/workflows/ci_v4.yml/badge.svg?branch=main)](https://github.com/trfore/ansible-role-mongodb-install/actions/workflows/ci_v4.yml)
- CentOS Stream 8
- Debian 10
- Ubuntu 20.04

## Requirements

- `community.general.yum_versionlock` (for CentOS & RHEL target host)
  ```bash
  ansible-galaxy collection install community.general
  ```

## Role Variables

### Common Variables

Common variables are listed below, along with default values (see `defaults/main.yml`):

| Variable                  | Default   | Description                                            | Required  |
| ------------------------- | --------- | ------------------------------------------------------ | --------- |
| mongodb_pkg_install       | `true`    | Boolean, `true` to install MongoDB via package manager | No        |
| mongodb_version           | `4.4.19`  | MongoDB Community stable releases `v4.4`, `v5`, `v6`   | Yes       |
| mongodb_version_maj_minor | Automatic | Extracts major and minor values from `mongodb_version` | Automatic |

### Package Install Variables

`defaults/main.yml`:

| Variable              | Default          | Description                                                           | Required |
| --------------------- | ---------------- | --------------------------------------------------------------------- | -------- |
| mongodb_gpg_key       | URL              | MongoDB GPG Key                                                       | No       |
| mongodb_pkg_hold      | `true`           | Boolean, `true` to hold package version                               | No       |
| mongodb_pkg_hold_list | MongoDB Packages | List of MongoDB packages installed from `mongodb-org`, `v4.4` to `v6` | No       |

### Binary Install Variables

`defaults/main.yml`:

| Variable               | Default    | Description                                                           | Required |
| ---------------------- | ---------- | --------------------------------------------------------------------- | -------- |
| mongodb_tar_src        | URL        | URL or relative PATH, MongoDB Community binary tar file (tar install) | No       |
| mongodb_tar_src_remote | `true`     | Boolean, `true` if downloading from URL (tar install)                 | No       |
| mongodb_path_exec      | `/usr/bin` | PATH, MongoDB binary path (tar install)                               | No       |

OS specific variables are listed below, along with default values:

`vars/debian.yml`:

| Variable             | Default                             | Description                                 | Required |
| -------------------- | ----------------------------------- | ------------------------------------------- | -------- |
| mongodb_path_db      | `/var/lib/mongodb`                  | PATH, MongoDB database folder (tar install) | No       |
| mongodb_path_log     | `/var/log/mongodb`                  | PATH, MongoDB log folder (tar install)      | No       |
| mongodb_dependencies | `["libcurl4","openssl","liblzma5"]` | Required packages for MongoDB (tar install) | No       |

`vars/redhat.yml`:

| Variable             | Default                                   | Description                                 | Required |
| -------------------- | ----------------------------------------- | ------------------------------------------- | -------- |
| mongodb_path_db      | `/var/lib/mongo`                          | PATH, MongoDB database folder (tar install) | No       |
| mongodb_path_log     | `/var/log/mongodb`                        | PATH, MongoDB log folder (tar install)      | No       |
| mongodb_dependencies | `["libcurl-minimal","openssl","xz-libs"]` | Required packages for MongoDB (tar install) | No       |

## Dependencies

- `community.general.yum_versionlock` (for CentOS & RHEL target host)

  ```bash
  ansible-galaxy collection install community.general
  ```

## Example Playbooks

- Package install via distribution's package manager.

```yaml
- hosts: servers
  roles:
    - name: Install MongoDB
      role: trfore.mongodb_install
```

```yaml
- hosts: servers
  vars:
    mongodb_pkg_install: true
    mongodb_version: '6.0.5'
  roles:
    - name: Install MongoDB
      role: trfore.mongodb_install
```

- Binary install from tar file.

```yaml
- hosts: servers
  vars:
    mongodb_pkg_install: false
    mongodb_version: '6.0.5'
  roles:
    - name: Install MongoDB
      role: trfore.mongodb_install
```

- Binary install from tar file, if you manually download the tarball to your control host.

```yaml
- hosts: servers
  vars:
    mongodb_pkg_install: false
    mongodb_tar_src: mongodb-linux-x86_64-debian10-4.4.19.tgz
    mongodb_tar_src_remote: false
  roles:
    - name: Install MongoDB
      role: trfore.mongodb_install
```

## License

This Ansible role is MIT.

MongoDB Community is Server Side Public License software from MongoDB, Inc. For additional information see: https://www.mongodb.com/licensing/server-side-public-license

## Author Information

Taylor Fore (https://github.com/trfore)

## References

### MongoDB

- https://www.mongodb.com/download-center/community/releases
- https://www.mongodb.com/docs/manual/administration/install-on-linux/
- https://www.mongodb.com/docs/manual/administration/production-notes/
- https://www.mongodb.com/docs/manual/reference/configuration-options/
- https://www.mongodb.com/docs/manual/reference/ulimit/
