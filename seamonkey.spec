# TODO:
# - consider --enable-libproxy
# - do something with *.rdf file, there if file conflict with other lang packages
#
# Conditional build:
%bcond_without	gtk3		# GTK+ 3.x instead of 2.x
%bcond_without	ldap		# disable e-mail address lookups in LDAP directories
%bcond_without	kerberos	# disable krb5 support
%bcond_without	lightning	# disable Lightning calendar
%bcond_with	crashreporter	# report crashes to crash-stats.mozilla.com
%bcond_with	tests		# enable tests (whatever they check)

%define		nspr_ver	4.13.1
%define		nss_ver		3.28.6

# The actual sqlite version (see RHBZ#480989):
%define		sqlite_build_version %(pkg-config --silence-errors --modversion sqlite3 2>/dev/null || echo ERROR)

# UPDATING TRANSALTIONS:
%if 0
rm -vf *.xpi
./builder -g
V=2.49.5
U=http://releases.mozilla.org/pub/mozilla.org/seamonkey/releases/$V/langpacks/linux-i686/
curl -s $U | sed -ne 's,.*href="\([^"]\+\)/".*,'"$U"'xpi/\1.xpi,p'
%endif

Summary:	SeaMonkey Community Edition - web browser
Summary(es.UTF-8):	Navegador de Internet SeaMonkey Community Edition
Summary(pl.UTF-8):	SeaMonkey Community Edition - przeglądarka WWW
Summary(pt_BR.UTF-8):	Navegador SeaMonkey Community Edition
Name:		seamonkey
Version:	2.49.5
Release:	3
License:	MPL v2.0
Group:		X11/Applications/Networking
Source0:	http://ftp.mozilla.org/pub/seamonkey/releases/%{version}/source/%{name}-%{version}.source.tar.xz
# Source0-md5:	91f60a7aca6f8bc053ffddc7259ae4ec
Source4:	%{name}.desktop
Source5:	%{name}-composer.desktop
Source7:	%{name}-mail.desktop
Source9:	%{name}.sh
Source100:	http://ftp.mozilla.org/pub/mozilla.org/seamonkey/releases/%{version}/langpacks/linux-i686/seamonkey-%{version}.cs.langpack.xpi
# Source100-md5:	1e0b73887e5d80589c5b2fd5d8538d7f
Source101:	http://ftp.mozilla.org/pub/mozilla.org/seamonkey/releases/%{version}/langpacks/linux-i686/seamonkey-%{version}.de.langpack.xpi
# Source101-md5:	eb4bf2ab50756280d1a39c1547129ced
Source102:	http://ftp.mozilla.org/pub/mozilla.org/seamonkey/releases/%{version}/langpacks/linux-i686/seamonkey-%{version}.en-GB.langpack.xpi
# Source102-md5:	c9bea7471fabf225009a5340733e4ce2
Source103:	http://ftp.mozilla.org/pub/mozilla.org/seamonkey/releases/%{version}/langpacks/linux-i686/seamonkey-%{version}.en-US.langpack.xpi
# Source103-md5:	42f234f11bcb6a127462caaf664dc21b
Source104:	http://ftp.mozilla.org/pub/mozilla.org/seamonkey/releases/%{version}/langpacks/linux-i686/seamonkey-%{version}.es-AR.langpack.xpi
# Source104-md5:	5fdf01f31dd24c06bc0c51a74d9673a6
Source105:	http://ftp.mozilla.org/pub/mozilla.org/seamonkey/releases/%{version}/langpacks/linux-i686/seamonkey-%{version}.es-ES.langpack.xpi
# Source105-md5:	948d3dbf4452e7e46f1a0d5026d2200c
Source106:	http://ftp.mozilla.org/pub/mozilla.org/seamonkey/releases/%{version}/langpacks/linux-i686/seamonkey-%{version}.fr.langpack.xpi
# Source106-md5:	5dbd832a5d4d81aa52f7435123ade06e
Source107:	http://ftp.mozilla.org/pub/mozilla.org/seamonkey/releases/%{version}/langpacks/linux-i686/seamonkey-%{version}.hu.langpack.xpi
# Source107-md5:	b002ed727428960d34ded53ec290667b
Source108:	http://ftp.mozilla.org/pub/mozilla.org/seamonkey/releases/%{version}/langpacks/linux-i686/seamonkey-%{version}.it.langpack.xpi
# Source108-md5:	12d37399fda4202144a82b458f75d27c
Source109:	http://ftp.mozilla.org/pub/mozilla.org/seamonkey/releases/%{version}/langpacks/linux-i686/seamonkey-%{version}.ja.langpack.xpi
# Source109-md5:	f5e304d3ba8d526b28e92693f23154c9
Source110:	http://ftp.mozilla.org/pub/mozilla.org/seamonkey/releases/%{version}/langpacks/linux-i686/seamonkey-%{version}.lt.langpack.xpi
# Source110-md5:	40db7b6ee7b1ddd5723e51c335f73eec
Source111:	http://ftp.mozilla.org/pub/mozilla.org/seamonkey/releases/%{version}/langpacks/linux-i686/seamonkey-%{version}.nb-NO.langpack.xpi
# Source111-md5:	cfde049afaaba0afe9f8b85ac704ba85
Source112:	http://ftp.mozilla.org/pub/mozilla.org/seamonkey/releases/%{version}/langpacks/linux-i686/seamonkey-%{version}.nl.langpack.xpi
# Source112-md5:	21a733c0b344840a2d81958a0fe72bc1
Source113:	http://ftp.mozilla.org/pub/mozilla.org/seamonkey/releases/%{version}/langpacks/linux-i686/seamonkey-%{version}.pl.langpack.xpi
# Source113-md5:	1a2646b993dc540f09c8b04fc4107c45
Source114:	http://ftp.mozilla.org/pub/mozilla.org/seamonkey/releases/%{version}/langpacks/linux-i686/seamonkey-%{version}.pt-PT.langpack.xpi
# Source114-md5:	0e54c214e673c474400c36a934f946a8
Source115:	http://ftp.mozilla.org/pub/mozilla.org/seamonkey/releases/%{version}/langpacks/linux-i686/seamonkey-%{version}.ru.langpack.xpi
# Source115-md5:	c24ff5c5bafbfce18b0333ef31735f54
Source116:	http://ftp.mozilla.org/pub/mozilla.org/seamonkey/releases/%{version}/langpacks/linux-i686/seamonkey-%{version}.sk.langpack.xpi
# Source116-md5:	5ab1d6ebf6cee6dc822fc91e1ced4443
Source117:	http://ftp.mozilla.org/pub/mozilla.org/seamonkey/releases/%{version}/langpacks/linux-i686/seamonkey-%{version}.sv-SE.langpack.xpi
# Source117-md5:	e471259f0afcdb159ce5f0a8f24cfd5b
Source118:	http://ftp.mozilla.org/pub/mozilla.org/seamonkey/releases/%{version}/langpacks/linux-i686/seamonkey-%{version}.zh-CN.langpack.xpi
# Source118-md5:	7160e0ea724c68c6457bb5a76b996255
Source119:	http://ftp.mozilla.org/pub/mozilla.org/seamonkey/releases/%{version}/langpacks/linux-i686/seamonkey-%{version}.zh-TW.langpack.xpi
# Source119-md5:	5370bfa849ea4af22e6ef8d1500279c8
Patch1:		%{name}-pld-branding.patch
Patch2:		%{name}-agent.patch
Patch3:		%{name}-enable-addons.patch
# Edit patch below and restore --system-site-packages when system virtualenv gets 1.7 upgrade
Patch4:		%{name}-system-virtualenv.patch
Patch5:		%{name}-icu-detect.patch
Patch6:		%{name}-glibc2.30.patch
Patch7:		%{name}-crmf.patch
URL:		https://www.seamonkey-project.org/
BuildRequires:	GConf2-devel >= 1.2.1
BuildRequires:	OpenGL-devel
BuildRequires:	alsa-lib-devel
BuildRequires:	autoconf2_13 >= 2.13
BuildRequires:	bzip2-devel
BuildRequires:	cairo-devel >= 1.10.2-5
BuildRequires:	dbus-glib-devel >= 0.60
BuildRequires:	fontconfig-devel >= 1:2.7.0
BuildRequires:	freetype-devel >= 1:2.1.8
BuildRequires:	glib2-devel >= 1:2.22
%{!?with_gtk3:BuildRequires:	gtk+2-devel >= 2:2.18}
%{?with_gtk3:BuildRequires:	gtk+3-devel >= 3.4.0}
%{?with_kerberos:BuildRequires:	heimdal-devel >= 0.7.1}
BuildRequires:	hunspell-devel
# DECnet (dnprogs.spec), not dummy net (libdnet.spec)
#BuildRequires:	libdnet-devel
BuildRequires:	libevent-devel >= 1.4.7
# standalone libffi 3.0.9 or gcc's from 4.5(?)+
BuildRequires:	libffi-devel >= 6:3.0.9
BuildRequires:	libicu-devel >= 50.1
# requires libjpeg-turbo implementing at least libjpeg 6b API
BuildRequires:	libjpeg-devel >= 6b
BuildRequires:	libjpeg-turbo-devel
BuildRequires:	libnotify-devel >= 0.4
BuildRequires:	libpng(APNG)-devel >= 0.10
BuildRequires:	libpng-devel >= 2:1.6.21
BuildRequires:	libstdc++-devel >= 6:4.7
BuildRequires:	libvpx-devel >= 1.5.0
BuildRequires:	mozldap-devel >= 6.0
BuildRequires:	nspr-devel >= 1:%{nspr_ver}
BuildRequires:	nss-devel >= 1:%{nss_ver}
BuildRequires:	pango-devel >= 1:1.22.0
BuildRequires:	perl-base >= 1:5.6
BuildRequires:	perl-modules >= 5.004
BuildRequires:	pixman-devel >= 0.19.2
BuildRequires:	pkgconfig
BuildRequires:	python >= 1:2.7
BuildRequires:	python-modules >= 1:2.7
BuildRequires:	python-virtualenv >= 15
BuildRequires:	rpm >= 4.4.9-56
BuildRequires:	rpmbuild(macros) >= 1.601
BuildRequires:	sed >= 4.0
BuildRequires:	sqlite3-devel >= 3.17.0
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
Requires:	cairo >= 1.10.2-5
Requires:	dbus-glib >= 0.60
Requires:	glib2 >= 1:2.22
%{!?with_gtk3:Requires:	gtk+2 >= 2:2.18}
%{?with_gtk3:Requires:	gtk+3 >= 3.4.0}
Requires:	libjpeg-turbo
Requires:	libpng >= 2:1.6.21
Requires:	libpng(APNG) >= 0.10
Requires:	libvpx >= 1.5.0
Requires:	myspell-common
Requires:	nspr >= 1:%{nspr_ver}
Requires:	nss >= 1:%{nss_ver}
Requires:	pango >= 1:1.22.0
Requires:	pixman >= 0.19.2
Requires:	sqlite3 >= %{sqlite_build_version}
Requires:	startup-notification >= 0.8
Provides:	seamonkey-embedded = %{version}-%{release}
Provides:	wwwbrowser
Obsoletes:	iceape
Obsoletes:	iceape-js-debugger
Obsoletes:	iceape-mailnews
Obsoletes:	iceape-gnomevfs
Obsoletes:	light
Obsoletes:	mozilla
Obsoletes:	mozilla-gnomevfs
Obsoletes:	seamonkey-addon-lightning < 2.46
Obsoletes:	seamonkey-chat < 2.46
Obsoletes:	seamonkey-calendar
Obsoletes:	seamonkey-dom-inspector < 2.46
Obsoletes:	seamonkey-js-debugger
Obsoletes:	seamonkey-libs
Obsoletes:	seamonkey-mailnews
Obsoletes:	seamonkey-gnomevfs
Conflicts:	seamonkey-lang-resources < %{version}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		topdir		%{_builddir}/%{name}-%{version}
%define		objdir		%{topdir}/obj-%{_target_cpu}

