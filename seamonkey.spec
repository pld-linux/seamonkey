#
# Conditional build:
%bcond_without	gnomevfs	# disable GnomeVFS support
%bcond_with	gnomeui		# enable GnomeUI
%bcond_without	gnome		# disable gnomevfs (alias)
%bcond_without	svg		# disable svg support
#
%if %{without gnome}
%undefine	with_gnomevfs
%endif
%define	enigmail_ver	0.95.6
Summary:	SeaMonkey Community Edition - web browser
Summary(es.UTF-8):	Navegador de Internet SeaMonkey Community Edition
Summary(pl.UTF-8):	SeaMonkey Community Edition - przeglądarka WWW
Summary(pt_BR.UTF-8):	Navegador SeaMonkey Community Edition
Name:		seamonkey
Version:	1.1.8
Release:	1
License:	MPL 1.1 or GPL v2+ or LGPL v2.1+
Group:		X11/Applications/Networking
Source0:	ftp://ftp.mozilla.org/pub/mozilla.org/seamonkey/releases/%{version}/%{name}-%{version}.source.tar.bz2
# Source0-md5:	d91320fcd6a6aa48cc7c4d5ae596b09e
Source1:	http://www.mozilla-enigmail.org/download/source/enigmail-%{enigmail_ver}.tar.gz
# Source1-md5:	cfbe6ff77f80a349b396829757ad952a
Source2:	%{name}.desktop
Source3:	%{name}-composer.desktop
Source4:	%{name}-chat.desktop
Source5:	%{name}-mail.desktop
Source6:	%{name}-venkman.desktop
Patch0:		%{name}-pld-homepage.patch
Patch1:		%{name}-ldap-with-nss.patch
Patch2:		%{name}-kill_slim_hidden_def.patch
Patch3:		%{name}-lib_path.patch
Patch4:		%{name}-fonts.patch
Patch5:		%{name}-agent.patch
URL:		http://www.mozilla.org/projects/seamonkey/
BuildRequires:	automake
%{?with_svg:BuildRequires:	cairo-devel >= 1.0.0}
BuildRequires:	freetype-devel >= 1:2.1.8
BuildRequires:	libIDL-devel >= 0.8.0
%{?with_gnomevfs:BuildRequires:	gnome-vfs2-devel >= 2.0.0}
BuildRequires:	gtk+2-devel
%{?with_gnomeui:BuildRequires:	libgnomeui-devel >= 2.0}
BuildRequires:	libjpeg-devel >= 6b
BuildRequires:	libpng-devel >= 1.2.7
BuildRequires:	libstdc++-devel
BuildRequires:	nspr-devel >= 1:4.6.1
BuildRequires:	nss-devel >= 1:3.11.3
BuildRequires:	perl-modules >= 5.6.0
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.356
BuildRequires:	sed >= 4.0
BuildRequires:	xorg-lib-libXext-devel
BuildRequires:	xorg-lib-libXft-devel >= 2.1
BuildRequires:	xorg-lib-libXinerama-devel
BuildRequires:	xorg-lib-libXp-devel
BuildRequires:	xorg-lib-libXt-devel
BuildRequires:	zip >= 2.1
BuildRequires:	zlib-devel >= 1.2.3
Requires(post,postun):	%{name}-libs = %{epoch}:%{version}-%{release}
Requires:	%{name}-libs = %{epoch}:%{version}-%{release}
Requires:	browser-plugins >= 2.0
%{?with_svg:Requires:	cairo >= 1.0.0}
Requires:	nspr >= 1:4.6.1
Requires:	nss >= 1:3.11.3
Provides:	seamonkey-embedded = %{epoch}:%{version}-%{release}
Provides:	wwwbrowser
Obsoletes:	light
Obsoletes:	mozilla
Obsoletes:	seamonkey-calendar
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_seamonkeydir	%{_libdir}/%{name}
%define		_chromedir	%{_libdir}/%{name}/chrome

# firefox/thunderbird/seamonkey provide their own versions
%define		_noautoreqdep	libgfxpsshar.so libgkgfx.so libgtkxtbin.so libjsj.so libxlibrgb.so libxpcom_compat.so libxpcom_core.so libxpistub.so
# we don't want these to satisfy xulrunner-devel
%define		_noautoprov	libgtkembedmoz.so libldap50.so libmozjs.so libprldap50.so libssldap50.so libxpcom.so libxul.so
# and as we don't provide them, don't require either
%define		_noautoreq	libgtkembedmoz.so libldap50.so libmozjs.so libprldap50.so libssldap50.so libxpcom.so libxul.so

