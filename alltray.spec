Summary:	AllTray - small program to dock application into the system tray
Summary(pl):	AllTray - ma�y program do dokowania aplikacji w tacce systemowej
Name:		alltray
Version:	0.42
Release:	1
License:	GPL
Group:		X11/Applications
Source0:	http://dl.sourceforge.net/alltray/%{name}-%{version}.tar.gz
# Source0-md5:	2646556343a0350b4ede7dbd228c78ee
Patch0:		%{name}-notitlechange_nomenutitle.patch
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
Dzi�ki AllTray mo�na zdokowa� dowoln� aplikacj� (jak Evolution,
Thunderbird czy terminal) do tacki systemowej. Dzia�a dobrze z GNOME,
KDE, XFCE 4, Fluxboksem i WindowMakerem.

%prep
%setup -q
%patch0 -p1

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
