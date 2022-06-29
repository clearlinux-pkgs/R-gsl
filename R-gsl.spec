#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-gsl
Version  : 2.1.7.1
Release  : 6
URL      : https://cran.r-project.org/src/contrib/gsl_2.1-7.1.tar.gz
Source0  : https://cran.r-project.org/src/contrib/gsl_2.1-7.1.tar.gz
Summary  : Wrapper for the Gnu Scientific Library
Group    : Development/Tools
License  : GPL-3.0
Requires: R-gsl-lib = %{version}-%{release}
BuildRequires : buildreq-R
BuildRequires : gsl-dev

%description
An R wrapper for some of the functionality of the
 Gnu Scientific Library.

%package lib
Summary: lib components for the R-gsl package.
Group: Libraries

%description lib
lib components for the R-gsl package.


%prep
%setup -q -c -n gsl
cd %{_builddir}/gsl

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1641030509

%install
export SOURCE_DATE_EPOCH=1641030509
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
echo "CFLAGS = $CFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper" > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library gsl
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v4 -ftree-vectorize -mno-vzeroupper  " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library gsl
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library gsl
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc gsl || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/gsl/CITATION
/usr/lib64/R/library/gsl/DESCRIPTION
/usr/lib64/R/library/gsl/INDEX
/usr/lib64/R/library/gsl/Meta/Rd.rds
/usr/lib64/R/library/gsl/Meta/features.rds
/usr/lib64/R/library/gsl/Meta/hsearch.rds
/usr/lib64/R/library/gsl/Meta/links.rds
/usr/lib64/R/library/gsl/Meta/nsInfo.rds
/usr/lib64/R/library/gsl/Meta/package.rds
/usr/lib64/R/library/gsl/Meta/vignette.rds
/usr/lib64/R/library/gsl/NAMESPACE
/usr/lib64/R/library/gsl/R/gsl
/usr/lib64/R/library/gsl/R/gsl.rdb
/usr/lib64/R/library/gsl/R/gsl.rdx
/usr/lib64/R/library/gsl/doc/gslpaper.R
/usr/lib64/R/library/gsl/doc/gslpaper.Rnw
/usr/lib64/R/library/gsl/doc/gslpaper.pdf
/usr/lib64/R/library/gsl/doc/index.html
/usr/lib64/R/library/gsl/gsl_stickermaker.R
/usr/lib64/R/library/gsl/help/AnIndex
/usr/lib64/R/library/gsl/help/aliases.rds
/usr/lib64/R/library/gsl/help/figures/gsl.png
/usr/lib64/R/library/gsl/help/gsl.rdb
/usr/lib64/R/library/gsl/help/gsl.rdx
/usr/lib64/R/library/gsl/help/paths.rds
/usr/lib64/R/library/gsl/html/00Index.html
/usr/lib64/R/library/gsl/html/R.css

%files lib
%defattr(-,root,root,-)
/usr/lib64/R/library/gsl/libs/gsl.so
/usr/lib64/R/library/gsl/libs/gsl.so.avx2
/usr/lib64/R/library/gsl/libs/gsl.so.avx512