%define		specflags	-fno-strict-aliasing

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

%package libs
Summary:	SeaMonkey Community Edition shared libraries
Summary(pl.UTF-8):	Biblioteki współdzielone SeaMonkey Community Edition
Group:		Libraries
Obsoletes:	mozilla-libs

%description libs
SeaMonkey Community Edition shared libraries.

%description libs -l pl.UTF-8
Biblioteki współdzielone SeaMonkey Community Edition.

%package mailnews
Summary:	SeaMonkey Community Edition - programs for mail and news
Summary(pl.UTF-8):	SeaMonkey Community Edition - programy do poczty i newsów
Summary(ru.UTF-8):	Почтовая система на основе SeaMonkey Community Edition
Group:		X11/Applications/Networking
Requires(post,postun):	%{name} = %{epoch}:%{version}-%{release}
Requires:	%{name} = %{epoch}:%{version}-%{release}
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
Requires(post,postun):	%{name}-mailnews = %{epoch}:%{version}-%{release}
Requires:	%{name}-mailnews = %{epoch}:%{version}-%{release}
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
Requires(post,postun):	%{name} = %{epoch}:%{version}-%{release}
Requires:	%{name} = %{epoch}:%{version}-%{release}
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
Requires(post,postun):	%{name} = %{epoch}:%{version}-%{release}
Requires:	%{name} = %{epoch}:%{version}-%{release}
Obsoletes:	mozilla-js-debugger

%description js-debugger
JavaScript debugger for use with SeaMonkey Community Edition.

%description js-debugger -l pl.UTF-8
Odpluskwiacz JavaScriptu do używania z SeaMonkey Community Edition.

%package dom-inspector
Summary:	A tool for inspecting the DOM of pages in SeaMonkey Community Edition
Summary(pl.UTF-8):	Narzędzie do oglądania DOM stron w SeaMonkey Community Edition
Group:		X11/Applications/Networking
Requires(post,postun):	%{name} = %{epoch}:%{version}-%{release}
Requires:	%{name} = %{epoch}:%{version}-%{release}
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

%package gnomevfs
Summary:	Gnome-VFS module providing support for smb:// URLs
Summary(pl.UTF-8):	Moduł Gnome-VFS dodający wsparcie dla URLi smb://
Group:		X11/Applications/Networking
Requires(post,postun):	%{name} = %{epoch}:%{version}-%{release}
Requires:	%{name} = %{epoch}:%{version}-%{release}
Obsoletes:	mozilla-gnomevfs

%description gnomevfs
Gnome-VFS module providing support for smb:// URLs.

%description gnomevfs -l pl.UTF-8
Moduł Gnome-VFS dodający wsparcie dla URLi smb://.

%prep
%setup -qc
cd mozilla
tar -C mailnews/extensions -zxf %{SOURCE1}
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1

%build
cd mozilla

cp -f /usr/share/automake/config.* build/autoconf
cp -f /usr/share/automake/config.* nsprpub/build/autoconf
cp -f /usr/share/automake/config.* directory/c-sdk/config/autoconf
ac_cv_visibility_pragma=no; export ac_cv_visibility_pragma
%configure2_13 \
	%{!?debug:--disable-debug} \
	--disable-elf-dynstr-gc \
	%{!?with_gnomeui:--disable-gnomeui} \
	%{!?with_gnomevfs:--disable-gnomevfs} \
	--disable-pedantic \
	--disable-tests \
	--disable-xterm-updates \
	--enable-application=suite \
	--enable-crypto \
	--enable-default-toolkit=gtk2 \
	--enable-extensions \
	--enable-ldap \
	--enable-mathml \
	--enable-optimize="%{rpmcflags}" \
	--enable-postscript \
	%{!?debug:--enable-strip} \
	%{?with_svg:--enable-svg --enable-svg-renderer-cairo} \
	%{?with_svg:--enable-system-cairo} \
	--enable-xft \
	--enable-xinerama \
	--enable-xprint \
	--enable-old-abi-compat-wrappers \
	--with-default-mozilla-five-home=%{_seamonkeydir} \
	--with-pthreads \
	--with-system-jpeg \
	--with-system-nspr \
	--with-system-nss \
	--with-system-png \
	--with-system-zlib \
	--with-x

