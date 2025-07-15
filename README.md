# D.O.N.E.D. — Discord & Others Notification Engine Daemon

D.O.N.E.D. is a simple, extensible CLI utility for sending notifications from shell scripts to Discord, Telegram, Google Chats, Microsoft Teams, and Slack. It’s packaged for easy installation as both `.deb` and `.rpm`.

---

## Features

- Send notifications to one or more services with a single command
- Supports Discord, Telegram, Google Chats, Microsoft Teams, and Slack
- Easy setup and configuration
- Works on any Linux system (Debian/Ubuntu, RHEL/Fedora, Arch/Manjaro, etc.)
- Packaged as `.deb` and `.rpm` for easy deployment

---

## Installation

### From Prebuilt Packages

Download the latest `.deb` or `.rpm` from the `binaries/` directory.

**Debian/Ubuntu:**
```bash
sudo dpkg -i binaries/doned.deb
```

**RHEL/Fedora/Manjaro:**
```bash
sudo rpm -i binaries/doned.rpm
```

---

## Usage

### Setup

Run the setup command to configure your notification services:
```bash
doned setup
```
- Select one or more services (Discord, Telegram, Google Chats, Teams, Slack)
- Enter the required webhook URLs or tokens

### Send a Notification

Send a message to all configured services:
```bash
doned "Your message here"
```

Send to a specific service:
```bash
doned discord "Message for Discord only"
doned telegram "Message for Telegram only"
```

### Default Notification Behavior

If you run a command like:
```bash
sleep 3 && doned
```
D.O.N.E.D. will send a notification to all configured services:
```
✅ Your command 'sleep 3' has completed on <hostname>
```

### Test Notifications

Send a test notification to all configured services:
```bash
doned test
```

Send a test notification to a specific service:
```bash
doned test slack
```

### Show Status

Show your current configuration and webhook status:
```bash
doned status
```

---

## Configuration

Configuration is stored in `/etc/done.conf` and includes:
- NOTIFY_TYPES: Array of enabled services
- Service-specific tokens/URLs
- Commented template sections for all supported services

Example:
```bash
NOTIFY_TYPES=(discord telegram)
WEBHOOK_URL="https://discord.com/api/webhooks/..."
TELEGRAM_BOT_TOKEN="123456:ABC-DEF"
TELEGRAM_CHAT_ID="987654321"
```

---

## Building from Source

To build the `.deb` and `.rpm` packages yourself, see the `doned.spec` and `discord-notifier/DEBIAN` directories.

---

## Changelog

- Default: running `doned` sends a notification with the last command and hostname
- Fixed NOTIFY_TYPES array and config writing
- `doned test` and `doned status` now work for all types
- Rebuilt `.deb` and `.rpm` packages
- Warn on config overwrite in setup; config now includes commented templates for all media types

---

## License

MIT
