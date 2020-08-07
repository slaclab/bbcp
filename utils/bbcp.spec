# package information
#
# Building:
#    rpmbuild -ba --clean --define "commit  3c0b6c49" bbcp.spec
#

%define instdir  /usr

Name:        bbcp
Version:     14.9.2
Release:     1%{?dist}

Vendor:      SLAC
License:     GNU LGPL v3
Group:       External packages
URL:         http://www.slac.stanford.edu/~abh/bbcp/
Packager:    Wilko Kroeger <wilko@slac.stanford.edu>
Source:      %{name}-%{version}-%{commit}.tar.gz
BuildRoot:   %{_tmppath}/%{pkg}-%{version}
Prefix:      /usr
Autoreq:     0 
AutoReqProv: 0

Summary:     Securely and quickly copy data from source to target.  

%description
bbcp is a point-to-point network file copy application written by Andy Hanushevsky at SLAC. 
It is capable of transferring files at approaching line speeds in the WAN.


# =============== Scripts =====================

%prep
%setup -n %{name}-%{version}-%{commit} -q

%build
cd src
DEST_SYSNAME=linux  make


%install
install -d %{buildroot}%{instdir}/bin
cp bin/linux/bbcp %{buildroot}%{instdir}/bin/


%clean
rm -rf %{buildroot}


%files
%{instdir}/bin/bbcp

# ================= ChangeLog =========================

%changelog

* Wed Nov 5 2014 Wilko Kroeger  <wilko@slac.stanford.edu> 14.9.2-1
- bbcp from commit 3c0b6c49.

