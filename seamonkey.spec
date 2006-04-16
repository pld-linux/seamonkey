#
# Conditional build:
%bcond_without	gnomevfs	# disable GnomeVFS support
%bcond_without	heimdal		# disable heimdal support
%bcond_without	svg		# disable svg support
#
Summary:	SeaMonkey - web browser
Summary(es):	Navegador de Internet SeaMonkey
Summary(pl):	SeaMonkey - przegl±darka WWW
Summary(pt_BR):	Navegador SeaMonkey
Name:		seamonkey
Version:	1.0.1
Release:	0.6
License:	Mozilla Public License
Group:		X11/Applications/Networking
Source0:	http://ftp.mozilla.org/pub/mozilla.org/seamonkey/releases/%{version}/%{name}-%{version}.source.tar.bz2
# Source0-md5:	6921464b5251cafd529c04c2b9f98d5f
Source1:	%{name}.desktop
Source2:	%{name}-composer.desktop
Source3:	%{name}-chat.desktop
Source4:	%{name}-mail.desktop
Source5:	%{name}-venkman.desktop
#Source6:	%{name}-jconsole.desktop
#Source7:	%{name}-terminal.desktop
Patch0:		%{name}-pld-homepage.patch
Patch1:		%{name}-nss.patch
Patch2:		%{name}-ldap-with-nss.patch
Patch3:		%{name}-kill_slim_hidden_def.patch
URL:		http://www.mozilla.org/projects/seamonkey/
BuildRequires:	/bin/csh
BuildRequires:	/bin/ex
BuildRequires:	automake
%{?with_svg:BuildRequires:	cairo-devel >= 1.0.0}
BuildRequires:	freetype-devel >= 1:2.1.8
%{?with_gnomevfs:BuildRequires:	gnome-vfs2-devel >= 2.0.0}
BuildRequires:	tar >= 1:1.15.1
# for libnegotiateauth
%{?with_heimdal:BuildRequires:	heimdal-devel >= 0.7}
BuildRequires:	libjpeg-devel >= 6b
BuildRequires:	libpng-devel >= 1.2.0
BuildRequires:	libstdc++-devel
BuildRequires:	nspr-devel >= 1:4.6.1
BuildRequires:	nss-devel >= 3.10.2
BuildRequires:	perl-modules >= 5.6.0
BuildRequires:	pkgconfig
BuildRequires:	sed >= 4.0
BuildRequires:	tar >= 1:1.15.1
BuildRequires:	xcursor-devel
BuildRequires:	xft-devel >= 2.1-2
BuildRequires:	zip >= 2.1
BuildRequires:	zlib-devel >= 1.0.0
Requires(post,postun):	/sbin/ldconfig
Requires:	%{name}-libs = %{epoch}:%{version}-%{release}
%{?with_svg:Requires:	cairo >= 1.0.0}
Requires:	nspr >= 1:4.6.1
Requires:	nss >= 3.10.2
Provides:	mozilla-embedded = %{epoch}:%{version}-%{release}
Provides:	wwwbrowser
Obsoletes:	light
Obsoletes:	mozilla-embedded
Obsoletes:	mozilla-irc
Obsoletes:	mozilla-theme-NegativeModern
Obsoletes:	mozilla-theme-gold
Obsoletes:	mozilla-theme-kzilla
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		specflags	-fno-strict-aliasing

%define		_chromedir	%{_libdir}/%{name}/chrome
# mozilla and firefox provide their own versions
%define		_noautoreqdep	libgkgfx.so libgtkxtbin.so libjsj.so libmozjs.so libxpcom.so libxpcom_compat.so

%description
SeaMonkey is an open-source web browser, designed for standards
compliance, performance and portability.

%description -l es
SeaMonkey es un navegador de Internet que se basa en una versión
inicial de Netscape Communicator. Este software está en desarrollo,
por lo cual todavía es inestable.

%description -l pl
SeaMonkey jest potê¿n± graficzn± przegl±dark± WWW, która jest nastêpc±
Mozilli, która nastêpnie by³a nastêpczyni± Netscape Communikatora.

%description -l pt_BR
O SeaMonkey é um web browser baseado numa versão inicial do Netscape
Communicator. Este software está em fase de desenvolvimento, portanto,
ainda não estável.

%description -l ru
SeaMonkey - ÐÏÌÎÏÆÕÎËÃÉÏÎÁÌØÎÙÊ web-browser Ó ÏÔËÒÙÔÙÍÉ ÉÓÈÏÄÎÙÍÉ
ÔÅËÓÔÁÍÉ, ÒÁÚÒÁÂÏÔÁÎÎÙÊ ÄÌÑ ÍÁËÓÉÍÁÌØÎÏÇÏ ÓÏÏÔ×ÅÓÔ×ÉÑ ÓÔÁÎÄÁÒÔÁÍ,
ÍÁËÓÍÉÍÁÌØÎÏÊ ÐÅÒÅÎÏÓÉÍÏÓÔÉ É ÓËÏÒÏÓÔÉ ÒÁÂÏÔÙ

