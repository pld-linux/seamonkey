#
# Conditional build:
%bcond_without	gnomevfs	# disable GnomeVFS support
%bcond_with	gnomeui		# enable GnomeUI
%bcond_without	svg		# disable svg support
#
%define	_enigmail_ver	0.94.0
Summary:	SeaMonkey - web browser
Summary(es):	Navegador de Internet SeaMonkey
Summary(pl):	SeaMonkey - przegl±darka WWW
Summary(pt_BR):	Navegador SeaMonkey
Name:		seamonkey
Version:	1.0.2
Release:	1
License:	Mozilla Public License
Group:		X11/Applications/Networking
Source0:	http://ftp.mozilla.org/pub/mozilla.org/seamonkey/releases/%{version}/%{name}-source-%{version}.tar.bz2
# Source0-md5:	967e0441183492b0ade4ab2a394deb71
Source1:	http://www.mozilla-enigmail.org/downloads/src/enigmail-%{_enigmail_ver}.tar.gz
# Source1-md5:	d326c302c1d2d68217fffcaa01ca7632
Source2:	%{name}.desktop
Source3:	%{name}-composer.desktop
Source4:	%{name}-chat.desktop
Source5:	%{name}-mail.desktop
Source6:	%{name}-venkman.desktop
Patch0:		%{name}-pld-homepage.patch
Patch1:		%{name}-nss.patch
Patch2:		%{name}-ldap-with-nss.patch
Patch3:		%{name}-kill_slim_hidden_def.patch
Patch4:		%{name}-lib_path.patch
URL:		http://www.mozilla.org/projects/seamonkey/
BuildRequires:	/bin/csh
BuildRequires:	/bin/ex
BuildRequires:	automake
%{?with_svg:BuildRequires:	cairo-devel >= 1.0.0}
BuildRequires:	freetype-devel >= 1:2.1.8
%{?with_gnomevfs:BuildRequires:	gnome-vfs2-devel >= 2.0.0}
BuildRequires:	gtk+2-devel
%{?with_gnomeui:BuildRequires:	libgnomeui-devel >= 2.0}
BuildRequires:	libjpeg-devel >= 6b
BuildRequires:	libpng-devel >= 1.2.7
BuildRequires:	libstdc++-devel
BuildRequires:	nspr-devel >= 1:4.6.1
BuildRequires:	nss-devel >= 3.10.2
BuildRequires:	perl-modules >= 5.6.0
BuildRequires:	pkgconfig
BuildRequires:	sed >= 4.0
BuildRequires:	tar >= 1:1.15.1
BuildRequires:	xorg-lib-libXcursor-devel
BuildRequires:	xorg-lib-libXft-devel >= 2.1-2
BuildRequires:	zip >= 2.1
BuildRequires:	zlib-devel >= 1.2.3
Requires(post,postun):	/sbin/ldconfig
Requires(post,postun):	%{name}-libs = %{epoch}:%{version}-%{release}
Requires:	%{name}-libs = %{epoch}:%{version}-%{release}
%{?with_svg:Requires:	cairo >= 1.0.0}
Requires:	nspr >= 1:4.6.1
Requires:	nss >= 3.10.2
Provides:	seamonkey-embedded = %{epoch}:%{version}-%{release}
Provides:	wwwbrowser
Obsoletes:	light
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		specflags	-fno-strict-aliasing

%define		_seamonkeydir	%{_libdir}/%{name}
%define		_chromedir	%{_libdir}/%{name}/chrome
# seamonkey, mozilla and firefox provide their own versions
%define		_noautoreqdep	libgfxpsshar.so libgkgfx.so libgtkembedmoz.so libgtkxtbin.so libjsj.so libldap50.so libmozjs.so libprldap50.so libssldap50.so libxlibrgb.so libxpcom.so libxpcom_compat.so libxpcom_core.so libxpistub.so

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

%description mailnews
Programs for mail and news integrated with browser.

%description mailnews -l pl
Programy pocztowe i obs³uga newsów zintegrowane z przegl±dark±.

%description mailnews -l ru
ëÌÉÅÎÔ ÐÏÞÔÙ É ÎÏ×ÏÓÔÅÊ, ÎÁ ÏÓÎÏ×Å SeaMonkey. ðÏÄÄÅÒÖÉ×ÁÅÔ IMAP, POP É
NNTP É ÉÍÅÅÔ ÐÒÏÓÔÏÊ ÉÎÔÅÒÆÅÊÓ ÐÏÌØÚÏ×ÁÔÅÌÑ.

