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


%changelog
* Mon May 02 2011 Funda Wang <fwang@mandriva.org> 0.8.0-1
+ Revision: 662290
- fix build with gcc 4.6
- new version 0.8.0

* Wed Sep 09 2009 Thierry Vignaud <tv@mandriva.org> 0.7.3-2mdv2010.0
+ Revision: 434980
- rebuild

* Thu Apr 24 2008 Funda Wang <fwang@mandriva.org> 0.7.3-1mdv2009.0
+ Revision: 197225
- New version 0.7.3

* Thu Jan 03 2008 Olivier Blin <oblin@mandriva.com> 0.7.1-1mdv2008.1
+ Revision: 140933
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request
    - import wpd2sxw


* Sun Jun 11 2006 Charles A Edwards <eslrahc@mandriva.org> 0.7.1-1mdv2007.0
- 0.7.1
- mkrel

* Fri Oct 14 2005 Götz Waschk <waschk@mandriva.org> 0.7.0-2mdk
- rebuild for new libgsf

* Wed Mar 30 2005 Charles A Edwards <eslrahc@mandrake.org> 0.7.0-1mdk
- 0.7.0
- source now writerperfect

* Sat Jun 05 2004 Marcel Pol <mpol@mandrake.org> 0.6.0-2mdk
- rebuild

* Sun Feb 01 2004 Marcel Pol <mpol@mandrake.org> 0.6.0-1mdk
- 0.6.0

* Sun Nov 16 2003 Marcel Pol <mpol@gmx.net> 0.5.2.1-1mdk
- 0.5.2

* Thu Sep 18 2003 Marcel Pol <mpol@gmx.net> 0.5.1-1mdk
- 0.5.1

* Sat May 31 2003 Marcel Pol <mpol@gmx.net> 0.4.0-1mdk
- from Torstein Dybdahl <torsted@runbox.no>
    - Initial Mandrake Release
 
