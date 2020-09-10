## Workflow

- Building locally

```
fedpkg -dist f32 mockbuild
```

Building with custom parameters:

```
fedpkg --dist f32 mockbuild  --mock-config ./fedora-32-x86_64-bazel.cfg --enable-network
```

- Cleanup

```
fedpkg clean -x
```

## Running builds on copr

Create copr api config by visiting [https://copr.fedorainfracloud.org/api/](https://copr.fedorainfracloud.org/api/)
and put it into `.devcontainer/config/copr` file.