%{__make}

cd mailnews/extensions/enigmail
./makemake -r
%{__make}
cd ../../..

%install
rm -rf $RPM_BUILD_ROOT
cd mozilla
install -d \
	$RPM_BUILD_ROOT{%{_bindir},%{_sbindir},%{_datadir}} \
	$RPM_BUILD_ROOT{%{_desktopdir},%{_pixmapsdir}} \
	$RPM_BUILD_ROOT%{_datadir}/%{name}/{chrome,defaults,dictionaries,icons,greprefs,res,searchplugins} \
	$RPM_BUILD_ROOT%{_seamonkeydir}/{components,plugins}

# preparing to create register
# remove empty directory trees
rm -fr dist/bin/chrome/{US,chatzilla,classic,comm,content-packs,cview,embed,embed-sample,en-US,en-mac,en-unix,en-win,help,inspector,messenger,modern,pipnss,pippki,toolkit,venkman,xmlterm}
# non-unix
rm -f dist/bin/chrome/en-{mac,win}.jar

# creating and installing register
LD_LIBRARY_PATH="dist/bin" MOZILLA_FIVE_HOME="dist/bin" dist/bin/regxpcom
LD_LIBRARY_PATH="dist/bin" MOZILLA_FIVE_HOME="dist/bin" dist/bin/regchrome

ln -sf ../../share/%{name}/chrome $RPM_BUILD_ROOT%{_chromedir}
ln -sf ../../share/%{name}/defaults $RPM_BUILD_ROOT%{_seamonkeydir}/defaults
ln -sf ../../share/%{name}/dictionaries $RPM_BUILD_ROOT%{_seamonkeydir}/dictionaries
ln -sf ../../share/%{name}/greprefs $RPM_BUILD_ROOT%{_seamonkeydir}/greprefs
ln -sf ../../share/%{name}/icons $RPM_BUILD_ROOT%{_seamonkeydir}/icons
ln -sf ../../share/%{name}/res $RPM_BUILD_ROOT%{_seamonkeydir}/res
ln -sf ../../share/%{name}/searchplugins $RPM_BUILD_ROOT%{_seamonkeydir}/searchplugins

