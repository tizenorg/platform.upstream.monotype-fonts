%define _fontsdir               %{_datadir}/fonts
%define _ttffontsdir            %{_fontsdir}/truetype
%define _miscfontsdir           %{_fontsdir}/misc
%define _fontsconfdir           %{_sysconfdir}/fonts
%define _fontsconfddir          %{_fontsconfdir}/conf.d
%define _fontsconfavaildir      %{_datadir}/%{name}/conf.avail

Name:           monotype-fonts
Version:        1.00
Release:        0
License:        Apache-2.0
Summary:        Fonts package that provides the Clear Sans font
Url:            https://01.org/clear-sans
Group:          Graphics & UI Framework/Fonts
# Upstream only provides a zip file, so source is imported manually
Source:         %{name}-%{version}.tar.xz
Source1001: 	monotype-fonts.manifest
BuildArch:      noarch
Requires(post): %{_bindir}/fc-cache

%description
Fonts package that provides the Clear Sans font

%prep
%setup -q
cp %{SOURCE1001} .

%build

%install
mkdir -p %{buildroot}%{_ttffontsdir}
install -m 0644 TTF/*.ttf %{buildroot}%{_ttffontsdir}/

%post
if [ -x %{_bindir}/fc-cache ]; then
    %{_bindir}/fc-cache %{_ttffontsdir} || :
fi

%postun
if [ -x %{_bindir}/fc-cache ]; then
    %{_bindir}/fc-cache %{_ttffontsdir} || :
fi

%files
%manifest %{name}.manifest
%license LICENSE-2.0.txt
%{_ttffontsdir}/*.ttf