%define		filterout_cpp	-D_FORTIFY_SOURCE=[0-9]+

# don't satisfy other packages
%define		_noautoprovfiles	%{_libdir}/%{name}
# and as we don't provide them, don't require either
%define		_noautoreq	liblgpllibs.so libmozavcodec.so libmozavutil.so libmozgtk.so libmozsandbox.so libxul.so

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
Obsoletes:	iceape-addon-lightning

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
Obsoletes:	iceape-chat
Obsoletes:	mozilla-chat

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
Obsoletes:	iceape-dom-inspector
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

%package lang-cs
Summary:	Czech resources for SeaMonkey
Summary(pl.UTF-8):	Czeskie pliki językowe dla SeaMonkeya
Group:		I18n
Requires:	seamonkey >= %{version}
Provides:	seamonkey-lang-resources = %{version}
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
BuildArch:	noarch

%description lang-de
German resources for SeaMonkey.

%description lang-de -l pl.UTF-8
Niemieckie pliki językowe dla SeaMonkeya.

%package lang-en_GB
Summary:	English (British) resources for SeaMonkey
Summary(pl.UTF-8):	Angielskie (brytyjskie) pliki językowe dla SeaMonkeya
Group:		I18n
Requires:	seamonkey >= %{version}
Provides:	seamonkey-lang-resources = %{version}
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
BuildArch:	noarch

