# Ashbloom

<div align="center">

| Swatch | Hex Code | Description |
| :---: | :---: | :--- |
| ![#D65987](https://placehold.co/80x40/D65987/D65987.png) | `#D65987` | Rose |
| ![#F6ACB4](https://placehold.co/80x40/F6ACB4/F6ACB4.png) | `#F6ACB4` | Pink |
| ![#c0a952](https://placehold.co/80x40/c0a952/c0a952.png) | `#c0a952` | Gold |
| ![#e8e2d0](https://placehold.co/80x40/e8e2d0/e8e2d0.png) | `#e8e2d0` | Cream |
| ![#44BFF1](https://placehold.co/80x40/44BFF1/44BFF1.png) | `#44BFF1` | Sky Blue |
| ![#45379B](https://placehold.co/80x40/45379B/45379B.png) | `#45379B` | Deep Purple |
| ![#202124](https://placehold.co/80x40/202124/202124.png) | `#202124` | Slate |

</div>


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


<details>
  <summary><b>Click to view Ashbloom Screenshots</b></summary>
  <br>
<p align="center">
  <img src="https://github.com/onthecouch/ashbloom/raw/main/skins/jellyfin/screenshot/login.png" alt="Ashbloom Login" width="100%">
  <br>
  <br>
  <img src="https://github.com/onthecouch/ashbloom/raw/main/skins/jellyfin/screenshot/frontsidebar.png" alt="Ashbloom Sidebar" width="100%">
  <br>
  <br>
<img src="https://github.com/onthecouch/ashbloom/raw/main/skins/jellyfin/screenshot/front.png" alt="Ashbloom Front Screenshot" width="100%">
  <br>
  <br>
  <img src="https://github.com/onthecouch/ashbloom/raw/main/skins/jellyfin/screenshot/music.png" alt="Ashbloom Seekbar" width="100%">
</p>
</details>

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


<details>
  <summary><b>Click to view Uptime Kuma Screenshot</b></summary>
  <br>
<p align="center">
 <img src="https://github.com/onthecouch/ashbloom/raw//main/skins/uptime-kuma/screenshot/uptime-kuma.png" alt="Uptime Kuma Status Page" width="100%">
 <br>
 <br>
</p>
</details>
---

**Future Stuff**
I'm planning to add more skins here as I get around to styling other services I use. For now, this repo is just a reserve for my future self.
