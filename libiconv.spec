%define prefix /usr/local/samma

Summary: libiconv
Name: libiconv
Group: Development/Languages
Version: 1.12
Release: 1
Packager: Designet
License: Designet
Vendor: DesigNET, INC

Source0: libiconv-1.12.tar.gz

Patch1: libiconv-1.12-ja-4.patch

BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

%description
libiconv

%prep

%setup

%patch1 -p1

CFLAGS="$RPM_OPT_FLAGS" ./configure --prefix=%{prefix}
make

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{prefix}/lib
mkdir -p $RPM_BUILD_ROOT%{prefix}/include
#mkdir -p $RPM_BUILD_ROOT%{_mandir}/man/man3
mkdir -p $RPM_BUILD_ROOT%{prefix}/man/man3
make prefix=$RPM_BUILD_ROOT%{prefix} install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%{prefix}/lib/*
%{prefix}/include/*
%{prefix}/bin/*
%{prefix}/share/*