%description lang-es
Spanish (Spain) resources for SeaMonkey.

%description lang-es -l ca.UTF-8
Recursos espanyols (Espanya) per SeaMonkey.

%description lang-es -l es.UTF-8
Recursos españoles (España) para SeaMonkey.

%description lang-es -l pl.UTF-8
Hiszpańskie pliki językowe dla SeaMonkeya (wersja dla Hiszpanii).

%package lang-fr
Summary:	French resources for SeaMonkey
Summary(pl.UTF-8):	Francuskie pliki językowe dla SeaMonkeya
Group:		I18n
Requires:	seamonkey >= %{version}
Provides:	seamonkey-lang-resources = %{version}
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
BuildArch:	noarch

%description lang-ja
Japanese resources for SeaMonkey.

%description lang-ja -l pl.UTF-8
Japońskie pliki językowe dla SeaMonkeya.

%package lang-lt
Summary:	Lithuanian resources for SeaMonkey
Summary(pl.UTF-8):	Litewskie pliki językowe dla SeaMonkeya
Group:		I18n
Requires:	seamonkey >= %{version}
Provides:	seamonkey-lang-resources = %{version}
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
BuildArch:	noarch

%description lang-pl
Polish resources for SeaMonkey.

%description lang-pl -l pl.UTF-8
Polskie pliki językowe dla SeaMonkeya.