cp -frL dist/bin/chrome/*	$RPM_BUILD_ROOT%{_datadir}/%{name}/chrome
cp -frL dist/bin/components/{[!m],m[!y]}*	$RPM_BUILD_ROOT%{_seamonkeydir}/components
cp -frL dist/bin/defaults/*	$RPM_BUILD_ROOT%{_datadir}/%{name}/defaults
cp -frL dist/bin/dictionaries/*	$RPM_BUILD_ROOT%{_datadir}/%{name}/dictionaries
cp -frL dist/bin/greprefs/*	$RPM_BUILD_ROOT%{_datadir}/%{name}/greprefs
cp -frL dist/bin/res/*		$RPM_BUILD_ROOT%{_datadir}/%{name}/res
cp -frL dist/bin/searchplugins/* $RPM_BUILD_ROOT%{_datadir}/%{name}/searchplugins

install dist/bin/*.so $RPM_BUILD_ROOT%{_seamonkeydir}

ln -s %{_libdir}/libnssckbi.so $RPM_BUILD_ROOT%{_seamonkeydir}/libnssckbi.so

install %{SOURCE2} %{SOURCE3} %{SOURCE4} %{SOURCE5} %{SOURCE6} \
	$RPM_BUILD_ROOT%{_desktopdir}

install suite/branding/icons/gtk/seamonkey.png $RPM_BUILD_ROOT%{_pixmapsdir}

install dist/bin/seamonkey-bin $RPM_BUILD_ROOT%{_seamonkeydir}
install dist/bin/regchrome $RPM_BUILD_ROOT%{_seamonkeydir}
install dist/bin/regxpcom $RPM_BUILD_ROOT%{_seamonkeydir}
install dist/bin/xpidl $RPM_BUILD_ROOT%{_seamonkeydir}

cp $RPM_BUILD_ROOT%{_chromedir}/installed-chrome.txt \
        $RPM_BUILD_ROOT%{_chromedir}/%{name}-installed-chrome.txt

cat << 'EOF' > $RPM_BUILD_ROOT%{_bindir}/seamonkey
#!/bin/sh
# (c) vip at linux.pl, wolf at pld-linux.org

LD_LIBRARY_PATH=%{_seamonkeydir}${LD_LIBRARY_PATH:+:$LD_LIBRARY_PATH}
export LD_LIBRARY_PATH

MOZILLA_FIVE_HOME="%{_seamonkeydir}"
SEAMONKEY="$MOZILLA_FIVE_HOME/seamonkey-bin"
if [ "$1" == "-remote" ]; then
	exec $SEAMONKEY "$@"
fi

PING=`$SEAMONKEY -remote 'ping()' 2>&1 >/dev/null`
	if [ -n "$PING" ]; then
		if [ -f "`pwd`/$1" ]; then
		exec $SEAMONKEY "file://`pwd`/$1"
		else
		exec $SEAMONKEY "$@"
		fi
fi

		if [ -z "$1" ]; then
	exec $SEAMONKEY -remote 'xfeDoCommand (openBrowser)'
		elif [ "$1" == "-mail" ]; then
	exec $SEAMONKEY -remote 'xfeDoCommand (openInbox)'
		elif [ "$1" == "-compose" ]; then
	exec $SEAMONKEY -remote 'xfeDoCommand (composeMessage)'
fi

[[ $1 == -* ]] && exec $SEAMONKEY "$@"

				if [ -f "`pwd`/$1" ]; then
					URL="file://`pwd`/$1"
				else
					URL="$1"
				fi
if grep -q -E 'browser.tabs.opentabfor.middleclick.*true' \
		~/.mozilla/default/*/prefs.js; then
	exec $SEAMONKEY -remote "OpenUrl($URL,new-tab)"
				else
	exec $SEAMONKEY -remote "OpenUrl($URL,new-window)"
fi

echo "Cannot execute SeaMonkey ($SEAMONKEY)!" >&2
exit 1
EOF

cat << 'EOF' > $RPM_BUILD_ROOT%{_sbindir}/%{name}-chrome+xpcom-generate
#!/bin/sh
umask 022
cd %{_datadir}/%{name}/chrome
cat *-installed-chrome.txt > installed-chrome.txt
rm -f chrome.rdf overlays.rdf
rm -f %{_seamonkeydir}/components/{compreg,xpti}.dat

LD_LIBRARY_PATH=%{_seamonkeydir}${LD_LIBRARY_PATH:+:$LD_LIBRARY_PATH}
export LD_LIBRARY_PATH

MOZILLA_FIVE_HOME=%{_seamonkeydir} %{_seamonkeydir}/regxpcom
MOZILLA_FIVE_HOME=%{_seamonkeydir} %{_seamonkeydir}/regchrome
exit 0
EOF

%browser_plugins_add_browser %{name} -p %{_libdir}/%{name}/plugins

%clean
rm -rf $RPM_BUILD_ROOT

%post
%{_sbindir}/%{name}-chrome+xpcom-generate
%update_browser_plugins

%postun
%{_sbindir}/%{name}-chrome+xpcom-generate
if [ "$1" = 0 ]; then
	%update_browser_plugins
fi

%post mailnews -p %{_sbindir}/%{name}-chrome+xpcom-generate
%postun mailnews -p %{_sbindir}/%{name}-chrome+xpcom-generate

%post addon-enigmail -p %{_sbindir}/%{name}-chrome+xpcom-generate
%postun addon-enigmail -p %{_sbindir}/%{name}-chrome+xpcom-generate

%post chat -p %{_sbindir}/%{name}-chrome+xpcom-generate
%postun chat -p %{_sbindir}/%{name}-chrome+xpcom-generate

%post js-debugger -p %{_sbindir}/%{name}-chrome+xpcom-generate
%postun js-debugger -p %{_sbindir}/%{name}-chrome+xpcom-generate

%post dom-inspector -p %{_sbindir}/%{name}-chrome+xpcom-generate
%postun dom-inspector -p %{_sbindir}/%{name}-chrome+xpcom-generate