%package addon-enigmail
Summary:	Enigmail %{_enigmail_ver} - PGP/GPG support for SeaMonkey
Summary(pl):	Enigmail %{_enigmail_ver} - obs³uga PGP/GPG dla SeaMonkey
Group:		X11/Applications/Networking
Requires(post,postun):	%{name}-mailnews = %{epoch}:%{version}-%{release}
Requires(post,postun):	/sbin/ldconfig
Requires:	%{name}-mailnews = %{epoch}:%{version}-%{release}
Requires:	gnupg >= 1.4.2.2

%description addon-enigmail
Enigmail is an extension to the mail client of SeaMonkey / Mozilla /
Netscape and Mozilla Thunderbird which allows users to access the
authentication and encryption features provided by GnuPG.

%description addon-enigmail -l pl
Enigmail jest rozszerzeniem dla klienta pocztowego SeaMonkey, Mozilla
i Mozilla Thunderdbird pozwalaj±cym u¿ytkownikowi korzystaæ z
funkcjonalno¶ci GnuPG.

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
Provides:	seamonkey-embedded-devel = %{epoch}:%{version}-%{release}
Obsoletes:	mozilla-devel
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
tar -C mailnews/extensions -zxf %{SOURCE1}

%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1

%build
BUILD_OFFICIAL="1"; export BUILD_OFFICIAL
MOZILLA_OFFICIAL="1"; export MOZILLA_OFFICIAL

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
	--enable-calendar \
	--enable-crypto \
	--enable-default-toolkit=gtk2 \
	--enable-extensions \
	--enable-ldap \
	--enable-mathml \
	--enable-optimize="%{rpmcflags}" \
	--enable-postscript \
	%{!?debug:--enable-strip} \
	%{?with_svg:--enable-svg --enable-svg-renderer-cairo} \
	--enable-xft \
	--enable-xinerama \
	--enable-xprint \
	--enable-old-abi-compat-wrappers \
	--with-default-mozilla-five-home=%{_seamonkeydir} \
	--with-pthreads \
	--with-system-jpeg \
	--with-system-nspr \
	--with-system-png \
	--with-system-zlib \
	--with-x

%{__make}

cd mailnews/extensions/enigmail
sed 's/"mozilla"/"%{name}-%{version}"/g' -i makemake
./makemake -r
%{__make}
cd ../../..

%install
rm -rf $RPM_BUILD_ROOT
install -d \
	$RPM_BUILD_ROOT{%{_bindir},%{_sbindir},%{_datadir}} \
	$RPM_BUILD_ROOT{%{_desktopdir},%{_pixmapsdir}} \
	$RPM_BUILD_ROOT%{_datadir}/%{name}/{chrome,defaults,icons,greprefs,myspell,res,searchplugins} \
	$RPM_BUILD_ROOT%{_seamonkeydir}/{components,plugins} \
	$RPM_BUILD_ROOT{%{_includedir}/%{name}/idl,%{_pkgconfigdir}}

# preparing to create register
# remove empty directory trees
rm -fr dist/bin/chrome/{US,chatzilla,classic,comm,content-packs,cview,embed,embed-sample,en-US,en-mac,en-unix,en-win,help,inspector,messenger,modern,pipnss,pippki,toolkit,venkman,xmlterm}
# non-unix
rm -f dist/bin/chrome/en-{mac,win}.jar

# creating and installing register
LD_LIBRARY_PATH="dist/bin" MOZILLA_FIVE_HOME="dist/bin" dist/bin/regxpcom
LD_LIBRARY_PATH="dist/bin" MOZILLA_FIVE_HOME="dist/bin" dist/bin/regchrome
#install dist/bin/component.reg $RPM_BUILD_ROOT%{_seamonkeydir}

ln -sf ../../share/%{name}/chrome $RPM_BUILD_ROOT%{_chromedir}
ln -sf ../../share/%{name}/defaults $RPM_BUILD_ROOT%{_seamonkeydir}/defaults
ln -sf ../../share/%{name}/greprefs $RPM_BUILD_ROOT%{_seamonkeydir}/greprefs
ln -sf ../../share/%{name}/icons $RPM_BUILD_ROOT%{_seamonkeydir}/icons
ln -sf ../../share/%{name}/res $RPM_BUILD_ROOT%{_seamonkeydir}/res
ln -sf ../../share/%{name}/searchplugins $RPM_BUILD_ROOT%{_seamonkeydir}/searchplugins
ln -sf ../../../share/%{name}/myspell $RPM_BUILD_ROOT%{_seamonkeydir}/components/myspell

