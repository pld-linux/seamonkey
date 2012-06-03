#
# Conditional build:
%bcond_without	enigmail	# don't build enigmail - GPG/PGP support
%bcond_without	gnomeui		# disable gnomeui support
%bcond_without	gnome		# disable gnomeui (alias)
%bcond_without	ldap		# disable e-mail address lookups in LDAP directories
%bcond_without	lightning	# disable Sunbird/Lightning calendar
%bcond_with	xulrunner	# build with system xulrunner
%bcond_with	tests		# enable tests (whatever they check)
%bcond_without	kerberos	# disable krb5 support

%if %{without gnome}
%undefine	with_gnomeui
%endif

%define		enigmail_ver	1.4.1
%define		nspr_ver	4.9
%define		nss_ver		3.13.3
%define		xulrunner_ver	12.0

%if %{without xulrunner}
# The actual sqlite version (see RHBZ#480989):
%define		sqlite_build_version %(pkg-config --silence-errors --modversion sqlite3 2>/dev/null || echo ERROR)
%endif

Summary:	SeaMonkey Community Edition - web browser
Summary(es.UTF-8):	Navegador de Internet SeaMonkey Community Edition
Summary(pl.UTF-8):	SeaMonkey Community Edition - przeglądarka WWW
Summary(pt_BR.UTF-8):	Navegador SeaMonkey Community Edition
Name:		seamonkey
Version:	2.9.1
Release:	0.1
License:	MPL 1.1 or GPL v2+ or LGPL v2.1+
Group:		X11/Applications/Networking
Source0:	ftp://ftp.mozilla.org/pub/mozilla.org/seamonkey/releases/%{version}/source/%{name}-%{version}.source.tar.bz2
# Source0-md5:	8dd18d93a6570c3c9f3873bb177ccc6b
Source1:	http://www.mozilla-enigmail.org/download/source/enigmail-%{enigmail_ver}.tar.gz
# Source1-md5:	0eba75fbcf8f0bb32d538df102fbb8e9
Source2:	%{name}.desktop
Source3:	%{name}-composer.desktop
Source4:	%{name}-chat.desktop
Source5:	%{name}-mail.desktop
Source6:	%{name}-venkman.desktop
Source7:	%{name}.sh
Patch0:		%{name}-pld-homepage.patch
Patch1:		%{name}-agent.patch
Patch2:		%{name}-glueload-fix.patch
Patch3:		system-mozldap.patch
Patch4:		makefile.patch
Patch5:		system-cairo.patch
URL:		http://www.seamonkey-project.org/
BuildRequires:	GConf2-devel >= 1.2.1
BuildRequires:	OpenGL-devel
BuildRequires:	alsa-lib-devel
BuildRequires:	automake
BuildRequires:	bzip2-devel
BuildRequires:	cairo-devel >= 1.10.2-5
BuildRequires:	dbus-glib-devel >= 0.60
BuildRequires:	freetype-devel >= 1:2.1.8
BuildRequires:	glib2-devel >= 1:2.18
BuildRequires:	gtk+2-devel >= 2:2.10
%{?with_kerberos:BuildRequires:	heimdal-devel >= 0.7.1}
BuildRequires:	hunspell-devel
BuildRequires:	libIDL-devel >= 0.8.0
BuildRequires:	libdnet-devel
BuildRequires:	libevent-devel >= 1.4.7
# standalone libffi 3.0.9 or gcc's from 4.5(?)+
BuildRequires:	libffi-devel >= 6:3.0.9
%{?with_gnomeui:BuildRequires:  libgnome-devel >= 2.0}
%{?with_gnomeui:BuildRequires:  libgnome-keyring-devel}
%{?with_gnomeui:BuildRequires:  libgnomeui-devel >= 2.2.0}
BuildRequires:	libiw-devel
BuildRequires:	libjpeg-devel >= 6b
BuildRequires:	libnotify-devel >= 0.4
BuildRequires:	libpng(APNG)-devel >= 0.10
BuildRequires:	libpng-devel >= 1.4.1
BuildRequires:	libstdc++-devel
BuildRequires:	libvpx-devel
BuildRequires:	nspr-devel >= 1:%{nspr_ver}
BuildRequires:	nss-devel >= 1:%{nss_ver}
BuildRequires:	pango-devel >= 1:1.14.0
BuildRequires:	perl-base >= 1:5.6
BuildRequires:	perl-modules >= 5.004
BuildRequires:	pkgconfig
BuildRequires:	python >= 1:2.5
BuildRequires:	python-modules
BuildRequires:	rpm >= 4.4.9-56
BuildRequires:	rpmbuild(macros) >= 1.601
BuildRequires:	sed >= 4.0
BuildRequires:	sqlite3-devel >= 3.7.10
BuildRequires:	startup-notification-devel >= 0.8
BuildRequires:	xorg-lib-libXScrnSaver-devel
BuildRequires:	xorg-lib-libXext-devel
BuildRequires:	xorg-lib-libXinerama-devel
BuildRequires:	xorg-lib-libXt-devel
%if %{with xulrunner}
BuildRequires:	xulrunner-devel >= 2:%{xulrunner_ver}
%endif
BuildRequires:	yasm
BuildRequires:	zip
BuildRequires:	zlib-devel >= 1.2.3
Requires(post):	mktemp >= 1.5-18
Requires:	desktop-file-utils
Requires:	hicolor-icon-theme
%if %{with xulrunner}
%requires_eq_to	xulrunner xulrunner-devel
%else
Requires:	browser-plugins >= 2.0
Requires:	cairo >= 1.10.2-5
Requires:	dbus-glib >= 0.60
Requires:	gtk+2 >= 2:2.18
Requires:	libpng >= 1.4.1
Requires:	libpng(APNG) >= 0.10
Requires:	myspell-common
Requires:	nspr >= 1:%{nspr_ver}
Requires:	nss >= 1:%{nss_ver}
Requires:	pango >= 1:1.14.0
Requires:	sqlite3 >= %{sqlite_build_version}
Requires:	startup-notification >= 0.8
%endif
Provides:	seamonkey-embedded = %{version}-%{release}
Provides:	wwwbrowser
Obsoletes:	light
Obsoletes:	mozilla
Obsoletes:	seamonkey-calendar
Obsoletes:	seamonkey-libs
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		topdir		%{_builddir}/%{name}-%{version}
%define		objdir		%{topdir}/obj-%{_target_cpu}

