# Ashbloom

So, this is Ashbloom. It's essentially my personal color palette that I've started rolling out across my self-hosted apps.

I wanted something that felt grounded but still had some life to it. The foundation is mostly dark slate and charcoal—pretty standard for dark mode lovers—but I’ve thrown in specific blooming accents to make things pop. You'll see a lot of Gold, Sky Blue, Purple, Rose, and Pink gradients throughout.

It’s a work in progress, and I’m just dumping the skins here as I make them.

---

## Skins

Here’s what I have so far.

### Jellyfin
This one is a heavy modification of the ElegantFin theme. It creates a much darker, cleaner look with the Ashbloom gradients on seek bars and headers.

**⚠️ A quick warning:**
I’ve only really tested this on **Jellyfin Media Player (JMP)** on Windows. If you try to use this on a web browser (like Firefox), the header layout completely breaks. Honestly, I’m too lazy to fix the web compatibility right now since I exclusively use JMP. So, use with caution.

**How to install:**
1. Open your Jellyfin Dashboard.
2. Go to **General** > **Custom CSS**.
3. Paste this line in:

```css
@import url('https://cdn.jsdelivr.net/gh/onthecouch/ashbloom@main/skins/jellyfin/ashbloom-jellyfin.css');
```

---

### Uptime Kuma
A very stripped-down, flat theme for Uptime Kuma using the IBM Plex Mono font. It gets rid of a lot of the default bulk and replaces the status indicators with the Ashbloom colors (Gold for up, Rose for down).

**How to install:**
1. Go to **Settings** > **Appearance**.
2. Find the **Custom CSS** box.
3. Paste this line in:

```css
@import url('https://cdn.jsdelivr.net/gh/onthecouch/ashbloom@main/skins/uptime-kuma/index.css');
```

---

**Future Stuff**
I'm planning to add more skins here as I get around to styling other services I use. For now, this repo is just a reserve for my future self.