%package libs
Summary:	SeaMonkey shared libraries
Summary(pl):	Biblioteki wspó³dzielone SeaMonkey
Group:		Libraries

%description libs
SeaMonkey shared libraries.

%description libs -l pl
Biblioteki wspó³dzielone SeaMonkey.

%package mailnews
Summary:	SeaMonkey - programs for mail and news
Summary(pl):	SeaMonkey - programy do poczty i newsów
Summary(ru):	ðÏÞÔÏ×ÁÑ ÓÉÓÔÅÍÁ ÎÁ ÏÓÎÏ×Å SeaMonkey
Group:		X11/Applications/Networking
Requires(post,postun):	%{name} = %{epoch}:%{version}-%{release}
Requires(post,postun):	/sbin/ldconfig
Requires:	%{name} = %{epoch}:%{version}-%{release}
Obsoletes:	mozilla-mail

%description mailnews
Programs for mail and news integrated with browser.

%description mailnews -l pl
Programy pocztowe i obs³uga newsów zintegrowane z przegl±dark±.

%description mailnews -l ru
ëÌÉÅÎÔ ÐÏÞÔÙ É ÎÏ×ÏÓÔÅÊ, ÎÁ ÏÓÎÏ×Å SeaMonkey. ðÏÄÄÅÒÖÉ×ÁÅÔ IMAP, POP É
NNTP É ÉÍÅÅÔ ÐÒÏÓÔÏÊ ÉÎÔÅÒÆÅÊÓ ÐÏÌØÚÏ×ÁÔÅÌÑ.

%package chat
Summary:	SeaMonkey Chat - IRC client integratd with SeaMonkey
Summary(pl):	SeaMonkey Chat - zintegrowany z Mozill± klient IRC-a
Group:		X11/Applications/Networking
Requires(post,postun):	%{name} = %{epoch}:%{version}-%{release}
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description chat
SeaMonkey Chat - IRC client that is integrated with the SeaMonkey web
browser.

%description chat -l pl
SeaMonkey Chat - klient IRC-a zintegrowany z przegl±dark± SeaMonkey.

%package js-debugger
Summary:	JavaScript debugger for use with SeaMonkey
Summary(pl):	Odpluskwiacz JavaScriptu do u¿ywania z SeaMonkey
Group:		X11/Applications/Networking
Requires(post,postun):	%{name} = %{epoch}:%{version}-%{release}
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description js-debugger
JavaScript debugger for use with SeaMonkey.

%description js-debugger -l pl
Odpluskwiacz JavaScriptu do u¿ywania z SeaMonkey.

%package dom-inspector
Summary:	A tool for inspecting the DOM of pages in SeaMonkey
Summary(pl):	Narzêdzie do ogl±dania DOM stron w SeaMonkey
Group:		X11/Applications/Networking
Requires(post,postun):	%{name} = %{epoch}:%{version}-%{release}
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description dom-inspector
This is a tool that allows you to inspect the DOM for web pages in
SeaMonkey. This is of great use to people who are doing SeaMonkey
chrome development or web page development.

%description dom-inspector -l pl
To narzêdzie pozwala na ogl±danie DOM dla stron WWW w SeaMonkey. Jest
bardzo przydatne dla ludzi rozwijaj±cych chrome w SeaMonkey lub
tworz±cych strony WWW.

%package gnomevfs
Summary:	Gnome-VFS module providing support for smb:// URLs
Summary(pl):	Modu³ Gnome-VFS dodaj±cy wsparcie dla URLi smb://
Group:		X11/Applications/Networking
Requires(post,postun):	%{name} = %{epoch}:%{version}-%{release}
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description gnomevfs
Gnome-VFS module providing support for smb:// URLs.

%description gnomevfs -l pl
Modu³ Gnome-VFS dodaj±cy wsparcie dla URLi smb://.

%package calendar
Summary:	SeaMonkey calendar
Summary(pl):	Kalendarz SeaMonkey
Group:		X11/Applications/Networking
Requires(post,postun):	%{name} = %{epoch}:%{version}-%{release}
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description calendar
This package contains the calendar application from the SeaMonkey
suite.

%description calendar -l pl
Ten pakiet zawiera kalendarz z zestawu aplikacji SeaMonkey.

