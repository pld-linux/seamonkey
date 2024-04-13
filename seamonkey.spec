# TODO:
# - consider --enable-libproxy
# - do something with *.rdf file, there if file conflict with other lang packages
#
# Conditional build:
%bcond_without	kerberos	# krb5 support
%bcond_without	lightning	# Lightning calendar
%bcond_without	gold		# gold linker
%bcond_with	crashreporter	# report crashes to crash-stats.mozilla.com
%bcond_with	system_cairo	# build with system cairo (not supported in 2.53.9+)
%bcond_with	tests		# enable tests (whatever they check)
%bcond_with	lowmem		# lower memory requirements

%ifarch %{ix86} %{arm} aarch64
%define		with_lowmem	1
%endif
%ifarch %{ix86}
# /usr/bin/ld.gold: internal error in relocate_section, at i386.cc:3683 (seamonkey 2.53.9, binutils 2.37-1)
%undefine	with_gold
%endif

%define		nspr_ver	4.32
%define		nss_ver		3.90

# UPDATING TRANSALTIONS:
%if 0
rm -vf *.xpi
./builder -g
V=2.49.5
U=https://releases.mozilla.org/pub/mozilla.org/seamonkey/releases/$V/langpacks/linux-i686/
curl -s $U | sed -ne 's,.*href="\([^"]\+\)/".*,'"$U"'xpi/\1.xpi,p'
%endif

