#Firefox globals
%global moz_extensions %{_datadir}/mozilla/extensions
%global firefox_app_id \{ec8030f7-c20a-464f-9b0e-13a3a9e97384\}

#Addon
%global src_ext_id uBlock0@raymondhill.net
%global inst_dir %{moz_extensions}/%{firefox_app_id}/%{src_ext_id}

Name:           mozilla-ublock-origin
Version:        1.3.2
Release:        1%{?dist}
Summary:        An efficient blocker add-on for various browsers. Fast, potent, and lean.

Group:          Applications/Internet
License:        GPLv3
URL:            https://github.com/gorhill/uBlock
Source0:        https://github.com/gorhill/uBlock/releases/download/%{version}/uBlock0.firefox.xpi
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:      noarch
BuildRequires:  zip

%description
uBlock Origin is NOT an "ad blocker": it is a wide-spectrum blocker -- 
which happens to be able to function as a mere "ad blocker". The 
default behavior of uBlock Origin when newly installed is to block ads, 
trackers and malware sites -- through EasyList, EasyPrivacy, Peter Lowe's
ad/tracking/malware servers, various lists of malware sites, and uBlock
Origin's own filter lists.

%prep
#%setup -q -c

%build
rm -rf %{buildroot}

%install

mkdir -p %{buildroot}%{moz_extensions}/%{firefox_app_id}
install -Dp -m 644 %{SOURCE0} %{buildroot}%{inst_dir}.xpi

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%{inst_dir}.xpi

%changelog
* Tue Nov 3 2015 Chris Smart <csmart@kororaproject.org>- 1.3.2-1
- Initial build