%define		filterout_cpp	-D_FORTIFY_SOURCE=[0-9]+

# don't satisfy other packages
%define		_noautoprovfiles	%{_libdir}/%{name}
# and as we don't provide them, don't require either
%define		_noautoreq	libmozjs.so libxpcom.so libxul.so libjemalloc.so %{!?with_xulrunner:libmozalloc.so}
%define		_noautoreqdep	libgfxpsshar.so libgkgfx.so libgtkxtbin.so libjsj.so libxpcom_compat.so libxpistub.so

%description
SeaMonkey Community Edition is an open-source web browser, designed
for standards compliance, performance and portability.

%description -l es.UTF-8
SeaMonkey Community Edition es un navegador de Internet que se basa en
una versión inicial de Netscape Communicator.

%description -l pl.UTF-8
SeaMonkey Community Edition jest potężną graficzną przeglądarką WWW,
która jest następcą Mozilli, która następnie była następczynią
Netscape Communikatora.

%description -l pt_BR.UTF-8
O SeaMonkey Community Edition é um web browser baseado numa versão
inicial do Netscape Communicator.

%description -l ru.UTF-8
SeaMonkey Community Edition - полнофункциональный web-browser с
открытыми исходными текстами, разработанный для максимального
соотвествия стандартам, максмимальной переносимости и скорости работы

%package mailnews
Summary:	SeaMonkey Community Edition - programs for mail and news
Summary(pl.UTF-8):	SeaMonkey Community Edition - programy do poczty i newsów
Summary(ru.UTF-8):	Почтовая система на основе SeaMonkey Community Edition
Group:		X11/Applications/Networking
Requires(post,postun):	%{name} = %{version}-%{release}
Requires:	%{name} = %{version}-%{release}
Obsoletes:	mozilla-mailnews

%description mailnews
Programs for mail and news integrated with browser.

%description mailnews -l pl.UTF-8
Programy pocztowe i obsługa newsów zintegrowane z przeglądarką.

%description mailnews -l ru.UTF-8
Клиент почты и новостей, на основе SeaMonkey Community Edition.
Поддерживает IMAP, POP и NNTP и имеет простой интерфейс пользователя.

%package addon-enigmail
Summary:	Enigmail %{enigmail_ver} - PGP/GPG support for SeaMonkey Community Edition
Summary(pl.UTF-8):	Enigmail %{enigmail_ver} - obsługa PGP/GPG dla SeaMonkey Community Edition
Group:		X11/Applications/Networking
Requires(post,postun):	%{name}-mailnews = %{version}-%{release}
Requires:	%{name}-mailnews = %{version}-%{release}
Requires:	gnupg >= 1.4.2.2

%description addon-enigmail
Enigmail is an extension to the mail client of SeaMonkey / Mozilla /
Netscape and Mozilla Thunderbird which allows users to access the
authentication and encryption features provided by GnuPG.

%description addon-enigmail -l pl.UTF-8
Enigmail jest rozszerzeniem dla klienta pocztowego SeaMonkey, Mozilla
i Mozilla Thunderdbird pozwalającym użytkownikowi korzystać z
funkcjonalności GnuPG.

%package chat
Summary:	SeaMonkey Community Edition Chat - integrated IRC client
Summary(pl.UTF-8):	SeaMonkey Community Edition Chat - zintegrowany klient IRC-a
Group:		X11/Applications/Networking
Requires(post,postun):	%{name} = %{version}-%{release}
Requires:	%{name} = %{version}-%{release}
Obsoletes:	mozilla-chat

%description chat
SeaMonkey Community Edition Chat - IRC client that is integrated with
the SeaMonkey Community Edition web browser.

%description chat -l pl.UTF-8
SeaMonkey Community Edition Chat - klient IRC-a zintegrowany z
przeglądarką SeaMonkey Community Edition.

%package js-debugger
Summary:	JavaScript debugger for use with SeaMonkey Community Edition
Summary(pl.UTF-8):	Odpluskwiacz JavaScriptu do używania z SeaMonkey Community Edition
Group:		X11/Applications/Networking
Requires(post,postun):	%{name} = %{version}-%{release}
Requires:	%{name} = %{version}-%{release}
Obsoletes:	mozilla-js-debugger

%description js-debugger
JavaScript debugger for use with SeaMonkey Community Edition.

%description js-debugger -l pl.UTF-8
Odpluskwiacz JavaScriptu do używania z SeaMonkey Community Edition.

%package dom-inspector
Summary:	A tool for inspecting the DOM of pages in SeaMonkey Community Edition
Summary(pl.UTF-8):	Narzędzie do oglądania DOM stron w SeaMonkey Community Edition
Group:		X11/Applications/Networking
Requires(post,postun):	%{name} = %{version}-%{release}
Requires:	%{name} = %{version}-%{release}
Obsoletes:	mozilla-dom-inspector

%description dom-inspector
This is a tool that allows you to inspect the DOM for web pages in
SeaMonkey Community Edition. This is of great use to people who are
doing SeaMonkey Community Edition chrome development or web page
development.

