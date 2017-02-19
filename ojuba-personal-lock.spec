%global owner ojuba-org

Name:		ojuba-personal-lock
Summary:	Folder Encrpytion GUI
Summary(ar): خزنة أعجوبة الشخصية
Version:	0.3
Release:	1%{?dist}
License:	WAQFv2
URL: http://ojuba.org
Source0: https://github.com/%{owner}/%{name}/archive/%{version}/%{name}-%{version}.tar.gz
Requires:	fuse-encfs
Requires:	python
Requires:	pygobject3 >= 3.0.2
BuildRequires:	python2-devel
BuildRequires:	gettext
BuildRequires:	intltool
BuildArch:      noarch

%description -l ar
واجهة رسومية للمشفر فيوز

%description
PyGTK+ front-end for fuse-encfs

%prep
%autosetup -n %{name}-%{version}

%build
make %{?_smp_mflags}

%install
%makeinstall DESTDIR=$RPM_BUILD_ROOT



# Register as an application to be visible in the software center
#
# NOTE: It would be *awesome* if this file was maintained by the upstream
# project, translated and installed into the right place during `make install`.
#
# See http://www.freedesktop.org/software/appstream/docs/ for more details.
#
mkdir -p $RPM_BUILD_ROOT%{_datadir}/appdata
cat > $RPM_BUILD_ROOT%{_datadir}/appdata/%{name}.appdata.xml <<EOF
<?xml version="1.0" encoding="UTF-8"?>
<!-- Copyright 2017 Mosaab Alzoubi <moceap@hotmail.com> -->
<!--
EmailAddress: moceap@hotmail.com
SentUpstream: 2017-2-18
-->
<application>
  <id type="desktop">%{name}.desktop</id>
  <metadata_license>CC0-1.0</metadata_license>
  <summary>Folder Encrpytion GUI</summary>
  <summary xml:lang="ar">خزنة أعجوبة الشخصية</summary>
  <description>
    <p>
	Folder Encrpytion GUI.
    </p>
  </description>
  <description xml:lang="ar">
    <p>
	خزنة أعجوبة الشخصية.
    </p>
  </description>
  <url type="homepage">https://github.com/ojuba-org/%{name}</url>
  <screenshots>
    <screenshot type="default">http://ojuba.org/screenshots/%{name}.png</screenshot>
  </screenshots>
  <updatecontact>moceap@hotmail.com</updatecontact>
</application>
EOF




%post
touch --no-create %{_datadir}/icons/hicolor || :
if [ -x %{_bindir}/gtk-update-icon-cache ] ; then
%{_bindir}/gtk-update-icon-cache --quiet %{_datadir}/icons/hicolor || :
fi

%postun
touch --no-create %{_datadir}/icons/hicolor || :
if [ -x %{_bindir}/gtk-update-icon-cache ] ; then
%{_bindir}/g/u  %{_datadir}/icons/hicolor || :
fi

%files
%license waqf2-ar.pdf
%doc waqf2-ar.pdf
%{_bindir}/%{name}
%{python2_sitelib}/*.egg-info
%{_datadir}/applications/*.desktop
%{_datadir}/locale/*/*/*.mo
%{_datadir}/%{name}/*.svg
%{_datadir}/icons/hicolor/*/apps/*.svg
%{_datadir}/appdata/%{name}.appdata.xml

%changelog
* Sun Feb 19 2017 Mosaab Alzoubi <moceap@hotmail.com> - 0.3-1
- Update to 0.3
- New way to Github
- Add Appdata

* Sat Feb 15 2014 Mosaab Alzoubi <moceap@hotmail.com> - 0.2.4-2
- Full Rivision.

* Sun Jun 2 2012  Muayyad Saleh AlSadi <alsadi@ojuba.org> - 0.2.4-1
- port to gtk3

* Mon Jul 19 2010 Muayyad Saleh Alsadi <alsadi@ojuba.org> - 0.2.1-1
- minor fixes

* Sun Jul 18 2010 Muayyad Saleh Alsadi <alsadi@ojuba.org> - 0.2.0-1
- initial release