%package devel
Summary:	Headers for developing programs that will use SeaMonkey
Summary(pl):	SeaMonkey - pliki nag³ówkowe i biblioteki
Summary(pt_BR):	Arquivos de inclusão para desenvolvimento de programas que usam o SeaMonkey
Summary(ru):	æÁÊÌÙ, ÎÅÏÂÈÏÄÉÍÙÅ ÄÌÑ ÉÓÐÏÌØÚÏ×ÁÎÉÑ ÐÒÏÇÒÁÍÍ, ×ËÌÀÞÁÀÝÉÈ SeaMonkey
Group:		X11/Development/Libraries
Requires:	%{name} = %{epoch}:%{version}-%{release}
Requires:	nspr-devel >= 1:4.6.1
Provides:	mozilla-embedded-devel = %{epoch}:%{version}-%{release}
Obsoletes:	mozilla-embedded-devel
Obsoletes:	mozilla-firefox-devel

%description devel
SeaMonkey development package.

%description devel -l pl
Biblioteki i pliki nag³ówkowe.

%description devel -l pt_BR
Arquivos de inclusão para desenvolvimento de programas que usam o
SeaMonkey.

%description devel -l ru
úÁÇÏÌÏ×ÏÞÎÙÅ ÆÁÊÌÙ, ÎÅÏÂÈÏÄÉÍÙÅ ÄÌÑ ÒÁÚÒÁÂÏÔËÉ ÐÒÏÇÒÁÍÍ, ÉÓÐÅÏÌØÚÕÀÝÉÈ
SeaMonkey

%prep
%setup -q -c -T
tar jxf %{SOURCE0} --strip-components=1

%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1

%build
BUILD_OFFICIAL="1"; export BUILD_OFFICIAL
MOZILLA_OFFICIAL="1"; export MOZILLA_OFFICIAL

cp -f /usr/share/automake/config.* build/autoconf
cp -f /usr/share/automake/config.* nsprpub/build/autoconf
cp -f /usr/share/automake/config.* directory/c-sdk/config/autoconf
%configure2_13 \
	%{!?debug:--disable-debug} \
	--disable-elf-dynstr-gc \
	--disable-pedantic \
	--disable-tests \
	--enable-application=suite \
	--enable-calendar \
	--enable-crypto \
	--enable-extensions \
	--enable-ldap \
	--enable-mathml \
	--enable-optimize="%{rpmcflags}" \
	--enable-postscript \
	%{!?debug:--enable-strip} \
	%{?with_svg:--enable-svg --enable-svg-renderer-cairo} \
	--enable-default-toolkit=gtk2 \
	%{!?with_gnomevfs:--disable-gnomevfs} \
	--enable-xft \
	--enable-xinerama \
	--enable-xprint \
	--disable-xterm-updates \
	--enable-old-abi-compat-wrappers \
	--with-default-mozilla-five-home=%{_libdir}/%{name} \
	--with-pthreads \
	--with-system-jpeg \
	--with-system-nspr \
	--with-system-png \
	--with-system-zlib \
	--with-x

%if %{with heimdal}
sed -i config/autoconf.mk \
	-e 's/@USE_GSSAPI@/1/; s/@GSSAPI_INCLUDES@//'
%endif

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d \
	$RPM_BUILD_ROOT{%{_bindir},%{_sbindir},%{_datadir}/idl} \
	$RPM_BUILD_ROOT{%{_desktopdir},%{_pixmapsdir}} \
	$RPM_BUILD_ROOT%{_datadir}/%{name}/{chrome,defaults,icons,res,searchplugins,greprefs} \
	$RPM_BUILD_ROOT%{_libdir}/%{name}/{components,plugins} \
	$RPM_BUILD_ROOT{%{_includedir}/%{name},%{_pkgconfigdir}}

# preparing to create register
# remove empty directory trees
rm -fr dist/bin/chrome/{US,chatzilla,classic,comm,content-packs,cview,embed,embed-sample,en-US,en-mac,en-unix,en-win,help,inspector,messenger,modern,pipnss,pippki,toolkit,venkman,xmlterm}
# non-unix
rm -f dist/bin/chrome/en-{mac,win}.jar

# creating and installing register
LD_LIBRARY_PATH="dist/bin" MOZILLA_FIVE_HOME="dist/bin" dist/bin/regxpcom
LD_LIBRARY_PATH="dist/bin" MOZILLA_FIVE_HOME="dist/bin" dist/bin/regchrome
#install dist/bin/component.reg $RPM_BUILD_ROOT%{_libdir}/%{name}

ln -sf ../../share/%{name}/chrome $RPM_BUILD_ROOT%{_chromedir}
ln -sf ../../share/%{name}/defaults $RPM_BUILD_ROOT%{_libdir}/%{name}/defaults
ln -sf ../../share/%{name}/greprefs $RPM_BUILD_ROOT%{_libdir}/%{name}/greprefs
ln -sf ../../share/%{name}/icons $RPM_BUILD_ROOT%{_libdir}/%{name}/icons
ln -sf ../../share/%{name}/res $RPM_BUILD_ROOT%{_libdir}/%{name}/res
ln -sf ../../share/%{name}/searchplugins $RPM_BUILD_ROOT%{_libdir}/%{name}/searchplugins