Summary:	SeaMonkey Community Edition - web browser
Summary(es.UTF-8):	Navegador de Internet SeaMonkey Community Edition
Summary(pl.UTF-8):	SeaMonkey Community Edition - przeglądarka WWW
Summary(pt_BR.UTF-8):	Navegador SeaMonkey Community Edition
Name:		seamonkey
Version:	2.53.18
Release:	1
License:	MPL v2.0
Group:		X11/Applications/Networking
Source0:	https://releases.mozilla.org/pub/seamonkey/releases/%{version}/source/%{name}-%{version}.source.tar.xz
# Source0-md5:	6ac064816caa2c3fe6bc1f130bd9599b
Source4:	%{name}.desktop
Source5:	%{name}-composer.desktop
Source7:	%{name}-mail.desktop
Source9:	%{name}.sh
Source100:	https://releases.mozilla.org/pub/seamonkey/releases/%{version}/langpack/seamonkey-%{version}.cs.langpack.xpi
# Source100-md5:	9c8bac37197299450f9f0640d36513ff
Source101:	https://releases.mozilla.org/pub/seamonkey/releases/%{version}/langpack/seamonkey-%{version}.de.langpack.xpi
# Source101-md5:	67de9240a5f47d08a3aa0e05b84ae2fd
Source102:	https://releases.mozilla.org/pub/seamonkey/releases/%{version}/langpack/seamonkey-%{version}.el.langpack.xpi
# Source102-md5:	a6dd39b888a42261475b29d5b9c2afc3
Source103:	https://releases.mozilla.org/pub/seamonkey/releases/%{version}/langpack/seamonkey-%{version}.en-GB.langpack.xpi
# Source103-md5:	58cfb46eae8cfced94b429817b30dec1
Source104:	https://releases.mozilla.org/pub/seamonkey/releases/%{version}/langpack/seamonkey-%{version}.en-US.langpack.xpi
# Source104-md5:	0170a5f8e4314bed6fce4ec42b1a6676
Source105:	https://releases.mozilla.org/pub/seamonkey/releases/%{version}/langpack/seamonkey-%{version}.es-AR.langpack.xpi
# Source105-md5:	a9137c2d369d80e4da5d706e838b0b90
Source106:	https://releases.mozilla.org/pub/seamonkey/releases/%{version}/langpack/seamonkey-%{version}.es-ES.langpack.xpi
# Source106-md5:	b86936b85c43986f601fe105f1a128ee
Source107:	https://releases.mozilla.org/pub/seamonkey/releases/%{version}/langpack/seamonkey-%{version}.fi.langpack.xpi
# Source107-md5:	c197113dbca44a23e90666245f20cff0
Source108:	https://releases.mozilla.org/pub/seamonkey/releases/%{version}/langpack/seamonkey-%{version}.fr.langpack.xpi
# Source108-md5:	4ee5600b2dc983a080f3208c7a4389a7
Source109:	https://releases.mozilla.org/pub/seamonkey/releases/%{version}/langpack/seamonkey-%{version}.hu.langpack.xpi
# Source109-md5:	16775c3d1099c76d293944f8a618b930
Source110:	https://releases.mozilla.org/pub/seamonkey/releases/%{version}/langpack/seamonkey-%{version}.it.langpack.xpi
# Source110-md5:	73ffd5f16cb42c5c2e175dad98f5c36b
Source111:	https://releases.mozilla.org/pub/seamonkey/releases/%{version}/langpack/seamonkey-%{version}.ja.langpack.xpi
# Source111-md5:	790f607d8686041649cb6d25a16c6665
Source112:	https://releases.mozilla.org/pub/seamonkey/releases/%{version}/langpack/seamonkey-%{version}.ka.langpack.xpi
# Source112-md5:	d1e7a96d2ad0198fd8502fcd6b2ad6e4
Source113:	https://releases.mozilla.org/pub/seamonkey/releases/%{version}/langpack/seamonkey-%{version}.nb-NO.langpack.xpi
# Source113-md5:	d73a43b445dbd904ce34e109cc1eb7c9
Source114:	https://releases.mozilla.org/pub/seamonkey/releases/%{version}/langpack/seamonkey-%{version}.nl.langpack.xpi
# Source114-md5:	8582b43803cc7ff38883aab7165b33ce
Source115:	https://releases.mozilla.org/pub/seamonkey/releases/%{version}/langpack/seamonkey-%{version}.pl.langpack.xpi
# Source115-md5:	e125bbf76efa67d1afd495a808844351
Source116:	https://releases.mozilla.org/pub/seamonkey/releases/%{version}/langpack/seamonkey-%{version}.pt-BR.langpack.xpi
# Source116-md5:	f28564c0d3f34eec08141f3d8eb38c2a
Source117:	https://releases.mozilla.org/pub/seamonkey/releases/%{version}/langpack/seamonkey-%{version}.pt-PT.langpack.xpi
# Source117-md5:	b92809004b73904985e295e9d519d73b
Source118:	https://releases.mozilla.org/pub/seamonkey/releases/%{version}/langpack/seamonkey-%{version}.ru.langpack.xpi
# Source118-md5:	91bbde04e7b9897bdc70e21c3fb49216
Source119:	https://releases.mozilla.org/pub/seamonkey/releases/%{version}/langpack/seamonkey-%{version}.sk.langpack.xpi
# Source119-md5:	3cd03d5b6866f15cf559113c3788fbcf
Source120:	https://releases.mozilla.org/pub/seamonkey/releases/%{version}/langpack/seamonkey-%{version}.sv-SE.langpack.xpi
# Source120-md5:	b16a9aafa2ebcbe2907de735b43f1eff
Source121:	https://releases.mozilla.org/pub/seamonkey/releases/%{version}/langpack/seamonkey-%{version}.zh-CN.langpack.xpi
# Source121-md5:	ecbc19c599e637ec1ed0c5b9bed135db
Source122:	https://releases.mozilla.org/pub/seamonkey/releases/%{version}/langpack/seamonkey-%{version}.zh-TW.langpack.xpi
# Source122-md5:	5020c2761abdaf2704adee3ea773d5ee
Patch1:		%{name}-mozilla-revert-1332139.patch
Patch2:		%{name}-pld-branding.patch
Patch3:		%{name}-enable-addons.patch
# Edit patch below and restore --system-site-packages when system virtualenv gets 1.7 upgrade
Patch4:		%{name}-system-virtualenv.patch
Patch7:		glibc-double.patch
URL:		https://www.seamonkey-project.org/
BuildRequires:	GConf2-devel >= 1.2.1
BuildRequires:	autoconf2_13 >= 2.13
%{?with_system_cairo:BuildRequires:	cairo-devel >= 1.10.2-5}
BuildRequires:	cargo
BuildRequires:	dbus-devel >= 0.60
BuildRequires:	dbus-glib-devel >= 0.60
BuildRequires:	fontconfig-devel >= 1:2.7.0
# pkgconfig(freetype2) >= 9.10.3
BuildRequires:	freetype-devel >= 1:2.2.1
BuildRequires:	glib2-devel >= 1:2.22
BuildRequires:	gn
BuildRequires:	gtk+3-devel >= 3.4.0
%{?with_kerberos:BuildRequires:	heimdal-devel >= 0.7.1}
# DECnet (dnprogs.spec), not dummy net (libdnet.spec)
#BuildRequires:	libdnet-devel
BuildRequires:	libevent-devel >= 1.4.7
# standalone libffi 3.0.9 or gcc's from 4.5(?)+
BuildRequires:	libffi-devel >= 6:3.0.9
BuildRequires:	libicu-devel >= 67.1
# requires libjpeg-turbo implementing at least libjpeg 6b API
BuildRequires:	libjpeg-devel >= 6b
BuildRequires:	libjpeg-turbo-devel
BuildRequires:	libnotify-devel >= 0.4
BuildRequires:	libpng(APNG)-devel >= 0.10
BuildRequires:	libpng-devel >= 2:1.6.35
BuildRequires:	libstdc++-devel >= 6:4.7
BuildRequires:	libvpx-devel >= 1.5.0
BuildRequires:	nodejs >= 8.11.0
BuildRequires:	nspr-devel >= 1:%{nspr_ver}
BuildRequires:	nss-devel >= 1:%{nss_ver}
BuildRequires:	pango-devel >= 1:1.22.0
BuildRequires:	perl-base >= 1:5.6
BuildRequires:	perl-modules >= 5.004
BuildRequires:	pixman-devel >= 0.19.2
BuildRequires:	pkgconfig
BuildRequires:	python >= 1:2.7.3
BuildRequires:	python-modules >= 1:2.7.3
BuildRequires:	python-virtualenv >= 15
BuildRequires:	python3 >= 1:3.5.0
BuildRequires:	rpm-build >= 4.6
BuildRequires:	rpmbuild(macros) >= 1.601
BuildRequires:	rust >= 1.47.0
BuildRequires:	rust-cbindgen
BuildRequires:	sed >= 4.0
BuildRequires:	startup-notification-devel >= 0.8
BuildRequires:	tar >= 1:1.22
BuildRequires:	xorg-lib-libX11-devel
BuildRequires:	xorg-lib-libXcomposite-devel
BuildRequires:	xorg-lib-libXdamage-devel
BuildRequires:	xorg-lib-libXext-devel
BuildRequires:	xorg-lib-libXfixes-devel
BuildRequires:	xorg-lib-libXt-devel
BuildRequires:	xz
%ifarch %{ix86} %{x8664}
BuildRequires:	yasm >= 1.0.1
%endif
BuildRequires:	zip
BuildRequires:	zlib-devel >= 1.2.3
Requires(post):	mktemp >= 1.5-18
Requires:	desktop-file-utils
Requires:	fontconfig >= 1:2.7.0
Requires:	hicolor-icon-theme
Requires:	browser-plugins >= 2.0
%{?with_system_cairo:Requires:	cairo >= 1.10.2-5}
Requires:	dbus-glib >= 0.60
Requires:	glib2 >= 1:2.22
Requires:	gtk+3 >= 3.4.0
Requires:	libjpeg-turbo
Requires:	libpng >= 2:1.6.35
Requires:	libpng(APNG) >= 0.10
Requires:	libvpx >= 1.5.0
Requires:	myspell-common
Requires:	nspr >= 1:%{nspr_ver}
Requires:	nss >= 1:%{nss_ver}
Requires:	pango >= 1:1.22.0
Requires:	pixman >= 0.19.2
Requires:	startup-notification >= 0.8
Provides:	seamonkey-embedded = %{version}-%{release}
Provides:	wwwbrowser
Obsoletes:	iceape < 2.47
Obsoletes:	iceape-js-debugger < 2.40
Obsoletes:	iceape-lang-be < 2.47
Obsoletes:	iceape-lang-ca < 2.47
Obsoletes:	iceape-lang-gl < 2.47
Obsoletes:	iceape-lang-lt < 2.47
Obsoletes:	iceape-lang-tr < 2.47
Obsoletes:	iceape-lang-uk < 2.47
Obsoletes:	iceape-mailnews < 2.9
Obsoletes:	iceape-gnomevfs < 2.9
Obsoletes:	light < 1.4.13
Obsoletes:	mozilla < 1.8
Obsoletes:	mozilla-gnomevfs < 1.8
Obsoletes:	mozilla-js-debugger < 1.8
Obsoletes:	mozilla-mailnews < 1.8
Obsoletes:	seamonkey-calendar < 1.1
Obsoletes:	seamonkey-js-debugger < 2.31
Obsoletes:	seamonkey-lang-be < 2.47
Obsoletes:	seamonkey-lang-ca < 2.47
Obsoletes:	seamonkey-lang-gl < 2.47
Obsoletes:	seamonkey-lang-lt < 2.53
Obsoletes:	seamonkey-lang-tr < 2.47
Obsoletes:	seamonkey-lang-uk < 2.47
Obsoletes:	seamonkey-libs < 1.1.8-2
Obsoletes:	seamonkey-mailnews < 2.9.1
Obsoletes:	seamonkey-gnomevfs < 2.9.1
Conflicts:	seamonkey-lang-resources < %{version}
# TODO: change to supported archs list
ExcludeArch:	x32
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		topdir		%{_builddir}/%{name}-%{version}
%define		objdir		%{topdir}/obj-%{_target_cpu}

