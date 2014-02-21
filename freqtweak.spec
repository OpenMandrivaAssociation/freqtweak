Name:		freqtweak
Summary:	GUI-based sound file tweaker
Version:	0.7.2
Release:	3
License:	GPLv2+
Group:		Sound
Url:		http://freqtweak.sourceforge.net/
Source0:	http://prdownloads.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
# From Debian: fixes a variable cast error on x86-64 - AdamW 2008/03
Patch0:		freqtweak-0.7.0-long.patch
Patch1:		freqtweak-0.7.2-deb-missing-include.patch
BuildRequires:	wxgtku2.8-devel
BuildRequires:	pkgconfig(fftw3)
BuildRequires:	pkgconfig(jack)
BuildRequires:	pkgconfig(libxml-2.0)
BuildRequires:	pkgconfig(sigc++-1.2)

%description
FreqTweak is a tool for FFT-based realtime audio spectral manipulation and
display. It provides several algorithms for processing audio data in the
frequency domain and a highly interactive GUI to manipulate the associated
filters for each. It also provides high-resolution spectral displays in the
form of scrolling-raster spectragrams and energy vs frequency plots
displaying both pre- and post-processed spectra.

%files
%doc README AUTHORS ChangeLog NEWS THANKS
%{_bindir}/%{name}
%{_datadir}/%{name}
%{_mandir}/man1/%{name}.1*
%{_datadir}/applications/%{name}.desktop

#----------------------------------------------------------------------------

%prep
%setup -q
%patch0 -p0 -b .long
%patch1 -p1

%build
%configure2_5x
%make

%install
%makeinstall_std

#menu
mkdir -p %{buildroot}%{_datadir}/applications/
cat << EOF > %{buildroot}%{_datadir}/applications/%{name}.desktop
[Desktop Entry]
Type=Application
Exec=%{name}
Icon=sound_section
Name=FreqTweak
Comment=Sound manipulator
Categories=AudioVideo;Audio;
EOF