%post gnomevfs -p %{_sbindir}/%{name}-chrome+xpcom-generate
%postun gnomevfs -p %{_sbindir}/%{name}-chrome+xpcom-generate

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/seamonkey
%attr(744,root,root) %{_sbindir}/%{name}-chrome+xpcom-generate

# browser plugins v2
%{_browserpluginsconfdir}/browsers.d/%{name}.*
%config(noreplace) %verify(not md5 mtime size) %{_browserpluginsconfdir}/blacklist.d/%{name}.*.blacklist

%dir %{_chromedir}
%dir %{_seamonkeydir}/components
%dir %{_seamonkeydir}/defaults
%dir %{_seamonkeydir}/dictionaries
%dir %{_seamonkeydir}/greprefs
%dir %{_seamonkeydir}/icons
%dir %{_seamonkeydir}/plugins
%dir %{_seamonkeydir}/res
%dir %{_seamonkeydir}/searchplugins
%dir %{_datadir}/%{name}

%attr(755,root,root) %{_seamonkeydir}/seamonkey-bin
%attr(755,root,root) %{_seamonkeydir}/reg*
%attr(755,root,root) %{_seamonkeydir}/xpidl

%attr(755,root,root) %{_seamonkeydir}/libnssckbi.so

%attr(755,root,root) %{_seamonkeydir}/components/libaccess*.so
%attr(755,root,root) %{_seamonkeydir}/components/libappcomps.so
%attr(755,root,root) %{_seamonkeydir}/components/libauth*.so
%attr(755,root,root) %{_seamonkeydir}/components/libautoconfig.so
%attr(755,root,root) %{_seamonkeydir}/components/libcaps.so
%attr(755,root,root) %{_seamonkeydir}/components/libchrome.so
%attr(755,root,root) %{_seamonkeydir}/components/libcomposer.so
%attr(755,root,root) %{_seamonkeydir}/components/libcookie.so
%attr(755,root,root) %{_seamonkeydir}/components/libdocshell.so
%attr(755,root,root) %{_seamonkeydir}/components/libeditor.so
%attr(755,root,root) %{_seamonkeydir}/components/libembedcomponents.so
%attr(755,root,root) %{_seamonkeydir}/components/libfileview.so
%attr(755,root,root) %{_seamonkeydir}/components/libgfx*.so
%attr(755,root,root) %{_seamonkeydir}/components/libgk*.so
%attr(755,root,root) %{_seamonkeydir}/components/libhtmlpars.so
%attr(755,root,root) %{_seamonkeydir}/components/libi18n.so
%attr(755,root,root) %{_seamonkeydir}/components/libimg*.so
%attr(755,root,root) %{_seamonkeydir}/components/libjar50.so
%attr(755,root,root) %{_seamonkeydir}/components/libjsd.so
%attr(755,root,root) %{_seamonkeydir}/components/libmork.so
%attr(755,root,root) %{_seamonkeydir}/components/libmoz*.so
%attr(755,root,root) %{_seamonkeydir}/components/libmyspell.so
%attr(755,root,root) %{_seamonkeydir}/components/libnecko*.so
%attr(755,root,root) %{_seamonkeydir}/components/libnkdatetime.so
%attr(755,root,root) %{_seamonkeydir}/components/libnkfinger.so
%attr(755,root,root) %{_seamonkeydir}/components/libns*.so
%attr(755,root,root) %{_seamonkeydir}/components/liboji.so
%attr(755,root,root) %{_seamonkeydir}/components/libp3p.so
%attr(755,root,root) %{_seamonkeydir}/components/libpermissions.so
%attr(755,root,root) %{_seamonkeydir}/components/libpipboot.so
%attr(755,root,root) %{_seamonkeydir}/components/libpipnss.so
%attr(755,root,root) %{_seamonkeydir}/components/libpippki.so
%attr(755,root,root) %{_seamonkeydir}/components/libpref.so
%attr(755,root,root) %{_seamonkeydir}/components/libprofile.so
%attr(755,root,root) %{_seamonkeydir}/components/librdf.so
%attr(755,root,root) %{_seamonkeydir}/components/libremoteservice.so
%attr(755,root,root) %{_seamonkeydir}/components/libschemavalidation.so
%attr(755,root,root) %{_seamonkeydir}/components/libsearchservice.so
%attr(755,root,root) %{_seamonkeydir}/components/libspellchecker.so
%attr(755,root,root) %{_seamonkeydir}/components/libsql.so
%attr(755,root,root) %{_seamonkeydir}/components/libsroaming.so
%attr(755,root,root) %{_seamonkeydir}/components/libstoragecomps.so
%attr(755,root,root) %{_seamonkeydir}/components/libsystem-pref.so
%attr(755,root,root) %{_seamonkeydir}/components/libtransformiix.so
%attr(755,root,root) %{_seamonkeydir}/components/libtxmgr.so
%attr(755,root,root) %{_seamonkeydir}/components/libtypeaheadfind.so
%attr(755,root,root) %{_seamonkeydir}/components/libuconv.so
%attr(755,root,root) %{_seamonkeydir}/components/libucv*.so
%attr(755,root,root) %{_seamonkeydir}/components/libuniversalchardet.so
%attr(755,root,root) %{_seamonkeydir}/components/libwallet.so
%attr(755,root,root) %{_seamonkeydir}/components/libwalletviewers.so
%attr(755,root,root) %{_seamonkeydir}/components/libwebbrwsr.so
%attr(755,root,root) %{_seamonkeydir}/components/libwebsrvcs.so
%attr(755,root,root) %{_seamonkeydir}/components/libwidget_gtk2.so
%attr(755,root,root) %{_seamonkeydir}/components/libx*.so