%define		filterout_cpp	-D_FORTIFY_SOURCE=[0-9]+

# don't satisfy other packages
%define		_noautoprovfiles	%{_libdir}/%{name}
# and as we don't provide them, don't require either
%define		_noautoreq	liblgpllibs.so libmozavcodec.so libmozavutil.so libmozgtk.so libmozsandbox.so libmozsqlite3.so libxul.so

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

%package addon-lightning
Summary:	An integrated calendar for SeaMonkey
Summary(pl.UTF-8):	Zintegrowany kalendarz dla SeaMonkey
Group:		Applications/Networking
Requires:	%{name} = %{version}-%{release}
Obsoletes:	iceape-addon-lightning < 2.46

%description addon-lightning
Lightning is an calendar extension to Icedove email client.

%description addon-lightning -l pl.UTF-8
Lightning to rozszerzenie do klienta poczty Icedove dodające
funkcjonalność kalendarza.

%package chat
Summary:	SeaMonkey Community Edition Chat - integrated IRC client
Summary(pl.UTF-8):	SeaMonkey Community Edition Chat - zintegrowany klient IRC-a
Group:		X11/Applications/Networking
Requires(post,postun):	%{name} = %{version}-%{release}
Requires:	%{name} = %{version}-%{release}
Obsoletes:	iceape-chat < 2.46
Obsoletes:	mozilla-chat < 1.8

%description chat
SeaMonkey Community Edition Chat - IRC client that is integrated with
the SeaMonkey Community Edition web browser.

%description chat -l pl.UTF-8
SeaMonkey Community Edition Chat - klient IRC-a zintegrowany z
przeglądarką SeaMonkey Community Edition.

%package dom-inspector
Summary:	A tool for inspecting the DOM of pages in SeaMonkey Community Edition
Summary(pl.UTF-8):	Narzędzie do oglądania DOM stron w SeaMonkey Community Edition
Group:		X11/Applications/Networking
Requires(post,postun):	%{name} = %{version}-%{release}
Requires:	%{name} = %{version}-%{release}
Obsoletes:	iceape-dom-inspector < 2.46
Obsoletes:	mozilla-dom-inspector < 1.8

%description dom-inspector
This is a tool that allows you to inspect the DOM for web pages in
SeaMonkey Community Edition. This is of great use to people who are
doing SeaMonkey Community Edition chrome development or web page
development.

%description dom-inspector -l pl.UTF-8
To narzędzie pozwala na oglądanie DOM dla stron WWW w SeaMonkey
Community Edition. Jest bardzo przydatne dla ludzi rozwijających
chrome w SeaMonkey Community Edition lub tworzących strony WWW.

%package lang-cs
Summary:	Czech resources for SeaMonkey
Summary(pl.UTF-8):	Czeskie pliki językowe dla SeaMonkeya
Group:		I18n
Requires:	seamonkey >= %{version}
Provides:	seamonkey-lang-resources = %{version}
Obsoletes:	iceape-lang-cs < 2.47
BuildArch:	noarch

%description lang-cs
Czech resources for SeaMonkey.

%description lang-cs -l pl.UTF-8
Czeskie pliki językowe dla SeaMonkeya.

%package lang-de
Summary:	German resources for SeaMonkey
Summary(pl.UTF-8):	Niemieckie pliki językowe dla SeaMonkeya
Group:		I18n
Requires:	seamonkey >= %{version}
Provides:	seamonkey-lang-resources = %{version}
Obsoletes:	iceape-lang-de < 2.47
BuildArch:	noarch

%description lang-de
German resources for SeaMonkey.

%description lang-de -l pl.UTF-8
Niemieckie pliki językowe dla SeaMonkeya.

