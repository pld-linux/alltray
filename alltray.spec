Summary:	AllTray - small program to dock application into the system tray
Summary(pl.UTF-8):	AllTray - mały program do dokowania aplikacji w tacce systemowej
Name:		alltray
Version:	0.70
Release:	2
License:	GPL v2+
Group:		X11/Applications
#Source0Download: https://github.com/mbt/alltray/releases
# dev versions:
#Source0:	https://github.com/mbt/alltray/archive/v%{version}/%{name}-%{version}.tar.gz
Source0:	http://downloads.sourceforge.net/alltray/%{name}-%{version}.tar.gz
# Source0-md5:	675a0a60f22fae04da787095ef0bd7d9
Patch0:		%{name}-link.patch
URL:		https://launchpad.net/alltray
BuildRequires:	GConf2-devel >= 2.0
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gdk-pixbuf2-xlib-devel >= 2.0
BuildRequires:	gtk+2-devel >= 2:2.4.0
BuildRequires:	libtool
BuildRequires:	pkgconfig
BuildRequires:	xorg-lib-libX11-devel
Requires:	gtk+2 >= 2:2.4.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
With AllTray you can dock any application with no native tray icon
(like Evolution, Thunderbird, Terminals) into the system tray. It
works well with Gnome, KDE, Xfce 4, Fluxbox and WindowMaker.

%description -l pl.UTF-8
Dzięki AllTray można zadokować dowolną aplikację (jak Evolution,
Thunderbird czy terminal) do tacki systemowej. Działa dobrze z GNOME,
KDE, Xfce 4, Fluxboksem i WindowMakerem.

%prep
%setup -q
%patch0 -p1

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-static

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# liballtray.so.0.0.0 is explicitly LD_PRELOADed
%{__rm} $RPM_BUILD_ROOT%{_libdir}/lib*.{la,so}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README
%attr(755,root,root) %{_bindir}/alltray
%attr(755,root,root) %{_libdir}/liballtray.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/liballtray.so.0
%{_mandir}/man1/alltray.1*
%{_desktopdir}/alltray.desktop
%{_pixmapsdir}/alltray.png