cp -frL dist/bin/chrome/*	$RPM_BUILD_ROOT%{_datadir}/%{name}/chrome
cp -frL dist/bin/components/*	$RPM_BUILD_ROOT%{_libdir}/%{name}/components
cp -frL dist/bin/defaults/*	$RPM_BUILD_ROOT%{_datadir}/%{name}/defaults
cp -frL dist/bin/res/*		$RPM_BUILD_ROOT%{_datadir}/%{name}/res
cp -frL dist/bin/searchplugins/* $RPM_BUILD_ROOT%{_datadir}/%{name}/searchplugins
cp -frL dist/gre/greprefs/*	$RPM_BUILD_ROOT%{_datadir}/%{name}/greprefs
cp -frL dist/idl/*		$RPM_BUILD_ROOT%{_datadir}/idl
cp -frL dist/include/*		$RPM_BUILD_ROOT%{_includedir}/%{name}
cp -frL dist/public/ldap{,-private} $RPM_BUILD_ROOT%{_includedir}/%{name}

install dist/bin/*.so $RPM_BUILD_ROOT%{_libdir}

ln -s %{_libdir}/libxpcom.so $RPM_BUILD_ROOT%{_libdir}/%{name}/libxpcom.so
ln -s %{_libdir}/libnssckbi.so $RPM_BUILD_ROOT%{_libdir}/%{name}/libnssckbi.so

for f in build/unix/*.pc ; do
	sed -e 's/seamonkey-%{version}/seamonkey/' $f \
		> $RPM_BUILD_ROOT%{_pkgconfigdir}/$(basename $f)
done

sed -e 's,lib/seamonkey-%{version},lib,g;s/seamonkey-%{version}/seamonkey/g' build/unix/seamonkey-gtkmozembed.pc \
		> $RPM_BUILD_ROOT%{_pkgconfigdir}/seamonkey-gtkmozembed.pc

# add includir/dom to Cflags, for openvrml.spec, perhaps others
sed -i -e '/Cflags:/{/{includedir}\/dom/!s,$, -I${includedir}/dom,}' $RPM_BUILD_ROOT%{_pkgconfigdir}/seamonkey-plugin.pc

rm -f $RPM_BUILD_ROOT%{_pkgconfigdir}/seamonkey-nss.pc $RPM_BUILD_ROOT%{_pkgconfigdir}/seamonkey-nspr.pc

install %{SOURCE1} %{SOURCE2} %{SOURCE3} %{SOURCE4} %{SOURCE5} \
	$RPM_BUILD_ROOT%{_desktopdir}

install suite/branding/icons/gtk/seamonkey.png $RPM_BUILD_ROOT%{_pixmapsdir}

install dist/bin/seamonkey-bin $RPM_BUILD_ROOT%{_bindir}
install dist/bin/regchrome $RPM_BUILD_ROOT%{_bindir}
install dist/bin/regxpcom $RPM_BUILD_ROOT%{_bindir}
install dist/bin/xpidl $RPM_BUILD_ROOT%{_bindir}

cp $RPM_BUILD_ROOT%{_chromedir}/installed-chrome.txt \
        $RPM_BUILD_ROOT%{_chromedir}/%{name}-installed-chrome.txt

cat << 'EOF' > $RPM_BUILD_ROOT%{_bindir}/seamonkey
#!/bin/sh
# (c) vip at linux.pl, wolf at pld-linux.org

MOZILLA_FIVE_HOME=%{_libdir}/seamonkey
if [ "$1" == "-remote" ]; then
	%{_bindir}/seamonkey-bin "$@"
else
	PING=`%{_bindir}/seamonkey-bin -remote 'ping()' 2>&1 >/dev/null`
	if [ -n "$PING" ]; then
		if [ -f "`pwd`/$1" ]; then
			%{_bindir}/seamonkey-bin "file://`pwd`/$1"
		else
			%{_bindir}/seamonkey-bin "$@"
		fi
	else
		if [ -z "$1" ]; then
			%{_bindir}/seamonkey-bin -remote 'xfeDoCommand (openBrowser)'
		elif [ "$1" == "-mail" ]; then
			%{_bindir}/seamonkey-bin -remote 'xfeDoCommand (openInbox)'
		elif [ "$1" == "-compose" ]; then
			%{_bindir}/seamonkey-bin -remote 'xfeDoCommand (composeMessage)'
		else
			if [ -f "`pwd`/$1" ]; then
				URL="file://`pwd`/$1"
			else
				URL="$1"
			fi
			grep browser.tabs.opentabfor.middleclick ~/.mozilla/default/*/prefs.js | grep true > /dev/null
			if [ $? -eq 0 ]; then
				%{_bindir}/seamonkey-bin -remote "OpenUrl($URL,new-tab)"
			else
				%{_bindir}/seamonkey-bin -remote "OpenUrl($URL,new-window)"
			fi
		fi
	fi