%description dom-inspector -l pl.UTF-8
To narzędzie pozwala na oglądanie DOM dla stron WWW w SeaMonkey
Community Edition. Jest bardzo przydatne dla ludzi rozwijających
chrome w SeaMonkey Community Edition lub tworzących strony WWW.

%prep
%setup -qc
cd comm-release
tar -C mailnews/extensions -zxf %{SOURCE1}
#patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1

%build
cd comm-release
%if %{with xulrunner}
if [ "$(grep -E '^[0-9]+\.' mozilla/config/milestone.txt)" != "%{xulrunner_ver}" ]; then
	echo >&2
	echo >&2 "Xulrunner version %{xulrunner_ver} does not match mozilla/config/milestone.txt!"
	echo >&2
	exit 1
fi
%endif

cp -f %{_datadir}/automake/config.* build/autoconf
cp -f %{_datadir}/automake/config.* mozilla/build/autoconf
cp -f %{_datadir}/automake/config.* mozilla/nsprpub/build/autoconf
cp -f %{_datadir}/automake/config.* ldap/sdks/c-sdk/config/autoconf

cat << EOF > .mozconfig
mk_add_options MOZ_OBJDIR=%{objdir}

export CFLAGS="%{rpmcflags}"
export CXXFLAGS="%{rpmcflags}"

%if %{with crashreporter}
export MOZ_DEBUG_SYMBOLS=1
%endif

# Options for 'configure' (same as command-line options).
ac_add_options --prefix=%{_prefix}
ac_add_options --exec-prefix=%{_exec_prefix}
ac_add_options --bindir=%{_bindir}
ac_add_options --sbindir=%{_sbindir}
ac_add_options --sysconfdir=%{_sysconfdir}
ac_add_options --datadir=%{_datadir}
ac_add_options --includedir=%{_includedir}
ac_add_options --libdir=%{_libdir}
ac_add_options --libexecdir=%{_libexecdir}
ac_add_options --localstatedir=%{_localstatedir}
ac_add_options --sharedstatedir=%{_sharedstatedir}
ac_add_options --mandir=%{_mandir}
ac_add_options --infodir=%{_infodir}
ac_add_options --disable-elf-hack
%if %{?debug:1}0
ac_add_options --disable-optimize
ac_add_options --enable-debug
ac_add_options --enable-debug-modules
ac_add_options --enable-debugger-info-modules
ac_add_options --enable-crash-on-assert
%else
ac_add_options --disable-debug
ac_add_options --disable-debug-modules
ac_add_options --disable-logging
ac_add_options --enable-optimize="%{rpmcflags} -Os"
%endif
ac_add_options --disable-strip
ac_add_options --disable-strip-libs
%if %{with tests}
ac_add_options --enable-tests
%else
ac_add_options --disable-tests
%endif
ac_add_options --enable-gio
%if %{with gnomeui}
ac_add_options --enable-gnomeui
%else
ac_add_options --disable-gnomeui
%endif
ac_add_options --disable-gnomevfs
%if %{with ldap}
ac_add_options --enable-ldap
ac_add_options --with-system-ldap
%else
ac_add_options --disable-ldap
%endif
%if %{with crashreporter}
ac_add_options --enable-crashreporter
%else
ac_add_options --disable-crashreporter
%endif
ac_add_options --disable-xterm-updates
ac_add_options --enable-postscript
%if %{with lightning}
ac_add_options --enable-calendar
%else
ac_add_options --disable-calendar
%endif
ac_add_options --disable-installer
ac_add_options --disable-javaxpcom
ac_add_options --disable-updater
ac_add_options --disable-xprint
ac_add_options --disable-permissions
ac_add_options --disable-pref-extensions
ac_add_options --enable-canvas
ac_add_options --enable-crypto
ac_add_options --enable-mathml
ac_add_options --enable-libxul
ac_add_options --enable-pango
ac_add_options --enable-reorder
ac_add_options --enable-startup-notification
ac_add_options --enable-svg
ac_add_options --enable-system-cairo
ac_add_options --enable-system-hunspell
ac_add_options --enable-system-sqlite
ac_add_options --enable-application=suite
ac_add_options --enable-default-toolkit=cairo-gtk2
ac_add_options --enable-xinerama
ac_add_options --with-distribution-id=org.pld-linux
%if %{with xulrunner}
ac_add_options --enable-shared-js
ac_add_options --with-system-libxul
ac_add_options --with-libxul-sdk=$(pkg-config --variable=sdkdir libxul)
%endif
ac_add_options --with-pthreads
ac_add_options --with-system-bz2
ac_add_options --with-system-ffi
ac_add_options --with-system-jpeg
ac_add_options --with-system-libevent
ac_add_options --with-system-libvpx
ac_add_options --with-system-nspr
ac_add_options --with-system-nss
ac_add_options --with-system-png
ac_add_options --with-system-zlib
ac_add_options --enable-single-profile
ac_add_options --disable-profilesharing
ac_add_options --with-default-mozilla-five-home=%{_libdir}/%{name}
EOF

%{__make} -j1 -f client.mk build \
	STRIP="/bin/true" \
	MOZ_MAKE_FLAGS="%{?_smp_mflags}" \
	CC="%{__cc}" \
	CXX="%{__cxx}"

%if %{with crashreporter}
# create debuginfo for crash-stats.mozilla.com
%{__make} -j1 -C obj-%{_target_cpu} buildsymbols
%endif

%if %{with enigmail}
cd mailnews/extensions/enigmail
./makemake -r -o %{objdir}
%{__make} -C %{objdir}/mailnews/extensions/enigmail \
	STRIP="/bin/true" \
	CC="%{__cc}" \
	CXX="%{__cxx}"
%endif

