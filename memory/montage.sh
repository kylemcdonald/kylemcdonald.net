#!/usr/bin/env bash

cd cache
grep "jpg" ../content.md | \
	cut -d'(' -f2 | \
	cut -d')' -f1 | \
	head -n4 | \
	xargs -n1 curl -O
montage *.jpg -geometry 512x512+0+0 ../montage.jpg
cd ..
