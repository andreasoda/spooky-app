"""Generates the Spooky website (English at the root, Italian under /it/).

Edit the texts below, then run `python3 tools/build-site.py` from the
repository root and commit the regenerated pages: both languages share the
same header, footer and structure, so they cannot drift apart.
"""
import os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
REPO = "https://github.com/andreasoda/spooky-app"
DOWNLOAD = REPO + "/releases/latest/download/Spooky.pkg"
RELEASES = REPO + "/releases"
ISSUES = REPO + "/issues"
STUDIO = "https://sokitstudio.com"
SUPPORT = "support@sokitstudio.com"
PRIVACY_MAIL = "privacy@sokitstudio.com"

T = {
    "en": {
        "lang": "en", "base": "", "other": "it/", "other_label": "Italiano",
        "nav": [("index.html", "Spooky"), ("install.html", "Install"), ("privacy.html", "Privacy"), (RELEASES, "Downloads")],
        "footer": "Spooky is made by Sokit Studio (Andrea Soda). Mac, iPad and iPhone are trademarks of Apple Inc.",
        "contact": "Questions and feedback",
    },
    "it": {
        "lang": "it", "base": "../", "other": "../", "other_label": "English",
        "nav": [("index.html", "Spooky"), ("install.html", "Installazione"), ("privacy.html", "Privacy"), (RELEASES, "Download")],
        "footer": "Spooky è un'app di Sokit Studio (Andrea Soda). Mac, iPad e iPhone sono marchi di Apple Inc.",
        "contact": "Domande e suggerimenti",
    },
}


def page(lang, file, title, description, body):
    t = T[lang]
    base = t["base"]
    links = "".join(
        f'<a href="{href if href.startswith("http") else href}"{" class=\"current\"" if href == file else ""}>{label}</a>'
        for href, label in t["nav"]
    )
    other = t["other"] + file
    html = f"""<!doctype html>
<html lang="{t['lang']}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{description}">
<link rel="icon" type="image/png" href="{base}assets/favicon.png">
<link rel="stylesheet" href="{base}assets/style.css">
</head>
<body>
<div class="wrap">
<header class="top">
  <a class="brand" href="index.html"><img src="{base}assets/icon.png" alt="">Spooky</a>
  <nav class="links">{links}<a href="{other}">{t['other_label']}</a></nav>
</header>
{body}
<footer>
  <div class="row">
    <span>{t['footer']}</span>
    <a href="mailto:{SUPPORT}">{t['contact']}</a>
  </div>
</footer>
</div>
</body>
</html>
"""
    path = os.path.join(ROOT, "" if lang == "en" else "it", file)
    with open(path, "w") as f:
        f.write(html)


# Home