%install
rm -rf $RPM_BUILD_ROOT
cd comm-release
install -d \
	$RPM_BUILD_ROOT{%{_bindir},%{_sbindir},%{_libdir}} \
	$RPM_BUILD_ROOT{%{_desktopdir},%{_pixmapsdir}} \
	$RPM_BUILD_ROOT%{_datadir}/%{name} \
	$RPM_BUILD_ROOT%{_libdir}/%{name}/plugins

%browser_plugins_add_browser %{name} -p %{_libdir}/%{name}/plugins

cd %{objdir}
install -d mozilla/dist/%{_libdir}/%{name}
%{__make} -C suite/installer install \
	DESTDIR=$RPM_BUILD_ROOT \
	installdir=%{_libdir}/%{name} \
	MOZ_PKG_APPDIR=%{_libdir}/%{name} \
	MOZ_PKG_DIR=%{_libdir}/%{name} \
	PKG_SKIP_STRIP=1 \
	LIBXUL_SDK=1

%if %{with xulrunner}
# >= 5.0 seems to require this
ln -s ../xulrunner $RPM_BUILD_ROOT%{_libdir}/%{name}/xulrunner
%endif

# Enable crash reporter for Thunderbird application
%if %{with crashreporter}
%{__sed} -i -e 's/\[Crash Reporter\]/[Crash Reporter]\nEnabled=1/' $RPM_BUILD_ROOT%{_libdir}/%{name}/application.ini

# Add debuginfo for crash-stats.mozilla.com
install -d $RPM_BUILD_ROOT%{_exec_prefix}/lib/debug%{_libdir}/%{name}
cp -a mozilla/dist/%{name}-%{version}.en-US.linux-*.crashreporter-symbols.zip $RPM_BUILD_ROOT%{_prefix}/lib/debug%{_libdir}/%{name}
%endif

# copy manually lightning files, somewhy they are not installed by make
cp -a mozilla/dist/bin/extensions/calendar-timezones@mozilla.org \
	mozilla/dist/bin/extensions/{e2fda1a4-762b-4020-b5ad-a41df1933103} \
	$RPM_BUILD_ROOT%{_libdir}/%{name}/extensions
		
# move arch independant ones to datadir
mv $RPM_BUILD_ROOT%{_libdir}/%{name}/chrome $RPM_BUILD_ROOT%{_datadir}/%{name}/chrome
mv $RPM_BUILD_ROOT%{_libdir}/%{name}/defaults $RPM_BUILD_ROOT%{_datadir}/%{name}/defaults
mv $RPM_BUILD_ROOT%{_libdir}/%{name}/isp $RPM_BUILD_ROOT%{_datadir}/%{name}/isp
mv $RPM_BUILD_ROOT%{_libdir}/%{name}/searchplugins $RPM_BUILD_ROOT%{_datadir}/%{name}/searchplugins

ln -s ../../share/%{name}/chrome $RPM_BUILD_ROOT%{_libdir}/%{name}/chrome
ln -s ../../share/%{name}/defaults $RPM_BUILD_ROOT%{_libdir}/%{name}/defaults
ln -s ../../share/%{name}/isp $RPM_BUILD_ROOT%{_libdir}/%{name}/isp
ln -s ../../share/%{name}/searchplugins $RPM_BUILD_ROOT%{_libdir}/%{name}/searchplugins

# dir for arch independant extensions besides arch dependant extensions
# see mozilla/xpcom/build/nsXULAppAPI.h
# XRE_SYS_LOCAL_EXTENSION_PARENT_DIR and XRE_SYS_SHARE_EXTENSION_PARENT_DIR
install -d $RPM_BUILD_ROOT%{_datadir}/%{name}/extensions
 
%if %{without xulrunner}
%{__rm} -r $RPM_BUILD_ROOT%{_libdir}/%{name}/dictionaries
ln -s %{_datadir}/myspell $RPM_BUILD_ROOT%{_libdir}/%{name}/dictionaries
%endif

# remove %{_bindir}/seamonkey -> %{_libdir}/%{name}/seamonkey symlink
%{__rm} $RPM_BUILD_ROOT%{_bindir}/seamonkey
sed 's,@LIBDIR@,%{_libdir},' %{SOURCE7} > $RPM_BUILD_ROOT%{_bindir}/seamonkey
chmod a+rx $RPM_BUILD_ROOT%{_bindir}/seamonkey

install %{SOURCE2} %{SOURCE3} %{SOURCE4} %{SOURCE5} %{SOURCE6} \
	$RPM_BUILD_ROOT%{_desktopdir}

cp -p %{topdir}/comm-release/suite/branding/nightly/content/icon64.png $RPM_BUILD_ROOT%{_pixmapsdir}/%{name}.png

# files created by iceweasel -register
touch $RPM_BUILD_ROOT%{_libdir}/%{name}/components/compreg.dat
touch $RPM_BUILD_ROOT%{_libdir}/%{name}/components/xpti.dat

cat << 'EOF' > $RPM_BUILD_ROOT%{_libdir}/%{name}/register
#!/bin/sh
umask 022
rm -f %{_libdir}/%{name}/components/{compreg,xpti}.dat

# it attempts to touch files in $HOME/.mozilla
# beware if you run this with sudo!!!
export HOME=$(mktemp -d)
# also TMPDIR could be pointing to sudo user's homedir
unset TMPDIR TMP || :

%{_libdir}/%{name}/seamonkey -register

rm -rf $HOME
EOF
chmod 755 $RPM_BUILD_ROOT%{_libdir}/%{name}/register

