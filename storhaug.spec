Name:      storhaug
Summary:   High-Availability Add-on for NFS-Ganesha
Version:   1.0
Release:   1%{?prereltag:.%{prereltag}}%{?dist}
License:   GPLv2
URL:       https://github.com/gluster/storhaug
BuildArch: noarch
Obsoletes: storhaug-smb < 1.0
Source0:   https://github.com/gluster/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz

Requires:  glusterfs-server
Requires:  ctdb
Requires:  firewalld

%description
High-Availability add-on for storage servers

### NFS (NFS-Ganesha)
%package nfs
Summary:   storhaug NFS-Ganesha module
Requires:  %{name} = %{version}-%{release}
Requires:  nfs-ganesha-gluster

%description nfs
High-Availability NFS add-on for NFS-Ganesha

%build

%prep
%setup -q -n %{name}-%{version}

%install
install -d -m 0755 %{buildroot}%{_sbindir}
mkdir -p %{buildroot}%{_sysconfdir}/ctdb/nfs-checks-ganesha.d
mkdir -p %{buildroot}%{_sysconfdir}/sysconfig/storhaug.d
install -m 0744 storhaug %{buildroot}%{_sbindir}/storhaug
install -m 0744 20.nfs-ganesha.check %{buildroot}%{_sysconfdir}/ctdb/nfs-checks-ganesha.d/
install -m 0744 nfs-ganesha-callout %{buildroot}%{_sysconfdir}/ctdb
gzip -c storhaug.8 %{_mandir}/man8/storhaug.8.gz

%clean

%files
%{!?_licensedir:%global license %%doc}
%license LICENSE
%{_sbindir}/storhaug
%dir %{_sysconfdir}/sysconfig/storhaug.d
%{_mandir}/man8/storhaug.8.*

%files nfs
%dir %{_sysconfdir}/ctdb/nfs-checks-ganesha.d
     %{_sysconfdir}/ctdb/nfs-checks-ganesha.d/20.nfs-ganesha.check
     %{_sysconfdir}/ctdb/nfs-ganesha-callout

%changelog
* Thu Jan 10 2019 Zarren Spry <zarrenspry@gmail.com>
- Added option to run remote commands as a system user.

* Wed Jul 11 2018 Kaleb S. KEITHLEY <kkeithle at redhat.com>
- /etc/sysconfig/storhaug.d, Vendor

* Fri Jun 8 2018 Kaleb S. KEITHLEY <kkeithle at redhat.com> 1.0-1
- Reboot, Initial version
