#!/bin/sh
# based on script by (c) vip at linux.pl, wolf at pld-linux.org

LIBDIR="@LIBDIR@/seamonkey"

SEAMONKEY="$LIBDIR/seamonkey"
PWD=${PWD:-$(pwd)}

if [ "$1" = "-remote" ]; then
	exec $SEAMONKEY "$@"
else
	if ! $SEAMONKEY -remote 'ping()' 2>/dev/null; then
		if [ -f "$PWD/$1" ]; then
			exec $SEAMONKEY "file://$PWD/$1"
		else
			exec $SEAMONKEY "$@"
		fi
	else
		if [ -z "$1" ]; then
			exec $SEAMONKEY -remote 'xfeDoCommand(openBrowser)'
		elif [ "$1" = "-mail" ]; then
			exec $SEAMONKEY -remote 'xfeDoCommand(openInbox)'
		elif [ "$1" = "-compose" -o "$1" = "-editor" ]; then
			exec $SEAMONKEY -remote 'xfeDoCommand(composeMessage)'
		else
			if [ -f "$PWD/$1" ]; then
				URL="file://$PWD/$1"
			else
				URL="$1"
			fi
			if ! grep -q browser.tabs.opentabfor.middleclick.*false ~/.seamonkey/*/prefs.js; then
				exec $SEAMONKEY -new-tab "$URL"
			else
				exec $SEAMONKEY -new-window "$URL"
			fi
		fi
	fi
fi
