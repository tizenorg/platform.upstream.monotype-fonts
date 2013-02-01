%define _fontsdir               %{_datadir}/fonts
%define _ttfontsdir             %{_fontsdir}/truetype
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
BuildArch:      noarch
Requires(post): %{_bindir}/fc-cache

%description
Fonts package that provides the Clear Sans font

%prep
%setup -q

%build

%install
mkdir -p %{buildroot}%{_ttfontsdir}
install -m 0644 ttf/*.ttf %{buildroot}%{_ttfontsdir}/

%post
if [ -x %{_bindir}/fc-cache ]; then
    %{_bindir}/fc-cache %{_ttffontsdir} || :
fi

%postun
if [ -x %{_bindir}/fc-cache ]; then
    %{_bindir}/fc-cache %{_ttffontsdir} || :
fi

%files
%{_ttfontsdir}/*.ttf
