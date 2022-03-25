%global debug_package %{nil}
Summary: Intel Memory and Storage Tool (MAS)
Name: intelmas
Version: 1.12
Release: 1%{?dist}
License: custom

Url: https://www.intel.com/content/www/us/en/download/19520/
Source0: https://downloadmirror.intel.com/690882/Intel_MAS_CLI_Tool_Linux_%{version}.zip

BuildRequires: bsdtar

%define _build_id_links none

%description
Intel Memory and Storage Tool (MAS) supports firmware upgrades and 4Kn sector size changes for PCIe/NVMe/SATA flash/Optane SSDs

%prep
%setup -c

%build
bsdtar -xf %{name}-*.x86_64.rpm

%install
cp -ax %{_builddir}/%{name}-%{version}/usr %{buildroot}/

%files
%{_bindir}/%{name}
/usr/lib/%{name}/