%if %{with enigmail}
ext_dir=$RPM_BUILD_ROOT%{_libdir}/%{name}/extensions/\{847b3a00-7ab1-11d4-8f02-006008948af5\}
install -d $ext_dir/{chrome,components,defaults/preferences}
cd mozilla/dist/bin
#cp -rfLp chrome/enigmail.jar $ext_dir/chrome
#cp -rfLp chrome/enigmime.jar $ext_dir/chrome
cp -rfLp components/enig* $ext_dir/components
cp -rfLp components/libenigmime.so $ext_dir/components
cp -rfLp components/libipc.so $ext_dir/components
cp -rfLp components/ipc.xpt $ext_dir/components
cp -rfLp defaults/preferences/enigmail.js $ext_dir/defaults/preferences
cd -
cp -p %{topdir}/comm-release/mailnews/extensions/enigmail/package/install.rdf $ext_dir
cp -p %{topdir}/comm-release/mailnews/extensions/enigmail/package/chrome.manifest $ext_dir/chrome.manifest
%endif

# never package these. always remove
# nss
%{__rm} -f $RPM_BUILD_ROOT%{_libdir}/%{name}/lib{freebl3,nss3,nssckbi,nssdbm3,nssutil3,smime3,softokn3,ssl3}.*
# nspr
%{__rm} -f $RPM_BUILD_ROOT%{_libdir}/%{name}/lib{nspr4,plc4,plds4}.so
# mozldap
%{__rm} -f $RPM_BUILD_ROOT%{_libdir}/%{name}/lib{ldap,ldif,prldap,ssldap}60.so
# testpilot quiz
%{__rm} -f $RPM_BUILD_ROOT%{_libdir}/%{name}/distribution/extensions/tbtestpilot@labs.mozilla.com.xpi

%clean
rm -rf $RPM_BUILD_ROOT

%post
%{_libdir}/%{name}/register || :
%update_browser_plugins
%update_icon_cache hicolor
%update_desktop_database

%postun
if [ "$1" = 0 ]; then
	%update_browser_plugins
	%update_icon_cache hicolor
fi

%post mailnews
%{_libdir}/%{name}/register || :

%post addon-enigmail
%{_libdir}/%{name}/register || :

%post chat
%{_libdir}/%{name}/register || :

%post js-debugger
%{_libdir}/%{name}/register || :

%post dom-inspector
%{_libdir}/%{name}/register || :

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/seamonkey
%attr(744,root,root) %{_sbindir}/%{name}-chrome+xpcom-generate

# browser plugins v2
%{_browserpluginsconfdir}/browsers.d/%{name}.*
%config(noreplace) %verify(not md5 mtime size) %{_browserpluginsconfdir}/blacklist.d/%{name}.*.blacklist

%dir %{_libdir}/%{name}
%dir %{_libdir}/%{name}/chrome
%dir %{_libdir}/%{name}/components
%dir %{_libdir}/%{name}/defaults
%dir %{_libdir}/%{name}/dictionaries
%dir %{_libdir}/%{name}/greprefs
%dir %{_libdir}/%{name}/icons
%dir %{_libdir}/%{name}/plugins
%dir %{_libdir}/%{name}/res
%dir %{_libdir}/%{name}/searchplugins
%dir %{_datadir}/%{name}

%attr(755,root,root) %{_libdir}/%{name}/libgfxpsshar.so
%attr(755,root,root) %{_libdir}/%{name}/libgkgfx.so
%attr(755,root,root) %{_libdir}/%{name}/libgtkembedmoz.so
%attr(755,root,root) %{_libdir}/%{name}/libgtkxtbin.so
%attr(755,root,root) %{_libdir}/%{name}/libjsj.so
%attr(755,root,root) %{_libdir}/%{name}/libldap50.so
%attr(755,root,root) %{_libdir}/%{name}/libmozjs.so
%attr(755,root,root) %{_libdir}/%{name}/libprldap50.so
%attr(755,root,root) %{_libdir}/%{name}/libssldap50.so
%attr(755,root,root) %{_libdir}/%{name}/libxlibrgb.so
%attr(755,root,root) %{_libdir}/%{name}/libxpcom.so
%attr(755,root,root) %{_libdir}/%{name}/libxpcom_compat.so
%attr(755,root,root) %{_libdir}/%{name}/libxpcom_core.so
%attr(755,root,root) %{_libdir}/%{name}/libxpistub.so

%attr(755,root,root) %{_libdir}/%{name}/seamonkey-bin
%attr(755,root,root) %{_libdir}/%{name}/regchrome
%attr(755,root,root) %{_libdir}/%{name}/regxpcom
%attr(755,root,root) %{_libdir}/%{name}/xpidl

%attr(755,root,root) %{_libdir}/%{name}/libnssckbi.so

