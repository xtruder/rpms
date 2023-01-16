# RPMs

Custom x-truder rpm packages. You can install packages via https://copr.fedorainfracloud.org/coprs/offlinehacker/xtruder-rpms/

## Writing spec file

### Notes regarding arch and copr

Copr requires `BuildArch` to be set to `x86_64` or `aarch64`, otherwise it will refuse to download
sources for some reason.

## Building packages

- Building locally

```
fedpkg --release f37 mockbuild --enable-network
```

Building with custom parameters:

```
fedpkg --release f37 mockbuild  --mock-config ./fedora-37-x86_64-bazel.cfg --enable-network
```

- Cleanup

```
fedpkg clean -x
```

## Running builds on copr

Create copr api config by visiting [https://copr.fedorainfracloud.org/api/](https://copr.fedorainfracloud.org/api/)
and put it into `.devcontainer/config/copr` file.

## Installing packages

- Add yum repo

```
cat /etc/yum.repos.d/offlinehacker-xtruder-rpms-fedora.repo 
[copr:copr.fedorainfracloud.org:offlinehacker:xtruder-rpms]
name=Copr repo for xtruder-rpms owned by offlinehacker
baseurl=https://download.copr.fedorainfracloud.org/results/offlinehacker/xtruder-rpms/fedora-$releasever-$basearch/
type=rpm-md
skip_if_unavailable=True
gpgcheck=1
gpgkey=https://download.copr.fedorainfracloud.org/results/offlinehacker/xtruder-rpms/pubkey.gpg
repo_gpgcheck=0
enabled=1
enabled_metadata=1
```

- Installing on fedora silverblue

```
sudo rpm-ostree install <pkg_name>
```

- Cleaning package cache

```
sudo rpm-ostree  refresh-md -f
```

## Packaging

### Preparing package and downloading sources

```
fedpkg prep
```

This will download and unpack sources

If you have issue with that command you can use `spectool` to download sources instead:

```
spectool  -g -C . myspec.spec
```

### Packaging python packages

To generate package from pypi use: https://github.com/fedora-python/pyp2rpm (`sudo dnf install pyp2rpm`)

Example usage:

```
pyp2rpm -o fedora trezor_agent > trezor_agent.spec
```

### Packaging go packages

This guide will get you started: https://developers.redhat.com/articles/2021/05/21/build-your-own-rpm-package-sample-go-program#


## Notes

- Unpacking rpm files

```shell
rpm2cpio gnome-shell-extension-workspaces-bar-0-0.20211125git667571d.fc37.noarch.rpm | cpio -idmv
```