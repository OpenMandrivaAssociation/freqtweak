%define name 	freqtweak
%define version 0.6.1
%define release  %mkrel 1

Name: 		%{name}
Summary: 	GUI-based sound file tweaker
Version: 	%{version}
Release: 	%{release}

Source0:	%{name}-%{version}.tar.bz2
#Patch0:	freqtweak-0.5.3-gcc34.patch.bz2
URL:		http://freqtweak.sourceforge.net/
License:	GPL
Group:		Sound
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires:	wxGTK2.4-devel >= 2.4.0-2mdk 
BuildRequires:	fftw-devel jackit-devel

%description
FreqTweak is a tool for FFT-based realtime audio spectral manipulation and
display. It provides several algorithms for processing audio data in the
frequency domain and a highly interactive GUI to manipulate the associated
filters for each. It also provides high-resolution spectral displays in the
form of scrolling-raster spectragrams and energy vs frequency plots
displaying both pre- and post-processed spectra.

%prep
%setup -q
#%patch0 -p0

%build
%configure
%make
										
%install
rm -rf $RPM_BUILD_ROOT
%makeinstall

#menu
mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications/
cat << EOF > %buildroot%{_datadir}/applications/mandriva-%{name}.desktop
[Desktop Entry]
Type=Application
Exec=%{name}
Icon=sound_section
Name=FreqTweak
Comment=Sound manipulator
Categories=Audio;
EOF

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_menus
		
%postun
%clean_menus

%files
%defattr(-,root,root)
%doc README AUTHORS ChangeLog NEWS THANKS
%{_bindir}/%{name}
%{_datadir}/%{name}
%{_mandir}/man1/%{name}.1*
%{_datadir}/applications/mandriva-%{name}.desktop