%{_seamonkeydir}/components/access*.xpt
%{_seamonkeydir}/components/alerts.xpt
%{_seamonkeydir}/components/appshell.xpt
%{_seamonkeydir}/components/appstartup.xpt
%{_seamonkeydir}/components/autocomplete.xpt
%{_seamonkeydir}/components/autoconfig.xpt
%{_seamonkeydir}/components/bookmarks.xpt
%{_seamonkeydir}/components/caps.xpt
%{_seamonkeydir}/components/chardet.xpt
%{_seamonkeydir}/components/chrome.xpt
%{_seamonkeydir}/components/commandhandler.xpt
%{_seamonkeydir}/components/composer.xpt
%{_seamonkeydir}/components/content*.xpt
%{_seamonkeydir}/components/cookie.xpt
%{_seamonkeydir}/components/directory.xpt
%{_seamonkeydir}/components/docshell.xpt
%{_seamonkeydir}/components/dom*.xpt
%{_seamonkeydir}/components/downloadmanager.xpt
%{_seamonkeydir}/components/editor.xpt
%{_seamonkeydir}/components/embed_base.xpt
%{_seamonkeydir}/components/extensions.xpt
%{_seamonkeydir}/components/exthandler.xpt
%{_seamonkeydir}/components/find.xpt
%{_seamonkeydir}/components/filepicker.xpt
%{_seamonkeydir}/components/gfx*.xpt
%{?with_svg:%{_seamonkeydir}/components/gksvgrenderer.xpt}
%{_seamonkeydir}/components/history.xpt
%{_seamonkeydir}/components/htmlparser.xpt
%{?with_gnomeui:%{_seamonkeydir}/components/imgicon.xpt}
%{_seamonkeydir}/components/imglib2.xpt
%{_seamonkeydir}/components/intl.xpt
%{_seamonkeydir}/components/jar.xpt
%{_seamonkeydir}/components/js*.xpt
%{_seamonkeydir}/components/layout*.xpt
%{_seamonkeydir}/components/locale.xpt
%{_seamonkeydir}/components/lwbrk.xpt
%{_seamonkeydir}/components/mimetype.xpt
%{_seamonkeydir}/components/moz*.xpt
%{_seamonkeydir}/components/necko*.xpt
%{_seamonkeydir}/components/oji.xpt
%{_seamonkeydir}/components/p3p.xpt
%{_seamonkeydir}/components/pipboot.xpt
%{_seamonkeydir}/components/pipnss.xpt
%{_seamonkeydir}/components/pippki.xpt
%{_seamonkeydir}/components/plugin.xpt
%{_seamonkeydir}/components/pref.xpt
%{_seamonkeydir}/components/prefetch.xpt
%{_seamonkeydir}/components/prefmigr.xpt
%{_seamonkeydir}/components/profile.xpt
%{_seamonkeydir}/components/progressDlg.xpt
%{_seamonkeydir}/components/proxyObjInst.xpt
%{_seamonkeydir}/components/rdf.xpt
%{_seamonkeydir}/components/related.xpt
%{_seamonkeydir}/components/saxparser.xpt
%{_seamonkeydir}/components/search.xpt
%{_seamonkeydir}/components/schemavalidation.xpt
%{_seamonkeydir}/components/shistory.xpt
%{_seamonkeydir}/components/signonviewer.xpt
%{_seamonkeydir}/components/spellchecker.xpt
%{_seamonkeydir}/components/sql.xpt
%{_seamonkeydir}/components/storage.xpt
%{_seamonkeydir}/components/toolkitremote.xpt
%{_seamonkeydir}/components/txmgr.xpt
%{_seamonkeydir}/components/txtsvc.xpt
%{_seamonkeydir}/components/typeaheadfind.xpt
%{_seamonkeydir}/components/uconv.xpt
%{_seamonkeydir}/components/unicharutil.xpt
%{_seamonkeydir}/components/uriloader.xpt
%{_seamonkeydir}/components/urlformatter.xpt
%{_seamonkeydir}/components/wallet*.xpt
%{_seamonkeydir}/components/webBrowser_core.xpt
%{_seamonkeydir}/components/webbrowserpersist.xpt
%{_seamonkeydir}/components/webshell_idls.xpt
%{_seamonkeydir}/components/websrvcs.xpt
%{_seamonkeydir}/components/widget.xpt
%{_seamonkeydir}/components/windowds.xpt
%{_seamonkeydir}/components/windowwatcher.xpt
%{_seamonkeydir}/components/x*.xpt

