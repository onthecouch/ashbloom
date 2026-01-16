# Ashbloom

It's essentially my personal color palette that I've started rolling out across my self-hosted apps.

I wanted something that felt grounded but still had some life to it. The foundation is mostly dark slate and charcoal—pretty standard for dark mode lovers—but I’ve thrown in specific blooming accents to make things pop. You'll see a lot of Gold, Sky Blue, Purple, Rose, and Pink gradients throughout.

It’s a work in progress, and I’m just dumping the skins here as I make them.

---

## Skins


### Jellyfin
This one is a heavy modification of the ElegantFin theme. It creates a much darker, cleaner look with the Ashbloom gradients on seek bars and headers.

**⚠️ A quick warning:**

Might not work on some browser or phone device.

**How to install:**
1. Open your Jellyfin Dashboard.
2. Go to **General** > **Custom CSS**.
3. Paste this line in:

```css
@import url('https://cdn.jsdelivr.net/gh/onthecouch/ashbloom@main/skins/jellyfin/ashbloom-jellyfin.css');
```
**To add custom media cover of mine**
add this after previous css
```css
@import url('https://cdn.jsdelivr.net/gh/onthecouch/ashbloom@main/skins/jellyfin/custom-media-cover.css');
```

The CSS is without text title, so i can redesign it later with text title on the image directly.


### Screenshot

<p align="center">
  <img src="https://github.com/onthecouch/ashbloom/raw/main/skins/jellyfin/screenshot/front.png" alt="Ashbloom Front Screenshot" width="100%">
  <br>
  <img src="https://github.com/onthecouch/ashbloom/raw/main/skins/jellyfin/screenshot/frontsidebar.png" alt="Ashbloom Sidebar" width="100%">
  <br>
  <img src="https://github.com/onthecouch/ashbloom/raw/main/skins/jellyfin/screenshot/login.png" alt="Ashbloom Login" width="100%">
  <br>
  <img src="https://github.com/onthecouch/ashbloom/raw/main/skins/jellyfin/screenshot/music.png" alt="Ashbloom Seekbar" width="100%">
</p>


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
