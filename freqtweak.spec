%define rel	2
%define cvs	0
%if %cvs
%define release	%mkrel 0.%cvs.%rel
%define tarname	%name-%cvs.tar.lzma
%define dirname	%name
%else
%define release	%mkrel %rel
%define tarname	%name-%version.tar.gz
%define dirname	%name-%version
%endif

Name: 		freqtweak
Summary: 	GUI-based sound file tweaker
Version: 	0.7.2
Release: 	%{release}
Source0:	http://prdownloads.sourceforge.net/%{name}/%{tarname}
# From Debian: fixes a variable cast error on x86-64 - AdamW 2008/03
Patch0:		freqtweak-0.7.0-long.patch
Patch1:		freqtweak-0.7.2-deb-missing-include.patch
URL:		http://freqtweak.sourceforge.net/
License:	GPLv2+
Group:		Sound
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires:	wxgtku-devel
BuildRequires:	fftw-devel
BuildRequires:	jackit-devel
BuildRequires:	libxml2-devel
BuildRequires:	libsigc++1.2-devel

%description
FreqTweak is a tool for FFT-based realtime audio spectral manipulation and
display. It provides several algorithms for processing audio data in the
frequency domain and a highly interactive GUI to manipulate the associated
filters for each. It also provides high-resolution spectral displays in the
form of scrolling-raster spectragrams and energy vs frequency plots
displaying both pre- and post-processed spectra.

%prep
%setup -q -n %{dirname}
%patch0 -p0 -b .long
%patch1 -p1

%build
%if %cvs
./autogen.sh
%endif
%configure2_5x
%make
										
%install
rm -rf %{buildroot}
%makeinstall

#menu
mkdir -p %{buildroot}%{_datadir}/applications/
cat << EOF > %buildroot%{_datadir}/applications/mandriva-%{name}.desktop
[Desktop Entry]
Type=Application
Exec=%{name}
Icon=sound_section
Name=FreqTweak
Comment=Sound manipulator
Categories=AudioVideo;Audio;
EOF

%clean
rm -rf %{buildroot}

%if %mdkversion < 200900
%post
%{update_menus}
%endif
		
%if %mdkversion < 200900
%postun
%{clean_menus}
%endif

%files
%defattr(-,root,root)
%doc README AUTHORS ChangeLog NEWS THANKS
%{_bindir}/%{name}
%{_datadir}/%{name}
%{_mandir}/man1/%{name}.1*
%{_datadir}/applications/mandriva-%{name}.desktop



%changelog
* Sun Dec 05 2010 Oden Eriksson <oeriksson@mandriva.com> 0.7.2-2mdv2011.0
+ Revision: 610772
- rebuild

* Sat Jan 09 2010 JÃ©rÃ´me Brenier <incubusss@mandriva.org> 0.7.2-1mdv2010.1
+ Revision: 488118
- new version 0.7.2
- drop wx28 patch (merged upstream)
- add a patch from Debian for a missing include

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild

* Sun Dec 28 2008 Adam Williamson <awilliamson@mandriva.org> 0.7.0-0.20080311.2mdv2009.1
+ Revision: 320116
- adjust build deps and rebuild with wx 2.8
- add wx28.patch: make it build with wx 2.8

* Thu Jul 24 2008 Thierry Vignaud <tv@mandriva.org> 0.7.0-0.20080311.1mdv2009.0
+ Revision: 245413
- rebuild

  + Pixel <pixel@mandriva.com>
    - rpm filetriggers deprecates update_menus/update_scrollkeeper/update_mime_database/update_icon_cache/update_desktop_database/post_install_gconf_schemas

* Wed Mar 12 2008 Adam Williamson <awilliamson@mandriva.org> 0.7.0-0.20080311.1mdv2008.1
+ Revision: 187019
- add long.patch (from debian, fixes a code error that prevents build on x86-64)
- build against wxGTK 2.6
- update buildrequires
- spec clean
- update to CVS snapshot (debian's doing this so it's likely safe, and fixes build issues)

  + Thierry Vignaud <tv@mandriva.org>
    - auto convert menu to XDG
    - kill re-definition of %%buildroot on Pixel's request
    - use %%mkrel
    - import freqtweak

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot


* Sun Jul 25 2004 Per Øyvind Karlsen <peroyvind@linux-mandrake.com> 0.6.1-1mdk
- 0.6.1
- drop P0

* Wed Jun 30 2004 Thierry Vignaud <tvignaud@mandrakesoft.com> 0.5.3-2mdk
- rebuild with new g++
- patch 0: fix compiling with new g++

* Mon Feb 16 2004 Austin Acton <austin@mandrake.org> 0.5.3-1mdk
- 0.5.3
- buildrequires for lib64

* Wed Aug 20 2003 Austin Acton <aacton@yorku.ca> 0.5.2-1mdk
- 0.5.2
- add manpage

* Thu Jul 17 2003 Austin Acton <aacton@yorku.ca> 0.5.1-1mdk
- 0.5.1

* Mon Mar 24 2003 Lenny Cartier <lenny@mandrakesoft.com> 0.4.7-1mdk
- 0.4.7

* Thu Feb 13 2003 Götz Waschk <waschk@linux-mandrake.com> 0.4.5-2mdk
- rebuild against wxGTK 2.4

* Thu Jan 30 2003 Austin Acton <aacton@yorku.ca> 0.4.5-1mdk
- initial package
