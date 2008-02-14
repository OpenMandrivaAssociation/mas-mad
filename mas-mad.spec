%define name mas-mad
%define version 0.6.3
%define release %mkrel 4
%define oname mas-codec_mp1a_mad

Summary: MAD mp3 decoder for MAS
Name: %{name}
Version: %{version}
Release: %{release}
Source0: %{oname}-%{version}.tar.gz
License: GPL
Group: Sound
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
URL: http://www.mediaapplicationserver.net/indexframes.html
BuildRequires: libmas-devel > 0.6.2-1mdk 
BuildRequires: libmad-devel
BuildRequires: imake
ExcludeArch: x86_64

%description
This is a mp3 decoder plugin for MAS based on the MAD library.

%prep
%setup -q -n %oname-%version

%build
masmkmf
make ||:

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%_libdir/mas/libmas_codec_mp1a_mad_device.so*
