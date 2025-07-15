Name:           doned
Version:        1.0
Release:        1%{?dist}
Summary:        Discord & Others Notification Engine
License:        MIT
Group:          Applications/System
BuildArch:      noarch
Requires:       curl
Source0:        doned
Source1:        notify-discord

%description
D.O.N.E.D. (Discord & Others Notification Engine Daemon) - CLI utility for sending notifications to Discord, Telegram, Google Chats, Microsoft Teams, and Slack from shell scripts.

%prep

%build

%install
mkdir -p %{buildroot}/usr/local/bin
install -m 0755 %{SOURCE0} %{buildroot}/usr/local/bin/doned
install -m 0755 %{SOURCE1} %{buildroot}/usr/local/bin/notify-discord

%files
/usr/local/bin/doned
/usr/local/bin/notify-discord

%changelog
* Tue Jul 15 2025 Your Name <you@example.com> - 1.0-1
- Initial RPM release