fi
EOF

cat << 'EOF' > $RPM_BUILD_ROOT%{_sbindir}/%{name}-chrome+xpcom-generate
#!/bin/sh
umask 022
cd %{_datadir}/%{name}/chrome
cat *-installed-chrome.txt > installed-chrome.txt
rm -f chrome.rdf overlays.rdf
rm -f %{_libdir}/%{name}/components/{compreg,xpti}.dat
MOZILLA_FIVE_HOME=%{_libdir}/%{name} %{_bindir}/regxpcom
MOZILLA_FIVE_HOME=%{_libdir}/%{name} %{_bindir}/regchrome
exit 0
EOF

%clean
rm -rf $RPM_BUILD_ROOT

%post
umask 022
%{_sbindir}/%{name}-chrome+xpcom-generate

%postun
if [ "$1" = "1" ]; then
	%{_sbindir}/%{name}-chrome+xpcom-generate
fi

%post	libs -p /sbin/ldconfig
%postun	libs -p /sbin/ldconfig

%post mailnews
/sbin/ldconfig
%{_sbindir}/%{name}-chrome+xpcom-generate

%postun mailnews
/sbin/ldconfig
%{_sbindir}/%{name}-chrome+xpcom-generate

%post chat
%{_sbindir}/%{name}-chrome+xpcom-generate

%postun chat
%{_sbindir}/%{name}-chrome+xpcom-generate

%post js-debugger
%{_sbindir}/%{name}-chrome+xpcom-generate

%postun js-debugger
%{_sbindir}/%{name}-chrome+xpcom-generate

%post dom-inspector
%{_sbindir}/%{name}-chrome+xpcom-generate

%postun dom-inspector
%{_sbindir}/%{name}-chrome+xpcom-generate

%post gnomevfs
%{_sbindir}/%{name}-chrome+xpcom-generate

%postun gnomevfs
%{_sbindir}/%{name}-chrome+xpcom-generate

%post calendar
%{_sbindir}/%{name}-chrome+xpcom-generate

%postun calendar
%{_sbindir}/%{name}-chrome+xpcom-generate

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/seamonkey*
%attr(755,root,root) %{_bindir}/reg*
%attr(744,root,root) %{_sbindir}/%{name}-chrome+xpcom-generate

%dir %{_libdir}/%{name}
%dir %{_chromedir}
%dir %{_libdir}/%{name}/components
%dir %{_libdir}/%{name}/defaults
%dir %{_libdir}/%{name}/greprefs
%dir %{_libdir}/%{name}/icons
%dir %{_libdir}/%{name}/plugins
%dir %{_libdir}/%{name}/res
%dir %{_libdir}/%{name}/searchplugins
%dir %{_datadir}/%{name}

%attr(755,root,root) %{_libdir}/%{name}/libxpcom.so
%attr(755,root,root) %{_libdir}/%{name}/libnssckbi.so

