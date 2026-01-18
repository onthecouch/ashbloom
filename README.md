<div align="center">
<h1>Ashbloom</h1>
</div>

<div align="center">

| Swatch | Hex Code | Description |
| :---: | :---: | :--- |
| ![#F04770](https://placehold.co/80x40/F04770/F04770.png) | `#F04770` | Rose |
| ![#FF9E64](https://placehold.co/80x40/FF9E64/FF9E64.png) | `#FF9E64` | Orange |
| ![#F2CD60](https://placehold.co/80x40/F2CD60/F2CD60.png) | `#F2CD60` | Gold |
| ![#6DEcb9](https://placehold.co/80x40/6DEcb9/6DEcb9.png) | `#6DEcb9` | Mint |
| ![#3DD6F5](https://placehold.co/80x40/3DD6F5/3DD6F5.png) | `#3DD6F5` | Cyan |
| ![#9E86FF](https://placehold.co/80x40/9E86FF/9E86FF.png) | `#9E86FF` | Purple |
| ![#e8e2d0](https://placehold.co/80x40/e8e2d0/e8e2d0.png) | `#e8e2d0` | Cream |
| ![#202124](https://placehold.co/80x40/202124/202124.png) | `#202124` | Slate |

</div>


It's essentially my personal color palette that I've started rolling out across my self-hosted apps.

I wanted something that felt grounded but still had some life to it. The foundation is mostly dark slate and charcoal—pretty standard for dark mode lovers—but I’ve thrown in specific blooming accents to make things pop. You'll see a lot of Gold, Sky Blue, Purple, Rose, and Pink gradients throughout.

It’s a work in progress, and I’m just dumping the skins here as I make them.

---

## Skins

### oh-my-posh

<details>
  <summary><b>Click to view oh-my-posh theme</b></summary>
  <br>
<p align="center">
   <img src="https://raw.githubusercontent.com/onthecouch/ashbloom/main/skins/oh-my-posh/scrot.png" alt="oh-my-posh term style' width="100%">
</p>
</details>
<br>

**Typography:** Maple Mono NF (Regular, 14pt).

**Global Behavior**

  * Transient Prompt: Enabled. Collapses the previous prompt into a single Rose dot (•) upon execution to prevent visual clutter.

  * Console Title: Dynamic. Updates window title to Ashbloom :: <CurrentFolder>.

  * Shell Integration: Enabled. Supports VS Code terminal navigation markers.

**Segment Layout:**

  * **Block 1 (Left):** Date (02 Jan 15:04) → Shell Icon → Git Status (Branch/Upstream/Staging).

  * **Block 2 (Right):** Last Exit Code (Conditional) → Execution Time.

  * **Block 3 (Left):** Current Path (Full).

  * **Block 4 (Left):** Root Indicator (!) → Input Chevron (❯).

**How to install**
1. Download the themes.
2. Open Powershell and run

   ```powershell
      notepad $PROFILE
   ```

3. Add the path `oh-my-posh init pwsh --config "$HOME\.config\oh-my-posh\ashbloom.omp.json" | Invoke-Expression`
4. Reload `. $PROFILE`

### k9s

<details>
  <summary><b>Click to view k9s skins</b></summary>
  <br>
<p align="center">
   <img src="" alt="k9s screenshot' width="100%">
</p>
</details>
<br>

**How to install**
1. Download the skins and put it in k9s skins folder.
`cd $env:LOCALAPPDATA\k9s`

2. Update the config files in the same directory

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
