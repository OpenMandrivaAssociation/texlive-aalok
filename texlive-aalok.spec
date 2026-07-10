%global tl_name aalok
%global tl_revision 76924

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.6
Release:	%{tl_revision}.1
Summary:	LaTeX class file for the Marathi journal Aalok
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/unicodetex/latex/aalok
License:	gpl3+ other-free fdl
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/aalok.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/aalok.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/aalok.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
Requires(pre):	texlive-tlpkg
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
aalok mraatthii niytkaalikaacii akssrjulnnii krnnyaakritaa laattek-vrg.
This package provides the class file for typesetting 'Aalok', a Marathi
journal with LaTeX.

%prep
%setup -q -c -a1 -a2
rm -rf tlpkg
if [ -d RELOC ]; then
	cp -a RELOC/. .
	rm -rf RELOC
fi

%build

%install
mkdir -p %{buildroot}%{_datadir}/texmf-dist
# Flat tlnet layout: tex/ doc/ source/ fonts/ ... -> texmf-dist/
if [ -d texmf-dist ]; then
	cp -a texmf-dist/. %{buildroot}%{_datadir}/texmf-dist/
elif [ -d texmf ]; then
	mkdir -p %{buildroot}%{_datadir}/texmf
	cp -a texmf/. %{buildroot}%{_datadir}/texmf/
else
	for d in * .[!.]* ..?*; do
		[ -e "$d" ] || continue
		case "$d" in tlpkg|RELOC) continue ;; esac
		cp -a "$d" %{buildroot}%{_datadir}/texmf-dist/
	done
fi
rm -rf %{buildroot}%{_datadir}/texmf-dist/tlpkg

%files
%dir %{_datadir}/texmf-dist
%dir %{_datadir}/texmf-dist/doc
%dir %{_datadir}/texmf-dist/source
%dir %{_datadir}/texmf-dist/tex
%dir %{_datadir}/texmf-dist/doc/latex
%dir %{_datadir}/texmf-dist/source/latex
%dir %{_datadir}/texmf-dist/tex/latex
%dir %{_datadir}/texmf-dist/doc/latex/aalok
%dir %{_datadir}/texmf-dist/source/latex/aalok
%dir %{_datadir}/texmf-dist/tex/latex/aalok
%doc %{_datadir}/texmf-dist/doc/latex/aalok/COPYING
%doc %{_datadir}/texmf-dist/doc/latex/aalok/LICENSE.md
%doc %{_datadir}/texmf-dist/doc/latex/aalok/README.txt
%doc %{_datadir}/texmf-dist/doc/latex/aalok/aalok.pdf
%doc %{_datadir}/texmf-dist/source/latex/aalok/aalok.dtx
%doc %{_datadir}/texmf-dist/source/latex/aalok/aalok.ins
%{_datadir}/texmf-dist/tex/latex/aalok/aalok.cls