%attr(755,root,root) %{_libdir}/%{name}/components/libaccess*.so
%attr(755,root,root) %{_libdir}/%{name}/components/libappcomps.so
%attr(755,root,root) %{_libdir}/%{name}/components/libauth*.so
%attr(755,root,root) %{_libdir}/%{name}/components/libautoconfig.so
%attr(755,root,root) %{_libdir}/%{name}/components/libcaps.so
%attr(755,root,root) %{_libdir}/%{name}/components/libchrome.so
%attr(755,root,root) %{_libdir}/%{name}/components/libcomposer.so
%attr(755,root,root) %{_libdir}/%{name}/components/libcookie.so
%attr(755,root,root) %{_libdir}/%{name}/components/libdocshell.so
%attr(755,root,root) %{_libdir}/%{name}/components/libeditor.so
%attr(755,root,root) %{_libdir}/%{name}/components/libembedcomponents.so
%attr(755,root,root) %{_libdir}/%{name}/components/libfileview.so
%attr(755,root,root) %{_libdir}/%{name}/components/libgfx*.so
%attr(755,root,root) %{_libdir}/%{name}/components/libgk*.so
%attr(755,root,root) %{_libdir}/%{name}/components/libhtmlpars.so
%attr(755,root,root) %{_libdir}/%{name}/components/libi18n.so
%attr(755,root,root) %{_libdir}/%{name}/components/libimg*.so
%attr(755,root,root) %{_libdir}/%{name}/components/libjar50.so
%attr(755,root,root) %{_libdir}/%{name}/components/libjsd.so
%attr(755,root,root) %{_libdir}/%{name}/components/libmork.so
%attr(755,root,root) %{_libdir}/%{name}/components/libmoz*.so
%attr(755,root,root) %{_libdir}/%{name}/components/libmyspell.so
%attr(755,root,root) %{_libdir}/%{name}/components/libnecko*.so
#%{?with_heimdal:%attr(755,root,root) %{_libdir}/%{name}/components/libnegotiateauth.so}
%attr(755,root,root) %{_libdir}/%{name}/components/libnkdatetime.so
%attr(755,root,root) %{_libdir}/%{name}/components/libnkfinger.so
%attr(755,root,root) %{_libdir}/%{name}/components/libns*.so
%attr(755,root,root) %{_libdir}/%{name}/components/liboji.so
%attr(755,root,root) %{_libdir}/%{name}/components/libp3p.so
%attr(755,root,root) %{_libdir}/%{name}/components/libpipboot.so
%attr(755,root,root) %{_libdir}/%{name}/components/libpipnss.so
%attr(755,root,root) %{_libdir}/%{name}/components/libpippki.so
%attr(755,root,root) %{_libdir}/%{name}/components/libpref.so
%attr(755,root,root) %{_libdir}/%{name}/components/libprofile.so
%attr(755,root,root) %{_libdir}/%{name}/components/librdf.so
%attr(755,root,root) %{_libdir}/%{name}/components/libspellchecker.so
%attr(755,root,root) %{_libdir}/%{name}/components/libtransformiix.so
%attr(755,root,root) %{_libdir}/%{name}/components/libtxmgr.so
%attr(755,root,root) %{_libdir}/%{name}/components/libtypeaheadfind.so
%attr(755,root,root) %{_libdir}/%{name}/components/libuconv.so
%attr(755,root,root) %{_libdir}/%{name}/components/libucv*.so
%attr(755,root,root) %{_libdir}/%{name}/components/libuniversalchardet.so
%attr(755,root,root) %{_libdir}/%{name}/components/libwallet.so
%attr(755,root,root) %{_libdir}/%{name}/components/libwalletviewers.so
%attr(755,root,root) %{_libdir}/%{name}/components/libwebbrwsr.so
%attr(755,root,root) %{_libdir}/%{name}/components/libwebsrvcs.so
%attr(755,root,root) %{_libdir}/%{name}/components/libwidget_gtk2.so
%attr(755,root,root) %{_libdir}/%{name}/components/libx*.so

# needs revision:
%attr(755,root,root) %{_libdir}/%{name}/components/libpermissions.so
%attr(755,root,root) %{_libdir}/%{name}/components/libremoteservice.so
%attr(755,root,root) %{_libdir}/%{name}/components/libschemavalidation.so
%attr(755,root,root) %{_libdir}/%{name}/components/libsearchservice.so
%attr(755,root,root) %{_libdir}/%{name}/components/libsql.so
%attr(755,root,root) %{_libdir}/%{name}/components/libsroaming.so
%attr(755,root,root) %{_libdir}/%{name}/components/libstoragecomps.so
%attr(755,root,root) %{_libdir}/%{name}/components/libwebdav.so

%{_libdir}/%{name}/components/access*.xpt
%{_libdir}/%{name}/components/appshell.xpt
%{_libdir}/%{name}/components/autocomplete.xpt
%{_libdir}/%{name}/components/autoconfig.xpt
%{_libdir}/%{name}/components/bookmarks.xpt
%{_libdir}/%{name}/components/caps.xpt
%{_libdir}/%{name}/components/chardet.xpt
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
%{_libdir}/%{name}/components/exthandler.xpt
%{_libdir}/%{name}/components/find.xpt
%{_libdir}/%{name}/components/filepicker.xpt
%{_libdir}/%{name}/components/gfx*.xpt
%{?with_svg:%{_libdir}/%{name}/components/gksvgrenderer.xpt}
#%{_libdir}/%{name}/components/helperAppDlg.xpt
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
#%{_libdir}/%{name}/components/plugin.xpt
%{_libdir}/%{name}/components/pref.xpt
%{_libdir}/%{name}/components/prefetch.xpt
%{_libdir}/%{name}/components/prefmigr.xpt
%{_libdir}/%{name}/components/profile.xpt
#%{_libdir}/%{name}/components/profilesharingsetup.xpt
%{_libdir}/%{name}/components/progressDlg.xpt
%{_libdir}/%{name}/components/proxyObjInst.xpt
%{_libdir}/%{name}/components/rdf.xpt
%{_libdir}/%{name}/components/related.xpt
%{_libdir}/%{name}/components/search.xpt
%{_libdir}/%{name}/components/shistory.xpt
%{_libdir}/%{name}/components/sidebar.xpt
%{_libdir}/%{name}/components/signonviewer.xpt
%{_libdir}/%{name}/components/spellchecker.xpt
%{_libdir}/%{name}/components/txmgr.xpt
%{_libdir}/%{name}/components/txtsvc.xpt
%{_libdir}/%{name}/components/typeaheadfind.xpt
%{_libdir}/%{name}/components/uconv.xpt
%{_libdir}/%{name}/components/unicharutil.xpt
%{_libdir}/%{name}/components/uriloader.xpt
#%{_libdir}/%{name}/components/urlbarhistory.xpt
%{_libdir}/%{name}/components/wallet*.xpt
%{_libdir}/%{name}/components/webBrowser_core.xpt
%{_libdir}/%{name}/components/webbrowserpersist.xpt
%{_libdir}/%{name}/components/webshell_idls.xpt
%{_libdir}/%{name}/components/websrvcs.xpt
%{_libdir}/%{name}/components/widget.xpt
%{_libdir}/%{name}/components/windowds.xpt
%{_libdir}/%{name}/components/windowwatcher.xpt
%{_libdir}/%{name}/components/x*.xpt