%package lang-el
Summary:	Greek resources for SeaMonkey
Summary(pl.UTF-8):	Greckie pliki językowe dla SeaMonkeya
Group:		I18n
Requires:	seamonkey >= %{version}
Provides:	seamonkey-lang-resources = %{version}
BuildArch:	noarch

%description lang-el
Greek resources for SeaMonkey.

%description lang-el -l pl.UTF-8
Greckie pliki językowe dla SeaMonkeya.

%package lang-en_GB
Summary:	English (British) resources for SeaMonkey
Summary(pl.UTF-8):	Angielskie (brytyjskie) pliki językowe dla SeaMonkeya
Group:		I18n
Requires:	seamonkey >= %{version}
Provides:	seamonkey-lang-resources = %{version}
Obsoletes:	iceape-lang-en_GB < 2.47
BuildArch:	noarch

%description lang-en_GB
English (British) resources for SeaMonkey.

%description lang-en_GB -l pl.UTF-8
Angielskie (brytyjskie) pliki językowe dla SeaMonkeya.

%package lang-en_US
Summary:	English (American) resources for SeaMonkey
Summary(pl.UTF-8):	Angielskie (amerykańskie) pliki językowe dla SeaMonkeya
Group:		I18n
Requires:	seamonkey >= %{version}
Provides:	seamonkey-lang-resources = %{version}
Obsoletes:	iceape-lang-en_US < 2.47
BuildArch:	noarch

%description lang-en_US
English (American) resources for SeaMonkey.

%description lang-en_US -l pl.UTF-8
Angielskie (amerykańskie) pliki językowe dla SeaMonkeya.

%package lang-es_AR
Summary:	Spanish (Andorra) resources for SeaMonkey
Summary(ca.UTF-8):	Recursos espanyols (Andorra) per SeaMonkey
Summary(es.UTF-8):	Recursos españoles (Andorra) para SeaMonkey
Summary(pl.UTF-8):	Hiszpańskie pliki językowe dla SeaMonkeya (wersja dla Andory)
Group:		I18n
Requires:	seamonkey >= %{version}
Provides:	seamonkey-lang-resources = %{version}
Obsoletes:	iceape-lang-es_AR < 2.47
BuildArch:	noarch

%description lang-es_AR
Spanish (Spain) resources for SeaMonkey.

%description lang-es_AR -l ca.UTF-8
Recursos espanyols (Andorra) per SeaMonkey.

%description lang-es_AR -l es.UTF-8
Recursos españoles (Andorra) para SeaMonkey.

%description lang-es_AR -l pl.UTF-8
Hiszpańskie pliki językowe dla SeaMonkeya (wersja dla Andory).

%package lang-es
Summary:	Spanish (Spain) resources for SeaMonkey
Summary(ca.UTF-8):	Recursos espanyols (Espanya) per SeaMonkey
Summary(es.UTF-8):	Recursos españoles (España) para SeaMonkey
Summary(pl.UTF-8):	Hiszpańskie pliki językowe dla SeaMonkeya (wersja dla Hiszpanii)
Group:		I18n
Requires:	seamonkey >= %{version}
Provides:	seamonkey-lang-resources = %{version}
Obsoletes:	iceape-lang-es < 2.47
BuildArch:	noarch

%description lang-es
Spanish (Spain) resources for SeaMonkey.

%description lang-es -l ca.UTF-8
Recursos espanyols (Espanya) per SeaMonkey.

%description lang-es -l es.UTF-8
Recursos españoles (España) para SeaMonkey.

%description lang-es -l pl.UTF-8
Hiszpańskie pliki językowe dla SeaMonkeya (wersja dla Hiszpanii).

%package lang-fi
Summary:	Finnish resources for SeaMonkey
Summary(pl.UTF-8):	Fińskie pliki językowe dla SeaMonkeya
Group:		I18n
Requires:	seamonkey >= %{version}
Provides:	seamonkey-lang-resources = %{version}
Obsoletes:	iceape-lang-fi < 2.47
BuildArch:	noarch

%description lang-fi
Finnish resources for SeaMonkey.

%description lang-fi -l pl.UTF-8
Fińskie pliki językowe dla SeaMonkeya.

%package lang-fr
Summary:	French resources for SeaMonkey
Summary(pl.UTF-8):	Francuskie pliki językowe dla SeaMonkeya
Group:		I18n
Requires:	seamonkey >= %{version}
Provides:	seamonkey-lang-resources = %{version}
Obsoletes:	iceape-lang-fr < 2.47
BuildArch:	noarch

%description lang-fr
French resources for SeaMonkey.

%description lang-fr -l pl.UTF-8
Francuskie pliki językowe dla SeaMonkeya.

%package lang-hu
Summary:	Hungarian resources for SeaMonkey
Summary(hu.UTF-8):	Magyar nyelv SeaMonkey-hez
Summary(pl.UTF-8):	Węgierskie pliki językowe dla SeaMonkeya
Group:		I18n
Requires:	seamonkey >= %{version}
Provides:	seamonkey-lang-resources = %{version}
Obsoletes:	iceape-lang-hu < 2.47
BuildArch:	noarch

%description lang-hu
Hungarian resources for SeaMonkey.

%description lang-hu -l hu.UTF-8
Magyar nyelv SeaMonkey-hez.

%description lang-hu -l pl.UTF-8
Węgierskie pliki językowe dla SeaMonkeya.

%package lang-it
Summary:	Italian resources for SeaMonkey
Summary(pl.UTF-8):	Włoskie pliki językowe dla SeaMonkeya
Group:		I18n
Requires:	seamonkey >= %{version}
Provides:	seamonkey-lang-resources = %{version}
Obsoletes:	iceape-lang-it < 2.47
BuildArch:	noarch

%description lang-it
Italian resources for SeaMonkey.

%description lang-it -l pl.UTF-8
Włoskie pliki językowe dla SeaMonkeya.