%{_seamonkeydir}/components/jsconsole-clhandler.js
%{_seamonkeydir}/components/nsCloseAllWindows.js
%{_seamonkeydir}/components/nsComposerCmdLineHandler.js
%{_seamonkeydir}/components/nsDictionary.js
%{_seamonkeydir}/components/nsDownloadProgressListener.js
%{_seamonkeydir}/components/nsFilePicker.js
%{_seamonkeydir}/components/nsHelperAppDlg.js
%{_seamonkeydir}/components/nsInterfaceInfoToIDL.js
%{_seamonkeydir}/components/nsKillAll.js
%{_seamonkeydir}/components/nsProgressDialog.js
%{_seamonkeydir}/components/nsProxyAutoConfig.js
%{_seamonkeydir}/components/nsResetPref.js
%{_seamonkeydir}/components/nsSchemaValidatorRegexp.js
%{_seamonkeydir}/components/nsSidebar.js
%{_seamonkeydir}/components/nsUpdateNotifier.js
%{_seamonkeydir}/components/nsURLFormatter.js
%{_seamonkeydir}/components/nsXmlRpcClient.js
%{_seamonkeydir}/components/xulappinfo.js

# not *.dat, so check-files can catch any new files
# (and they won't be just silently placed empty in rpm)
%ghost %{_seamonkeydir}/components/compreg.dat
%ghost %{_seamonkeydir}/components/xpti.dat

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

%files libs
%defattr(644,root,root,755)
%dir %{_seamonkeydir}
# libxpcom.so used by mozillaplug-in
# probably should add more if more packages require
%attr(755,root,root) %{_seamonkeydir}/libxpcom.so
%attr(755,root,root) %{_seamonkeydir}/libxpcom_compat.so
%attr(755,root,root) %{_seamonkeydir}/libxpcom_core.so

# add rest too
%attr(755,root,root) %{_seamonkeydir}/libgfxpsshar.so
%attr(755,root,root) %{_seamonkeydir}/libgkgfx.so
%attr(755,root,root) %{_seamonkeydir}/libgtkembedmoz.so
%attr(755,root,root) %{_seamonkeydir}/libgtkxtbin.so
%attr(755,root,root) %{_seamonkeydir}/libjsj.so
%attr(755,root,root) %{_seamonkeydir}/libldap50.so
%attr(755,root,root) %{_seamonkeydir}/libprldap50.so
%attr(755,root,root) %{_seamonkeydir}/libssldap50.so
%attr(755,root,root) %{_seamonkeydir}/libmozjs.so
%attr(755,root,root) %{_seamonkeydir}/libxpistub.so
%attr(755,root,root) %{_seamonkeydir}/libxlibrgb.so