cp -frL dist/bin/chrome/*	$RPM_BUILD_ROOT%{_datadir}/%{name}/chrome
cp -frL dist/bin/components/{[!m],m[!y]}*	$RPM_BUILD_ROOT%{_seamonkeydir}/components
cp -frL dist/bin/components/myspell/*	$RPM_BUILD_ROOT%{_datadir}/%{name}/myspell
cp -frL dist/bin/defaults/*	$RPM_BUILD_ROOT%{_datadir}/%{name}/defaults
cp -frL dist/bin/res/*		$RPM_BUILD_ROOT%{_datadir}/%{name}/res
cp -frL dist/bin/searchplugins/* $RPM_BUILD_ROOT%{_datadir}/%{name}/searchplugins
cp -frL dist/gre/greprefs/*	$RPM_BUILD_ROOT%{_datadir}/%{name}/greprefs
cp -frL dist/idl/*		$RPM_BUILD_ROOT%{_includedir}/%{name}/idl
cp -frL dist/include/*		$RPM_BUILD_ROOT%{_includedir}/%{name}
cp -frL dist/public/ldap{,-private} $RPM_BUILD_ROOT%{_includedir}/%{name}

install dist/bin/*.so $RPM_BUILD_ROOT%{_seamonkeydir}

ln -s %{_libdir}/libnssckbi.so $RPM_BUILD_ROOT%{_seamonkeydir}/libnssckbi.so

for f in build/unix/*.pc ; do
	sed -e 's/seamonkey-%{version}/seamonkey/' $f \
		> $RPM_BUILD_ROOT%{_pkgconfigdir}/$(basename $f)
done

sed -e 's,lib/seamonkey-%{version},lib,g;s/seamonkey-%{version}/seamonkey/g' build/unix/seamonkey-gtkmozembed.pc \
		> $RPM_BUILD_ROOT%{_pkgconfigdir}/seamonkey-gtkmozembed.pc

# add includir/dom to Cflags, for openvrml.spec, perhaps others
sed -i -e '/Cflags:/{/{includedir}\/dom/!s,$, -I${includedir}/dom,}' $RPM_BUILD_ROOT%{_pkgconfigdir}/seamonkey-plugin.pc

rm -f $RPM_BUILD_ROOT%{_pkgconfigdir}/seamonkey-nss.pc $RPM_BUILD_ROOT%{_pkgconfigdir}/seamonkey-nspr.pc

install %{SOURCE2} %{SOURCE3} %{SOURCE4} %{SOURCE5} %{SOURCE6} \
	$RPM_BUILD_ROOT%{_desktopdir}

install suite/branding/icons/gtk/seamonkey.png $RPM_BUILD_ROOT%{_pixmapsdir}

install dist/bin/seamonkey-bin $RPM_BUILD_ROOT%{_seamonkeydir}
install dist/bin/regchrome $RPM_BUILD_ROOT%{_seamonkeydir}
install dist/bin/regxpcom $RPM_BUILD_ROOT%{_seamonkeydir}
install dist/bin/xpidl $RPM_BUILD_ROOT%{_seamonkeydir}
install dist/bin/regchrome $RPM_BUILD_ROOT%{_bindir}
install dist/bin/regxpcom $RPM_BUILD_ROOT%{_bindir}
install dist/bin/xpidl $RPM_BUILD_ROOT%{_bindir}

cp $RPM_BUILD_ROOT%{_chromedir}/installed-chrome.txt \
        $RPM_BUILD_ROOT%{_chromedir}/%{name}-installed-chrome.txt

cat << 'EOF' > $RPM_BUILD_ROOT%{_bindir}/seamonkey
#!/bin/sh
# (c) vip at linux.pl, wolf at pld-linux.org

LD_LIBRARY_PATH=%{_seamonkeydir}${LD_LIBRARY_PATH:+:$LD_LIBRARY_PATH}
export LD_LIBRARY_PATH

MOZILLA_FIVE_HOME=%{_seamonkeydir}
if [ "$1" == "-remote" ]; then
	%{_seamonkeydir}/seamonkey-bin "$@"
else
	PING=`%{_seamonkeydir}/seamonkey-bin -remote 'ping()' 2>&1 >/dev/null`
	if [ -n "$PING" ]; then
		if [ -f "`pwd`/$1" ]; then
			%{_seamonkeydir}/seamonkey-bin "file://`pwd`/$1"
		else
			%{_seamonkeydir}/seamonkey-bin "$@"
		fi
	else
		if [ -z "$1" ]; then
			%{_seamonkeydir}/seamonkey-bin -remote 'xfeDoCommand (openBrowser)'
		elif [ "$1" == "-mail" ]; then
			%{_seamonkeydir}/seamonkey-bin -remote 'xfeDoCommand (openInbox)'
		elif [ "$1" == "-compose" ]; then
			%{_seamonkeydir}/seamonkey-bin -remote 'xfeDoCommand (composeMessage)'
		else
			echo $1 | grep -q "^-" > /dev/null
			if [ $? -eq 0 ]; then
				%{_seamonkeydir}/seamonkey-bin "$@"
			else
				if [ -f "`pwd`/$1" ]; then
					URL="file://`pwd`/$1"
				else
					URL="$1"
				fi
				grep browser.tabs.opentabfor.middleclick ~/.mozilla/default/*/prefs.js | grep true > /dev/null
				if [ $? -eq 0 ]; then
					%{_seamonkeydir}/seamonkey-bin -remote "OpenUrl($URL,new-tab)"
				else
					%{_seamonkeydir}/seamonkey-bin -remote "OpenUrl($URL,new-window)"
				fi
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
rm -f %{_seamonkeydir}/components/{compreg,xpti}.dat