%attr(755,root,root) %{_libdir}/%{name}/components/libaccessibility.so
%attr(755,root,root) %{_libdir}/%{name}/components/libappcomps.so
%attr(755,root,root) %{_libdir}/%{name}/components/libauth.so
%attr(755,root,root) %{_libdir}/%{name}/components/libautoconfig.so
%attr(755,root,root) %{_libdir}/%{name}/components/libcaps.so
%attr(755,root,root) %{_libdir}/%{name}/components/libchrome.so
%attr(755,root,root) %{_libdir}/%{name}/components/libcomposer.so
%attr(755,root,root) %{_libdir}/%{name}/components/libcookie.so
%attr(755,root,root) %{_libdir}/%{name}/components/libdocshell.so
%attr(755,root,root) %{_libdir}/%{name}/components/libeditor.so
%attr(755,root,root) %{_libdir}/%{name}/components/libembedcomponents.so
%attr(755,root,root) %{_libdir}/%{name}/components/libfileview.so
%attr(755,root,root) %{_libdir}/%{name}/components/libgfx_gtk.so
%attr(755,root,root) %{_libdir}/%{name}/components/libgfxps.so
%attr(755,root,root) %{_libdir}/%{name}/components/libgfxxprint.so
%attr(755,root,root) %{_libdir}/%{name}/components/libgkdebug.so
%attr(755,root,root) %{_libdir}/%{name}/components/libgklayout.so
%attr(755,root,root) %{_libdir}/%{name}/components/libgkplugin.so
%attr(755,root,root) %{_libdir}/%{name}/components/libhtmlpars.so
%attr(755,root,root) %{_libdir}/%{name}/components/libi18n.so
%attr(755,root,root) %{_libdir}/%{name}/components/libimglib2.so
%attr(755,root,root) %{_libdir}/%{name}/components/libjar50.so
%attr(755,root,root) %{_libdir}/%{name}/components/libjsd.so
%attr(755,root,root) %{_libdir}/%{name}/components/libmork.so
%attr(755,root,root) %{_libdir}/%{name}/components/libmozfind.so
%attr(755,root,root) %{_libdir}/%{name}/components/libmozldap.so
%attr(755,root,root) %{_libdir}/%{name}/components/libmyspell.so
%attr(755,root,root) %{_libdir}/%{name}/components/libnecko.so
%attr(755,root,root) %{_libdir}/%{name}/components/libnecko2.so
%attr(755,root,root) %{_libdir}/%{name}/components/libnkdatetime.so
%attr(755,root,root) %{_libdir}/%{name}/components/libnkfinger.so
%attr(755,root,root) %{_libdir}/%{name}/components/libnsappshell.so
%attr(755,root,root) %{_libdir}/%{name}/components/libnsprefm.so
%attr(755,root,root) %{_libdir}/%{name}/components/liboji.so
%attr(755,root,root) %{_libdir}/%{name}/components/libp3p.so
%attr(755,root,root) %{_libdir}/%{name}/components/libpermissions.so
%attr(755,root,root) %{_libdir}/%{name}/components/libpipboot.so
%attr(755,root,root) %{_libdir}/%{name}/components/libpipnss.so
%attr(755,root,root) %{_libdir}/%{name}/components/libpippki.so
%attr(755,root,root) %{_libdir}/%{name}/components/libpref.so
%attr(755,root,root) %{_libdir}/%{name}/components/libprofile.so
%attr(755,root,root) %{_libdir}/%{name}/components/librdf.so
%attr(755,root,root) %{_libdir}/%{name}/components/libremoteservice.so
%attr(755,root,root) %{_libdir}/%{name}/components/libschemavalidation.so
%attr(755,root,root) %{_libdir}/%{name}/components/libsearchservice.so
%attr(755,root,root) %{_libdir}/%{name}/components/libspellchecker.so
%attr(755,root,root) %{_libdir}/%{name}/components/libsql.so
%attr(755,root,root) %{_libdir}/%{name}/components/libsroaming.so
%attr(755,root,root) %{_libdir}/%{name}/components/libstoragecomps.so
%attr(755,root,root) %{_libdir}/%{name}/components/libsystem-pref.so
%attr(755,root,root) %{_libdir}/%{name}/components/libtransformiix.so
%attr(755,root,root) %{_libdir}/%{name}/components/libtxmgr.so
%attr(755,root,root) %{_libdir}/%{name}/components/libtypeaheadfind.so
%attr(755,root,root) %{_libdir}/%{name}/components/libuconv.so
%attr(755,root,root) %{_libdir}/%{name}/components/libucvmath.so
%attr(755,root,root) %{_libdir}/%{name}/components/libuniversalchardet.so
%attr(755,root,root) %{_libdir}/%{name}/components/libwallet.so
%attr(755,root,root) %{_libdir}/%{name}/components/libwalletviewers.so
%attr(755,root,root) %{_libdir}/%{name}/components/libwebbrwsr.so
%attr(755,root,root) %{_libdir}/%{name}/components/libwebsrvcs.so
%attr(755,root,root) %{_libdir}/%{name}/components/libwidget_gtk2.so
%attr(755,root,root) %{_libdir}/%{name}/components/libxforms.so
%attr(755,root,root) %{_libdir}/%{name}/components/libxmlextras.so
%attr(755,root,root) %{_libdir}/%{name}/components/libxpcom_compat_c.so
%attr(755,root,root) %{_libdir}/%{name}/components/libxpconnect.so
%attr(755,root,root) %{_libdir}/%{name}/components/libxpinstall.so
%attr(755,root,root) %{_libdir}/%{name}/components/libxremoteservice.so

