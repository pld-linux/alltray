Summary:	AllTray - small program to dock application into the system tray
Summary(pl):	AllTray - ma³y program do dokowania aplikacji w system tray'u
Name:		alltray
Version:	0.42
Release:	1
License:	GPL
Group:		X11/Applications
Source0:	http://dl.sourceforge.net/alltray/%{name}-%{version}.tar.gz
# Source0-md5:	2646556343a0350b4ede7dbd228c78ee
Patch0:		%{name}-notitlechange_nomenutitle.patch
URL:		http://alltray.sourceforge.net/
BuildRequires:	gtk+2-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
With AllTray you can dock any application with no native tray icon
(like Evolution, Thunderbird, Terminals) into the system tray. It
works well with Gnome, KDE, XFCE 4, Fluxbox and WindowMaker.

%description -l pl
Dziêki AllTray mo¿esz zdokowaæ dowoln± aplikacjê (jak Evolution,
Thunderbird czy terminal) do systemtray'a. Dzia³a dobrze z Gnome, KDE,
XFCE 4, Fluxboxem i WindowMakerem.

%prep
%setup -q
%patch0 -p1

%build
%{__aclocal}
%{__automake}
%{__autoconf}
%{__automake}
%configure

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%doc AUTHORS ChangeLog COPYING
