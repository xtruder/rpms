# RPMs

Custom x-truder rpm packages. You can install packages via https://copr.fedorainfracloud.org/coprs/offlinehacker/xtruder-rpms/

## Writing spec file

### Notes regarding arch and copr

Copr requires `BuildArch` to be set to `x86_64` or `aarch64`, otherwise it will refuse to download
sources for some reason.

## Building packages

- Building locally

```
fedpkg --release f35 mockbuild
```

Building with custom parameters:

```
fedpkg --release f35 mockbuild  --mock-config ./fedora-35-x86_64-bazel.cfg --enable-network
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

## Development

- Preparing package:

```
fedpkg prep
```

This will download and unpack sources
