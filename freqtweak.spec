%define rel	1
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