%files mailnews
%defattr(644,root,root,755)
%attr(755,root,root) %{_seamonkeydir}/libmsgbaseutil.so
%attr(755,root,root) %{_seamonkeydir}/components/libaddrbook.so
%attr(755,root,root) %{_seamonkeydir}/components/libbayesflt.so
%attr(755,root,root) %{_seamonkeydir}/components/libimpText.so
%attr(755,root,root) %{_seamonkeydir}/components/libimpComm4xMail.so
%attr(755,root,root) %{_seamonkeydir}/components/libimport.so
%attr(755,root,root) %{_seamonkeydir}/components/liblocalmail.so
%attr(755,root,root) %{_seamonkeydir}/components/libmailnews.so
%attr(755,root,root) %{_seamonkeydir}/components/libmailview.so
%attr(755,root,root) %{_seamonkeydir}/components/libmime.so
%attr(755,root,root) %{_seamonkeydir}/components/libmimeemitter.so
%attr(755,root,root) %{_seamonkeydir}/components/libmsg*.so
%attr(755,root,root) %{_seamonkeydir}/components/libvcard.so

%{_seamonkeydir}/components/addrbook.xpt
%{_seamonkeydir}/components/impComm4xMail.xpt
%{_seamonkeydir}/components/import.xpt
%{_seamonkeydir}/components/mailnews.xpt
%{_seamonkeydir}/components/mailview.xpt
%{_seamonkeydir}/components/mime.xpt
%{_seamonkeydir}/components/msg*.xpt

%{_seamonkeydir}/components/mdn-service.js
%{_seamonkeydir}/components/nsAbLDAPAttributeMap.js
%{_seamonkeydir}/components/nsLDAPPrefsService.js
%{_seamonkeydir}/components/offlineStartup.js
%{_seamonkeydir}/components/smime-service.js

%{_datadir}/%{name}/chrome/messenger.jar

%{_datadir}/%{name}/chrome/icons/default/abcardWindow*.xpm
%{_datadir}/%{name}/chrome/icons/default/addressbookWindow*.xpm
%{_datadir}/%{name}/chrome/icons/default/messengerWindow*.xpm
%{_datadir}/%{name}/chrome/icons/default/msgcomposeWindow*.xpm

%{_desktopdir}/%{name}-mail.desktop

%files addon-enigmail
%defattr(644,root,root,755)
%attr(755,root,root) %{_seamonkeydir}/components/libenigmime.so
%{_seamonkeydir}/components/enigmail.xpt
%{_seamonkeydir}/components/enigmime.xpt
%{_seamonkeydir}/components/ipc.xpt
%{_seamonkeydir}/components/enigmail.js
%{_seamonkeydir}/components/enigprefs-service.js
%{_datadir}/%{name}/chrome/enigmail-en-US.jar
%{_datadir}/%{name}/chrome/enigmail-locale.jar
%{_datadir}/%{name}/chrome/enigmail-skin-tbird.jar
%{_datadir}/%{name}/chrome/enigmail-skin.jar
%{_datadir}/%{name}/chrome/enigmail.jar
%{_datadir}/%{name}/chrome/enigmime.jar

%files chat
%defattr(644,root,root,755)
%{_seamonkeydir}/components/chatzilla-service.js
%{_datadir}/%{name}/chrome/chatzilla.jar
%{_datadir}/%{name}/chrome/icons/default/chatzilla-window*.xpm
%{_desktopdir}/%{name}-chat.desktop

%files js-debugger
%defattr(644,root,root,755)
%{_seamonkeydir}/components/venkman-service.js
%{_datadir}/%{name}/chrome/venkman.jar
%{_datadir}/%{name}/chrome/icons/default/venkman-window*.xpm
%{_desktopdir}/%{name}-venkman.desktop

%files dom-inspector
%defattr(644,root,root,755)
%{_seamonkeydir}/components/inspector.xpt
%{_seamonkeydir}/components/inspector-cmdline.js
%{_datadir}/%{name}/chrome/inspector.jar
%{_datadir}/%{name}/chrome/icons/default/winInspectorMain*.xpm
%{_datadir}/%{name}/defaults/pref/inspector.js

%if %{with gnomevfs}
%files gnomevfs
%defattr(644,root,root,755)
%attr(755,root,root) %{_seamonkeydir}/components/libnkgnomevfs.so
%endif