# needs revision:
%{_libdir}/%{name}/components/alerts.xpt
%{_libdir}/%{name}/components/appstartup.xpt
%{_libdir}/%{name}/components/chrome.xpt
%{_libdir}/%{name}/components/extensions.xpt
%{_libdir}/%{name}/components/plugin.xpt
%{_libdir}/%{name}/components/schemavalidation.xpt
%{_libdir}/%{name}/components/sql.xpt
%{_libdir}/%{name}/components/storage.xpt
%{_libdir}/%{name}/components/toolkitremote.xpt
%{_libdir}/%{name}/components/webdav.xpt

# Is this a correct package for these files?
#%{_libdir}/%{name}/components/ipcd.xpt
#%attr(755,root,root) %{_libdir}/%{name}/components/libipcdc.so
%attr(755,root,root) %{_libdir}/%{name}/components/libsystem-pref.so

%{_libdir}/%{name}/components/jsconsole-clhandler.js
%{_libdir}/%{name}/components/nsCloseAllWindows.js
%{_libdir}/%{name}/components/nsDictionary.js
%{_libdir}/%{name}/components/nsDownloadProgressListener.js
%{_libdir}/%{name}/components/nsFilePicker.js
%{_libdir}/%{name}/components/nsHelperAppDlg.js
%{_libdir}/%{name}/components/nsInterfaceInfoToIDL.js
%{_libdir}/%{name}/components/nsKillAll.js
%{_libdir}/%{name}/components/nsProgressDialog.js
%{_libdir}/%{name}/components/nsProxyAutoConfig.js
%{_libdir}/%{name}/components/nsResetPref.js
%{_libdir}/%{name}/components/nsSidebar.js
%{_libdir}/%{name}/components/nsUpdateNotifier.js
%{_libdir}/%{name}/components/nsXmlRpcClient.js

# needs revision:
%{_libdir}/%{name}/components/nsAbLDAPAttributeMap.js
%{_libdir}/%{name}/components/nsComposerCmdLineHandler.js
%{_libdir}/%{name}/components/nsSchemaValidatorRegexp.js
%{_libdir}/%{name}/components/xulappinfo.js

# not *.dat, so check-files can catch any new files
# (and they won't be just silently placed empty in rpm)
%ghost %{_libdir}/%{name}/components/compreg.dat
%ghost %{_libdir}/%{name}/components/xpti.dat

%{_libdir}/%{name}/components/myspell

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
%{_datadir}/%{name}/chrome/tasks.jar
%{_datadir}/%{name}/chrome/toolkit.jar

# needs revision:
%{_datadir}/%{name}/chrome/reporter.jar
%{_datadir}/%{name}/chrome/sql.jar
%{_datadir}/%{name}/chrome/sroaming.jar
%{_datadir}/%{name}/chrome/xforms.jar

%ghost %{_datadir}/%{name}/chrome/chrome.rdf
%ghost %{_datadir}/%{name}/chrome/overlays.rdf
# not generated automatically ?
%{_datadir}/%{name}/chrome/stylesheets.rdf
%{_datadir}/%{name}/chrome/chromelist.txt
%{_datadir}/%{name}/chrome/icons
%exclude %{_datadir}/%{name}/chrome/icons/default/abcardWindow*.xpm
%exclude %{_datadir}/%{name}/chrome/icons/default/addressbookWindow*.xpm
%exclude %{_datadir}/%{name}/chrome/icons/default/calendar-window*.xpm
%exclude %{_datadir}/%{name}/chrome/icons/default/chatzilla-window*.xpm
%exclude %{_datadir}/%{name}/chrome/icons/default/messengerWindow*.xpm
%exclude %{_datadir}/%{name}/chrome/icons/default/msgcomposeWindow*.xpm
%exclude %{_datadir}/%{name}/chrome/icons/default/venkman-window*.xpm
%exclude %{_datadir}/%{name}/chrome/icons/default/winInspectorMain*.xpm

