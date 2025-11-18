Name:           doned
Version:        1.0
Release:        1%{?dist}
Summary:        Discord & Others Notification Engine
License:        GPL-2.0-only
Group:          Applications/System
BuildArch:      noarch
Requires:       bash, curl
Source0:        doned
Source1:        notify-discord

%description
D.O.N.E.D. (Discord & Others Notification Engine Daemon) - CLI utility for sending notifications to Discord, Telegram, Google Chats, Microsoft Teams, and Slack from shell scripts.

%prep

%build

%install
mkdir -p %{buildroot}/usr/bin
install -m 0755 %{SOURCE0} %{buildroot}/usr/bin/doned
install -m 0755 %{SOURCE1} %{buildroot}/usr/bin/notify-discord

%files
/usr/bin/doned
/usr/bin/notify-discord

%changelog
* Tue Jul 15 2025 John Clark <johnrandallclark25@gmail.com> - 1.0-1
- Initial RPM release