%package lang-ja
Summary:	Japanese resources for SeaMonkey
Summary(pl.UTF-8):	Japońskie pliki językowe dla SeaMonkeya
Group:		I18n
Requires:	seamonkey >= %{version}
Provides:	seamonkey-lang-resources = %{version}
Obsoletes:	iceape-lang-ja < 2.47
BuildArch:	noarch

%description lang-ja
Japanese resources for SeaMonkey.

%description lang-ja -l pl.UTF-8
Japońskie pliki językowe dla SeaMonkeya.

%package lang-ka
Summary:	Georgian resources for SeaMonkey
Summary(pl.UTF-8):	Gruzińskie pliki językowe dla SeaMonkeya
Group:		I18n
Requires:	seamonkey >= %{version}
Provides:	seamonkey-lang-resources = %{version}
BuildArch:	noarch

%description lang-ka
Georgian resources for SeaMonkey.

%description lang-ka -l pl.UTF-8
Gruzińskie pliki językowe dla SeaMonkeya.

%package lang-lt
Summary:	Lithuanian resources for SeaMonkey
Summary(pl.UTF-8):	Litewskie pliki językowe dla SeaMonkeya
Group:		I18n
Requires:	seamonkey >= %{version}
Provides:	seamonkey-lang-resources = %{version}
Obsoletes:	iceape-lang-lt < 2.47
BuildArch:	noarch

%description lang-lt
Lithuanian resources for SeaMonkey.

%description lang-lt -l pl.UTF-8
Litewskie pliki językowe dla SeaMonkeya.

%package lang-nb
Summary:	Norwegian Bokmaal resources for SeaMonkey
Summary(pl.UTF-8):	Norweskie (bokmaal) pliki językowe dla SeaMonkeya
Group:		I18n
Requires:	seamonkey >= %{version}
Provides:	seamonkey-lang-resources = %{version}
Obsoletes:	iceape-lang-nb < 2.47
BuildArch:	noarch

%description lang-nb
Norwegian Bokmaal resources for SeaMonkey.

%description lang-nb -l pl.UTF-8
Norweskie (bokmaal) pliki językowe dla SeaMonkeya.

%package lang-nl
Summary:	Dutch resources for SeaMonkey
Summary(pl.UTF-8):	Holenderskie pliki językowe dla SeaMonkeya
Group:		I18n
Requires:	seamonkey >= %{version}
Provides:	seamonkey-lang-resources = %{version}
Obsoletes:	iceape-lang-nl < 2.47
BuildArch:	noarch

%description lang-nl
Dutch resources for SeaMonkey.

%description lang-nl -l pl.UTF-8
Holenderskie pliki językowe dla SeaMonkeya.

%package lang-pl
Summary:	Polish resources for SeaMonkey
Summary(pl.UTF-8):	Polskie pliki językowe dla SeaMonkeya
Group:		I18n
Requires:	seamonkey >= %{version}
Provides:	seamonkey-lang-resources = %{version}
Obsoletes:	iceape-lang-pl < 2.47
BuildArch:	noarch

%description lang-pl
Polish resources for SeaMonkey.

%description lang-pl -l pl.UTF-8
Polskie pliki językowe dla SeaMonkeya.

%package lang-pt_BR
Summary:	Portuguese (Brazilian) resources for SeaMonkey
Summary(pl.UTF-8):	Portugalskie pliki językowe dla SeaMonkeya (wersja dla Brazylii)
Group:		I18n
Requires:	seamonkey >= %{version}
Provides:	seamonkey-lang-resources = %{version}
BuildArch:	noarch

%description lang-pt_BR
Portuguese (Brazilian) resources for SeaMonkey.

%description lang-pt_BR -l pl.UTF-8
Portugalskie pliki językowe dla SeaMonkeya (wersja dla Brazylii).

%package lang-pt
Summary:	Portuguese (Portugal) resources for SeaMonkey
Summary(pl.UTF-8):	Portugalskie pliki językowe dla SeaMonkeya (wersja dla Portugalii)
Group:		I18n
Requires:	seamonkey >= %{version}
Provides:	seamonkey-lang-resources = %{version}
Obsoletes:	iceape-lang-pt < 2.47
BuildArch:	noarch

%description lang-pt
Portuguese (Portugal) resources for SeaMonkey.

%description lang-pt -l pl.UTF-8
Portugalskie pliki językowe dla SeaMonkeya (wersja dla Portugalii).

%package lang-ru
Summary:	Russian resources for SeaMonkey
Summary(pl.UTF-8):	Rosyjskie pliki językowe dla SeaMonkeya
Group:		I18n
Requires:	seamonkey >= %{version}
Provides:	seamonkey-lang-resources = %{version}
Obsoletes:	iceape-lang-ru < 2.47
BuildArch:	noarch

%description lang-ru
Russian resources for SeaMonkey.

%description lang-ru -l pl.UTF-8
Rosyjskie pliki językowe dla SeaMonkeya.

%package lang-sk
Summary:	Slovak resources for SeaMonkey
Summary(pl.UTF-8):	Słowackie pliki językowe dla SeaMonkeya
Group:		I18n
Requires:	seamonkey >= %{version}
Provides:	seamonkey-lang-resources = %{version}
Obsoletes:	iceape-lang-sk < 2.47
BuildArch:	noarch

%description lang-sk
Slovak resources for SeaMonkey.

%description lang-sk -l pl.UTF-8
Słowackie pliki językowe dla SeaMonkeya.

%package lang-sv
Summary:	Swedish resources for SeaMonkey
Summary(pl.UTF-8):	Szwedzkie pliki językowe dla SeaMonkeya
Group:		I18n
Requires:	seamonkey >= %{version}
Provides:	seamonkey-lang-resources = %{version}
Obsoletes:	iceape-lang-sv < 2.47
BuildArch:	noarch

%description lang-sv
Swedish resources for SeaMonkey.

%description lang-sv -l pl.UTF-8
Szwedzkie pliki językowe dla SeaMonkeya.