%{_datadir}/%{name}/chrome/%{name}-installed-chrome.txt
%ghost %{_datadir}/%{name}/chrome/installed-chrome.txt

%{_datadir}/%{name}/defaults
%{_datadir}/%{name}/greprefs
%exclude %{_datadir}/%{name}/defaults/pref/inspector.js
%{_datadir}/%{name}/icons
%{_datadir}/%{name}/res
#%exclude %{_datadir}/%{name}/res/inspector
%{_datadir}/%{name}/searchplugins
%{_datadir}/idl/*

%{_pixmapsdir}/seamonkey.png
%{_desktopdir}/%{name}.desktop
%{_desktopdir}/%{name}-composer.desktop
#%{_desktopdir}/mozilla-jconsole.desktop
#%{_desktopdir}/mozilla-terminal.desktop

%files libs
%defattr(644,root,root,755)
# libxpcom.so used by mozillaplug-in
# probably should add more if more packages require
%attr(755,root,root) %{_libdir}/libxpcom.so
%attr(755,root,root) %{_libdir}/libxpcom_compat.so
%attr(755,root,root) %{_libdir}/libxpcom_core.so

# add rest too
%attr(755,root,root) %{_libdir}/libgfxpsshar.so
%attr(755,root,root) %{_libdir}/libgkgfx.so
%attr(755,root,root) %{_libdir}/libgtkembedmoz.so
%attr(755,root,root) %{_libdir}/libgtkxtbin.so
%attr(755,root,root) %{_libdir}/libjsj.so
%attr(755,root,root) %{_libdir}/libldap50.so
%attr(755,root,root) %{_libdir}/libprldap50.so
%attr(755,root,root) %{_libdir}/libssldap50.so
%attr(755,root,root) %{_libdir}/libmozjs.so
##%attr(755,root,root) %{_libdir}/libmoz_art_lgpl.so
%attr(755,root,root) %{_libdir}/libxpistub.so
%attr(755,root,root) %{_libdir}/libxlibrgb.so


%files mailnews
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libmsgbaseutil.so
%attr(755,root,root) %{_libdir}/%{name}/components/libaddrbook.so
%attr(755,root,root) %{_libdir}/%{name}/components/libbayesflt.so
%attr(755,root,root) %{_libdir}/%{name}/components/libimpText.so
%attr(755,root,root) %{_libdir}/%{name}/components/libimpComm4xMail.so
%attr(755,root,root) %{_libdir}/%{name}/components/libimport.so
%attr(755,root,root) %{_libdir}/%{name}/components/liblocalmail.so
%attr(755,root,root) %{_libdir}/%{name}/components/libmailnews.so
%attr(755,root,root) %{_libdir}/%{name}/components/libmailview.so
%attr(755,root,root) %{_libdir}/%{name}/components/libmimeemitter.so
%attr(755,root,root) %{_libdir}/%{name}/components/libmime.so
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
%{_libdir}/%{name}/components/nsLDAPPrefsService.js
%{_libdir}/%{name}/components/offlineStartup.js
%{_libdir}/%{name}/components/smime-service.js

%{_datadir}/%{name}/chrome/messenger.jar

%{_datadir}/%{name}/chrome/icons/default/abcardWindow*.xpm
%{_datadir}/%{name}/chrome/icons/default/addressbookWindow*.xpm
%{_datadir}/%{name}/chrome/icons/default/messengerWindow*.xpm
%{_datadir}/%{name}/chrome/icons/default/msgcomposeWindow*.xpm

%{_desktopdir}/%{name}-mail.desktop

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
%attr(755,root,root) %{_libdir}/%{name}/components/libinspector.so
%{_libdir}/%{name}/components/inspector.xpt
%{_libdir}/%{name}/components/inspector-cmdline.js
%{_datadir}/%{name}/chrome/inspector.jar
%{_datadir}/%{name}/chrome/icons/default/winInspectorMain*.xpm
%{_datadir}/%{name}/defaults/pref/inspector.js
#%{_datadir}/%{name}/res/inspector

%if %{with gnomevfs}
%files gnomevfs
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/%{name}/components/libnkgnomevfs.so
%endif

%files calendar
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/%{name}/components/libcalbasecomps.so
%{_libdir}/%{name}/components/calbase.xpt
%{_libdir}/%{name}/components/calbaseinternal.xpt
%{_libdir}/%{name}/components/calendarService.js
%{_libdir}/%{name}/components/cal[ACDEHIMORST]*.js
%{_datadir}/%{name}/chrome/calendar.jar
%{_datadir}/%{name}/chrome/icons/default/calendar-window*.xpm

%files devel
%defattr(644,root,root,755)
%{_includedir}/%{name}
%{_pkgconfigdir}/*
%attr(755,root,root) %{_bindir}/xpidl