LD_LIBRARY_PATH=%{_seamonkeydir}${LD_LIBRARY_PATH:+:$LD_LIBRARY_PATH}
export LD_LIBRARY_PATH

MOZILLA_FIVE_HOME=%{_seamonkeydir} %{_seamonkeydir}/regxpcom
MOZILLA_FIVE_HOME=%{_seamonkeydir} %{_seamonkeydir}/regchrome
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

%post addon-enigmail
%{_sbindir}/%{name}-chrome+xpcom-generate

%postun addon-enigmail
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
%attr(755,root,root) %{_bindir}/seamonkey
%attr(744,root,root) %{_sbindir}/%{name}-chrome+xpcom-generate

%dir %{_chromedir}
%dir %{_seamonkeydir}/components
%dir %{_seamonkeydir}/defaults
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
%attr(755,root,root) %{_seamonkeydir}/components/libwebdav.so
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
%{_seamonkeydir}/components/search.xpt
%{_seamonkeydir}/components/schemavalidation.xpt
%{_seamonkeydir}/components/shistory.xpt
%{_seamonkeydir}/components/sidebar.xpt
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
%{_seamonkeydir}/components/wallet*.xpt
%{_seamonkeydir}/components/webBrowser_core.xpt
%{_seamonkeydir}/components/webbrowserpersist.xpt
%{_seamonkeydir}/components/webdav.xpt
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
%{_seamonkeydir}/components/nsXmlRpcClient.js
%{_seamonkeydir}/components/xulappinfo.js

# not *.dat, so check-files can catch any new files
# (and they won't be just silently placed empty in rpm)
%ghost %{_seamonkeydir}/components/compreg.dat
%ghost %{_seamonkeydir}/components/xpti.dat

%{_seamonkeydir}/components/myspell

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
%{_datadir}/%{name}/myspell
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
%attr(755,root,root) %{_seamonkeydir}/components/libinspector.so
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

%files calendar
%defattr(644,root,root,755)
%attr(755,root,root) %{_seamonkeydir}/components/libcalbasecomps.so
%{_seamonkeydir}/components/calbase.xpt
%{_seamonkeydir}/components/calbaseinternal.xpt
%{_seamonkeydir}/components/calendarService.js
%{_seamonkeydir}/components/cal[ACDEHIMORST]*.js
%{_datadir}/%{name}/chrome/calendar.jar
%{_datadir}/%{name}/chrome/icons/default/calendar-window*.xpm

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/reg*
%attr(755,root,root) %{_bindir}/xpidl
%{_includedir}/%{name}
%{_pkgconfigdir}/*
