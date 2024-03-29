%global debug_package %{nil}
%global shortname sst
Summary: Solidigm Storage Tool (SST)
Name: solidigm
Version: 1.3
Release: 1%{?dist}
License: custom
BuildRequires: bsdtar
Url: https://www.intel.com/content/www/us/en/download/715595/
Source0: https://downloadmirror.intel.com/743764/SST_CLI_Linux_%{version}.zip

%define _build_id_links none

%description
Solidigm Storage Tool (SST) supports firmware upgrades and 4Kn sector size changes for Intel and Solidigm PCIe/NVMe/SATA NAND SSDs

%prep
%setup -c

%build
bsdtar -xf %{shortname}-*.x86_64.rpm

%install
cp -ax %{_builddir}/%{name}-%{version}/usr %{buildroot}/

%files
%{_bindir}/%{shortname}
/usr/lib/%{name}/
/usr/share/doc/%{shortname}/
