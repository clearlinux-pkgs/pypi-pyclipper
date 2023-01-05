#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pypi-pyclipper
Version  : 1.3.0.post4
Release  : 11
URL      : https://files.pythonhosted.org/packages/dd/03/09e2415b72b470851588dfc7c9b7b4f410a79ed8e2c6c1fb25dfec789b70/pyclipper-1.3.0.post4.tar.gz
Source0  : https://files.pythonhosted.org/packages/dd/03/09e2415b72b470851588dfc7c9b7b4f410a79ed8e2c6c1fb25dfec789b70/pyclipper-1.3.0.post4.tar.gz
Summary  : Cython wrapper for the C++ translation of the Angus Johnson's Clipper library (ver. 6.4.2)
Group    : Development/Tools
License  : MIT
Requires: pypi-pyclipper-filemap = %{version}-%{release}
Requires: pypi-pyclipper-lib = %{version}-%{release}
Requires: pypi-pyclipper-license = %{version}-%{release}
Requires: pypi-pyclipper-python = %{version}-%{release}
Requires: pypi-pyclipper-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pypi(cython)
BuildRequires : pypi(setuptools)
BuildRequires : pypi(setuptools_scm)
BuildRequires : pypi(setuptools_scm_git_archive)
BuildRequires : pypi(wheel)

%description
About
=====
.. image:: https://badge.fury.io/py/pyclipper.svg
:target: https://badge.fury.io/py/pyclipper
.. image:: https://github.com/fonttools/pyclipper/workflows/Build%20+%20Deploy/badge.svg
:target: https://github.com/fonttools/pyclipper/actions?query=workflow%3A%22Build+%2B+Deploy%22

%package filemap
Summary: filemap components for the pypi-pyclipper package.
Group: Default

%description filemap
filemap components for the pypi-pyclipper package.


%package lib
Summary: lib components for the pypi-pyclipper package.
Group: Libraries
Requires: pypi-pyclipper-license = %{version}-%{release}
Requires: pypi-pyclipper-filemap = %{version}-%{release}

%description lib
lib components for the pypi-pyclipper package.


%package license
Summary: license components for the pypi-pyclipper package.
Group: Default

%description license
license components for the pypi-pyclipper package.


%package python
Summary: python components for the pypi-pyclipper package.
Group: Default
Requires: pypi-pyclipper-python3 = %{version}-%{release}

%description python
python components for the pypi-pyclipper package.


%package python3
Summary: python3 components for the pypi-pyclipper package.
Group: Default
Requires: pypi-pyclipper-filemap = %{version}-%{release}
Requires: python3-core
Provides: pypi(pyclipper)

%description python3
python3 components for the pypi-pyclipper package.


%prep
%setup -q -n pyclipper-1.3.0.post4
cd %{_builddir}/pyclipper-1.3.0.post4
pushd ..
cp -a pyclipper-1.3.0.post4 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1668619832
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
export MAKEFLAGS=%{?_smp_mflags}
python3 -m build --wheel --skip-dependency-check --no-isolation
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 -m build --wheel --skip-dependency-check --no-isolation

popd

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-pyclipper
cp %{_builddir}/pyclipper-%{version}/LICENSE %{buildroot}/usr/share/package-licenses/pypi-pyclipper/eb3e3ccba1629cffa0ea8b33b7149a8b17b32bba || :
pip install --root=%{buildroot} --no-deps --ignore-installed dist/*.whl
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
pip install --root=%{buildroot}-v3 --no-deps --ignore-installed dist/*.whl
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files filemap
%defattr(-,root,root,-)
/usr/share/clear/filemap/filemap-pypi-pyclipper

%files lib
%defattr(-,root,root,-)
/usr/share/clear/optimized-elf/other*

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-pyclipper/eb3e3ccba1629cffa0ea8b33b7149a8b17b32bba

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
