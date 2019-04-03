Name:           nvl-pg-extension
Version:        1.0
Release:        1%{?dist}
Summary:        this is a postgresql extension nvl function just like oracle
License:        APACHE
URL:            https://github.com/rongfengliang/postgres-extension-demo
%define _topdir ~/rpmbuild/SOURCES
%define buildroot %{_topdir}/%{name}‑%{version}
BuildRoot:    %{buildroot}
%description
this is a postgresql extension nvl function just like oracle
%install
%{make_install}