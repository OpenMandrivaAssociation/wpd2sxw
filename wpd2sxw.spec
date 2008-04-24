%define rel        1
%define name	wpd2sxw
%define sourcename writerperfect
%define version	0.7.3
%define release	%mkrel %{rel}


Name:		%{name}
Summary:	Convert WordPerfect(tm) documents into OpenOffice.org Writer format
Version:	%{version}
Release:	%{release}
Source:		%{sourcename}-%{version}.tar.gz
Group:		Office
URL:		http://libwpd.sf.net/
BuildRoot:	%{_tmppath}/%{name}-%{version}-buildroot
License:	LGPL
BuildRequires:	libwpd-devel >= 0.7.0
Provides:	%{name} = %{version}-%{release}

%description
Tool for converting Word Perfect documents into OpenOffice.org
Writer format.


%prep
%setup -q -n %{sourcename}-%{version}

%build
%configure2_5x

%make

%install
umask 022
if [ -d $RPM_BUILD_ROOT ]; then rm -r $RPM_BUILD_ROOT; fi
%make DESTDIR=$RPM_BUILD_ROOT install

%clean
if [ -d $RPM_BUILD_ROOT ]; then rm -r $RPM_BUILD_ROOT; fi

%files
%defattr(-,root,root)
%{_bindir}/*
%doc CHANGES README