HOME = {
    "en": dict(
        title="Spooky: your Mac on your iPad",
        description="Use your Mac from your iPad or iPhone, at home or away: sharp picture, smooth motion, sound and microphone.",
        body=f"""
<section class="hero">
  <img class="icon" src="assets/icon.png" alt="Spooky icon">
  <h1>Your Mac, on your iPad.</h1>
  <p class="lead">Use your Mac from your iPad or iPhone as if it were in front of you: a sharp, smooth picture, the Mac's sound, and your iPad's microphone. At home or away.</p>
  <div class="buttons">
    <a class="button" href="{DOWNLOAD}">Download for Mac</a>
    <a class="button secondary" href="install.html">How to install</a>
  </div>
  <p class="note">The iPad and iPhone app is coming soon to the App Store.</p>
</section>
<section>
  <h2>What it does</h2>
  <div class="grid">
    <div class="card"><div class="glyph">✨</div><h3>Sharp and smooth</h3><p>Up to 120 frames a second with full colour, at your iPad's own resolution, and a bitrate that follows your network.</p></div>
    <div class="card"><div class="glyph">🖥️</div><h3>Mac screen or second screen</h3><p>Show the Mac's own screen, or add a second one, like Sidecar, sized for your iPad.</p></div>
    <div class="card"><div class="glyph">🔊</div><h3>Sound and microphone</h3><p>Hear the Mac on your iPad, and use your iPad's microphone as the Mac's microphone.</p></div>
    <div class="card"><div class="glyph">⌨️</div><h3>Touch, trackpad and keyboard</h3><p>Control the Mac with touch, a trackpad or a hardware keyboard, with the pointer drawn instantly on the iPad.</p></div>
    <div class="card"><div class="glyph">🌍</div><h3>At home and away</h3><p>At home Spooky finds your Mac by itself. Away from home it connects through Tailscale, free and encrypted.</p></div>
    <div class="card"><div class="glyph">🔒</div><h3>Private by design</h3><p>A direct, encrypted connection between your devices. No accounts, no Spooky servers, no tracking.</p></div>
  </div>
</section>
<section>
  <h2>Requirements</h2>
  <div class="grid">
    <div class="card"><h3>Mac</h3><p>macOS 27 or later.</p></div>
    <div class="card"><h3>iPad or iPhone</h3><p>iPadOS or iOS 27 or later.</p></div>
    <div class="card"><h3>Away from home</h3><p>Tailscale on the Mac and on the iPad or iPhone, with the same account.</p></div>
  </div>
</section>
"""),
    "it": dict(
        title="Spooky: il tuo Mac sull'iPad",
        description="Usa il Mac dall'iPad o dall'iPhone, in casa o fuori: immagine nitida, movimento fluido, audio e microfono.",
        body=f"""
<section class="hero">
  <img class="icon" src="../assets/icon.png" alt="Icona di Spooky">
  <h1>Il tuo Mac, sul tuo iPad.</h1>
  <p class="lead">Usa il Mac dall'iPad o dall'iPhone come se ce l'avessi davanti: immagine nitida e fluida, l'audio del Mac e il microfono dell'iPad. In casa o fuori.</p>
  <div class="buttons">
    <a class="button" href="{DOWNLOAD}">Scarica per Mac</a>
    <a class="button secondary" href="install.html">Come installarlo</a>
  </div>
  <p class="note">L'app per iPad e iPhone arriverà presto sull'App Store.</p>
</section>
<section>
  <h2>Cosa fa</h2>
  <div class="grid">
    <div class="card"><div class="glyph">✨</div><h3>Nitido e fluido</h3><p>Fino a 120 fotogrammi al secondo con il colore pieno, alla risoluzione dell'iPad, e una banda che si adatta alla rete.</p></div>
    <div class="card"><div class="glyph">🖥️</div><h3>Schermo del Mac o secondo schermo</h3><p>Mostra lo schermo del Mac, oppure aggiungine un secondo, come Sidecar, su misura per l'iPad.</p></div>
    <div class="card"><div class="glyph">🔊</div><h3>Audio e microfono</h3><p>Ascolta il Mac sull'iPad, e usa il microfono dell'iPad come microfono del Mac.</p></div>
    <div class="card"><div class="glyph">⌨️</div><h3>Tocco, trackpad e tastiera</h3><p>Controlla il Mac con il tocco, un trackpad o una tastiera, con il puntatore disegnato subito sull'iPad.</p></div>
    <div class="card"><div class="glyph">🌍</div><h3>In casa e fuori</h3><p>In casa Spooky trova il Mac da solo. Fuori casa si collega con Tailscale, gratuito e cifrato.</p></div>
    <div class="card"><div class="glyph">🔒</div><h3>Privato per come è fatto</h3><p>Un collegamento diretto e cifrato tra i tuoi dispositivi. Niente account, niente server di Spooky, nessun tracciamento.</p></div>
  </div>
</section>
<section>
  <h2>Requisiti</h2>
  <div class="grid">
    <div class="card"><h3>Mac</h3><p>macOS 27 o successivo.</p></div>
    <div class="card"><h3>iPad o iPhone</h3><p>iPadOS o iOS 27 o successivo.</p></div>
    <div class="card"><h3>Fuori casa</h3><p>Tailscale sul Mac e sull'iPad o iPhone, con lo stesso account.</p></div>
  </div>
</section>
"""),
}

# Install

