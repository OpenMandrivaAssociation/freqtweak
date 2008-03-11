%define cvs	20080311
%if %cvs
%define release	%mkrel 0.%cvs.1
%define tarname	%name-%cvs.tar.lzma
%define dirname	%name
%else
%define release	%mkrel 1
%define tarname	%name-%version.tar.bz2
%define dirname	%name-%version
%endif

Name: 		freqtweak
Summary: 	GUI-based sound file tweaker
Version: 	0.7.0
Release: 	%{release}
Source0:	http://prdownloads.sourceforge.net/%{name}/%{tarname}
URL:		http://freqtweak.sourceforge.net/
License:	GPLv2+
Group:		Sound
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires:	wxGTK2.6-devel
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

%post
%{update_menus}
		
%postun
%{clean_menus}

%files
%defattr(-,root,root)
%doc README AUTHORS ChangeLog NEWS THANKS
%{_bindir}/%{name}
%{_datadir}/%{name}
%{_mandir}/man1/%{name}.1*
%{_datadir}/applications/mandriva-%{name}.desktop

