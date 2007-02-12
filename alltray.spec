Summary:	AllTray - small program to dock application into the system tray
Summary(pl.UTF-8):	AllTray - mały program do dokowania aplikacji w tacce systemowej
Name:		alltray
Version:	0.66
Release:	1
License:	GPL v2
Group:		X11/Applications
Source0:	http://dl.sourceforge.net/alltray/%{name}-%{version}.tar.gz
# Source0-md5:	78b43bd2e19258b0518af99e21123561
#Patch0:		%{name}-notitlechange_nomenutitle.patch
URL:		http://alltray.sourceforge.net/
BuildRequires:	GConf2-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gtk+2-devel >= 2:2.4.0
BuildRequires:	libtool
BuildRequires:	pkgconfig
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
#%%patch0 -p1

%build
%{__aclocal}
%{__automake}
%{__autoconf}
%configure \
	--disable-static

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT%{_libdir}/lib*.la

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/liballtray*.so.*.*
%{_mandir}/man1/alltray.1*
%{_desktopdir}/%{name}.desktop
%{_pixmapsdir}/*.png
