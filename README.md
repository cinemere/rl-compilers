# rl-compilers

## installation problems:

* to fix some bug with build added the following to `CompilerGym/WORKSPACE`

```
# === Bug with importing argorithm ====
# https://github.com/bazelbuild/rules_scala/issues/726

http_archive(
    name = "zlib",
    build_file = "@bazel_tools//third_party/zlib:BUILD",
    sha256 = "c3e5e9fdd5004dcb542feda5ee4f0ff0744628baf8ed2dd5d66f8ca1197cb1a1",
    strip_prefix = "zlib-1.2.11",
    urls = ["https://zlib.net/zlib-1.2.11.tar.gz"],
)
```

* to fix some torch dependency i used the following torch version:

```
pip install torch==1.11.0
```

* to fix setuptools dependency bugs this recipy from github issues:

```
sudo apt install build-essential libtinfo5
conda create -y -n compiler_gym python=3.10 && conda activate compiler_gym
pip install pip==22.2 setuptools==59.6.0
pip install compiler_gym==0.2.5
```