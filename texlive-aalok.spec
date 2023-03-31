Name:		texlive-aalok
Version:	61719
Release:	2
Summary:	LaTeX class file for the Marathi journal 'Aalok'
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/aalok
License:	gpl3+ other-free fdl
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/aalok.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/aalok.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/aalok.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
aalok mraatthii niytkaalikaacii akssrjulnnii krnnyaakritaa
laattek-vrg. This package provides the class file for
typesetting 'Aalok', a Marathi journal with LaTeX.

%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/source/latex/aalok
%{_texmfdistdir}/tex/latex/aalok
%doc %{_texmfdistdir}/doc/latex/aalok

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
