Summary:	AllTray - small program to dock application into the system tray
Summary(pl):	AllTray - ma³y program do dokowania aplikacji w tacce systemowej
Name:		alltray
Version:	0.51
Release:	2
License:	GPL v2
Group:		X11/Applications
Source0:	http://dl.sourceforge.net/alltray/%{name}-%{version}.tar.gz
# Source0-md5:	44466a011131c4f132b64722dbdd8ae3
#Patch0:		%{name}-notitlechange_nomenutitle.patch
URL:		http://alltray.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gtk+2-devel >= 2:2.4.0
BuildRequires:	pkgconfig
Requires:	gtk+2 >= 2:2.4.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
With AllTray you can dock any application with no native tray icon
(like Evolution, Thunderbird, Terminals) into the system tray. It
works well with Gnome, KDE, XFCE 4, Fluxbox and WindowMaker.

%description -l pl
Dziêki AllTray mo¿na zdokowaæ dowoln± aplikacjê (jak Evolution,
Thunderbird czy terminal) do tacki systemowej. Dzia³a dobrze z GNOME,
KDE, XFCE 4, Fluxboksem i WindowMakerem.

%package devel
Summary:	Libraries and header files for alltray
Summary(pl):	Biblioteki i pliki nag³ówkowe dla alltray
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Libraries and header files for alltray.

%description devel -l pl
Biblioteki i pliki nag³ówkowe dla alltray.

%package static
Summary:	Static libraries for alltray
Summary(pl):	Statyczne biblioteki dla alltray
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
alltray static libraries.

%description static -l pl
Biblioteki statyczne dla alltray.

%prep
%setup -q
#%%patch0 -p1

%build
%{__aclocal}
%{__automake}
%{__autoconf}
%configure

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/liballtray*.so.*.*
%{_mandir}/man1/alltray.1*

%files devel
%defattr(644,root,root,755)
%{_libdir}/liballtray*.la

%files static
%defattr(644,root,root,755)
%{_libdir}/liballtray*.a
