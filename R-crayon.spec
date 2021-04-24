#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-crayon
Version  : 1.4.1
Release  : 73
URL      : https://cran.r-project.org/src/contrib/crayon_1.4.1.tar.gz
Source0  : https://cran.r-project.org/src/contrib/crayon_1.4.1.tar.gz
Summary  : Colored Terminal Output
Group    : Development/Tools
License  : MIT
BuildRequires : buildreq-R

%description
color and highlight codes. It also works in 'Emacs' 'ESS'. 'ANSI'
    color support is automatically detected. Colors and highlighting can
    be combined and nested. New styles can also be created easily.
    This package was inspired by the 'chalk' 'JavaScript' project.

%prep
%setup -q -c -n crayon
cd %{_builddir}/crayon

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1612887899

%install
export SOURCE_DATE_EPOCH=1612887899
rm -rf %{buildroot}
export LANG=C.UTF-8
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=haswell -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library crayon
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library crayon
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library crayon
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc crayon || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/crayon/DESCRIPTION
/usr/lib64/R/library/crayon/INDEX
/usr/lib64/R/library/crayon/LICENSE
/usr/lib64/R/library/crayon/Meta/Rd.rds
/usr/lib64/R/library/crayon/Meta/features.rds
/usr/lib64/R/library/crayon/Meta/hsearch.rds
/usr/lib64/R/library/crayon/Meta/links.rds
/usr/lib64/R/library/crayon/Meta/nsInfo.rds
/usr/lib64/R/library/crayon/Meta/package.rds
/usr/lib64/R/library/crayon/NAMESPACE
/usr/lib64/R/library/crayon/NEWS.md
/usr/lib64/R/library/crayon/R/crayon
/usr/lib64/R/library/crayon/R/crayon.rdb
/usr/lib64/R/library/crayon/R/crayon.rdx
/usr/lib64/R/library/crayon/help/AnIndex
/usr/lib64/R/library/crayon/help/aliases.rds
/usr/lib64/R/library/crayon/help/crayon.rdb
/usr/lib64/R/library/crayon/help/crayon.rdx
/usr/lib64/R/library/crayon/help/paths.rds
/usr/lib64/R/library/crayon/html/00Index.html
/usr/lib64/R/library/crayon/html/R.css
/usr/lib64/R/library/crayon/tests/testthat.R
/usr/lib64/R/library/crayon/tests/testthat/helper.R
/usr/lib64/R/library/crayon/tests/testthat/test-ansi256.R
/usr/lib64/R/library/crayon/tests/testthat/test-color.r
/usr/lib64/R/library/crayon/tests/testthat/test-combine.R
/usr/lib64/R/library/crayon/tests/testthat/test-has-style.r
/usr/lib64/R/library/crayon/tests/testthat/test-hyperlink.R
/usr/lib64/R/library/crayon/tests/testthat/test-make-style.r
/usr/lib64/R/library/crayon/tests/testthat/test-operations.R
/usr/lib64/R/library/crayon/tests/testthat/test-style-var.r
/usr/lib64/R/library/crayon/tests/testthat/test-styles.r
/usr/lib64/R/library/crayon/tests/testthat/test-utils.R
/usr/lib64/R/library/crayon/tests/testthat/test-vectors.r
