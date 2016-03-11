#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-crayon
Version  : 1.3.1
Release  : 10
URL      : http://cran.r-project.org/src/contrib/crayon_1.3.1.tar.gz
Source0  : http://cran.r-project.org/src/contrib/crayon_1.3.1.tar.gz
Summary  : Colored Terminal Output
Group    : Development/Tools
License  : MIT
Requires: R-memoise
BuildRequires : R-memoise
BuildRequires : clr-R-helpers

%description
# Crayon - stylish terminal output in R
[![Linux Build Status](https://travis-ci.org/gaborcsardi/crayon.svg?branch=master)](https://travis-ci.org/gaborcsardi/crayon)
[![Windows Build status](https://ci.appveyor.com/api/projects/status/github/gaborcsardi/crayon?svg=true)](https://ci.appveyor.com/project/gaborcsardi/crayon)
[![](http://www.r-pkg.org/badges/version/crayon)](http://cran.rstudio.com/web/packages/crayon/index.html)
[![CRAN RStudio mirror downloads](http://cranlogs.r-pkg.org/badges/crayon)](http://cran.r-project.org/web/packages/crayon/index.html)

%prep
%setup -q -c -n crayon

%build

%install
rm -rf %{buildroot}
export LANG=C
export CFLAGS="$CFLAGS -O3 -flto -ffunction-sections -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -ffunction-sections -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library
R CMD INSTALL --install-tests --build  -l %{buildroot}/usr/lib64/R/library crayon
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc -l %{buildroot}/usr/lib64/R/library crayon || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/crayon/ANSI-256-OSX.png
/usr/lib64/R/library/crayon/ANSI-8-OSX.png
/usr/lib64/R/library/crayon/DESCRIPTION
/usr/lib64/R/library/crayon/INDEX
/usr/lib64/R/library/crayon/LICENSE
/usr/lib64/R/library/crayon/Meta/Rd.rds
/usr/lib64/R/library/crayon/Meta/hsearch.rds
/usr/lib64/R/library/crayon/Meta/links.rds
/usr/lib64/R/library/crayon/Meta/nsInfo.rds
/usr/lib64/R/library/crayon/Meta/package.rds
/usr/lib64/R/library/crayon/NAMESPACE
/usr/lib64/R/library/crayon/NEWS.md
/usr/lib64/R/library/crayon/R/crayon
/usr/lib64/R/library/crayon/R/crayon.rdb
/usr/lib64/R/library/crayon/R/crayon.rdx
/usr/lib64/R/library/crayon/README.markdown
/usr/lib64/R/library/crayon/help/AnIndex
/usr/lib64/R/library/crayon/help/aliases.rds
/usr/lib64/R/library/crayon/help/crayon.rdb
/usr/lib64/R/library/crayon/help/crayon.rdx
/usr/lib64/R/library/crayon/help/paths.rds
/usr/lib64/R/library/crayon/html/00Index.html
/usr/lib64/R/library/crayon/html/R.css