INSTALL = {
    "en": dict(
        title="Install Spooky",
        description="How to install Spooky on the Mac and pair your iPad or iPhone.",
        body=f"""
<div class="prose"><h1>Install Spooky</h1><p>A few minutes, once.</p></div>
<section>
<ol class="steps">
  <li><h3>Download the installer</h3><p>Download <a href="{DOWNLOAD}">Spooky.pkg</a> and open it. It installs Spooky in Applications and Spooky Microphone, which lets the Mac use your iPad's microphone. The installer is signed and notarized by Apple.</p></li>
  <li><h3>Open Spooky on the Mac</h3><p>Spooky lives in the menu bar, as a small ghost. The first time, it asks for two macOS permissions: <strong>Screen Recording</strong>, to show the Mac's screen on your iPad, and <strong>Accessibility</strong>, to move the pointer and type from your iPad. macOS asks you to confirm them in System Settings; Spooky notices by itself when they are on.</p></li>
  <li><h3>Install the app on your iPad or iPhone</h3><p>The app is coming soon to the App Store.</p></li>
  <li><h3>Pair</h3><p>On the Mac, choose <strong>Pair a Device…</strong> in Spooky's menu and scan the code with the app. If the Mac and the iPad use the same Apple Account, the Mac also shows up by itself through iCloud.</p></li>
  <li><h3>Away from home (optional)</h3><p>Install <a href="https://tailscale.com/download/mac">Tailscale on the Mac</a> and <a href="https://apps.apple.com/app/tailscale/id1470499037">on the iPad or iPhone</a>, signed in with the same account. Spooky then reaches your Mac from anywhere.</p></li>
</ol>
</section>
<section class="prose">
<h2>For the smoothest picture</h2>
<p>Apple devices share a direct Wi-Fi link (used by AirDrop and Cursor and Keyboard) that can briefly take the iPad away from your home network. If the stream stutters at regular intervals:</p>
<ul>
  <li>set your router's 5 GHz network to <strong>channel 44</strong> (149 in the United States);</li>
  <li>turn off <strong>Cursor and Keyboard</strong> on the iPad (Settings › General › AirPlay &amp; Continuity) and on the Mac (System Settings › Displays › Advanced);</li>
  <li>turn off Low Power Mode on the iPad;</li>
  <li>keep the Mac's lid open.</li>
</ul>
</section>
"""),
    "it": dict(
        title="Installare Spooky",
        description="Come installare Spooky sul Mac e associare l'iPad o l'iPhone.",
        body=f"""
<div class="prose"><h1>Installare Spooky</h1><p>Pochi minuti, una volta sola.</p></div>
<section>
<ol class="steps">
  <li><h3>Scarica il programma di installazione</h3><p>Scarica <a href="{DOWNLOAD}">Spooky.pkg</a> e aprilo. Installa Spooky in Applicazioni e Spooky Microphone, che permette al Mac di usare il microfono dell'iPad. Il pacchetto è firmato e notarizzato da Apple.</p></li>
  <li><h3>Apri Spooky sul Mac</h3><p>Spooky vive nella barra dei menu, come un piccolo fantasma. La prima volta chiede due permessi di macOS: <strong>Registrazione schermo</strong>, per mostrare lo schermo del Mac sull'iPad, e <strong>Accessibilità</strong>, per muovere il mouse e scrivere dall'iPad. macOS chiede conferma in Impostazioni di Sistema; Spooky si accorge da solo quando il permesso è attivo.</p></li>
  <li><h3>Installa l'app sull'iPad o sull'iPhone</h3><p>L'app arriverà presto sull'App Store.</p></li>
  <li><h3>Associa</h3><p>Sul Mac scegli <strong>Associa un iPad…</strong> nel menu di Spooky e inquadra il codice con l'app. Se il Mac e l'iPad usano lo stesso Account Apple, il Mac compare anche da solo, tramite iCloud.</p></li>
  <li><h3>Fuori casa (facoltativo)</h3><p>Installa <a href="https://tailscale.com/download/mac">Tailscale sul Mac</a> e <a href="https://apps.apple.com/app/tailscale/id1470499037">sull'iPad o sull'iPhone</a>, con lo stesso account. Così Spooky raggiunge il Mac da ovunque.</p></li>
</ol>
</section>
<section class="prose">
<h2>Per l'immagine più fluida</h2>
<p>I dispositivi Apple condividono un collegamento Wi-Fi diretto (lo usano AirDrop e Cursore e tastiera) che può allontanare per un attimo l'iPad dalla rete di casa. Se lo streaming fa piccoli scatti a intervalli regolari:</p>
<ul>
  <li>metti la rete a 5 GHz del router sul <strong>canale 44</strong> (149 negli Stati Uniti);</li>
  <li>spegni <strong>Cursore e tastiera</strong> sull'iPad (Impostazioni › Generali › AirPlay e Continuity) e sul Mac (Impostazioni di Sistema › Schermi › Avanzate);</li>
  <li>disattiva il Risparmio energetico sull'iPad;</li>
  <li>tieni aperto il coperchio del Mac.</li>
</ul>
</section>
"""),
}