%{_libdir}/%{name}/components/access*.xpt
%{_libdir}/%{name}/components/alerts.xpt
%{_libdir}/%{name}/components/appshell.xpt
%{_libdir}/%{name}/components/appstartup.xpt
%{_libdir}/%{name}/components/autocomplete.xpt
%{_libdir}/%{name}/components/autoconfig.xpt
%{_libdir}/%{name}/components/bookmarks.xpt
%{_libdir}/%{name}/components/caps.xpt
%{_libdir}/%{name}/components/chardet.xpt
%{_libdir}/%{name}/components/chrome.xpt
%{_libdir}/%{name}/components/commandhandler.xpt
%{_libdir}/%{name}/components/composer.xpt
%{_libdir}/%{name}/components/content*.xpt
%{_libdir}/%{name}/components/cookie.xpt
%{_libdir}/%{name}/components/directory.xpt
%{_libdir}/%{name}/components/docshell.xpt
%{_libdir}/%{name}/components/dom*.xpt
%{_libdir}/%{name}/components/downloadmanager.xpt
%{_libdir}/%{name}/components/editor.xpt
%{_libdir}/%{name}/components/embed_base.xpt
%{_libdir}/%{name}/components/extensions.xpt
%{_libdir}/%{name}/components/exthandler.xpt
%{_libdir}/%{name}/components/find.xpt
%{_libdir}/%{name}/components/filepicker.xpt
%{_libdir}/%{name}/components/gfx*.xpt
%{?with_svg:%{_libdir}/%{name}/components/gksvgrenderer.xpt}
%{_libdir}/%{name}/components/history.xpt
%{_libdir}/%{name}/components/htmlparser.xpt
%{_libdir}/%{name}/components/imglib2.xpt
%{_libdir}/%{name}/components/intl.xpt
%{_libdir}/%{name}/components/jar.xpt
%{_libdir}/%{name}/components/js*.xpt
%{_libdir}/%{name}/components/layout*.xpt
%{_libdir}/%{name}/components/locale.xpt
%{_libdir}/%{name}/components/lwbrk.xpt
%{_libdir}/%{name}/components/mimetype.xpt
%{_libdir}/%{name}/components/moz*.xpt
%{_libdir}/%{name}/components/necko*.xpt
%{_libdir}/%{name}/components/oji.xpt
%{_libdir}/%{name}/components/p3p.xpt
%{_libdir}/%{name}/components/pipboot.xpt
%{_libdir}/%{name}/components/pipnss.xpt
%{_libdir}/%{name}/components/pippki.xpt
%{_libdir}/%{name}/components/plugin.xpt
%{_libdir}/%{name}/components/pref.xpt
%{_libdir}/%{name}/components/prefetch.xpt
%{_libdir}/%{name}/components/prefmigr.xpt
%{_libdir}/%{name}/components/profile.xpt
%{_libdir}/%{name}/components/progressDlg.xpt
%{_libdir}/%{name}/components/proxyObjInst.xpt
%{_libdir}/%{name}/components/rdf.xpt
%{_libdir}/%{name}/components/related.xpt
%{_libdir}/%{name}/components/saxparser.xpt
%{_libdir}/%{name}/components/search.xpt
%{_libdir}/%{name}/components/schemavalidation.xpt
%{_libdir}/%{name}/components/shistory.xpt
%{_libdir}/%{name}/components/signonviewer.xpt
%{_libdir}/%{name}/components/spellchecker.xpt
%{_libdir}/%{name}/components/sql.xpt
%{_libdir}/%{name}/components/storage.xpt
%{_libdir}/%{name}/components/toolkitremote.xpt
%{_libdir}/%{name}/components/txmgr.xpt
%{_libdir}/%{name}/components/txtsvc.xpt
%{_libdir}/%{name}/components/typeaheadfind.xpt
%{_libdir}/%{name}/components/uconv.xpt
%{_libdir}/%{name}/components/unicharutil.xpt
%{_libdir}/%{name}/components/uriloader.xpt
%{_libdir}/%{name}/components/urlformatter.xpt
%{_libdir}/%{name}/components/wallet*.xpt
%{_libdir}/%{name}/components/webBrowser_core.xpt
%{_libdir}/%{name}/components/webbrowserpersist.xpt
%{_libdir}/%{name}/components/webshell_idls.xpt
%{_libdir}/%{name}/components/websrvcs.xpt
%{_libdir}/%{name}/components/widget.xpt
%{_libdir}/%{name}/components/windowds.xpt
%{_libdir}/%{name}/components/windowwatcher.xpt
%{_libdir}/%{name}/components/x*.xpt

%{_libdir}/%{name}/components/jsconsole-clhandler.js
%{_libdir}/%{name}/components/nsCloseAllWindows.js
%{_libdir}/%{name}/components/nsComposerCmdLineHandler.js
%{_libdir}/%{name}/components/nsDictionary.js
%{_libdir}/%{name}/components/nsDownloadProgressListener.js
%{_libdir}/%{name}/components/nsFilePicker.js
%{_libdir}/%{name}/components/nsHelperAppDlg.js
%{_libdir}/%{name}/components/nsInterfaceInfoToIDL.js
%{_libdir}/%{name}/components/nsKillAll.js
%{_libdir}/%{name}/components/nsProgressDialog.js
%{_libdir}/%{name}/components/nsProxyAutoConfig.js
%{_libdir}/%{name}/components/nsResetPref.js
%{_libdir}/%{name}/components/nsSchemaValidatorRegexp.js
%{_libdir}/%{name}/components/nsSidebar.js
%{_libdir}/%{name}/components/nsUpdateNotifier.js
%{_libdir}/%{name}/components/nsURLFormatter.js
%{_libdir}/%{name}/components/nsXmlRpcClient.js
%{_libdir}/%{name}/components/xulappinfo.js

# not *.dat, so check-files can catch any new files
# (and they won't be just silently placed empty in rpm)
%ghost %{_libdir}/%{name}/components/compreg.dat
%ghost %{_libdir}/%{name}/components/xpti.dat

%dir %{_datadir}/%{name}/chrome
%{_datadir}/%{name}/chrome/US.jar
%{_datadir}/%{name}/chrome/classic.jar
%{_datadir}/%{name}/chrome/comm.jar
%{_datadir}/%{name}/chrome/content-packs.jar
%{_datadir}/%{name}/chrome/cview.jar
%{_datadir}/%{name}/chrome/embed-sample.jar
%{_datadir}/%{name}/chrome/en-US.jar
%{_datadir}/%{name}/chrome/en-unix.jar
%{_datadir}/%{name}/chrome/help.jar
%{_datadir}/%{name}/chrome/layoutdebug.jar
%{_datadir}/%{name}/chrome/modern.jar
%{_datadir}/%{name}/chrome/pipnss.jar
%{_datadir}/%{name}/chrome/pippki.jar
%{_datadir}/%{name}/chrome/reporter.jar
%{_datadir}/%{name}/chrome/sql.jar
%{_datadir}/%{name}/chrome/sroaming.jar
%{_datadir}/%{name}/chrome/tasks.jar
%{_datadir}/%{name}/chrome/toolkit.jar
%{_datadir}/%{name}/chrome/xforms.jar

