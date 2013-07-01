%define _fontsdir               %{_datadir}/fonts
%define _ttffontsdir            %{_fontsdir}/truetype
%define _miscfontsdir           %{_fontsdir}/misc
%define _fontsconfdir           %{_sysconfdir}/fonts
%define _fontsconfddir          %{_fontsconfdir}/conf.d
%define _fontsconfavaildir      %{_datadir}/%{name}/conf.avail

Name:           monotype-fonts
Version:        0.0.1
Release:        0
License:        Intel Proprietary
Summary:        Fonts package that provides the Clear Sans font
Url:            http://www.intel.com/
Group:          System/Fonts
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
install -m 0644 ttf/*.ttf %{buildroot}%{_ttffontsdir}/

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
%license COPYING
%{_ttffontsdir}/*.ttf
