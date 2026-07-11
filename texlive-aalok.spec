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
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
aalok mraatthii niytkaalikaacii akssrjulnnii krnnyaakritaa laattek-vrg.
This package provides the class file for typesetting 'Aalok', a Marathi
journal with LaTeX.

