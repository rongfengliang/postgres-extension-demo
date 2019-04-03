Name:           nvl-pg-extension
Version:        1.0
Release:        1%{?dist}
Summary:        this is a postgresql extension nvl function just like oracle
License:        APACHE
URL:            https://github.com/rongfengliang/postgres-extension-demo
Source:        https://github.com/rongfengliang/pg-extension-rpm-demo/archive/nvl-pg-extension-1.0.zip

%define _topdir        /root/postgres-extension-demo/extension

%description
this is a postgresql extension nvl function just like oracle

%install
%{make_install}

%files
%{_topdir}/nvlfunc--1.0.sql
%{_topdir}/nvlfunc.control