%package lang-zh_CN
Summary:	Simplified Chinese resources for SeaMonkey
Summary(pl.UTF-8):	Chińskie (uproszczone) pliki językowe dla SeaMonkeya
Group:		I18n
Requires:	seamonkey >= %{version}
Provides:	seamonkey-lang-resources = %{version}
Obsoletes:	iceape-lang-zh_CN < 2.47
BuildArch:	noarch

%description lang-zh_CN
Simplified Chinese resources for SeaMonkey.

%description lang-zh_CN -l pl.UTF-8
Chińskie uproszczone pliki językowe dla SeaMonkeya.

%package lang-zh_TW
Summary:	Traditional Chinese resources for SeaMonkey
Summary(pl.UTF-8):	Chińskie tradycyjne pliki językowe dla SeaMonkeya
Group:		I18n
Requires:	seamonkey >= %{version}
Provides:	seamonkey-lang-resources = %{version}
Obsoletes:	iceape-lang-zh_TW < 2.47
BuildArch:	noarch

%description lang-zh_TW
Traditional Chinese resources for SeaMonkey.

%description lang-zh_TW -l pl.UTF-8
Chińskie tradycyjne pliki językowe dla SeaMonkeya.

%prep
unpack() {
	local args="$1" file="$2"
	cp -p $file .
}
%define __unzip unpack
%setup -q %(seq -f '-a %g' 100 122 | xargs)
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch7 -p1

%build
cat << EOF > .mozconfig
mk_add_options MOZ_OBJDIR=%{objdir}

export CFLAGS="%{rpmcflags} -D_FILE_OFFSET_BITS=64"
export CXXFLAGS="%{rpmcxxflags} -D_FILE_OFFSET_BITS=64"

%if %{with lowmem}
export CFLAGS="$CFLAGS -g0"
export CXXFLAGS="$CXXFLAGS -g0"
export MOZ_DEBUG_FLAGS=" "
export LLVM_USE_SPLIT_DWARF=1
export LLVM_PARALLEL_LINK_JOBS=1
export MOZ_LINK_FLAGS="-Wl,--no-keep-memory -Wl,--reduce-memory-overheads"
export RUSTFLAGS="-Cdebuginfo=0"
%endif

%if %{with crashreporter}
export MOZ_DEBUG_SYMBOLS=1
%endif

# Options for 'configure' (same as command-line options).
ac_add_options --prefix=%{_prefix}
ac_add_options --libdir=%{_libdir}
%if %{?debug:1}0
ac_add_options --disable-optimize
ac_add_options --enable-crash-on-assert
ac_add_options --enable-debug
ac_add_options --enable-debug-modules
ac_add_options --enable-debugger-info-modules
%else
ac_add_options --disable-debug
%endif
ac_add_options --disable-strip
ac_add_options --disable-install-strip
%if %{with tests}
ac_add_options --enable-tests
%else
ac_add_options --disable-tests
%endif
%if %{with crashreporter}
ac_add_options --enable-crashreporter
%else
ac_add_options --disable-crashreporter
%endif
ac_add_options --disable-elf-hack
ac_add_options --disable-necko-wifi
ac_add_options --disable-updater
ac_add_options --enable-application=comm/suite
%if %{with lightning}
ac_add_options --enable-calendar
%endif
ac_add_options --enable-chrome-format=omni
ac_add_options --enable-default-toolkit=cairo-gtk3
ac_add_options --enable-dominspector
ac_add_options --enable-irc
%if %{without gold}
ac_add_options --enable-linker=bfd
%endif
# breaks build
#ac_add_options --enable-shared-js
ac_add_options --enable-startup-notification
%if %{with system_cairo}
ac_add_options --enable-system-cairo
%endif
ac_add_options --with-distribution-id=org.pld-linux
ac_add_options --with-system-bz2
ac_add_options --with-system-ffi
ac_add_options --with-system-icu
ac_add_options --with-system-jpeg
ac_add_options --with-system-libevent
ac_add_options --with-system-libvpx
ac_add_options --with-system-nspr
ac_add_options --with-system-nss
ac_add_options --with-system-pixman
ac_add_options --with-system-png
ac_add_options --with-system-zlib
EOF

%{__make} -j1 build \
	AUTOCONF=/usr/bin/autoconf2_13 \
	STRIP="/bin/true" \
	MOZ_MAKE_FLAGS="%{?_smp_mflags}" \
	installdir=%{_libdir}/%{name} \
	XLIBS="-lX11 -lXt" \
	CC="%{__cc}" \
	CXX="%{__cxx}"

%if %{with crashreporter}
# create debuginfo for crash-stats.mozilla.com
%{__make} -j1 -C obj-%{_target_cpu} buildsymbols
%endif

%install
rm -rf $RPM_BUILD_ROOT
install -d \
	$RPM_BUILD_ROOT{%{_bindir},%{_libdir}} \
	$RPM_BUILD_ROOT{%{_desktopdir},%{_pixmapsdir}} \
	$RPM_BUILD_ROOT%{_datadir}/%{name} \
	$RPM_BUILD_ROOT%{_libdir}/%{name}/plugins \
	$RPM_BUILD_ROOT%{_mandir}/man1

%browser_plugins_add_browser %{name} -p %{_libdir}/%{name}/plugins

cd %{objdir}
cwd=`pwd`
%{__make} -C comm/suite/installer stage-package \
	DESTDIR=$RPM_BUILD_ROOT \
	installdir=%{_libdir}/%{name} \
	PKG_SKIP_STRIP=1

