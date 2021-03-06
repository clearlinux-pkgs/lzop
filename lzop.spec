#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : lzop
Version  : 1.04
Release  : 3
URL      : https://www.lzop.org/download/lzop-1.04.tar.gz
Source0  : https://www.lzop.org/download/lzop-1.04.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : GPL-2.0
Requires: lzop-bin = %{version}-%{release}
Requires: lzop-license = %{version}-%{release}
Requires: lzop-man = %{version}-%{release}
BuildRequires : lzo-dev

%description
==================================================================
lzop -- a very fast file compressor
==================================================================

%package bin
Summary: bin components for the lzop package.
Group: Binaries
Requires: lzop-license = %{version}-%{release}

%description bin
bin components for the lzop package.


%package doc
Summary: doc components for the lzop package.
Group: Documentation
Requires: lzop-man = %{version}-%{release}

%description doc
doc components for the lzop package.


%package license
Summary: license components for the lzop package.
Group: Default

%description license
license components for the lzop package.


%package man
Summary: man components for the lzop package.
Group: Default

%description man
man components for the lzop package.


%prep
%setup -q -n lzop-1.04
cd %{_builddir}/lzop-1.04

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1604608416
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$FFLAGS -fno-lto "
export FFLAGS="$FFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
%configure --disable-static
make  %{?_smp_mflags}

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make %{?_smp_mflags} check

%install
export SOURCE_DATE_EPOCH=1604608416
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/lzop
cp %{_builddir}/lzop-1.04/COPYING %{buildroot}/usr/share/package-licenses/lzop/4cc77b90af91e615a64ae04893fdffa7939db84c
%make_install

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/lzop

%files doc
%defattr(0644,root,root,0755)
%doc /usr/share/doc/lzop/*

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/lzop/4cc77b90af91e615a64ae04893fdffa7939db84c

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/lzop.1