%ghost %{_datadir}/%{name}/chrome/chrome.rdf
%ghost %{_datadir}/%{name}/chrome/overlays.rdf
# not generated automatically ?
%{_datadir}/%{name}/chrome/stylesheets.rdf
%{_datadir}/%{name}/chrome/chromelist.txt
%{_datadir}/%{name}/chrome/icons
%exclude %{_datadir}/%{name}/chrome/icons/default/abcardWindow*.xpm
%exclude %{_datadir}/%{name}/chrome/icons/default/addressbookWindow*.xpm
%exclude %{_datadir}/%{name}/chrome/icons/default/chatzilla-window*.xpm
%exclude %{_datadir}/%{name}/chrome/icons/default/messengerWindow*.xpm
%exclude %{_datadir}/%{name}/chrome/icons/default/msgcomposeWindow*.xpm
%exclude %{_datadir}/%{name}/chrome/icons/default/venkman-window*.xpm
%exclude %{_datadir}/%{name}/chrome/icons/default/winInspectorMain*.xpm

%{_datadir}/%{name}/chrome/%{name}-installed-chrome.txt
%ghost %{_datadir}/%{name}/chrome/installed-chrome.txt

%{_datadir}/%{name}/defaults
%{_datadir}/%{name}/dictionaries
%{_datadir}/%{name}/greprefs
%exclude %{_datadir}/%{name}/defaults/pref/inspector.js
%{_datadir}/%{name}/icons
%{_datadir}/%{name}/res
%{_datadir}/%{name}/searchplugins

%{_pixmapsdir}/seamonkey.png
%{_desktopdir}/%{name}.desktop
%{_desktopdir}/%{name}-composer.desktop

%files mailnews
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/%{name}/libmsgbaseutil.so
%attr(755,root,root) %{_libdir}/%{name}/components/libaddrbook.so
%attr(755,root,root) %{_libdir}/%{name}/components/libbayesflt.so
%attr(755,root,root) %{_libdir}/%{name}/components/libimpText.so
%attr(755,root,root) %{_libdir}/%{name}/components/libimpComm4xMail.so
%attr(755,root,root) %{_libdir}/%{name}/components/libimport.so
%attr(755,root,root) %{_libdir}/%{name}/components/liblocalmail.so
%attr(755,root,root) %{_libdir}/%{name}/components/libmailnews.so
%attr(755,root,root) %{_libdir}/%{name}/components/libmailview.so
%attr(755,root,root) %{_libdir}/%{name}/components/libmime.so
%attr(755,root,root) %{_libdir}/%{name}/components/libmimeemitter.so
%attr(755,root,root) %{_libdir}/%{name}/components/libmsg*.so
%attr(755,root,root) %{_libdir}/%{name}/components/libvcard.so

%{_libdir}/%{name}/components/addrbook.xpt
%{_libdir}/%{name}/components/impComm4xMail.xpt
%{_libdir}/%{name}/components/import.xpt
%{_libdir}/%{name}/components/mailnews.xpt
%{_libdir}/%{name}/components/mailview.xpt
%{_libdir}/%{name}/components/mime.xpt
%{_libdir}/%{name}/components/msg*.xpt

%{_libdir}/%{name}/components/mdn-service.js
%{_libdir}/%{name}/components/nsAbLDAPAttributeMap.js
%{_libdir}/%{name}/components/nsLDAPPrefsService.js
%{_libdir}/%{name}/components/offlineStartup.js
%{_libdir}/%{name}/components/smime-service.js

%{_datadir}/%{name}/chrome/messenger.jar

%{_datadir}/%{name}/chrome/icons/default/abcardWindow*.xpm
%{_datadir}/%{name}/chrome/icons/default/addressbookWindow*.xpm
%{_datadir}/%{name}/chrome/icons/default/messengerWindow*.xpm
%{_datadir}/%{name}/chrome/icons/default/msgcomposeWindow*.xpm

%{_desktopdir}/%{name}-mail.desktop

%files addon-enigmail
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/%{name}/components/libenigmime.so
%{_libdir}/%{name}/components/enigmail.xpt
%{_libdir}/%{name}/components/enigmime.xpt
%{_libdir}/%{name}/components/ipc.xpt
%{_libdir}/%{name}/components/enigmail.js
%{_libdir}/%{name}/components/enigprefs-service.js
%{_datadir}/%{name}/chrome/enigmail-en-US.jar
%{_datadir}/%{name}/chrome/enigmail-locale.jar
%{_datadir}/%{name}/chrome/enigmail-skin-tbird.jar
%{_datadir}/%{name}/chrome/enigmail-skin.jar
%{_datadir}/%{name}/chrome/enigmail.jar
%{_datadir}/%{name}/chrome/enigmime.jar

%files chat
%defattr(644,root,root,755)
%{_libdir}/%{name}/components/chatzilla-service.js
%{_datadir}/%{name}/chrome/chatzilla.jar
%{_datadir}/%{name}/chrome/icons/default/chatzilla-window*.xpm
%{_desktopdir}/%{name}-chat.desktop

%files js-debugger
%defattr(644,root,root,755)
%{_libdir}/%{name}/components/venkman-service.js
%{_datadir}/%{name}/chrome/venkman.jar
%{_datadir}/%{name}/chrome/icons/default/venkman-window*.xpm
%{_desktopdir}/%{name}-venkman.desktop

%files dom-inspector
%defattr(644,root,root,755)
%{_libdir}/%{name}/components/inspector.xpt
%{_libdir}/%{name}/components/inspector-cmdline.js
%{_datadir}/%{name}/chrome/inspector.jar
%{_datadir}/%{name}/chrome/icons/default/winInspectorMain*.xpm
%{_datadir}/%{name}/defaults/pref/inspector.js
