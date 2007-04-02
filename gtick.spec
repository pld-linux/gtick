#
# Conditional build:
%bcond_without  sndfile		# build without sndfile
#
Summary:	Metronome application for GNU/Linux
Summary(pl.UTF-8):	Metronom dla Linuksa
Name:		gtick
Version:	0.3.13
Release:	1
License:	GPL
Group:		X11/Applications/Sound
Source0:	http://www.antcom.de/gtick/download/%{name}-%{version}.tar.gz
# Source0-md5:	13365ce8f605657370518dd62df8994b
Source1:	%{name}.desktop
URL:		http://www.antcom.de/gtick/
BuildRequires:	gtk+2-devel
%{?with_sndfile:BuildRequires:  libsndfile-devel}
BuildRequires:	pkgconfig
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
gtick is a metronome application supporting different meters (Even,
2/4, 3/4, 4/4 and more) and speeds ranging from 10 to 1000 bpm. It
utilizes GTK+ and OSS (ALSA compatible).

%description -l pl.UTF-8
Metronom muzyczny z estetycznym i wygodnym interfejsem GTK+.
Kompatybilny z OSS i ALSA. Jest łatwy w obsłudze oraz posiada
możliwość regulacji parametrów w szerokich zakresach.

%prep
%setup -q

%build
%configure \
	--with%{!?with_sndfile:out}-sndfile
%{__make}

%install

rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_desktopdir} \
	$RPM_BUILD_ROOT%{_pixmapsdir}

install %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}
install src/icon64x64.xpm $RPM_BUILD_ROOT%{_pixmapsdir}/%{name}.xpm

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/%{name}
%{_mandir}/man1/%{name}.1.*
%{_desktopdir}/%{name}.desktop
%{_pixmapsdir}/%{name}.xpm
%doc README TODO ChangeLog
%doc doc/NOTES
%doc NEWS THANKS INSTALL AUTHORS ABOUT-NLS