%package lang-pt
Summary:	Portuguese (Portugal) resources for SeaMonkey
Summary(pl.UTF-8):	Portugalskie pliki językowe dla SeaMonkeya (wersja dla Portugalii)
Group:		I18n
Requires:	seamonkey >= %{version}
Provides:	seamonkey-lang-resources = %{version}
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
%setup -q %(seq -f '-a %g' 100 119 | xargs)
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1

%build
cat << EOF > .mozconfig
mk_add_options MOZ_OBJDIR=%{objdir}

%if %{with crashreporter}
export MOZ_DEBUG_SYMBOLS=1
%endif

# Options for 'configure' (same as command-line options).
ac_add_options --prefix=%{_prefix}
%if %{?debug:1}0
ac_add_options --disable-optimize
ac_add_options --enable-crash-on-assert
ac_add_options --enable-debug
ac_add_options --enable-debug-modules
ac_add_options --enable-debugger-info-modules
%else
ac_add_options --disable-debug
ac_add_options --enable-optimize="%{rpmcflags} -Os"
%endif
ac_add_options --disable-strip
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
ac_add_options --disable-gnomeui
ac_add_options --disable-necko-wifi
ac_add_options --disable-updater
ac_add_options --enable-application=suite
%if %{with lightning}
ac_add_options --enable-calendar
%endif
ac_add_options --enable-chrome-format=omni
ac_add_options --enable-default-toolkit=%{?with_gtk3:cairo-gtk3}%{!?with_gtk3:cairo-gtk2}
ac_add_options --enable-extensions=default
ac_add_options --enable-gio
%if %{with ldap}
ac_add_options --enable-ldap
%else
ac_add_options --disable-ldap
%endif
ac_add_options --enable-safe-browsing
# breaks build
#ac_add_options --enable-shared-js
ac_add_options --enable-startup-notification
ac_add_options --enable-system-cairo
ac_add_options --enable-system-hunspell
ac_add_options --enable-system-sqlite
ac_add_options --with-default-mozilla-five-home=%{_libdir}/%{name}
ac_add_options --with-distribution-id=org.pld-linux
ac_add_options --with-pthreads
ac_add_options --with-system-bz2
ac_add_options --with-system-ffi
ac_add_options --with-system-icu
ac_add_options --with-system-jpeg
ac_add_options --with-system-libevent
ac_add_options --with-system-libvpx
ac_add_options --with-system-nspr
ac_add_options --with-system-nss
ac_add_options --with-system-png
ac_add_options --with-system-zlib
EOF

%{__make} -j1 -f client.mk build \
	AUTOCONF=/usr/bin/autoconf2_13 \
	STRIP="/bin/true" \
	MOZ_MAKE_FLAGS="%{?_smp_mflags}" \
	installdir=%{_libdir}/%{name} \
	XLIBS="-lX11 -lXt" \
	CC="%{__cc}" \
	CXX="%{__cxx} -std=gnu++11"

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
%{__make} -C suite/installer stage-package \
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
%{__mv} $RPM_BUILD_ROOT%{_libdir}/%{name}/searchplugins $RPM_BUILD_ROOT%{_datadir}/%{name}/searchplugins

