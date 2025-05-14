# Contributing

## Contribute

- [Fork the repository](https://github.com/trfore/ansible-role-mongodb-install/fork) on github and clone it.
- Create a new branch and add your code.
- Write test that cover the changes and expected outcome.
- Test your changes locally using `tox`.
  - All pushed code is tested using GH runners on a broad test matrix that covers several MongoDB versions and Linux distributions.
  - The Tox configuration mirrors the test matrix on GH, however, for local testing feel free to choose one of the default test with the latest MongoDB release and your preferred OS, e.g. `py3.11-ansible2.18-mongo8-ubuntu24-default`; and any new test you wish to add to avoid running the large test matrix on your local machine.
- Push the changes to your fork and submit a pull-request on github.

```sh
## example workflow ##
git clone https://github.com/USERNAME/ansible-role-mongodb-install && cd ansible-role-mongodb-install
git checkout -b MY_BRANCH
# add code and test
tox run-parallel
git push -u origin MY_BRANCH
gh pr create --title 'feature: add ...'
```

## Local Testing

- A local installation of [Docker](https://docs.docker.com/engine/installation/) is required to run the `molecule` test scenarios.

### Using Tox

- Tox automates the process of running formatting/linting tools and Ansible Molecule tests.
- All `tox` environments are created within the project directory under `.tox`.

```sh
# list environments and test
tox list
# lint all files
tox -e lint run

# run a specific test environment
tox -e py3.11-ansible2.18-mongo8-ubuntu24-default run

# run all test in parallel
tox run-parallel
```

- For iterative development and testing, the tox molecule environments are written to accept `molecule` arguments. This
  allows for codebase changes to be tested as you write across multiple distros and versions of `ansible-core`. Note:
  When passing molecule args via tox, include the scenario arg `-s [SCENARIO_NAME]`.

```sh
# molecule converge
tox -e py3.11-ansible2.18-mongo8-ubuntu24-default run -- converge -s default
# molecule test w/o destroying the container
tox -e py3.11-ansible2.18-mongo8-ubuntu24-default run -- test -s default --destroy=never

# exec into the container via Tox
tox -e py3.11-ansible2.18-mongo8-ubuntu24-default run -- login -s default
# exec into the container via Docker
docker exec -it py3.11-ansible2.18-mongo8-ubuntu24-default  bash

# parallel testing
tox -f default run-parallel -- test -s default --destroy=never
# remove all containers
tox -f default run-parallel -- destroy -s default
```

- You can also pass environment variables to tox for: `MOLECULE_IMAGE` and `MONGODB_VERSION`.

```sh
# use a different docker image
MOLECULE_IMAGE='trfore/docker-debian13-systemd' tox -e py-ansible2.17-mongo8-debian12-default run

# test a specific version of MongoDB
MONGODB_VERSION='8.0.0' tox -e py-ansible2.17-mongo8-debian12-default run
```

### Manually using Ansible Molecule

- Setup a virtual development environment using python virtual environments.
- Install the pre-commit hooks.

```sh
cd ansible-role-mongodb-install
python3 -m venv .venv && source .venv/bin/activate
python3 -m pip install -r requirements/dev-requirements.txt
pre-commit install

# test code using molecule
molecule test

# set a specific scenario and keep container running
molecule test -s default --destroy=never

# format and lint code using pre-commit
pre-commit run --all-files

# commit your changes
git add ...
git commit -m 'feature: ...'
git push ...
```

## Additional References

- [Ansible community guide](https://docs.ansible.com/ansible/devel/community/index.html)
- [Github Docs: Forking a repository](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/working-with-forks/fork-a-repo#forking-a-repository)
- [Ansible Docs: `ansible-core` support matrix](https://docs.ansible.com/ansible/latest/reference_appendices/release_and_maintenance.html#ansible-core-support-matrix)
- [MongoDB Docs: MongoDB Agent Compatibility Matrix](https://www.mongodb.com/docs/ops-manager/current/core/requirements/#operating-systems-compatible-with-the-mongodb-agent)
- [MongoDB Docs: Enabling Transparent Hugepages (THP) for MongoDB 8](https://www.mongodb.com/docs/manual/administration/tcmalloc-performance/)
- [MongoDB Docs: Disabling Transparent Hugepages (THP) for MongoDB 7 or Earlier](https://www.mongodb.com/docs/manual/tutorial/disable-transparent-huge-pages/)
