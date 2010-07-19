Name:		ojuba-personal-lock
Summary:	Folder Encrpytion GUI
Version:	0.2.1
Release:	1
License:	Waqf
Group:		System Environment/Base
URL:		http://git.ojuba.org/cgit/ojuba-personal-lock/about/
Source:		%{name}-%{version}.tar.bz2
Requires:	fuse-encfs python pygtk2 notify-python
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:      noarch

%description
PyGTK+ front-end for fuse-encfs

%prep
%setup -q

%build
make %{?_smp_mflags}
%install
rm -rf $RPM_BUILD_ROOT
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
%defattr(-,root,root,-)
%doc LICENSE-en LICENSE-ar.txt README
%{_bindir}/%{name}
%{python_sitelib}/*.egg-info
%{_datadir}/applications/*.desktop
%{_datadir}/locale/*/*/*.mo
%{_datadir}/%{name}/*.svg
%{_datadir}/icons/hicolor/*/apps/*.svg

%changelog
* Mon Jul 19 2010 Muayyad Saleh Alsadi <alsadi@ojuba.org> - 0.2.1-1
- minor fixes

* Sun Jul 18 2010 Muayyad Saleh Alsadi <alsadi@ojuba.org> - 0.2.0-1
- initial release

