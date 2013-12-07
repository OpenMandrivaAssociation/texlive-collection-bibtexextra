# revision 32275
# category Collection
# catalog-ctan undef
# catalog-date undef
# catalog-license undef
# catalog-version undef
Name:		texlive-collection-bibtexextra
Epoch:		1
Version:	20131201
Release:	2
Summary:	BibTeX additional styles
Group:		Publishing
URL:		http://tug.org/texlive
License:	http://www.tug.org/texlive/LICENSE.TL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/collection-bibtexextra.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires:	texlive-collection-latex
Requires:	texlive-aichej
Requires:	texlive-amsrefs
Requires:	texlive-apacite
Requires:	texlive-apalike2
Requires:	texlive-beebe
Requires:	texlive-besjournals
Requires:	texlive-bibarts
Requires:	texlive-bibexport
Requires:	texlive-bibhtml
Requires:	texlive-biblatex
Requires:	texlive-biblatex-apa
Requires:	texlive-biblatex-bwl
Requires:	texlive-biblatex-caspervector
Requires:	texlive-biblatex-chem
Requires:	texlive-biblatex-chicago
Requires:	texlive-biblatex-dw
Requires:	texlive-biblatex-fiwi
Requires:	texlive-biblatex-gost
Requires:	texlive-biblatex-historian
Requires:	texlive-biblatex-ieee
Requires:	texlive-biblatex-juradiss
Requires:	texlive-biblatex-luh-ipw
Requires:	texlive-biblatex-mla
Requires:	texlive-biblatex-musuos
Requires:	texlive-biblatex-nature
Requires:	texlive-biblatex-nejm
Requires:	texlive-biblatex-philosophy
Requires:	texlive-biblatex-phys
Requires:	texlive-biblatex-publist
Requires:	texlive-biblatex-science
Requires:	texlive-biblatex-swiss-legal
Requires:	texlive-biblatex-trad
Requires:	texlive-biblist
Requires:	texlive-bibtopic
Requires:	texlive-bibtopicprefix
Requires:	texlive-bibunits
Requires:	texlive-breakcites
Requires:	texlive-cell
Requires:	texlive-chbibref
Requires:	texlive-chicago
Requires:	texlive-chicago-annote
Requires:	texlive-chembst
Requires:	texlive-chscite
Requires:	texlive-collref
Requires:	texlive-compactbib
Requires:	texlive-custom-bib
Requires:	texlive-din1505
Requires:	texlive-dk-bib
Requires:	texlive-doipubmed
Requires:	texlive-fbs
Requires:	texlive-figbib
Requires:	texlive-footbib
Requires:	texlive-francais-bst
Requires:	texlive-geschichtsfrkl
Requires:	texlive-harvard
Requires:	texlive-harvmac
Requires:	texlive-historische-zeitschrift
Requires:	texlive-ijqc
Requires:	texlive-inlinebib
Requires:	texlive-iopart-num
Requires:	texlive-jneurosci
Requires:	texlive-jurabib
Requires:	texlive-ksfh_nat
Requires:	texlive-listbib
Requires:	texlive-logreq
Requires:	texlive-margbib
Requires:	texlive-multibib
Requires:	texlive-multibibliography
Requires:	texlive-munich
Requires:	texlive-notes2bib
Requires:	texlive-oscola
Requires:	texlive-perception
Requires:	texlive-pnas2009
Requires:	texlive-rsc
Requires:	texlive-showtags
Requires:	texlive-sort-by-letters
Requires:	texlive-splitbib
Requires:	texlive-uni-wtal-ger
Requires:	texlive-uni-wtal-lin
Requires:	texlive-urlbst
Requires:	texlive-usebib
Requires:	texlive-vak
Requires:	texlive-xcite

%description
Additional BibTeX styles and bibliography data(bases), notably
including BibLaTeX.

#-----------------------------------------------------------------------
%files

#-----------------------------------------------------------------------
%prep
%setup -c -a0

%build

%install