# Privacy

PRIVACY = {
    "en": dict(
        title="Spooky privacy policy",
        description="What Spooky does with your data: it stays on your devices.",
        body=f"""
<div class="prose">
<h1>Privacy policy</h1>
<p>Last updated: 7 October 2026.</p>
<p><strong>In short: Spooky does not collect, store or share your data. Everything stays between your own devices.</strong></p>
<h2>No servers, no accounts, no tracking</h2>
<p>Spooky has no servers and no user accounts. The Mac app and the iPad and iPhone app connect to each other directly, over your local network or through Tailscale. Spooky contains no analytics, advertising or tracking code.</p>
<h2>What travels between your devices</h2>
<p>During a session the Mac sends its screen and sound to your iPad or iPhone, and your device sends back keyboard, pointer and touch input, the clipboard when you copy something, and, if you turn it on, its microphone. All of this travels encrypted, only between your paired devices, and is not recorded.</p>
<h2>Pairing</h2>
<p>When you pair a device, Spooky creates a key that only your devices know. It is stored in the Keychain and, so that your other devices find the Mac without scanning a code again, in iCloud Keychain and iCloud key-value storage under your own Apple Account, together with the Mac's name and network addresses. Apple handles this data under its own privacy policy; Spooky cannot read it from anywhere else.</p>
<h2>Permissions</h2>
<p>On the Mac, Spooky asks for Screen Recording (to show the screen), Accessibility (to move the pointer and type), local network access, and system audio (to play the Mac's sound on your device). On the iPad or iPhone it asks for local network access, the camera (only to scan the pairing code; no image is kept) and, if you turn it on, the microphone.</p>
<h2>Diagnostics</h2>
<p>The Mac app writes diagnostic logs about connection quality (for example frame rate and network delay) to your Mac only, in <code>~/Library/Logs/Spooky</code>. They are never sent anywhere. You can delete them at any time.</p>
<h2>Third parties</h2>
<p>If you use Tailscale to connect away from home, Tailscale's own privacy policy applies to that service.</p>
<h2>Contact</h2>
<p>Spooky is published by Andrea Soda (<a href="{STUDIO}">Sokit Studio</a>), the data controller for the processing described here. Privacy questions and requests: <a href="mailto:{PRIVACY_MAIL}">{PRIVACY_MAIL}</a>; support: <a href="mailto:{SUPPORT}">{SUPPORT}</a>.</p>
<h2>Support requests</h2>
<p>If you write to us, your email address and message are used only to answer you (legal basis: your request, art. 6(1)(b) and (f) GDPR) and are deleted within 24 months of the last exchange.</p>
<h2>This website</h2>
<p>This site uses no cookies, analytics or scripts. It is hosted by GitHub Pages: GitHub may log visitors' IP addresses for security, under <a href="https://docs.github.com/site-policy/privacy-policies/github-general-privacy-statement">its privacy statement</a>.</p>
<h2>Your rights</h2>
<p>You can ask for access to, correction or deletion of your data, restriction of or objection to its processing, and portability, at the address above. You can also lodge a complaint with your data protection authority; in Italy, the <a href="https://www.garanteprivacy.it">Garante per la protezione dei dati personali</a>.</p>
</div>
"""),
    "it": dict(
        title="Informativa sulla privacy di Spooky",
        description="Cosa fa Spooky con i tuoi dati: restano sui tuoi dispositivi.",
        body=f"""
<div class="prose">
<h1>Informativa sulla privacy</h1>
<p>Ultimo aggiornamento: 7 ottobre 2026.</p>
<p><strong>In breve: Spooky non raccoglie, non conserva e non condivide i tuoi dati. Tutto resta tra i tuoi dispositivi.</strong></p>
<h2>Niente server, niente account, nessun tracciamento</h2>
<p>Spooky non ha server né account utente. L'app per Mac e l'app per iPad e iPhone si collegano direttamente tra loro, sulla rete di casa o tramite Tailscale. Spooky non contiene codice di statistiche, pubblicità o tracciamento.</p>
<h2>Cosa viaggia tra i tuoi dispositivi</h2>
<p>Durante una sessione il Mac invia schermo e audio all'iPad o all'iPhone, e il dispositivo rimanda tastiera, puntatore e tocchi, gli Appunti quando copi qualcosa e, se lo attivi, il microfono. Tutto viaggia cifrato, solo tra i tuoi dispositivi associati, e non viene registrato.</p>
<h2>Associazione</h2>
<p>Quando associ un dispositivo, Spooky crea una chiave che conoscono solo i tuoi dispositivi. È salvata nel Portachiavi e, perché gli altri tuoi dispositivi trovino il Mac senza inquadrare di nuovo il codice, nel Portachiavi iCloud e nell'archivio iCloud del tuo Account Apple, insieme al nome del Mac e ai suoi indirizzi di rete. Apple gestisce questi dati secondo la propria informativa; Spooky non può leggerli da nessun altro posto.</p>
<h2>Permessi</h2>
<p>Sul Mac Spooky chiede Registrazione schermo (per mostrare lo schermo), Accessibilità (per muovere il puntatore e scrivere), l'accesso alla rete locale e all'audio di sistema (per far sentire il Mac sul dispositivo). Sull'iPad o sull'iPhone chiede l'accesso alla rete locale, la fotocamera (solo per inquadrare il codice di associazione; nessuna immagine viene conservata) e, se lo attivi, il microfono.</p>
<h2>Diagnostica</h2>
<p>L'app per Mac scrive dei log diagnostici sulla qualità del collegamento (per esempio fotogrammi al secondo e ritardo di rete) solo sul tuo Mac, in <code>~/Library/Logs/Spooky</code>. Non vengono mai inviati da nessuna parte. Puoi cancellarli quando vuoi.</p>
<h2>Terze parti</h2>
<p>Se usi Tailscale per collegarti fuori casa, per quel servizio vale l'informativa sulla privacy di Tailscale.</p>
<h2>Contatti</h2>
<p>Spooky è pubblicata da Andrea Soda (<a href="{STUDIO}">Sokit Studio</a>), titolare dei trattamenti descritti qui. Domande e richieste sulla privacy: <a href="mailto:{PRIVACY_MAIL}">{PRIVACY_MAIL}</a>; assistenza: <a href="mailto:{SUPPORT}">{SUPPORT}</a>.</p>
<h2>Richieste di assistenza</h2>
<p>Se ci scrivi, il tuo indirizzo email e il messaggio servono solo a risponderti (base giuridica: la tua richiesta, art. 6, par. 1, lett. b e f del GDPR) e vengono cancellati entro 24 mesi dall'ultimo scambio.</p>
<h2>Questo sito</h2>
<p>Questo sito non usa cookie, statistiche né script. È ospitato da GitHub Pages: GitHub può registrare l'indirizzo IP dei visitatori per motivi di sicurezza, secondo <a href="https://docs.github.com/site-policy/privacy-policies/github-general-privacy-statement">la propria informativa</a>.</p>
<h2>I tuoi diritti</h2>
<p>Puoi chiedere all'indirizzo sopra l'accesso ai tuoi dati, la rettifica, la cancellazione, la limitazione del trattamento, l'opposizione e la portabilità. Puoi anche proporre reclamo al <a href="https://www.garanteprivacy.it">Garante per la protezione dei dati personali</a>.</p>
</div>
"""),
}

for lang in ("en", "it"):
    for file, content in (("index.html", HOME), ("install.html", INSTALL), ("privacy.html", PRIVACY)):
        page(lang, file, content[lang]["title"], content[lang]["description"], content[lang]["body"])
print("ok")