cp -a dist/seamonkey/* $RPM_BUILD_ROOT%{_libdir}/%{name}/
cp -p dist/man/man1/seamonkey.1 $RPM_BUILD_ROOT%{_mandir}/man1

# Enable crash reporter for Thunderbird application
%if %{with crashreporter}
%{__sed} -i -e 's/\[Crash Reporter\]/[Crash Reporter]\nEnabled=1/' $RPM_BUILD_ROOT%{_libdir}/%{name}/application.ini

# Add debuginfo for crash-stats.mozilla.com
install -d $RPM_BUILD_ROOT%{_exec_prefix}/lib/debug%{_libdir}/%{name}
cp -a dist/%{name}-%{version}.en-US.linux-*.crashreporter-symbols.zip $RPM_BUILD_ROOT%{_prefix}/lib/debug%{_libdir}/%{name}
%endif

# move arch independent ones to datadir
%{__mv} $RPM_BUILD_ROOT%{_libdir}/%{name}/chrome $RPM_BUILD_ROOT%{_datadir}/%{name}/chrome
%{__mv} $RPM_BUILD_ROOT%{_libdir}/%{name}/defaults $RPM_BUILD_ROOT%{_datadir}/%{name}/defaults
%{__mv} $RPM_BUILD_ROOT%{_libdir}/%{name}/fonts $RPM_BUILD_ROOT%{_datadir}/%{name}/fonts

ln -s ../../share/%{name}/chrome $RPM_BUILD_ROOT%{_libdir}/%{name}/chrome
ln -s ../../share/%{name}/defaults $RPM_BUILD_ROOT%{_libdir}/%{name}/defaults
ln -s ../../share/%{name}/fonts $RPM_BUILD_ROOT%{_libdir}/%{name}/fonts

%{__mv} $RPM_BUILD_ROOT%{_libdir}/%{name}/isp $RPM_BUILD_ROOT%{_datadir}/%{name}/isp
ln -s ../../share/%{name}/isp $RPM_BUILD_ROOT%{_libdir}/%{name}/isp

# dir for arch independant extensions besides arch dependant extensions
# see mozilla/xpcom/build/nsXULAppAPI.h
# XRE_SYS_LOCAL_EXTENSION_PARENT_DIR and XRE_SYS_SHARE_EXTENSION_PARENT_DIR
install -d $RPM_BUILD_ROOT%{_datadir}/%{name}/extensions
 
%{__rm} -r $RPM_BUILD_ROOT%{_libdir}/%{name}/dictionaries
ln -s %{_datadir}/myspell $RPM_BUILD_ROOT%{_libdir}/%{name}/dictionaries

sed 's,@LIBDIR@,%{_libdir},' %{SOURCE9} > $RPM_BUILD_ROOT%{_bindir}/seamonkey
chmod a+rx $RPM_BUILD_ROOT%{_bindir}/seamonkey

install %{SOURCE4} %{SOURCE5} %{SOURCE7} \
	$RPM_BUILD_ROOT%{_desktopdir}

for d in 16 32 48 64 128 ; do
install -d $RPM_BUILD_ROOT%{_iconsdir}/hicolor/${d}x${d}/apps
cp -p %{topdir}/comm/suite/branding/seamonkey/default${d}.png $RPM_BUILD_ROOT%{_iconsdir}/hicolor/${d}x${d}/apps/%{name}.png
done

# don't package, rely on system mozldap libraries
%{__sed} -i '/lib\(ldap\|ldif\|prldap\)60.so/d' $RPM_BUILD_ROOT%{_libdir}/%{name}/dependentlibs.list
%{__rm} $RPM_BUILD_ROOT%{_libdir}/%{name}/lib{ldap,ldif,prldap}60.so

cd ..
for a in *.xpi; do
	basename=$(basename $a .langpack.xpi)
	basename=${basename##seamonkey-%{version}.}
	cp -p $a $RPM_BUILD_ROOT%{_datadir}/%{name}/extensions/langpack-$basename@seamonkey.mozilla.org.xpi
done

%{__rm} $RPM_BUILD_ROOT%{_libdir}/%{name}/{license.txt,precomplete,removed-files}

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_browser_plugins
%update_icon_cache hicolor
%update_desktop_database

%postun
if [ "$1" = 0 ]; then
	%update_browser_plugins
	%update_icon_cache hicolor
fi

%files
%defattr(644,root,root,755)
%doc AUTHORS
%attr(755,root,root) %{_bindir}/seamonkey
%{_mandir}/man1/seamonkey.1*

# browser plugins v2
%{_browserpluginsconfdir}/browsers.d/%{name}.*
%config(noreplace) %verify(not md5 mtime size) %{_browserpluginsconfdir}/blacklist.d/%{name}.*.blacklist

%dir %{_libdir}/%{name}
%attr(755,root,root) %{_libdir}/%{name}/liblgpllibs.so
%attr(755,root,root) %{_libdir}/%{name}/libmozavcodec.so
%attr(755,root,root) %{_libdir}/%{name}/libmozavutil.so
%attr(755,root,root) %{_libdir}/%{name}/libmozgtk.so
%attr(755,root,root) %{_libdir}/%{name}/libmozsandbox.so
%attr(755,root,root) %{_libdir}/%{name}/libmozsqlite3.so
%attr(755,root,root) %{_libdir}/%{name}/libxul.so

%{_libdir}/%{name}/blocklist.xml
%{_libdir}/%{name}/omni.ja

%if %{with crashreporter}
%{_libdir}/%{name}/crashreporter
%{_libdir}/%{name}/crashreporter-override.ini
%{_libdir}/%{name}/crashreporter.ini
%{_libdir}/%{name}/Throbber-small.gif
%endif

# config?
%{_libdir}/%{name}/application.ini
%{_libdir}/%{name}/chrome.manifest

%{_libdir}/%{name}/dependentlibs.list
%{_libdir}/%{name}/platform.ini
%attr(755,root,root) %{_libdir}/%{name}/run-mozilla.sh
%attr(755,root,root) %{_libdir}/%{name}/seamonkey-bin
%attr(755,root,root) %{_libdir}/%{name}/plugin-container

%attr(755,root,root) %{_libdir}/%{name}/seamonkey
%dir %{_libdir}/%{name}/plugins

# symlinks
%{_libdir}/%{name}/chrome
%{_libdir}/%{name}/defaults
%{_libdir}/%{name}/fonts
%{_libdir}/%{name}/dictionaries

%dir %{_datadir}/%{name}
%{_datadir}/%{name}/chrome
%{_datadir}/%{name}/defaults
%{_datadir}/%{name}/fonts

%dir %{_datadir}/%{name}/extensions
%dir %{_libdir}/%{name}/extensions
# the signature of the default theme
%{_libdir}/%{name}/extensions/{972ce4c6-7e08-4474-a285-3208198ce6fd}.xpi
%{_libdir}/%{name}/extensions/modern@themes.mozilla.org.xpi

%{_libdir}/%{name}/isp
%dir %{_datadir}/%{name}/isp
%{_datadir}/%{name}/isp/Bogofilter.sfd
%{_datadir}/%{name}/isp/DSPAM.sfd
%{_datadir}/%{name}/isp/POPFile.sfd
%{_datadir}/%{name}/isp/SpamAssassin.sfd
%{_datadir}/%{name}/isp/SpamPal.sfd
%{_datadir}/%{name}/isp/movemail.rdf
%{_datadir}/%{name}/isp/rss.rdf

%{_iconsdir}/hicolor/*x*/apps/seamonkey.png
%{_desktopdir}/%{name}.desktop
%{_desktopdir}/%{name}-composer.desktop
%{_desktopdir}/%{name}-mail.desktop

