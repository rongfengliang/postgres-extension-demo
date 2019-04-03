Name:           nvl-pg-extension
Version:        1.0
Release:        1%{?dist}
Summary:        this is a postgresql extension nvl function just like oracle
License:        APACHE
URL:            https://github.com/rongfengliang/postgres-extension-demo
%define _topdir ~/rpmbuild/SOURCES
%define buildroot %{_topdir}/%{name}‑%{version}
%description
this is a postgresql extension nvl function just like oracle
%install
%{make_install}
%files
%{buildroot}/%{name}‑%{version}/Makefile
%{buildroot}/%{name}‑%{version}/nvlfunc--1.0.sql
%{buildroot}/%{name}‑%{version}/nvlfunc.control


