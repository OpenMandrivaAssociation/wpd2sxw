Name:		wpd2sxw
Summary:	Convert WordPerfect(tm) documents into OpenOffice.org Writer format
Version:	0.8.0
Release:	1
Source:		http://downloads.sourceforge.net/libwpd/writerperfect-%{version}.tar.bz2
Patch0:		writerperfect-0.8.0-gcc4.6.patch
Group:		Office
URL:		http://libwpd.sf.net/
BuildRoot:	%{_tmppath}/%{name}-%{version}-buildroot
License:	LGPL
BuildRequires:	libwpd-devel >= 0.9.0
BuildRequires:	libwpg-devel >= 0.2.0

%description
Tool for converting Word Perfect documents into OpenOffice.org
Writer format.

%prep
%setup -qn writerperfect-%{version}
%patch0 -p0

%build
%configure2_5x
%make

%install
rm -fr %buildroot
%makeinstall_std

%clean
rm -fr %buildroot

%files
%defattr(-,root,root)
%{_bindir}/*
%doc ChangeLog README