%if %{with lightning}
%files addon-lightning
%defattr(644,root,root,755)
%{_libdir}/%{name}/extensions/{e2fda1a4-762b-4020-b5ad-a41df1933103}.xpi
%endif

%files chat
%defattr(644,root,root,755)
%{_libdir}/%{name}/extensions/{59c81df5-4b7a-477b-912d-4e0fdf64e5f2}.xpi

%files dom-inspector
%defattr(644,root,root,755)
%{_libdir}/%{name}/extensions/inspector@mozilla.org.xpi

%files lang-cs
%defattr(644,root,root,755)
%{_datadir}/%{name}/extensions/langpack-cs@seamonkey.mozilla.org.xpi

%files lang-de
%defattr(644,root,root,755)
%{_datadir}/%{name}/extensions/langpack-de@seamonkey.mozilla.org.xpi

%files lang-el
%defattr(644,root,root,755)
%{_datadir}/%{name}/extensions/langpack-el@seamonkey.mozilla.org.xpi

%files lang-en_GB
%defattr(644,root,root,755)
%{_datadir}/%{name}/extensions/langpack-en-GB@seamonkey.mozilla.org.xpi

%files lang-en_US
%defattr(644,root,root,755)
%{_datadir}/%{name}/extensions/langpack-en-US@seamonkey.mozilla.org.xpi

%files lang-es_AR
%defattr(644,root,root,755)
%{_datadir}/%{name}/extensions/langpack-es-AR@seamonkey.mozilla.org.xpi

%files lang-es
%defattr(644,root,root,755)
%{_datadir}/%{name}/extensions/langpack-es-ES@seamonkey.mozilla.org.xpi

%files lang-fi
%defattr(644,root,root,755)
%{_datadir}/%{name}/extensions/langpack-fi@seamonkey.mozilla.org.xpi

%files lang-fr
%defattr(644,root,root,755)
%{_datadir}/%{name}/extensions/langpack-fr@seamonkey.mozilla.org.xpi

%files lang-hu
%defattr(644,root,root,755)
%{_datadir}/%{name}/extensions/langpack-hu@seamonkey.mozilla.org.xpi

%files lang-it
%defattr(644,root,root,755)
%{_datadir}/%{name}/extensions/langpack-it@seamonkey.mozilla.org.xpi

%files lang-ja
%defattr(644,root,root,755)
%{_datadir}/%{name}/extensions/langpack-ja@seamonkey.mozilla.org.xpi

%files lang-ka
%defattr(644,root,root,755)
%{_datadir}/%{name}/extensions/langpack-ka@seamonkey.mozilla.org.xpi

#%files lang-lt
#%defattr(644,root,root,755)
#%{_datadir}/%{name}/extensions/langpack-lt@seamonkey.mozilla.org.xpi

%files lang-nb
%defattr(644,root,root,755)
%{_datadir}/%{name}/extensions/langpack-nb-NO@seamonkey.mozilla.org.xpi

%files lang-nl
%defattr(644,root,root,755)
%{_datadir}/%{name}/extensions/langpack-nl@seamonkey.mozilla.org.xpi

%files lang-pl
%defattr(644,root,root,755)
%{_datadir}/%{name}/extensions/langpack-pl@seamonkey.mozilla.org.xpi

%files lang-pt_BR
%defattr(644,root,root,755)
%{_datadir}/%{name}/extensions/langpack-pt-BR@seamonkey.mozilla.org.xpi

%files lang-pt
%defattr(644,root,root,755)
%{_datadir}/%{name}/extensions/langpack-pt-PT@seamonkey.mozilla.org.xpi

%files lang-ru
%defattr(644,root,root,755)
%{_datadir}/%{name}/extensions/langpack-ru@seamonkey.mozilla.org.xpi

%files lang-sk
%defattr(644,root,root,755)
%{_datadir}/%{name}/extensions/langpack-sk@seamonkey.mozilla.org.xpi

%files lang-sv
%defattr(644,root,root,755)
%{_datadir}/%{name}/extensions/langpack-sv-SE@seamonkey.mozilla.org.xpi

%files lang-zh_CN
%defattr(644,root,root,755)
%{_datadir}/%{name}/extensions/langpack-zh-CN@seamonkey.mozilla.org.xpi

%files lang-zh_TW
%defattr(644,root,root,755)
%{_datadir}/%{name}/extensions/langpack-zh-TW@seamonkey.mozilla.org.xpi