ln -s ../../share/%{name}/chrome $RPM_BUILD_ROOT%{_libdir}/%{name}/chrome
ln -s ../../share/%{name}/defaults $RPM_BUILD_ROOT%{_libdir}/%{name}/defaults
ln -s ../../share/%{name}/fonts $RPM_BUILD_ROOT%{_libdir}/%{name}/fonts
ln -s ../../share/%{name}/searchplugins $RPM_BUILD_ROOT%{_libdir}/%{name}/searchplugins

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

for d in 32 48 64 ; do
install -d $RPM_BUILD_ROOT%{_iconsdir}/hicolor/${d}x${d}/apps
cp -p %{topdir}/suite/branding/nightly/content/icon${d}.png $RPM_BUILD_ROOT%{_iconsdir}/hicolor/${d}x${d}/apps/%{name}.png
done

# files created by seamonkey -register
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

# don't package, rely on system mozldap libraries
%{__sed} -i '/lib\(ldap\|ldif\|prldap\)60.so/d' $RPM_BUILD_ROOT%{_libdir}/%{name}/dependentlibs.list
%{__rm} $RPM_BUILD_ROOT%{_libdir}/%{name}/lib{ldap,ldif,prldap}60.so

cd ..
for a in *.xpi; do
	basename=$(basename $a .langpack.xpi)
	basename=${basename##seamonkey-%{version}.}
	cp -p $a $RPM_BUILD_ROOT%{_datadir}/%{name}/extensions/langpack-$basename@seamonkey.mozilla.org.xpi
done

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
%attr(755,root,root) %{_libdir}/%{name}/libxul.so
%dir %{_libdir}/%{name}/gtk2
%attr(755,root,root) %{_libdir}/%{name}/gtk2/libmozgtk.so

%{_libdir}/%{name}/blocklist.xml
%{_libdir}/%{name}/omni.ja
%attr(755,root,root) %{_libdir}/%{name}/register

%if %{with crashreporter}
%{_libdir}/%{name}/crashreporter
%{_libdir}/%{name}/crashreporter-override.ini
%{_libdir}/%{name}/crashreporter.ini
%{_libdir}/%{name}/Throbber-small.gif
%endif

# config?
%{_libdir}/%{name}/application.ini
%{_libdir}/%{name}/chrome.manifest

%dir %{_libdir}/%{name}/components
%{_libdir}/%{name}/components/components.manifest
%attr(755,root,root) %{_libdir}/%{name}/components/libsuite.so

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
%{_libdir}/%{name}/searchplugins

%dir %{_datadir}/%{name}
%{_datadir}/%{name}/chrome
%{_datadir}/%{name}/defaults
%{_datadir}/%{name}/fonts
%{_datadir}/%{name}/searchplugins

%dir %{_libdir}/%{name}/distribution
%dir %{_libdir}/%{name}/distribution/extensions

%dir %{_datadir}/%{name}/extensions
%dir %{_libdir}/%{name}/extensions
# the signature of the default theme
%{_libdir}/%{name}/extensions/{972ce4c6-7e08-4474-a285-3208198ce6fd}.xpi
%{_libdir}/%{name}/extensions/modern@themes.mozilla.org.xpi

# files created by seamonkey -register
%ghost %{_libdir}/%{name}/components/compreg.dat
%ghost %{_libdir}/%{name}/components/xpti.dat

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
%{_libdir}/%{name}/distribution/extensions/{e2fda1a4-762b-4020-b5ad-a41df1933103}
%endif

%files chat
%defattr(644,root,root,755)
%{_libdir}/%{name}/distribution/extensions/{59c81df5-4b7a-477b-912d-4e0fdf64e5f2}.xpi

%files dom-inspector
%defattr(644,root,root,755)
%{_libdir}/%{name}/distribution/extensions/inspector@mozilla.org.xpi

%files lang-cs
%defattr(644,root,root,755)
%{_datadir}/%{name}/extensions/langpack-cs@seamonkey.mozilla.org.xpi

%files lang-de
%defattr(644,root,root,755)
%{_datadir}/%{name}/extensions/langpack-de@seamonkey.mozilla.org.xpi

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

%files lang-lt
%defattr(644,root,root,755)
%{_datadir}/%{name}/extensions/langpack-lt@seamonkey.mozilla.org.xpi

%files lang-nb
%defattr(644,root,root,755)
%{_datadir}/%{name}/extensions/langpack-nb-NO@seamonkey.mozilla.org.xpi

%files lang-nl
%defattr(644,root,root,755)
%{_datadir}/%{name}/extensions/langpack-nl@seamonkey.mozilla.org.xpi

%files lang-pl
%defattr(644,root,root,755)
%{_datadir}/%{name}/extensions/langpack-pl@seamonkey.mozilla.org.xpi

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
