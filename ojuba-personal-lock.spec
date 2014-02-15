%global owner ojuba-org
%global commit #Write commit number here

Name:		ojuba-personal-lock
Summary:	Folder Encrpytion GUI
Version:	0.2.4
Release:	2%{?dist}
License:	WAQFv2
Group:		System Environment/Base
URL:		https://github.com/ojuba-org/ojuba-personal-lock
Source0:	https://github.com/%{owner}/%{name}/archive/%{commit}/%{name}-%{commit}.tar.gz
Requires:	fuse-encfs
Requires:	python
Requires:	pygobject3 >= 3.0.2
BuildRequires:	python2-devel
BuildRequires:	gettext
BuildRequires:	intltool
BuildArch:      noarch

%description
PyGTK+ front-end for fuse-encfs

%prep
%setup -q -n %{name}-%{commit}

%build
make %{?_smp_mflags}

%install
%makeinstall DESTDIR=$RPM_BUILD_ROOT

%post
touch --no-create %{_datadir}/icons/hicolor || :
if [ -x %{_bindir}/gtk-update-icon-cache ] ; then
%{_bindir}/gtk-update-icon-cache --quiet %{_datadir}/icons/hicolor || :
fi

%postun
touch --no-create %{_datadir}/icons/hicolor || :
if [ -x %{_bindir}/gtk-update-icon-cache ] ; then
%{_bindir}/gtk-update-icon-cache --quiet %{_datadir}/icons/hicolor || :
fi

%files
%doc README waqf2-ar.pdf
%{_bindir}/%{name}
%{python2_sitelib}/*.egg-info
%{_datadir}/applications/*.desktop
%{_datadir}/locale/*/*/*.mo
%{_datadir}/%{name}/*.svg
%{_datadir}/icons/hicolor/*/apps/*.svg

%changelog
* Sat Feb 15 2014 Mosaab Alzoubi <moceap@hotmail.com> - 0.2.4-2
- Full Rivision.

* Sun Jun 2 2012  Muayyad Saleh AlSadi <alsadi@ojuba.org> - 0.2.4-1
- port to gtk3

* Mon Jul 19 2010 Muayyad Saleh Alsadi <alsadi@ojuba.org> - 0.2.1-1
- minor fixes

* Sun Jul 18 2010 Muayyad Saleh Alsadi <alsadi@ojuba.org> - 0.2.0-1
- initial release

