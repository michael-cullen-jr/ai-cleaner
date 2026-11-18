"""Generate the SEO guide pages (EN + ES) and sitemap.xml.

Usage:  python tools/build_guides.py
Edit the GUIDES list below to change or add articles, then run the script and commit.
"""
import html, json, pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent
SITE = 'https://iacleaner.com'
UPDATED = '2026-11-18'

T = {
  'en': {'home': '/', 'guides': '/guides/', 'guides_name': 'Guides', 'open': 'Open IA Cleaner', 'files': '/#images',
         'cta_title': 'Clean your files in seconds', 'cta_text': 'Free, no sign-up, and everything runs in your browser — nothing is uploaded.',
         'related': 'More guides', 'updated': 'Updated', 'read': 'min read', 'footer': 'IA Cleaner · Private by design — your files never leave your device.',
         'idx_title': 'Guides — remove AI metadata and hidden characters | IA Cleaner',
         'idx_desc': 'Step-by-step guides to remove C2PA, EXIF and PDF metadata and to clean hidden characters from AI-generated text.',
         'idx_h1': 'Guides', 'idx_lead': 'Practical, step-by-step guides about the hidden data inside your files — and how to remove it.',
         'locale': 'en_US'},
  'es': {'home': '/es/', 'guides': '/es/guias/', 'guides_name': 'Guías', 'open': 'Abrir IA Cleaner', 'files': '/es/#images',
         'cta_title': 'Limpia tus archivos en segundos', 'cta_text': 'Gratis, sin registro y todo se procesa en tu navegador: no se sube nada.',
         'related': 'Más guías', 'updated': 'Actualizado', 'read': 'min de lectura', 'footer': 'IA Cleaner · Privado por diseño: tus archivos nunca salen de tu dispositivo.',
         'idx_title': 'Guías: elimina metadatos de IA y caracteres ocultos | IA Cleaner',
         'idx_desc': 'Guías paso a paso para quitar metadatos C2PA, EXIF y de PDF, y para limpiar caracteres ocultos de textos generados con IA.',
         'idx_h1': 'Guías', 'idx_lead': 'Guías prácticas, paso a paso, sobre los datos ocultos que llevan tus archivos y cómo eliminarlos.',
         'locale': 'es_ES'},
}

GUIDES = [
 {
  'id': 'instagram',
  'en': {
   'slug': 'instagram-ai-info-label',
   'title': 'Why Instagram shows “AI info” on your photo — and how to remove the metadata behind it',
   'seo_title': 'Instagram “AI info” Label on Your Photo? Why It Happens & How to Remove the Metadata',
   'desc': 'Instagram and Facebook read C2PA and IPTC metadata to add the “AI info” label — even to real photos with small AI edits. Here is how to check and clean your image before posting.',
   'lead': 'Posted a real photo and Instagram tagged it with “AI info”? It is usually not the pixels — it is the metadata your editing app wrote into the file. Here is how it works and how to clean it.',
   'cta': 'images', 'mins': 5,
   'body': '''
<h2>What is the “AI info” label?</h2>
<p>Meta adds an <strong>“AI info”</strong> label (formerly “Made with AI”) to posts, Reels and Stories on Instagram, Facebook and Threads when it believes an image was created or modified with AI. Depending on the case it appears under your username or in the post’s menu.</p>

<h2>Why does my real photo get the label?</h2>
<p>One of the main signals Meta reads is the <strong>metadata inside the file</strong>, using two industry standards:</p>
<ul>
<li><strong>C2PA / Content Credentials:</strong> a signed record that AI generators and some editors embed in the image.</li>
<li><strong>IPTC <code>DigitalSourceType</code></strong> in the XMP metadata, with values such as <code>trainedAlgorithmicMedia</code> (fully AI-generated) or <code>compositeWithTrainedAlgorithmicMedia</code> (a photo edited with AI).</li>
</ul>
<p>Editing apps can write these fields as soon as you use a generative feature — for example <strong>Generative Fill or Generative Remove</strong> in Photoshop or Lightroom, or AI erase tools on some phones. That is why photographers often see the label on genuine photos where AI only removed a small object.</p>

<h2>Step 1 — Check what your image contains</h2>
<ol>
<li>Open <a href="/#images">IA Cleaner → Images</a>.</li>
<li>Drop the exact file you were going to post.</li>
<li>Look for entries marked <strong>AI</strong>, such as <em>XMP</em> with <code>DigitalSourceType</code> or <em>JUMBF / C2PA Content Credentials</em>.</li>
</ol>

<h2>Step 2 — Remove the metadata and post the clean copy</h2>
<ol>
<li>Click <strong>Download</strong> to get the cleaned image. It is cleaned <strong>losslessly</strong> — same pixels, no extra compression.</li>
<li>Upload that cleaned file to Instagram.</li>
<li>Make cleaning the <strong>last step</strong>: if you open and re-export the image in an editor afterwards, it may write the metadata again.</li>
</ol>
<p>On a phone, open <a href="/#images">iacleaner.com</a> in your browser, choose the photo from your gallery, download the clean copy and post that one.</p>

<h2>What this can’t guarantee</h2>
<ul>
<li>Metadata is <strong>one</strong> of the signals. Meta also looks for invisible watermarks embedded in the pixels (such as Google’s SynthID), uses its own detection, and applies the label when you turn on <em>“Add AI label”</em> yourself. Removing metadata doesn’t affect those.</li>
<li>Meta’s rules ask you to <strong>disclose realistic content made or significantly altered with AI</strong>, and it may add a label or take action if you don’t. If your image is AI-generated, label it — this tool is for files where the metadata doesn’t reflect what you actually did.</li>
</ul>
'''},
  'es': {
   'slug': 'etiqueta-ia-instagram',
   'title': 'Por qué Instagram pone «Información de IA» en tu foto y cómo quitar los metadatos que la activan',
   'seo_title': 'Etiqueta «Información de IA» en Instagram: por qué sale y cómo quitarla',
   'desc': '¿Instagram marca tu foto, publicación o historia con «Información de IA»? Suele deberse a metadatos C2PA o IPTC. Compruébalo y quítalos gratis en tu navegador, sin subir la foto. Guía paso a paso.',
   'lead': '¿Has subido una foto real e Instagram la ha marcado con «Información de IA»? Normalmente no son los píxeles: son los metadatos que tu app de edición escribió en el archivo. Te explicamos cómo funciona y cómo limpiarlo.',
   'cta': 'images', 'mins': 5,
   'body': '''
<h2>¿Qué es la etiqueta «Información de IA»?</h2>
<p>Meta añade la etiqueta <strong>«Información de IA»</strong> (antes «Hecho con IA») a publicaciones, reels e historias de Instagram, Facebook y Threads cuando cree que una imagen se ha creado o modificado con IA. Según el caso, aparece bajo tu nombre de usuario o en el menú de la publicación.</p>

<h2>¿Por qué sale en mi foto real?</h2>
<p>Una de las principales señales que lee Meta son los <strong>metadatos del archivo</strong>, según dos estándares del sector:</p>
<ul>
<li><strong>C2PA / Content Credentials:</strong> un registro firmado que los generadores de IA y algunos editores incrustan en la imagen.</li>
<li><strong>IPTC <code>DigitalSourceType</code></strong> en los metadatos XMP, con valores como <code>trainedAlgorithmicMedia</code> (generada totalmente con IA) o <code>compositeWithTrainedAlgorithmicMedia</code> (foto editada con IA).</li>
</ul>
<p>Las apps de edición pueden escribir estos campos en cuanto usas una función generativa, por ejemplo el <strong>Relleno generativo o Eliminar generativo</strong> de Photoshop o Lightroom, o el borrador con IA de algunos móviles. Por eso muchos fotógrafos ven la etiqueta en fotos auténticas en las que la IA solo quitó un objeto pequeño.</p>

<h2>Paso 1: revisa qué contiene tu imagen</h2>
<ol>
<li>Abre <a href="/es/#images">IA Cleaner → Imágenes</a>.</li>
<li>Arrastra exactamente el archivo que ibas a publicar.</li>
<li>Busca entradas marcadas con <strong>IA</strong>, como <em>XMP</em> con <code>DigitalSourceType</code> o <em>JUMBF / C2PA Content Credentials</em>.</li>
</ol>

<h2>Paso 2: quita los metadatos y publica la copia limpia</h2>
<ol>
<li>Pulsa <strong>Descargar</strong> para obtener la imagen limpia. Se limpia <strong>sin pérdida</strong>: mismos píxeles, sin compresión extra.</li>
<li>Sube ese archivo limpio a Instagram.</li>
<li>Haz que limpiar sea el <strong>último paso</strong>: si después vuelves a abrir y exportar la imagen en un editor, puede volver a escribir los metadatos.</li>
</ol>
<p>Desde el móvil, abre <a href="/es/#images">iacleaner.com</a> en el navegador, elige la foto de tu galería, descarga la copia limpia y publica esa.</p>

<h2>Lo que no puede garantizar</h2>
<ul>
<li>Los metadatos son <strong>una</strong> de las señales. Meta también busca marcas de agua invisibles integradas en los píxeles (como SynthID de Google), usa su propia detección y pone la etiqueta si tú activas <em>«Añadir etiqueta de IA»</em>. Quitar los metadatos no afecta a nada de eso.</li>
<li>Las normas de Meta piden <strong>declarar el contenido realista creado o muy modificado con IA</strong>, y pueden añadir la etiqueta o tomar medidas si no lo haces. Si tu imagen está generada con IA, etiquétala: esta herramienta es para archivos cuyos metadatos no reflejan lo que de verdad hiciste.</li>
</ul>
'''},
 },
 {
  'id': 'tiktok',
  'en': {
   'slug': 'tiktok-ai-generated-label',
   'title': 'Why TikTok labels your photo or video “AI-generated” — and how to remove the metadata behind it',
   'seo_title': 'TikTok “AI-generated” Label on Your Photo or Video? Why It Happens & How to Remove It',
   'desc': 'TikTok reads C2PA Content Credentials in the photos and videos you upload to add the “AI-generated” label automatically. Here is how to check your images (JPG, PNG) and videos (MP4, MOV) and clean them before posting.',
   'lead': 'Posted a photo, a carousel or a video and TikTok tagged it “AI-generated” even though you only used AI for a small part of it? The label is often triggered by metadata inside the file. Here is how it works and how to clean it.',
   'cta': 'images', 'mins': 5,
   'body': '''
<h2>What is TikTok’s “AI-generated” label?</h2>
<p>TikTok shows an <strong>“AI-generated”</strong> label on videos and photos that were created or significantly edited with AI. It can appear because you turned on the AI-generated content setting yourself, because the content was made with TikTok’s own AI effects, or because TikTok detected it automatically.</p>

<h2>How TikTok detects it automatically</h2>
<p>TikTok reads <strong>C2PA Content Credentials</strong>: a signed record that many AI generators and some editing apps embed in the file, saying how it was made. If the record says AI was involved, TikTok can add the label as soon as you upload.</p>
<p>In a video, that information lives in special boxes of the MP4 or MOV container, next to other metadata:</p>
<ul>
<li><strong>C2PA manifest</strong> — the Content Credentials themselves.</li>
<li><strong>XMP</strong> — can include the IPTC field <code>DigitalSourceType</code> with values like <code>trainedAlgorithmicMedia</code>.</li>
<li><strong>User data</strong> — the app or encoder that produced the video, and often the <strong>GPS location</strong> where it was recorded.</li>
</ul>
<h2>Photos and carousels</h2>
<p>Photo posts work the same way. An image made or edited with an AI tool can carry C2PA Content Credentials and XMP fields such as <code>DigitalSourceType</code>, plus EXIF data like the camera, the editing app and the GPS location. If you post several images in a carousel, each one can carry its own metadata, so clean all of them — IA Cleaner lets you drop them at once and download everything in a single ZIP.</p>

<h2>Step 1 — Check what your video contains</h2>
<ol>
<li>Open IA Cleaner → <a href="/#images">Images</a> (photos) or <a href="/#video">Video</a>.</li>
<li>Drop the photos (JPG, PNG, WebP) or the video (MP4, MOV) you were going to post. You can also do it from your phone’s browser.</li>
<li>Look for entries such as <em>C2PA / Content Credentials (uuid)</em>, <em>XMP (uuid)</em> or <em>User data (udta)</em>, and for AI-related words in the report.</li>
</ol>

<h2>Step 2 — Remove the metadata and upload the clean copy</h2>
<ol>
<li>Click <strong>Download clean image</strong> or <strong>Download clean video</strong> (or <em>Download all</em> for a carousel). Cleaning is <strong>lossless</strong>: pixels and frames are not re-encoded, so quality stays the same.</li>
<li>Upload those files to TikTok.</li>
<li>Clean it as the <strong>last step</strong>: if you open and export the video again in an editor, it may write the metadata back.</li>
</ol>

<h2>What this can’t guarantee</h2>
<ul>
<li>Metadata is <strong>one</strong> of the signals. Content made with TikTok’s own AI effects is labeled by TikTok itself, TikTok has its own detection, and it has announced invisible watermarks for AI content made with its tools. Removing metadata doesn’t affect any of that.</li>
<li>TikTok’s rules ask you to <strong>label realistic content that was generated or significantly edited with AI</strong>, and unlabeled content can be labeled, limited or removed. If your video is AI-generated, label it — this tool is for files whose metadata doesn’t reflect what you actually did, and for removing private data like your location.</li>
</ul>
'''},
  'es': {
   'slug': 'etiqueta-ia-tiktok',
   'title': 'Por qué TikTok marca tu foto o vídeo como «Generado por IA» y cómo quitar los metadatos que lo activan',
   'seo_title': 'Etiqueta «Generado por IA» en TikTok: por qué sale y cómo quitarla',
   'desc': '¿TikTok marca tu foto o vídeo como «Generado por IA»? Suele deberse a metadatos C2PA. Compruébalo y límpialos gratis, sin perder calidad y sin subir el archivo.',
   'lead': '¿Has subido una foto, un carrusel o un vídeo y TikTok lo ha marcado como «Generado por IA» aunque solo usaste la IA para una parte pequeña? Muchas veces la etiqueta la activan los metadatos del archivo. Te explicamos cómo funciona y cómo limpiarlo.',
   'cta': 'images', 'mins': 5,
   'body': '''
<h2>¿Qué es la etiqueta «Generado por IA» de TikTok?</h2>
<p>TikTok muestra la etiqueta <strong>«Generado por IA»</strong> en vídeos y fotos creados o muy editados con IA. Puede aparecer porque tú activaste el ajuste de contenido generado por IA, porque usaste los efectos de IA de TikTok o porque TikTok lo detectó automáticamente.</p>

<h2>Cómo lo detecta TikTok automáticamente</h2>
<p>TikTok lee las <strong>Content Credentials (C2PA)</strong>: un registro firmado que muchos generadores de IA y algunas apps de edición incrustan en el archivo para indicar cómo se hizo. Si ese registro dice que intervino la IA, TikTok puede añadir la etiqueta en cuanto subes el archivo.</p>
<p>En un vídeo, esa información va en bloques especiales del contenedor MP4 o MOV, junto a otros metadatos:</p>
<ul>
<li><strong>Manifiesto C2PA</strong>: las Content Credentials propiamente dichas.</li>
<li><strong>XMP</strong>: puede incluir el campo IPTC <code>DigitalSourceType</code> con valores como <code>trainedAlgorithmicMedia</code>.</li>
<li><strong>Datos de usuario</strong>: la app o el codificador que generó el vídeo y, a menudo, la <strong>ubicación GPS</strong> donde se grabó.</li>
</ul>
<h2>Fotos y carruseles</h2>
<p>Las publicaciones de fotos funcionan igual. Una imagen creada o editada con una herramienta de IA puede llevar Content Credentials (C2PA) y campos XMP como <code>DigitalSourceType</code>, además de datos EXIF como la cámara, la app de edición y la ubicación GPS. Si publicas varias imágenes en un carrusel, cada una puede llevar sus propios metadatos, así que límpialas todas: IA Cleaner te deja arrastrarlas a la vez y descargarlas juntas en un ZIP.</p>

<h2>Paso 1: revisa qué contiene tu vídeo</h2>
<ol>
<li>Abre IA Cleaner → <a href="/es/#images">Imágenes</a> (fotos) o <a href="/es/#video">Vídeo</a>.</li>
<li>Arrastra las fotos (JPG, PNG, WebP) o el vídeo (MP4, MOV) que ibas a publicar. También puedes hacerlo desde el navegador del móvil.</li>
<li>Busca entradas como <em>C2PA / Content Credentials (uuid)</em>, <em>XMP (uuid)</em> o <em>Datos de usuario (udta)</em>, y palabras relacionadas con IA en el informe.</li>
</ol>

<h2>Paso 2: quita los metadatos y sube la copia limpia</h2>
<ol>
<li>Pulsa <strong>Descargar imagen limpia</strong> o <strong>Descargar vídeo limpio</strong> (o <em>Descargar todo</em> si es un carrusel). La limpieza es <strong>sin pérdida</strong>: no se vuelven a codificar los píxeles ni los fotogramas, así que la calidad no cambia.</li>
<li>Sube esos archivos a TikTok.</li>
<li>Haz que limpiar sea el <strong>último paso</strong>: si vuelves a abrir y exportar el vídeo en un editor, puede volver a escribir los metadatos.</li>
</ol>

<h2>Lo que no puede garantizar</h2>
<ul>
<li>Los metadatos son <strong>una</strong> de las señales. El contenido hecho con los efectos de IA de TikTok lo etiqueta la propia TikTok, que además tiene su propia detección y ha anunciado marcas de agua invisibles para el contenido de IA creado con sus herramientas. Quitar los metadatos no afecta a nada de eso.</li>
<li>Las normas de TikTok piden <strong>etiquetar el contenido realista generado o muy editado con IA</strong>, y el que no se etiqueta puede ser etiquetado, limitado o eliminado. Si tu vídeo está generado con IA, etiquétalo: esta herramienta es para archivos cuyos metadatos no reflejan lo que de verdad hiciste y para quitar datos privados como tu ubicación.</li>
</ul>
'''},
 },
 {
  'id': 'c2pa',
  'en': {
   'slug': 'remove-c2pa-content-credentials',
   'title': 'How to remove C2PA / Content Credentials from an image',
   'seo_title': 'How to Remove C2PA & Content Credentials from an Image (Free)',
   'desc': 'What C2PA Content Credentials are, how to check if your image has them, and how to remove them for free without losing quality.',
   'lead': 'Images made or edited with AI tools often carry a hidden, signed record of how they were created. Here is what it is, how to check for it and how to remove it.',
   'cta': 'images', 'mins': 4,
   'body': '''
<h2>What is C2PA?</h2>
<p><strong>C2PA</strong> (Coalition for Content Provenance and Authenticity) is an open standard for attaching a <em>provenance record</em> to a file. Adobe calls it <strong>Content Credentials</strong>. The record — called a <em>manifest</em> — is cryptographically signed and can say which app created the image, whether AI was used and what edits were made.</p>
<p>Images exported by tools such as ChatGPT / DALL·E, Adobe Firefly or Microsoft Designer, and some cameras and phones, can include a C2PA manifest. Some platforms read it to show an “AI info” or “Made with AI” label.</p>

<h2>Where is it stored?</h2>
<ul>
<li><strong>JPEG:</strong> inside <code>APP11</code> segments (JUMBF boxes).</li>
<li><strong>PNG:</strong> in a <code>caBX</code> chunk.</li>
<li><strong>WebP:</strong> in a dedicated RIFF chunk.</li>
</ul>
<p>It often travels together with <strong>XMP</strong> metadata that includes the IPTC field <code>DigitalSourceType</code> with values like <code>trainedAlgorithmicMedia</code> — another common “AI-generated” marker.</p>

<h2>How to check if an image has Content Credentials</h2>
<ol>
<li>Upload it to the official verifier at <a href="https://contentcredentials.org/verify" rel="noopener">contentcredentials.org/verify</a>, or</li>
<li>Drop it into <a href="/#images">IA Cleaner</a>: it lists every metadata block it finds and flags AI-related ones before removing them.</li>
</ol>

<h2>How to remove C2PA with IA Cleaner (step by step)</h2>
<ol>
<li>Open <a href="/#images">IA Cleaner → Images</a>.</li>
<li>Drag your JPG, PNG or WebP onto the drop zone (you can add several at once).</li>
<li>Check the report: blocks such as <em>JUMBF / C2PA Content Credentials (APP11)</em> or <em>XMP</em> are listed and marked <strong>AI</strong>.</li>
<li>Click <strong>Download</strong>. The image is cleaned <strong>losslessly</strong> — only metadata is removed, pixels stay untouched.</li>
</ol>
<p>Verify the result by running the cleaned file through the verifier again: it should report that no Content Credentials were found.</p>

<h2>Other ways</h2>
<ul>
<li><strong>ExifTool</strong> (command line): <code>exiftool -all= image.jpg</code> removes EXIF, XMP and IPTC. Check its documentation for C2PA/JUMBF support in your version.</li>
<li><strong>Screenshot or re-export:</strong> works, but recompresses the image and loses quality.</li>
</ul>

<h2>What removing C2PA does not do</h2>
<p>Some AI images also carry <strong>invisible watermarks</strong> woven into the pixels themselves (for example Google’s SynthID). These are not metadata, so no metadata tool can remove them. And if a platform, publication or law requires you to disclose AI use, removing metadata doesn’t change that obligation.</p>
'''},
  'es': {
   'slug': 'quitar-c2pa-content-credentials',
   'title': 'Cómo quitar C2PA / Content Credentials de una imagen',
   'seo_title': 'Quitar C2PA y Content Credentials de una imagen gratis y sin perder calidad',
   'desc': 'Comprueba si tu imagen lleva Content Credentials (C2PA) de ChatGPT, Firefly u otras IA y elimínalas gratis en tu navegador. Sin registro, sin subir la imagen y sin perder calidad.',
   'lead': 'Las imágenes creadas o editadas con herramientas de IA suelen llevar un registro oculto y firmado de cómo se hicieron. Te explicamos qué es, cómo detectarlo y cómo quitarlo.',
   'cta': 'images', 'mins': 4,
   'body': '''
<h2>¿Qué es C2PA?</h2>
<p><strong>C2PA</strong> (Coalition for Content Provenance and Authenticity) es un estándar abierto para añadir a un archivo un <em>registro de procedencia</em>. Adobe lo llama <strong>Content Credentials</strong> («credenciales de contenido»). Ese registro —el <em>manifiesto</em>— va firmado criptográficamente y puede indicar qué aplicación creó la imagen, si se usó IA y qué ediciones se hicieron.</p>
<p>Las imágenes exportadas por herramientas como ChatGPT / DALL·E, Adobe Firefly o Microsoft Designer, y algunas cámaras y móviles, pueden incluir un manifiesto C2PA. Algunas plataformas lo leen para mostrar etiquetas como «Información de IA» o «Hecho con IA».</p>

<h2>¿Dónde se guarda?</h2>
<ul>
<li><strong>JPEG:</strong> en segmentos <code>APP11</code> (cajas JUMBF).</li>
<li><strong>PNG:</strong> en un bloque <code>caBX</code>.</li>
<li><strong>WebP:</strong> en un bloque RIFF propio.</li>
</ul>
<p>A menudo va acompañado de metadatos <strong>XMP</strong> con el campo IPTC <code>DigitalSourceType</code> y valores como <code>trainedAlgorithmicMedia</code>, otra marca habitual de «generado con IA».</p>

<h2>Cómo saber si una imagen tiene Content Credentials</h2>
<ol>
<li>Súbela al verificador oficial en <a href="https://contentcredentials.org/verify" rel="noopener">contentcredentials.org/verify</a>, o</li>
<li>Arrástrala a <a href="/es/#images">IA Cleaner</a>: muestra todos los bloques de metadatos que encuentra y marca los relacionados con IA antes de eliminarlos.</li>
</ol>

<h2>Cómo quitar C2PA con IA Cleaner (paso a paso)</h2>
<ol>
<li>Abre <a href="/es/#images">IA Cleaner → Imágenes</a>.</li>
<li>Arrastra tu JPG, PNG o WebP a la zona de carga (puedes añadir varios a la vez).</li>
<li>Revisa el informe: aparecen bloques como <em>JUMBF / C2PA Content Credentials (APP11)</em> o <em>XMP</em>, marcados con <strong>IA</strong>.</li>
<li>Pulsa <strong>Descargar</strong>. La imagen se limpia <strong>sin pérdida</strong>: solo se quitan los metadatos y los píxeles no se tocan.</li>
</ol>
<p>Comprueba el resultado pasando la imagen limpia otra vez por el verificador: debería indicar que no hay Content Credentials.</p>

<h2>Otras formas</h2>
<ul>
<li><strong>ExifTool</strong> (línea de comandos): <code>exiftool -all= imagen.jpg</code> elimina EXIF, XMP e IPTC. Revisa su documentación para saber si tu versión elimina también C2PA/JUMBF.</li>
<li><strong>Captura de pantalla o volver a exportar:</strong> funciona, pero recomprime la imagen y pierde calidad.</li>
</ul>

<h2>Lo que no hace quitar C2PA</h2>
<p>Algunas imágenes de IA llevan además <strong>marcas de agua invisibles</strong> integradas en los propios píxeles (por ejemplo, SynthID de Google). No son metadatos, así que ninguna herramienta de metadatos puede quitarlas. Y si una plataforma, una publicación o la ley te exige indicar que usaste IA, borrar los metadatos no cambia esa obligación.</p>
'''},
 },
 {
  'id': 'photoshop',
  'en': {
   'slug': 'photoshop-content-credentials-edit-history',
   'title': 'What Photoshop Content Credentials reveal about your edits — and how to remove them',
   'seo_title': 'Photoshop Content Credentials: What Edit History They Show & How to Remove It',
   'desc': 'Content Credentials from Photoshop can show your name, the tools you used, a summary of your edits, placed images and any generative AI use. See exactly what your file reveals and remove it before sending it to a client.',
   'lead': 'Exported a design and worried your client will see your messy process? Here is what Photoshop’s Content Credentials and edit log actually store, what you can control inside Photoshop, and how to check and clean the exported file.',
   'cta': 'images', 'mins': 6,
   'body': '''
<h2>What Photoshop can store in an exported image</h2>
<ul>
<li><strong>Content Credentials (C2PA):</strong> when the feature is on, the export carries a signed record with the app and version, optionally your name or connected accounts, and a list of <em>actions</em> such as “opened”, “colour adjustments”, “cropped”, “placed another image”, “resized” or “drawing”.</li>
<li><strong>Ingredients:</strong> if you placed other images, the record can list them as ingredients, sometimes with small thumbnails.</li>
<li><strong>Generative AI use:</strong> when you use Firefly features such as Generative Fill, Adobe adds Content Credentials saying AI was used, even if you never turned the feature on yourself.</li>
<li><strong>XMP history:</strong> separately, Photoshop writes a short history of saves into XMP, and if you enabled the <em>History Log</em> in Preferences it can write a detailed list of steps into the file’s metadata.</li>
</ul>

<h2>Does it show every edit you made?</h2>
<p>Not every brush stroke. Content Credentials store a <strong>summary of action types</strong> — you will see “colour adjustments ×3”, not each curve you tried. But that summary, plus the list of placed files and the AI flag, is often enough to tell how an image was built.</p>
<p>The detailed step-by-step list only appears if the <strong>History Log</strong> is set to save to metadata. That one can be very explicit, so check it.</p>

<h2>Can you hide some edits and keep others?</h2>
<p>Not individually. Inside Photoshop you can turn Content Credentials on or off and choose which <em>categories</em> of information to include (for example producer, edits and activity, connected accounts) before exporting. You can’t pick single edits to hide. If you want to keep nothing, export without Content Credentials or clean the exported copy.</p>

<h2>See what your file reveals, then clean it</h2>
<ol>
<li>Open <a href="/#images">IA Cleaner → Images</a> and drop the exported JPG, PNG or WebP.</li>
<li>Read the box <strong>What the original reveals about how it was made</strong>: the tool, the author or account, AI use and the <strong>edit history</strong> from Content Credentials and XMP.</li>
<li>Click <strong>Download clean image</strong>. The clean copy keeps every pixel and the colour profile, and none of that history.</li>
</ol>
<p>The file is processed in your browser and never uploaded, so it is safe for client work.</p>

<h2>Settings to check in Photoshop</h2>
<ul>
<li><strong>Content Credentials panel</strong> (<em>Window → Content Credentials</em>): turn it off, or untick what you don’t want to include.</li>
<li><strong>History Log</strong> (<em>Preferences → History Log</em>, or <em>History &amp; Content Credentials</em> in recent versions): don’t save log items to metadata.</li>
<li><strong>Export As / Save for Web:</strong> set <em>Metadata</em> to <em>None</em> or <em>Copyright</em> only.</li>
</ul>
<p>Remember that the PSD itself keeps all layers and history. Send a flattened export, not the working file.</p>
'''},
  'es': {
   'slug': 'photoshop-content-credentials-historial',
   'title': 'Qué revelan las Content Credentials de Photoshop sobre tus ediciones y cómo quitarlas',
   'seo_title': 'Content Credentials de Photoshop: qué historial de ediciones muestran y cómo quitarlo',
   'desc': 'Las Content Credentials de Photoshop pueden mostrar tu nombre, las herramientas que usaste, un resumen de tus ediciones, las imágenes colocadas y si usaste IA generativa. Mira qué revela tu archivo y quítalo antes de enviarlo a un cliente.',
   'lead': '¿Has exportado un diseño y te preocupa que tu cliente vea tu proceso? Esto es lo que guardan de verdad las Content Credentials y el registro de historia de Photoshop, qué puedes controlar desde Photoshop y cómo revisar y limpiar el archivo exportado.',
   'cta': 'images', 'mins': 6,
   'body': '''
<h2>Qué puede guardar Photoshop en una imagen exportada</h2>
<ul>
<li><strong>Content Credentials (C2PA):</strong> si la función está activada, la exportación lleva un registro firmado con la aplicación y su versión, opcionalmente tu nombre o tus cuentas conectadas, y una lista de <em>acciones</em> como «abrir», «ajustes de color», «recortar», «colocar otra imagen», «redimensionar» o «dibujar».</li>
<li><strong>Ingredientes:</strong> si colocaste otras imágenes, el registro puede listarlas como ingredientes, a veces con miniaturas.</li>
<li><strong>Uso de IA generativa:</strong> cuando usas funciones de Firefly como el Relleno generativo, Adobe añade Content Credentials que indican que se usó IA, aunque tú no hayas activado la función.</li>
<li><strong>Historial XMP:</strong> aparte, Photoshop escribe en XMP un breve historial de guardados y, si activaste el <em>Registro de historia</em> en Preferencias, puede escribir una lista detallada de pasos en los metadatos del archivo.</li>
</ul>

<h2>¿Muestra cada edición que hiciste?</h2>
<p>No cada pincelada. Las Content Credentials guardan un <strong>resumen por tipos de acción</strong>: verás «ajustes de color ×3», no cada curva que probaste. Pero ese resumen, junto con la lista de archivos colocados y la marca de IA, suele bastar para saber cómo se construyó la imagen.</p>
<p>La lista detallada paso a paso solo aparece si el <strong>Registro de historia</strong> está configurado para guardarse en los metadatos. Esa sí puede ser muy explícita, así que revísala.</p>

<h2>¿Se pueden ocultar algunas ediciones y dejar otras?</h2>
<p>No una a una. En Photoshop puedes activar o desactivar las Content Credentials y elegir qué <em>categorías</em> de información incluir (por ejemplo productor, ediciones y actividad, cuentas conectadas) antes de exportar. No puedes elegir ediciones concretas para ocultarlas. Si no quieres dejar nada, exporta sin Content Credentials o limpia la copia exportada.</p>

<h2>Mira qué revela tu archivo y límpialo</h2>
<ol>
<li>Abre <a href="/es/#images">IA Cleaner → Imágenes</a> y arrastra el JPG, PNG o WebP exportado.</li>
<li>Lee el recuadro <strong>Lo que el original revela sobre cómo se hizo</strong>: la herramienta, el autor o la cuenta, el uso de IA y el <strong>historial de ediciones</strong> de las Content Credentials y del XMP.</li>
<li>Pulsa <strong>Descargar imagen limpia</strong>. La copia limpia conserva todos los píxeles y el perfil de color, y nada de ese historial.</li>
</ol>
<p>El archivo se procesa en tu navegador y nunca se sube, así que es seguro para trabajos de clientes.</p>

<h2>Ajustes que conviene revisar en Photoshop</h2>
<ul>
<li><strong>Panel Content Credentials</strong> (<em>Ventana → Content Credentials</em>): desactívalo o desmarca lo que no quieras incluir.</li>
<li><strong>Registro de historia</strong> (<em>Preferencias → Registro de historia</em>, o <em>Historia y Content Credentials</em> en versiones recientes): no guardes los elementos del registro en los metadatos.</li>
<li><strong>Exportar como / Guardar para web:</strong> pon <em>Metadatos</em> en <em>Ninguno</em> o solo <em>Copyright</em>.</li>
</ul>
<p>Recuerda que el PSD conserva todas las capas y el historial. Envía una exportación acoplada, no el archivo de trabajo.</p>
'''},
 },
 {
  'id': 'chatgpt',
  'en': {
   'slug': 'chatgpt-hidden-characters',
   'title': 'ChatGPT hidden characters: what they are and how to remove them',
   'seo_title': 'ChatGPT Hidden Characters, oaicite & utm_source: How to Remove Them',
   'desc': 'Why text copied from ChatGPT can contain invisible characters, contentReference[oaicite] markers and utm_source=chatgpt.com links — and how to clean them.',
   'lead': 'Pasted some text from an AI chat and found strange gaps, “oaicite” codes or tracking tags in your links? Here is where they come from and how to clean them in one click.',
   'cta': 'text', 'mins': 5,
   'body': '''
<h2>What can be hidden in copied AI text</h2>
<ul>
<li><strong>Invisible Unicode characters</strong>: zero-width spaces (<code>U+200B</code>), word joiners (<code>U+2060</code>), byte-order marks (<code>U+FEFF</code>) and soft hyphens. They take up no space on screen but are still in the text.</li>
<li><strong>Special spaces</strong>: no-break (<code>U+00A0</code>) and narrow no-break spaces (<code>U+202F</code>) that look like normal spaces.</li>
<li><strong>Citation leftovers</strong>: when an answer cites sources, copying it into another app can leave markers such as <code>contentReference[oaicite:0]{index=0}</code> or <code>【4:0†source】</code>.</li>
<li><strong>Tracking parameters</strong>: links suggested by ChatGPT often end in <code>?utm_source=chatgpt.com</code>.</li>
<li><strong>Private-use characters</strong>: internal markers from the chat interface that show up as empty boxes in some apps.</li>
</ul>

<h2>Are they a watermark?</h2>
<p>Mostly no. In 2025 users noticed that some newer models occasionally produced narrow no-break spaces, and many assumed it was a watermark; OpenAI said it was not intentional. Most hidden characters come from formatting and copy-paste. They are still worth removing: they can break code, search, word counts and formatting, and they reveal where the text was copied from.</p>
<p>Note that AI-text detectors judge the <em>wording</em>, not these characters — cleaning them won’t change what a detector thinks of your writing.</p>

<h2>How to check and clean your text with IA Cleaner</h2>
<ol>
<li>Open <a href="/">IA Cleaner → Text</a> and paste your text.</li>
<li>A live counter tells you how many hidden characters were found.</li>
<li>Click <strong>Clean text</strong>. You’ll see every hidden character highlighted in place, with its Unicode code and name.</li>
<li>Copy the clean result or download it as a <code>.txt</code>.</li>
</ol>
<p>Compound emoji (👨‍👩‍👧) and flags are kept intact. An optional setting also converts curly quotes, em dashes and ellipses into plain characters.</p>

<h2>Hidden messages in Unicode tags</h2>
<p>A less common trick uses <strong>Unicode tag characters</strong> (<code>U+E0000–E007F</code>) to hide whole sentences inside normal-looking text — sometimes used for prompt injection. IA Cleaner decodes and shows any hidden message before removing it.</p>

<h2>Cleaning text inside Word and PowerPoint files</h2>
<p>If you already pasted AI text into a document, drop the <code>.docx</code>, <code>.pptx</code> or <code>.xlsx</code> into <a href="/#documents">Documents</a>: invisible characters are removed from the document text and its metadata is cleaned too.</p>
'''},
  'es': {
   'slug': 'caracteres-ocultos-chatgpt',
   'title': 'Caracteres ocultos de ChatGPT: qué son y cómo eliminarlos',
   'seo_title': 'Caracteres ocultos de ChatGPT: cómo detectarlos y quitarlos gratis',
   'desc': '¿Tu texto de ChatGPT lleva caracteres invisibles, marcas oaicite o enlaces utm_source=chatgpt.com? Pégalo, míralos marcados al instante y límpialo gratis, sin subir nada.',
   'lead': '¿Has pegado un texto de un chat de IA y te han aparecido huecos raros, códigos «oaicite» o etiquetas en los enlaces? Te explicamos de dónde salen y cómo limpiarlos con un clic.',
   'cta': 'text', 'mins': 5,
   'body': '''
<h2>Qué puede esconder un texto copiado de una IA</h2>
<ul>
<li><strong>Caracteres Unicode invisibles</strong>: espacios de ancho cero (<code>U+200B</code>), uniones de palabras (<code>U+2060</code>), marcas BOM (<code>U+FEFF</code>) y guiones suaves. No ocupan espacio en pantalla, pero siguen en el texto.</li>
<li><strong>Espacios especiales</strong>: espacios de no separación (<code>U+00A0</code>) y estrechos (<code>U+202F</code>) que parecen espacios normales.</li>
<li><strong>Restos de citas</strong>: cuando una respuesta cita fuentes, al copiarla en otra aplicación pueden quedar marcas como <code>contentReference[oaicite:0]{index=0}</code> o <code>【4:0†source】</code>.</li>
<li><strong>Parámetros de seguimiento</strong>: los enlaces que sugiere ChatGPT suelen terminar en <code>?utm_source=chatgpt.com</code>.</li>
<li><strong>Caracteres de uso privado</strong>: marcadores internos de la interfaz del chat que en algunas aplicaciones se ven como cuadros vacíos.</li>
</ul>

<h2>¿Son una marca de agua?</h2>
<p>En general, no. En 2025 algunos usuarios vieron que ciertos modelos nuevos generaban a veces espacios estrechos de no separación y muchos pensaron que era una marca de agua; OpenAI dijo que no era intencionado. La mayoría de caracteres ocultos vienen del formato y de copiar y pegar. Aun así conviene quitarlos: pueden romper código, búsquedas, recuentos de palabras y el formato, y delatan de dónde se copió el texto.</p>
<p>Ten en cuenta que los detectores de texto de IA analizan la <em>redacción</em>, no estos caracteres: limpiarlos no cambia lo que un detector opine de tu texto.</p>

<h2>Cómo revisar y limpiar tu texto con IA Cleaner</h2>
<ol>
<li>Abre <a href="/es/">IA Cleaner → Texto</a> y pega tu texto.</li>
<li>Un contador en directo te dice cuántos caracteres ocultos ha encontrado.</li>
<li>Pulsa <strong>Limpiar texto</strong>. Verás cada carácter oculto resaltado en su sitio, con su código Unicode y su nombre.</li>
<li>Copia el resultado limpio o descárgalo como <code>.txt</code>.</li>
</ol>
<p>Los emojis compuestos (👨‍👩‍👧) y las banderas se conservan. Una opción adicional convierte las comillas tipográficas, las rayas y los puntos suspensivos en caracteres simples.</p>

<h2>Mensajes ocultos en etiquetas Unicode</h2>
<p>Un truco menos habitual usa <strong>caracteres de etiqueta Unicode</strong> (<code>U+E0000–E007F</code>) para esconder frases enteras dentro de un texto normal; a veces se usa para inyección de prompts. IA Cleaner descodifica y te muestra el mensaje oculto antes de eliminarlo.</p>

<h2>Limpiar el texto dentro de archivos Word y PowerPoint</h2>
<p>Si ya pegaste el texto en un documento, arrastra el <code>.docx</code>, <code>.pptx</code> o <code>.xlsx</code> a <a href="/es/#documents">Documentos</a>: se eliminan los caracteres invisibles del texto y también se limpian sus metadatos.</p>
'''},
 },
 {
  'id': 'docs-emails',
  'en': {
   'slug': 'remove-ai-traces-documents-emails',
   'title': 'How to remove AI traces from documents and emails you polished with ChatGPT or Copilot',
   'seo_title': 'Remove ChatGPT & Copilot Traces from Documents and Emails (Metadata Guide)',
   'desc': 'Word files, PDFs and emails you polished with AI can carry metadata, embedded AI images, hidden characters and chatgpt.com links. See what they contain and clean them before sending.',
   'lead': 'You used ChatGPT or Copilot to polish a report, a cover letter or an email. Before you send it, check the technical traces the file carries — they can say more than the text itself.',
   'cta': 'documents', 'mins': 6,
   'body': '''
<h2>1. Document metadata (Word, PowerPoint, Excel)</h2>
<p>Every <code>.docx</code>, <code>.pptx</code> and <code>.xlsx</code> is a package that includes hidden properties:</p>
<ul>
<li><strong>Author</strong> and <strong>Last modified by</strong> — the account names that created and edited the file.</li>
<li><strong>Company</strong>, <strong>Manager</strong> and the <strong>Template</strong> the document was based on.</li>
<li><strong>Application</strong> and version, plus <strong>total editing time</strong>.</li>
<li><strong>Custom properties</strong> added by add-ins, templates, online tools or your organisation (for example classification labels).</li>
</ul>
<p>If you started from a document generated or exported by an online AI tool, its name can remain in these fields even after you rewrite every line.</p>

<h2>2. PDF properties</h2>
<p>A PDF stores <strong>Creator</strong> (the app that made the original) and <strong>Producer</strong> (the PDF engine), plus an XMP block. PDFs exported from AI writing or presentation tools often carry that tool’s name there. See the full <a href="/guides/remove-pdf-metadata/">PDF metadata guide</a>.</p>

<h2>3. AI images inside the document</h2>
<p>An illustration you generated with ChatGPT, DALL·E, Firefly or Midjourney and pasted into a slide keeps its own metadata — C2PA Content Credentials and XMP fields such as <code>trainedAlgorithmicMedia</code> — <strong>inside</strong> the <code>.pptx</code> or <code>.docx</code>. Anyone can unzip the file and read it.</p>

<h2>4. Copy-paste leftovers in the text</h2>
<ul>
<li><strong>Invisible characters</strong>: zero-width spaces, word joiners, special no-break spaces.</li>
<li><strong>Citation markers</strong> such as <code>contentReference[oaicite:0]{index=0}</code> or <code>【4:0†source】</code>.</li>
<li><strong>Links ending in <code>?utm_source=chatgpt.com</code></strong> — the recipient sees it when hovering or clicking.</li>
</ul>
<p>More details in <a href="/guides/chatgpt-hidden-characters/">ChatGPT hidden characters</a>.</p>

<h2>5. Emails: what travels with your message</h2>
<p>When you paste from a chat into Gmail or Outlook, you also paste its hidden characters, tracking parameters and sometimes HTML formatting (fonts, background colours). Attachments carry all the metadata above.</p>
<ol>
<li>Clean the text in <a href="/">IA Cleaner → Text</a> and copy the result.</li>
<li>Paste it into your email as <strong>plain text</strong>: <kbd>Ctrl</kbd>+<kbd>Shift</kbd>+<kbd>V</kbd> (<kbd>⌘</kbd>+<kbd>Shift</kbd>+<kbd>V</kbd> on Mac).</li>
<li>Clean any attachment in <a href="/#documents">Documents</a> before attaching it.</li>
</ol>

<h2>How to clean a document with IA Cleaner</h2>
<ol>
<li>Open <a href="/#documents">IA Cleaner → Documents</a> and drop your <code>.docx</code>, <code>.pptx</code>, <code>.xlsx</code> or PDF.</li>
<li>Keep both options on: <em>clean images embedded in documents</em> and <em>remove invisible characters from document text</em>.</li>
<li>Review the report — author, company, application, custom properties and embedded images are listed, AI-related ones are flagged.</li>
<li>Download the clean copy. Your text, layout and images are unchanged; only the hidden data is removed.</li>
</ol>

<h2>Other ways</h2>
<ul>
<li><strong>Word / PowerPoint on Windows:</strong> <em>File → Info → Check for Issues → Inspect Document → Document Properties and Personal Information → Remove All</em>.</li>
<li><strong>Word on Mac:</strong> <em>Word → Preferences → Security → Remove personal information from this file on save</em>.</li>
</ul>
<p>These built-in tools don’t clean images embedded in the document or hidden characters in the text.</p>

<h2>Checklist before you send</h2>
<ul>
<li>Text pasted as plain text, with no <code>oaicite</code> markers or <code>utm_source=chatgpt.com</code> links.</li>
<li>Document properties empty or correct (author, company, application).</li>
<li>Embedded images cleaned.</li>
<li>PDF exported <em>after</em> cleaning the original, or cleaned itself.</li>
</ul>
<p>IA Cleaner removes technical traces; it doesn’t change your wording.</p>
'''},
  'es': {
   'slug': 'quitar-rastros-ia-documentos-correos',
   'title': 'Cómo quitar los rastros de IA de documentos y correos que has pulido con ChatGPT o Copilot',
   'seo_title': 'Quitar rastros de ChatGPT de Word, PDF y correos (metadatos)',
   'desc': 'Los Word, PDF y correos que has pulido con IA pueden llevar metadatos, imágenes de IA y caracteres ocultos. Mira qué contienen y límpialos gratis antes de enviarlos.',
   'lead': 'Has usado ChatGPT o Copilot para pulir un informe, una carta de presentación o un correo. Antes de enviarlo, revisa los rastros técnicos que lleva el archivo: pueden decir más que el propio texto.',
   'cta': 'documents', 'mins': 6,
   'body': '''
<h2>1. Metadatos del documento (Word, PowerPoint, Excel)</h2>
<p>Todo <code>.docx</code>, <code>.pptx</code> y <code>.xlsx</code> es un paquete que incluye propiedades ocultas:</p>
<ul>
<li><strong>Autor</strong> y <strong>Modificado por</strong>: los nombres de las cuentas que crearon y editaron el archivo.</li>
<li><strong>Empresa</strong>, <strong>Administrador</strong> y la <strong>plantilla</strong> en la que se basó el documento.</li>
<li><strong>Aplicación</strong> y versión, además del <strong>tiempo total de edición</strong>.</li>
<li><strong>Propiedades personalizadas</strong> que añaden complementos, plantillas, herramientas online o tu organización (por ejemplo, etiquetas de clasificación).</li>
</ul>
<p>Si partiste de un documento generado o exportado por una herramienta de IA online, su nombre puede seguir en estos campos aunque hayas reescrito todas las líneas.</p>

<h2>2. Propiedades del PDF</h2>
<p>Un PDF guarda <strong>Creator</strong> (la aplicación del original) y <strong>Producer</strong> (el motor del PDF), además de un bloque XMP. Los PDF exportados desde herramientas de IA para escribir o hacer presentaciones suelen llevar ahí el nombre de la herramienta. Lo tienes explicado en la <a href="/es/guias/borrar-metadatos-pdf/">guía de metadatos de PDF</a>.</p>

<h2>3. Imágenes de IA dentro del documento</h2>
<p>Una ilustración que generaste con ChatGPT, DALL·E, Firefly o Midjourney y pegaste en una diapositiva conserva sus propios metadatos (Content Credentials C2PA y campos XMP como <code>trainedAlgorithmicMedia</code>) <strong>dentro</strong> del <code>.pptx</code> o <code>.docx</code>. Cualquiera puede descomprimir el archivo y leerlos.</p>

<h2>4. Restos de copiar y pegar en el texto</h2>
<ul>
<li><strong>Caracteres invisibles</strong>: espacios de ancho cero, uniones de palabras, espacios especiales de no separación.</li>
<li><strong>Marcas de citas</strong> como <code>contentReference[oaicite:0]{index=0}</code> o <code>【4:0†source】</code>.</li>
<li><strong>Enlaces que terminan en <code>?utm_source=chatgpt.com</code></strong>: el destinatario lo ve al pasar el ratón o al hacer clic.</li>
</ul>
<p>Más detalles en <a href="/es/guias/caracteres-ocultos-chatgpt/">Caracteres ocultos de ChatGPT</a>.</p>

<h2>5. Correos: lo que viaja con tu mensaje</h2>
<p>Al pegar desde un chat en Gmail u Outlook también pegas sus caracteres ocultos, los parámetros de seguimiento y a veces formato HTML (fuentes, colores de fondo). Los adjuntos llevan todos los metadatos anteriores.</p>
<ol>
<li>Limpia el texto en <a href="/es/">IA Cleaner → Texto</a> y copia el resultado.</li>
<li>Pégalo en el correo como <strong>texto sin formato</strong>: <kbd>Ctrl</kbd>+<kbd>Mayús</kbd>+<kbd>V</kbd> (<kbd>⌘</kbd>+<kbd>Mayús</kbd>+<kbd>V</kbd> en Mac).</li>
<li>Limpia los adjuntos en <a href="/es/#documents">Documentos</a> antes de adjuntarlos.</li>
</ol>

<h2>Cómo limpiar un documento con IA Cleaner</h2>
<ol>
<li>Abre <a href="/es/#documents">IA Cleaner → Documentos</a> y arrastra tu <code>.docx</code>, <code>.pptx</code>, <code>.xlsx</code> o PDF.</li>
<li>Deja activadas las dos opciones: <em>limpiar las imágenes incrustadas en documentos</em> y <em>quitar caracteres invisibles del texto de los documentos</em>.</li>
<li>Revisa el informe: aparecen el autor, la empresa, la aplicación, las propiedades personalizadas y las imágenes incrustadas, y se marcan las relacionadas con IA.</li>
<li>Descarga la copia limpia. El texto, el diseño y las imágenes no cambian; solo se eliminan los datos ocultos.</li>
</ol>

<h2>Otras formas</h2>
<ul>
<li><strong>Word / PowerPoint en Windows:</strong> <em>Archivo → Información → Comprobar si hay problemas → Inspeccionar documento → Propiedades del documento e información personal → Quitar todo</em>.</li>
<li><strong>Word en Mac:</strong> <em>Word → Preferencias → Seguridad → Quitar información personal de este archivo al guardar</em>.</li>
</ul>
<p>Estas herramientas integradas no limpian las imágenes incrustadas en el documento ni los caracteres ocultos del texto.</p>

<h2>Lista de comprobación antes de enviar</h2>
<ul>
<li>Texto pegado sin formato, sin marcas <code>oaicite</code> ni enlaces con <code>utm_source=chatgpt.com</code>.</li>
<li>Propiedades del documento vacías o correctas (autor, empresa, aplicación).</li>
<li>Imágenes incrustadas limpias.</li>
<li>PDF exportado <em>después</em> de limpiar el original, o limpiado directamente.</li>
</ul>
<p>IA Cleaner elimina los rastros técnicos; no cambia tu redacción.</p>
'''},
 },
 {
  'id': 'pdf',
  'en': {
   'slug': 'remove-pdf-metadata',
   'title': 'How to remove metadata from a PDF',
   'seo_title': 'How to Remove Metadata from a PDF (Author, Creator, XMP) — Free',
   'desc': 'See what metadata a PDF contains (author, creator app, dates, XMP) and remove it for free, without Acrobat and without uploading the file.',
   'lead': 'Every PDF carries information about who made it and with what software. Here is what is inside, why it matters and how to strip it without uploading your file anywhere.',
   'cta': 'documents', 'mins': 4,
   'body': '''
<h2>What metadata does a PDF contain?</h2>
<ul>
<li><strong>Document Info:</strong> Title, Author, Subject, Keywords, <em>Creator</em> (the app that made the original, e.g. Word) and <em>Producer</em> (the PDF engine), plus creation and modification dates.</li>
<li><strong>XMP metadata:</strong> an XML block that can repeat all of the above and add much more — editing history, tool names and, increasingly, AI-related tags.</li>
<li><strong>Page-level data</strong> and attachments, including C2PA provenance manifests in newer files.</li>
</ul>
<p>These fields can reveal your name, your company, the software you used (including AI writing or design tools) and when you worked on the file.</p>

<h2>How to remove PDF metadata with IA Cleaner</h2>
<ol>
<li>Open <a href="/#documents">IA Cleaner → Documents</a>.</li>
<li>Drop your PDF. The report lists every field found — Author, Creator, Producer, XMP — and flags AI-related values.</li>
<li>Click <strong>Download</strong> to get the cleaned copy.</li>
</ol>
<p>The PDF is <strong>rewritten from scratch</strong>, so the old values are not left behind in the file. Password-protected PDFs can’t be modified — remove the password first.</p>

<h2>Other ways</h2>
<ul>
<li><strong>Adobe Acrobat Pro:</strong> <em>Tools → Redact → Sanitize Document</em> removes hidden information (paid).</li>
<li><strong>Microsoft Word, before exporting:</strong> <em>File → Info → Check for Issues → Inspect Document</em>, then in the PDF export options untick <em>Document properties</em>.</li>
<li><strong>ExifTool:</strong> <code>exiftool -all:all= file.pdf</code>. Note that ExifTool edits PDFs <em>incrementally</em>, so the original metadata can still be recovered unless you rewrite the file afterwards (for example with <code>qpdf</code>).</li>
</ul>

<h2>Don’t forget the content</h2>
<p>Metadata is only part of the story: comments, tracked changes, hidden layers or text covered by black boxes can still be in the file. Clean the original document before exporting, and use proper redaction for sensitive text.</p>
'''},
  'es': {
   'slug': 'borrar-metadatos-pdf',
   'title': 'Cómo borrar los metadatos de un PDF',
   'seo_title': 'Borrar o eliminar metadatos de un PDF online gratis (autor, XMP), sin Acrobat',
   'desc': 'Mira qué metadatos tiene tu PDF (autor, programa, fechas, XMP) y bórralos gratis en tu navegador: sin Acrobat, sin registro y sin subir el archivo.',
   'lead': 'Todo PDF lleva información sobre quién lo hizo y con qué programa. Te contamos qué contiene, por qué importa y cómo eliminarla sin subir tu archivo a ningún sitio.',
   'cta': 'documents', 'mins': 4,
   'body': '''
<h2>¿Qué metadatos tiene un PDF?</h2>
<ul>
<li><strong>Información del documento:</strong> Título, Autor, Asunto, Palabras clave, <em>Creator</em> (la aplicación del original, por ejemplo Word) y <em>Producer</em> (el motor que generó el PDF), además de las fechas de creación y modificación.</li>
<li><strong>Metadatos XMP:</strong> un bloque XML que puede repetir todo lo anterior y añadir mucho más: historial de edición, nombres de herramientas y, cada vez más, etiquetas relacionadas con IA.</li>
<li><strong>Datos por página</strong> y adjuntos, incluidos manifiestos de procedencia C2PA en archivos recientes.</li>
</ul>
<p>Estos campos pueden revelar tu nombre, tu empresa, el software que usaste (incluidas herramientas de IA para escribir o diseñar) y cuándo trabajaste en el archivo.</p>

<h2>Cómo borrar los metadatos de un PDF con IA Cleaner</h2>
<ol>
<li>Abre <a href="/es/#documents">IA Cleaner → Documentos</a>.</li>
<li>Arrastra tu PDF. El informe muestra cada campo encontrado (Autor, Creator, Producer, XMP) y marca los valores relacionados con IA.</li>
<li>Pulsa <strong>Descargar</strong> para obtener la copia limpia.</li>
</ol>
<p>El PDF se <strong>reescribe desde cero</strong>, así que los valores antiguos no quedan escondidos dentro del archivo. Los PDF protegidos con contraseña no se pueden modificar: quita antes la contraseña.</p>

<h2>Otras formas</h2>
<ul>
<li><strong>Adobe Acrobat Pro:</strong> <em>Herramientas → Censurar → Desinfectar documento</em> elimina la información oculta (de pago).</li>
<li><strong>Microsoft Word, antes de exportar:</strong> <em>Archivo → Información → Comprobar si hay problemas → Inspeccionar documento</em> y, en las opciones de exportación a PDF, desmarca <em>Propiedades del documento</em>.</li>
<li><strong>ExifTool:</strong> <code>exiftool -all:all= archivo.pdf</code>. Ojo: ExifTool modifica los PDF de forma <em>incremental</em>, así que los metadatos originales se pueden recuperar si no reescribes el archivo después (por ejemplo con <code>qpdf</code>).</li>
</ul>

<h2>No te olvides del contenido</h2>
<p>Los metadatos son solo una parte: comentarios, control de cambios, capas ocultas o texto tapado con recuadros negros pueden seguir en el archivo. Limpia el documento original antes de exportarlo y usa una censura de verdad para el texto sensible.</p>
'''},
 },
 {
  'id': 'check-ai-image',
  'en': {
   'slug': 'check-if-image-is-ai-metadata',
   'title': 'How to tell if an image was made with AI by checking its metadata',
   'seo_title': 'Is This Image AI-Generated? Check Its Metadata for Free',
   'desc': 'Many AI images carry C2PA, XMP or prompt metadata that says which tool made them. Here is how to check any JPG, PNG or WebP for free, what each sign means and what metadata can’t tell you.',
   'lead': 'Before guessing from the pixels, look at what the file says about itself. Many AI tools write their name, the prompt or a provenance record into the image. Here is how to read it in seconds — and where this method stops working.',
   'cta': 'images', 'mins': 5,
   'body': '''
<h2>What AI tools leave inside an image</h2>
<ul>
<li><strong>C2PA / Content Credentials:</strong> a signed provenance record added by ChatGPT image generation, Adobe Firefly, Microsoft Designer and others. It often states that the image was created with generative AI and names the tool.</li>
<li><strong>XMP / IPTC <code>DigitalSourceType</code>:</strong> a standard field whose value <code>trainedAlgorithmicMedia</code> means “generated by AI”, and <code>compositeWithTrainedAlgorithmicMedia</code> means “edited with AI”.</li>
<li><strong>PNG text chunks:</strong> Stable Diffusion, ComfyUI and Automatic1111 save the full prompt, model and settings (<code>parameters</code>, <code>prompt</code>, <code>workflow</code>).</li>
<li><strong>EXIF Software field:</strong> sometimes simply the name of the app or model that saved the file.</li>
</ul>

<h2>How to check an image with IA Cleaner</h2>
<ol>
<li>Open <a href="/#images">IA Cleaner → Images</a>.</li>
<li>Drop the JPG, PNG or WebP. Nothing is uploaded: the file is read in your browser.</li>
<li>Read the report. Blocks related to AI are marked <strong>AI</strong>, and the card lists the <em>AI traces found in the original</em> — for example “c2pa”, “openai”, “firefly” or “stable diffusion”.</li>
</ol>
<p>If you only want to check, you don’t need to download anything. If the image is yours and you want to share it without that data, click <strong>Download clean image</strong>.</p>

<h2>What the result means</h2>
<ul>
<li><strong>AI traces found:</strong> the file was made or edited by an AI tool, or passed through one.</li>
<li><strong>No metadata found:</strong> this does <em>not</em> prove the image is real. Screenshots, social networks and most messaging apps strip metadata, so an AI image downloaded from Instagram or WhatsApp usually arrives clean.</li>
<li><strong>Camera data only (make, model, exposure):</strong> a good sign that it came from a camera, but EXIF can be copied or edited.</li>
</ul>

<h2>What metadata can’t tell you</h2>
<p>Some generators also hide an <strong>invisible watermark in the pixels</strong> (for example Google’s SynthID). That is not metadata, so neither IA Cleaner nor any metadata viewer can see it. To verify those you need the provider’s own checker. For images that have lost their metadata, the only remaining clues are visual ones and reverse image search.</p>
'''},
  'es': {
   'slug': 'saber-si-imagen-es-ia-metadatos',
   'title': 'Cómo saber si una imagen está hecha con IA mirando sus metadatos',
   'seo_title': '¿Esta imagen es de IA? Compruébalo gratis mirando sus metadatos',
   'desc': 'Muchas imágenes de IA llevan metadatos C2PA, XMP o el prompt, que dicen con qué herramienta se hicieron. Así puedes revisar cualquier JPG, PNG o WebP gratis, qué significa cada señal y qué no pueden decirte los metadatos.',
   'lead': 'Antes de adivinar por los píxeles, mira lo que el archivo dice de sí mismo. Muchas herramientas de IA escriben su nombre, el prompt o un registro de procedencia dentro de la imagen. Así puedes leerlo en segundos, y aquí está dónde deja de funcionar este método.',
   'cta': 'images', 'mins': 5,
   'body': '''
<h2>Qué dejan las herramientas de IA dentro de una imagen</h2>
<ul>
<li><strong>C2PA / Content Credentials:</strong> un registro de procedencia firmado que añaden la generación de imágenes de ChatGPT, Adobe Firefly, Microsoft Designer y otras. Suele indicar que la imagen se creó con IA generativa y con qué herramienta.</li>
<li><strong>Campo <code>DigitalSourceType</code> de XMP / IPTC:</strong> un campo estándar cuyo valor <code>trainedAlgorithmicMedia</code> significa «generada por IA» y <code>compositeWithTrainedAlgorithmicMedia</code>, «editada con IA».</li>
<li><strong>Bloques de texto PNG:</strong> Stable Diffusion, ComfyUI y Automatic1111 guardan el prompt completo, el modelo y los ajustes (<code>parameters</code>, <code>prompt</code>, <code>workflow</code>).</li>
<li><strong>Campo Software de EXIF:</strong> a veces es simplemente el nombre de la app o del modelo que guardó el archivo.</li>
</ul>

<h2>Cómo revisar una imagen con IA Cleaner</h2>
<ol>
<li>Abre <a href="/es/#images">IA Cleaner → Imágenes</a>.</li>
<li>Arrastra el JPG, PNG o WebP. No se sube nada: el archivo se lee en tu navegador.</li>
<li>Lee el informe. Los bloques relacionados con IA aparecen marcados con <strong>IA</strong> y la tarjeta muestra los <em>rastros de IA encontrados en el original</em>, por ejemplo «c2pa», «openai», «firefly» o «stable diffusion».</li>
</ol>
<p>Si solo quieres comprobarla, no hace falta descargar nada. Si la imagen es tuya y quieres compartirla sin esos datos, pulsa <strong>Descargar imagen limpia</strong>.</p>

<h2>Qué significa el resultado</h2>
<ul>
<li><strong>Se encuentran rastros de IA:</strong> el archivo se creó o se editó con una herramienta de IA, o pasó por una.</li>
<li><strong>No se encuentran metadatos:</strong> esto <em>no</em> demuestra que la imagen sea real. Las capturas de pantalla, las redes sociales y la mayoría de apps de mensajería borran los metadatos, así que una imagen de IA descargada de Instagram o WhatsApp suele llegar limpia.</li>
<li><strong>Solo datos de cámara (marca, modelo, exposición):</strong> buena señal de que viene de una cámara, aunque los datos EXIF se pueden copiar o editar.</li>
</ul>

<h2>Lo que los metadatos no pueden decirte</h2>
<p>Algunos generadores también esconden una <strong>marca de agua invisible en los píxeles</strong> (por ejemplo SynthID de Google). Eso no son metadatos, así que ni IA Cleaner ni ningún visor de metadatos puede verla. Para comprobarla necesitas la herramienta del propio proveedor. En imágenes que ya han perdido sus metadatos, solo quedan las pistas visuales y la búsqueda inversa de imágenes.</p>
'''},
 },
 {
  'id': 'phone-photos',
  'en': {
   'slug': 'remove-photo-metadata-iphone-android',
   'title': 'How to remove metadata from a photo on iPhone or Android',
   'seo_title': 'Remove Photo Metadata & Location on iPhone and Android (GPS, EXIF) — Free',
   'desc': 'Photos from your phone store GPS location, device model, date and editing apps. Here is how to remove that metadata on iPhone or Android, for free and without installing anything.',
   'lead': 'Every photo you take with your phone can carry the exact place where you took it, the phone model and the apps you edited it with. Here is how to share it without that information, straight from your phone’s browser.',
   'cta': 'images', 'mins': 4,
   'body': '''
<h2>What your phone saves inside each photo</h2>
<ul>
<li><strong>GPS location:</strong> latitude and longitude, often precise enough to find your home.</li>
<li><strong>Device and camera:</strong> phone make and model, lens, exposure settings.</li>
<li><strong>Dates:</strong> when the photo was taken and edited.</li>
<li><strong>Editing apps:</strong> the software that saved the file — including AI editors and AI erase/expand tools, which can add XMP fields or C2PA Content Credentials.</li>
</ul>

<h2>Remove it in your phone’s browser (iPhone and Android)</h2>
<ol>
<li>Open <a href="/#images">iacleaner.com → Images</a> in Safari or Chrome.</li>
<li>Tap the drop zone and choose the photo from your gallery. You can pick several.</li>
<li>Check the report: GPS, EXIF, XMP and AI-related entries are listed.</li>
<li>Tap <strong>Download clean image</strong> and share or post that copy.</li>
</ol>
<p>The photo never leaves your phone, and quality is unchanged: only metadata is removed. On iPhone, the browser usually converts HEIC photos to JPG when you pick them; if you have a <code>.HEIC</code> file saved elsewhere, convert it to JPG first.</p>

<h2>Built-in options (location only)</h2>
<ul>
<li><strong>iPhone:</strong> in Photos, tap <em>Share</em>, then <em>Options</em> at the top and turn off <em>Location</em> before sending.</li>
<li><strong>Android (Google Photos):</strong> open the photo, swipe up to see its details and remove or edit the location; some phones also have a “remove location data” switch in the share sheet.</li>
<li><strong>Stop saving it:</strong> turn off location for the Camera app in your phone’s privacy settings.</li>
</ul>
<p>These options usually remove only the location. Device data, editing apps and AI-related metadata stay in the file.</p>

<h2>Do social networks remove it?</h2>
<p>Most large platforms strip EXIF from the public copy, but they read it first when you upload — and they keep it. Email, cloud links, Telegram “files” and many forums send the original file untouched. Cleaning before you share is the only way to be sure.</p>
'''},
  'es': {
   'slug': 'quitar-metadatos-foto-movil',
   'title': 'Cómo quitar los metadatos de una foto en el móvil (iPhone y Android)',
   'seo_title': 'Quitar metadatos y ubicación de una foto en el móvil (iPhone y Android) gratis',
   'desc': 'Las fotos del móvil guardan la ubicación GPS, el modelo del teléfono, la fecha y las apps de edición. Así puedes quitar esos metadatos en iPhone o Android, gratis y sin instalar nada.',
   'lead': 'Cada foto que haces con el móvil puede llevar el lugar exacto donde la hiciste, el modelo del teléfono y las apps con las que la editaste. Así puedes compartirla sin esa información, directamente desde el navegador del móvil.',
   'cta': 'images', 'mins': 4,
   'body': '''
<h2>Qué guarda el móvil dentro de cada foto</h2>
<ul>
<li><strong>Ubicación GPS:</strong> latitud y longitud, a menudo con precisión suficiente para encontrar tu casa.</li>
<li><strong>Dispositivo y cámara:</strong> marca y modelo del teléfono, objetivo y ajustes de exposición.</li>
<li><strong>Fechas:</strong> cuándo se hizo y cuándo se editó la foto.</li>
<li><strong>Apps de edición:</strong> el programa que guardó el archivo, incluidos editores con IA y herramientas para borrar o ampliar con IA, que pueden añadir campos XMP o Content Credentials (C2PA).</li>
</ul>

<h2>Quítalos desde el navegador del móvil (iPhone y Android)</h2>
<ol>
<li>Abre <a href="/es/#images">iacleaner.com → Imágenes</a> en Safari o Chrome.</li>
<li>Toca la zona de carga y elige la foto de tu galería. Puedes elegir varias.</li>
<li>Revisa el informe: aparecen el GPS, los datos EXIF, XMP y las entradas relacionadas con IA.</li>
<li>Toca <strong>Descargar imagen limpia</strong> y comparte o publica esa copia.</li>
</ol>
<p>La foto no sale de tu móvil y la calidad no cambia: solo se eliminan los metadatos. En iPhone, el navegador suele convertir las fotos HEIC a JPG al elegirlas; si tienes un archivo <code>.HEIC</code> guardado en otro sitio, conviértelo antes a JPG.</p>

<h2>Opciones del propio móvil (solo la ubicación)</h2>
<ul>
<li><strong>iPhone:</strong> en Fotos, toca <em>Compartir</em>, luego <em>Opciones</em> arriba y desactiva <em>Ubicación</em> antes de enviarla.</li>
<li><strong>Android (Google Fotos):</strong> abre la foto, desliza hacia arriba para ver los detalles y quita o edita la ubicación; algunos móviles también tienen un interruptor para «quitar datos de ubicación» al compartir.</li>
<li><strong>Que no se guarde:</strong> desactiva la ubicación para la app Cámara en los ajustes de privacidad del móvil.</li>
</ul>
<p>Estas opciones suelen quitar solo la ubicación. Los datos del dispositivo, las apps de edición y los metadatos relacionados con IA siguen en el archivo.</p>

<h2>¿Las redes sociales los borran?</h2>
<p>La mayoría de grandes plataformas quitan el EXIF de la copia pública, pero lo leen antes al subirla, y se lo quedan. El correo, los enlaces de la nube, los «archivos» de Telegram y muchos foros envían el archivo original sin tocar. Limpiarla antes de compartirla es la única forma de estar seguro.</p>
'''},
 },
 {
  'id': 'word',
  'en': {
   'slug': 'remove-metadata-word-document',
   'title': 'How to remove metadata from a Word document',
   'seo_title': 'Remove Metadata from a Word Document (Author, Company) — Free',
   'desc': 'A .docx file stores the author, company, last editor, editing time and template. Here is how to see and remove that metadata for free, with or without Word.',
   'lead': 'Send a Word file and you may also be sending your full name, your company, who edited it last and how long you spent on it. Here is what a .docx stores and how to remove it — with Word’s own inspector or in your browser.',
   'cta': 'documents', 'mins': 5,
   'body': '''
<h2>What metadata a Word file contains</h2>
<ul>
<li><strong>Core properties:</strong> author, last modified by, title, subject, keywords, revision number, and creation and modification dates.</li>
<li><strong>Extended properties:</strong> company, manager, the application and version that saved it, the template and the total editing time.</li>
<li><strong>Custom properties:</strong> fields added by companies, add-ins and document systems — sometimes including AI-assistant or classification tags.</li>
<li><strong>Embedded images:</strong> each picture keeps its own EXIF, XMP or C2PA data, including AI-generated images pasted into the document.</li>
</ul>

<h2>Remove it in your browser with IA Cleaner</h2>
<ol>
<li>Open <a href="/#documents">IA Cleaner → Documents</a>.</li>
<li>Drop your <code>.docx</code> (also works with <code>.xlsx</code>, <code>.pptx</code> and <code>.odt</code>).</li>
<li>Keep <em>Also clean images embedded in documents</em> and <em>Remove invisible characters from document text</em> turned on.</li>
<li>Review the report and click <strong>Download clean document</strong>.</li>
</ol>
<p>Your text and layout are not changed. The file is cleaned locally — it is never uploaded.</p>

<h2>Remove it with Word’s Document Inspector</h2>
<ol>
<li>In Word, go to <em>File → Info → Check for Issues → Inspect Document</em>.</li>
<li>Click <em>Inspect</em>, then <em>Remove All</em> next to <em>Document Properties and Personal Information</em>.</li>
<li>Remove <em>Comments, Revisions and Versions</em> too if you don’t want them in the file, and save.</li>
</ol>
<p>On LibreOffice, use <em>File → Properties → General → Reset Properties</em> and turn on <em>Tools → Options → LibreOffice → Security → Options → Remove personal information on saving</em>.</p>

<h2>What metadata cleaning doesn’t touch</h2>
<p>Comments, tracked changes and hidden text are part of the document content, not its metadata. IA Cleaner leaves them as they are, so accept or delete them in Word (or use the Document Inspector) before sending. If you export to PDF, clean the Word file first and then <a href="/guides/remove-pdf-metadata/">check the PDF’s metadata</a> as well.</p>
'''},
  'es': {
   'slug': 'quitar-metadatos-word',
   'title': 'Cómo quitar los metadatos de un documento de Word',
   'seo_title': 'Quitar o borrar metadatos de Word y Excel (autor, empresa) online gratis',
   'desc': 'Los archivos de Word, Excel y PowerPoint guardan el autor, la empresa, quién los editó por última vez, el tiempo de edición y la plantilla. Así puedes ver y eliminar esos metadatos online gratis, con o sin Office.',
   'lead': 'Si envías un Word, puede que también estés enviando tu nombre completo, tu empresa, quién lo editó por última vez y cuánto tiempo le dedicaste. Esto es lo que guarda un .docx y cómo quitarlo, con el inspector de Word o desde el navegador.',
   'cta': 'documents', 'mins': 5,
   'body': '''
<h2>Qué metadatos tiene un archivo de Word</h2>
<ul>
<li><strong>Propiedades principales:</strong> autor, última modificación por, título, asunto, palabras clave, número de revisión y fechas de creación y modificación.</li>
<li><strong>Propiedades extendidas:</strong> empresa, responsable, la aplicación y versión que lo guardó, la plantilla y el tiempo total de edición.</li>
<li><strong>Propiedades personalizadas:</strong> campos que añaden empresas, complementos y sistemas documentales, a veces con etiquetas de asistentes de IA o de clasificación.</li>
<li><strong>Imágenes incrustadas:</strong> cada imagen conserva sus propios datos EXIF, XMP o C2PA, incluidas las imágenes generadas con IA que pegues en el documento.</li>
</ul>

<h2>Quítalos desde el navegador con IA Cleaner</h2>
<ol>
<li>Abre <a href="/es/#documents">IA Cleaner → Documentos</a>.</li>
<li>Arrastra tu <code>.docx</code> (también funciona con <code>.xlsx</code>, <code>.pptx</code> y <code>.odt</code>).</li>
<li>Deja activadas <em>Limpiar también las imágenes incrustadas en documentos</em> y <em>Quitar caracteres invisibles del texto de los documentos</em>.</li>
<li>Revisa el informe y pulsa <strong>Descargar documento limpio</strong>.</li>
</ol>
<p>El texto y el diseño no cambian. El archivo se limpia en tu equipo: nunca se sube.</p>

<h2>Quítalos con el Inspector de documento de Word</h2>
<ol>
<li>En Word, ve a <em>Archivo → Información → Comprobar si hay problemas → Inspeccionar documento</em>.</li>
<li>Pulsa <em>Inspeccionar</em> y luego <em>Quitar todo</em> junto a <em>Propiedades del documento e información personal</em>.</li>
<li>Quita también <em>Comentarios, revisiones y versiones</em> si no quieres que vayan en el archivo, y guarda.</li>
</ol>
<p>En LibreOffice, usa <em>Archivo → Propiedades → General → Restablecer propiedades</em> y activa <em>Herramientas → Opciones → LibreOffice → Seguridad → Opciones → Eliminar información personal al guardar</em>.</p>

<h2>Lo que la limpieza de metadatos no toca</h2>
<p>Los comentarios, el control de cambios y el texto oculto forman parte del contenido del documento, no de sus metadatos. IA Cleaner los deja como están, así que acéptalos o bórralos en Word (o usa el Inspector de documento) antes de enviarlo. Si lo exportas a PDF, limpia primero el Word y después <a href="/es/guias/borrar-metadatos-pdf/">revisa también los metadatos del PDF</a>.</p>
'''},
 },
 {
  'id': 'chatgpt-images',
  'en': {
   'slug': 'chatgpt-image-metadata',
   'title': 'ChatGPT image metadata: what it contains and how to remove it',
   'seo_title': 'ChatGPT & DALL·E Image Metadata (C2PA): How to See and Remove It',
   'desc': 'Images created with ChatGPT carry C2PA Content Credentials that say they were generated by OpenAI. Here is how to check them and remove the metadata for free, without losing quality.',
   'lead': 'Every image you generate in ChatGPT comes with a provenance record that says it was made by OpenAI’s image model. Platforms can read it and label your post as AI. Here is what is inside and how to remove it.',
   'cta': 'images', 'mins': 4,
   'body': '''
<h2>What OpenAI adds to ChatGPT images</h2>
<ul>
<li><strong>C2PA Content Credentials:</strong> a signed manifest stored in the file (in JPG as a JUMBF block, in PNG as a <code>caBX</code> chunk, in WebP as metadata). It records that the image was created by an OpenAI generator, plus the date and the actions taken.</li>
<li><strong>XMP:</strong> may repeat provenance data and an AI source type.</li>
</ul>
<p>Instagram, Facebook, TikTok, LinkedIn and others read C2PA to show labels such as “AI info” or “AI-generated”.</p>

<h2>How to check and remove it</h2>
<ol>
<li>Download the image from ChatGPT as usual.</li>
<li>Open <a href="/#images">IA Cleaner → Images</a> and drop it.</li>
<li>The report shows the <em>C2PA / Content Credentials</em> block marked <strong>AI</strong>, with OpenAI-related text from the manifest.</li>
<li>Click <strong>Download clean image</strong>. Only metadata is removed; pixels are untouched.</li>
</ol>

<h2>Common questions</h2>
<ul>
<li><strong>Is it a watermark?</strong> No. C2PA is metadata, not a visible mark or a pattern in the pixels. Removing it does not change how the image looks.</li>
<li><strong>Does a screenshot remove it?</strong> Yes, but it also lowers quality and adds your own device’s data. Cleaning the original keeps full quality.</li>
<li><strong>Can OpenAI still recognise the image?</strong> Possibly. OpenAI has said it also uses internal tools to identify its own images, and removing metadata doesn’t change that.</li>
<li><strong>Is it allowed?</strong> Removing metadata from your own images is legal, but platforms and workplaces may require you to disclose AI use. Be honest where it matters.</li>
</ul>
'''},
  'es': {
   'slug': 'metadatos-imagenes-chatgpt',
   'title': 'Metadatos de las imágenes de ChatGPT: qué contienen y cómo quitarlos',
   'seo_title': 'Metadatos C2PA de las imágenes de ChatGPT: cómo verlos y quitarlos',
   'desc': 'Las imágenes creadas con ChatGPT llevan Content Credentials (C2PA) que dicen que las generó OpenAI. Así puedes comprobarlo y quitar esos metadatos gratis, sin perder calidad.',
   'lead': 'Cada imagen que generas en ChatGPT lleva un registro de procedencia que dice que la hizo el modelo de imágenes de OpenAI. Las redes sociales pueden leerlo y marcar tu publicación como IA. Esto es lo que contiene y cómo quitarlo.',
   'cta': 'images', 'mins': 4,
   'body': '''
<h2>Qué añade OpenAI a las imágenes de ChatGPT</h2>
<ul>
<li><strong>Content Credentials (C2PA):</strong> un manifiesto firmado guardado dentro del archivo (en JPG como bloque JUMBF, en PNG como bloque <code>caBX</code>, en WebP como metadatos). Registra que la imagen la creó un generador de OpenAI, además de la fecha y las acciones realizadas.</li>
<li><strong>XMP:</strong> puede repetir los datos de procedencia y un tipo de origen de IA.</li>
</ul>
<p>Instagram, Facebook, TikTok, LinkedIn y otras leen el C2PA para mostrar etiquetas como «Información de IA» o «Generado por IA».</p>

<h2>Cómo comprobarlo y quitarlo</h2>
<ol>
<li>Descarga la imagen de ChatGPT como siempre.</li>
<li>Abre <a href="/es/#images">IA Cleaner → Imágenes</a> y arrástrala.</li>
<li>El informe muestra el bloque <em>C2PA / Content Credentials</em> marcado con <strong>IA</strong>, con el texto del manifiesto relacionado con OpenAI.</li>
<li>Pulsa <strong>Descargar imagen limpia</strong>. Solo se quitan los metadatos; los píxeles no se tocan.</li>
</ol>

<h2>Preguntas frecuentes</h2>
<ul>
<li><strong>¿Es una marca de agua?</strong> No. El C2PA son metadatos, no una marca visible ni un patrón en los píxeles. Quitarlo no cambia cómo se ve la imagen.</li>
<li><strong>¿Una captura de pantalla lo quita?</strong> Sí, pero también baja la calidad y añade los datos de tu propio dispositivo. Limpiar el original mantiene toda la calidad.</li>
<li><strong>¿Puede OpenAI seguir reconociendo la imagen?</strong> Es posible. OpenAI ha dicho que también usa herramientas internas para identificar sus propias imágenes, y quitar los metadatos no cambia eso.</li>
<li><strong>¿Está permitido?</strong> Quitar los metadatos de tus propias imágenes es legal, pero algunas plataformas y empresas exigen indicar el uso de IA. Sé honesto donde importe.</li>
</ul>
'''},
 },
 {
  'id': 'video',
  'en': {
   'slug': 'remove-video-metadata-mp4-mov',
   'title': 'How to remove metadata from a video (MP4 and MOV)',
   'seo_title': 'Remove Metadata from a Video (MP4, MOV) Online — Free, No Re-encoding',
   'desc': 'Videos store GPS location, phone model, editing apps and AI Content Credentials (C2PA). Remove them online for free, without re-encoding and without uploading the video.',
   'lead': 'A video from your phone or from an AI generator can carry where it was recorded, which device or app made it, and a provenance record saying it was AI-generated. Here is what an MP4 or MOV contains and how to strip it without losing quality.',
   'cta': 'video', 'mins': 5,
   'body': '''
<h2>What metadata a video file contains</h2>
<ul>
<li><strong>Location:</strong> iPhone and Android videos usually store the GPS coordinates where they were recorded.</li>
<li><strong>Device and software:</strong> make, model, iOS or Android version, and the app or encoder that exported the file.</li>
<li><strong>Dates</strong> of recording and editing.</li>
<li><strong>XMP:</strong> editing history from apps such as Premiere Pro or CapCut.</li>
<li><strong>C2PA / Content Credentials:</strong> a signed record that AI video tools and some editors add, often saying the video was generated or edited with AI. TikTok, Instagram and YouTube can read it.</li>
</ul>

<h2>How to remove video metadata with IA Cleaner</h2>
<ol>
<li>Open <a href="/#video">IA Cleaner → Video</a>.</li>
<li>Drop your MP4, MOV or M4V. On a phone, tap the drop zone and pick the video from your gallery.</li>
<li>Check the report: location, device data, XMP and Content Credentials are listed, and the box <em>What the original reveals</em> shows any tool, author or edit history found.</li>
<li>Click <strong>Download clean video</strong>.</li>
</ol>
<p>The video is cleaned <strong>losslessly</strong>: the metadata boxes are removed and the file structure is rebuilt, but no frame is re-encoded, so quality and size stay the same. Nothing is uploaded — even large videos are processed in your browser.</p>

<h2>What stays in the file</h2>
<ul>
<li>The basic technical data every player needs (resolution, duration, codec) and the container’s internal creation time.</li>
<li>Anything visible in the picture or audible in the sound, including visible watermarks and burned-in captions.</li>
<li>Invisible watermarks embedded in the frames themselves, such as Google’s SynthID. Those are not metadata.</li>
</ul>
<p>Other formats such as WebM, MKV or AVI are not supported yet. If you need them, export to MP4 first.</p>

<h2>Other ways</h2>
<ul>
<li><strong>ffmpeg:</strong> <code>ffmpeg -i in.mp4 -map_metadata -1 -c copy out.mp4</code> removes most global metadata without re-encoding, but can leave per-track data and does not always remove C2PA boxes.</li>
<li><strong>Re-exporting</strong> from a video editor usually drops the original metadata but re-encodes the video and adds the editor’s own.</li>
</ul>
'''},
  'es': {
   'slug': 'quitar-metadatos-video',
   'title': 'Cómo quitar los metadatos de un vídeo (MP4 y MOV)',
   'seo_title': 'Quitar o borrar metadatos de un vídeo (MP4, MOV) online gratis y sin recodificar',
   'desc': 'Los vídeos guardan la ubicación GPS, el modelo del móvil, las apps de edición y las Content Credentials (C2PA) de la IA. Bórralos online gratis, sin recodificar y sin subir el vídeo.',
   'lead': 'Un vídeo del móvil o de un generador de IA puede llevar dónde se grabó, con qué dispositivo o app se hizo y un registro de procedencia que dice que se generó con IA. Esto es lo que contiene un MP4 o MOV y cómo eliminarlo sin perder calidad.',
   'cta': 'video', 'mins': 5,
   'body': '''
<h2>Qué metadatos tiene un vídeo</h2>
<ul>
<li><strong>Ubicación:</strong> los vídeos de iPhone y Android suelen guardar las coordenadas GPS donde se grabaron.</li>
<li><strong>Dispositivo y software:</strong> marca, modelo, versión de iOS o Android y la app o el codificador que exportó el archivo.</li>
<li><strong>Fechas</strong> de grabación y de edición.</li>
<li><strong>XMP:</strong> historial de edición de apps como Premiere Pro o CapCut.</li>
<li><strong>C2PA / Content Credentials:</strong> un registro firmado que añaden las herramientas de vídeo con IA y algunos editores, y que a menudo dice que el vídeo se generó o editó con IA. TikTok, Instagram y YouTube pueden leerlo.</li>
</ul>

<h2>Cómo quitar los metadatos de un vídeo con IA Cleaner</h2>
<ol>
<li>Abre <a href="/es/#video">IA Cleaner → Vídeo</a>.</li>
<li>Arrastra tu MP4, MOV o M4V. En el móvil, toca la zona de carga y elige el vídeo de tu galería.</li>
<li>Revisa el informe: aparecen la ubicación, los datos del dispositivo, el XMP y las Content Credentials, y el recuadro <em>Lo que el original revela</em> muestra la herramienta, el autor o el historial de ediciones que haya.</li>
<li>Pulsa <strong>Descargar vídeo limpio</strong>.</li>
</ol>
<p>El vídeo se limpia <strong>sin pérdida</strong>: se eliminan los bloques de metadatos y se reconstruye la estructura del archivo, pero no se vuelve a codificar ningún fotograma, así que la calidad y el tamaño no cambian. No se sube nada: incluso los vídeos grandes se procesan en tu navegador.</p>

<h2>Lo que se queda en el archivo</h2>
<ul>
<li>Los datos técnicos básicos que necesita cualquier reproductor (resolución, duración, códec) y la fecha interna de creación del contenedor.</li>
<li>Todo lo que se ve en la imagen o se oye en el audio, incluidas las marcas de agua visibles y los subtítulos incrustados.</li>
<li>Las marcas de agua invisibles dentro de los propios fotogramas, como SynthID de Google. Eso no son metadatos.</li>
</ul>
<p>Otros formatos como WebM, MKV o AVI todavía no son compatibles. Si los necesitas, expórtalos antes a MP4.</p>

<h2>Otras formas</h2>
<ul>
<li><strong>ffmpeg:</strong> <code>ffmpeg -i entrada.mp4 -map_metadata -1 -c copy salida.mp4</code> quita la mayoría de metadatos globales sin recodificar, pero puede dejar datos por pista y no siempre elimina los bloques C2PA.</li>
<li><strong>Volver a exportar</strong> desde un editor de vídeo suele quitar los metadatos originales, pero recodifica el vídeo y añade los del propio editor.</li>
</ul>
'''},
 },
 {
  'id': 'samsung',
  'en': {
   'slug': 'samsung-galaxy-ai-label',
   'title': 'The AI label on Samsung Galaxy photos: what it is and what you can remove',
   'seo_title': 'Samsung Galaxy AI Label & Watermark on Photos: What You Can Remove',
   'desc': 'Photos edited with Galaxy AI get a visible mark and AI metadata that phones and social networks read. Here is what each part is, which one IA Cleaner removes and which one it can’t.',
   'lead': 'Edited a photo with Galaxy AI and now it shows an AI icon, or social networks label it as AI-generated? Samsung adds two different things to those images. Here is what each one is and what you can do about it.',
   'cta': 'images', 'mins': 4,
   'body': '''
<h2>Two different things: a visible mark and metadata</h2>
<ul>
<li><strong>A visible mark in the corner</strong> of images changed with generative Galaxy AI features (such as Generative Edit). It is part of the picture itself — pixels, not metadata.</li>
<li><strong>Metadata</strong> written into the file stating that the image was edited with AI. On recent models this can include C2PA Content Credentials. Gallery, other apps and social networks like Instagram, Facebook or TikTok can read it and show “AI-generated content” labels.</li>
</ul>

<h2>Remove the AI metadata</h2>
<ol>
<li>On your phone, open <a href="/#images">iacleaner.com → Images</a> in Samsung Internet or Chrome.</li>
<li>Tap the drop zone and choose the photo from your gallery.</li>
<li>The report shows the metadata found and flags AI-related entries; the box <em>What the original reveals</em> lists the tool and AI use.</li>
<li>Tap <strong>Download clean image</strong> and share that copy.</li>
</ol>
<p>The photo never leaves your phone and its pixels are not changed.</p>

<h2>What IA Cleaner can’t remove</h2>
<p>The visible mark is drawn into the image, so removing metadata does not touch it. IA Cleaner does not edit pixels. Also keep in mind that platforms can detect AI in other ways, and many require you to disclose realistic AI edits — be honest where it matters.</p>

<h2>Tips</h2>
<ul>
<li>Keep the original in your gallery; the clean copy is a separate file.</li>
<li>Galaxy AI features that don’t generate new content usually don’t add these labels. If you are unsure, drop the photo into IA Cleaner and check the report.</li>
</ul>
'''},
  'es': {
   'slug': 'etiqueta-ia-samsung-galaxy',
   'title': 'La etiqueta de IA en las fotos de Samsung Galaxy: qué es y qué puedes quitar',
   'seo_title': 'Quitar la etiqueta de IA de las fotos de Samsung (Galaxy AI): qué se puede y qué no',
   'desc': 'Las fotos editadas con Galaxy AI llevan una marca visible y metadatos de IA que leen el móvil y las redes sociales. Te explicamos qué es cada cosa, cuál quita IA Cleaner y cuál no.',
   'lead': '¿Has editado una foto con Galaxy AI y ahora sale un icono de IA, o las redes la marcan como «contenido generado por IA»? Samsung añade dos cosas distintas a esas imágenes. Esto es lo que es cada una y qué puedes hacer.',
   'cta': 'images', 'mins': 4,
   'body': '''
<h2>Dos cosas distintas: una marca visible y metadatos</h2>
<ul>
<li><strong>Una marca visible en la esquina</strong> de las imágenes modificadas con funciones generativas de Galaxy AI (como la Edición generativa). Forma parte de la propia imagen: son píxeles, no metadatos.</li>
<li><strong>Metadatos</strong> escritos dentro del archivo que indican que la imagen se editó con IA. En modelos recientes pueden incluir Content Credentials (C2PA). La Galería, otras apps y redes como Instagram, Facebook o TikTok pueden leerlos y mostrar etiquetas de «contenido generado por IA».</li>
</ul>

<h2>Quita los metadatos de IA</h2>
<ol>
<li>En el móvil, abre <a href="/es/#images">iacleaner.com → Imágenes</a> en Samsung Internet o Chrome.</li>
<li>Toca la zona de carga y elige la foto de tu galería.</li>
<li>El informe muestra los metadatos encontrados y marca los relacionados con IA; el recuadro <em>Lo que el original revela</em> indica la herramienta y el uso de IA.</li>
<li>Toca <strong>Descargar imagen limpia</strong> y comparte esa copia.</li>
</ol>
<p>La foto no sale de tu móvil y sus píxeles no cambian.</p>

<h2>Lo que IA Cleaner no puede quitar</h2>
<p>La marca visible está dibujada en la imagen, así que quitar los metadatos no la toca. IA Cleaner no edita píxeles. Ten en cuenta también que las plataformas pueden detectar la IA de otras formas y que muchas exigen indicar las ediciones realistas hechas con IA: sé honesto donde importe.</p>

<h2>Consejos</h2>
<ul>
<li>Guarda el original en la galería; la copia limpia es un archivo aparte.</li>
<li>Las funciones de Galaxy AI que no generan contenido nuevo no suelen añadir estas etiquetas. Si dudas, arrastra la foto a IA Cleaner y revisa el informe.</li>
</ul>
'''},
 },
 {
  'id': 'social',
  'en': {
   'slug': 'ai-label-facebook-x-linkedin',
   'title': 'AI labels on Facebook, Threads, LinkedIn, X and YouTube: why they appear',
   'seo_title': '“Made with AI” / “AI Info” Label on Facebook, LinkedIn, X & YouTube: Why & How to Fix',
   'desc': 'Facebook, Threads, LinkedIn, YouTube and other networks use C2PA and IPTC metadata — and what creators declare — to show AI labels. See what triggers them and how to check and clean your file before posting.',
   'lead': 'The same photo can get an “AI info” label on Facebook, a CR icon on LinkedIn and an “altered or synthetic” note on YouTube. Most of these labels start with the same thing: metadata inside your file. Here is how each network decides, and what you can check before posting.',
   'cta': 'images', 'mins': 5,
   'body': '''
<h2>What each network looks at</h2>
<ul>
<li><strong>Facebook and Threads (Meta):</strong> the same system as Instagram — the “AI info” label appears when the file carries C2PA Content Credentials or IPTC fields saying it was made or edited with AI, or when you mark it yourself. See the <a href="/guides/instagram-ai-info-label/">Instagram guide</a>.</li>
<li><strong>LinkedIn:</strong> shows a small <strong>CR</strong> icon on images with Content Credentials. Clicking it reveals the tool, and often that AI was used.</li>
<li><strong>YouTube:</strong> asks creators to disclose realistic altered or synthetic content, and also uses C2PA, for example to show “captured with a camera”.</li>
<li><strong>X and others:</strong> labelling rules change often; many rely on what the creator declares, on metadata or on their own detection.</li>
</ul>

<h2>Check and clean your file before posting</h2>
<ol>
<li>Open <a href="/#images">IA Cleaner → Images</a> (or <a href="/#video">Video</a> for MP4/MOV).</li>
<li>Drop the exact file you were going to upload.</li>
<li>Look for <em>C2PA / Content Credentials</em>, <em>XMP</em> with <code>DigitalSourceType</code> and the box <em>What the original reveals</em>.</li>
<li>Download the clean copy and upload that one.</li>
</ol>

<h2>What this won’t change</h2>
<ul>
<li>A label you added yourself, or one a network applies because of its own detection or your account settings.</li>
<li>Invisible watermarks in the pixels (such as SynthID) or visible logos.</li>
<li>Your obligations: most networks require you to disclose realistic AI-generated content. Removing metadata is about privacy and accuracy — for example when a small AI retouch marks a real photo as “AI” — not about hiding synthetic media.</li>
</ul>
'''},
  'es': {
   'slug': 'etiqueta-ia-facebook-x-linkedin',
   'title': 'Etiquetas de IA en Facebook, Threads, LinkedIn, X y YouTube: por qué aparecen',
   'seo_title': 'Quitar la etiqueta «Información de IA» en Facebook, LinkedIn, X y YouTube: por qué sale',
   'desc': 'Facebook, Threads, LinkedIn, YouTube y otras redes usan los metadatos C2PA e IPTC, y lo que declara el creador, para mostrar etiquetas de IA. Mira qué las activa y cómo revisar y limpiar tu archivo antes de publicar.',
   'lead': 'La misma foto puede recibir la etiqueta «Información de IA» en Facebook, un icono CR en LinkedIn y un aviso de «contenido alterado o sintético» en YouTube. Casi todas empiezan por lo mismo: los metadatos de tu archivo. Así decide cada red y esto es lo que puedes revisar antes de publicar.',
   'cta': 'images', 'mins': 5,
   'body': '''
<h2>Qué mira cada red</h2>
<ul>
<li><strong>Facebook y Threads (Meta):</strong> el mismo sistema que Instagram. La etiqueta «Información de IA» aparece cuando el archivo lleva Content Credentials (C2PA) o campos IPTC que dicen que se creó o editó con IA, o cuando la marcas tú. Mira la <a href="/es/guias/etiqueta-ia-instagram/">guía de Instagram</a>.</li>
<li><strong>LinkedIn:</strong> muestra un pequeño icono <strong>CR</strong> en las imágenes con Content Credentials. Al pulsarlo se ve la herramienta y, a menudo, que se usó IA.</li>
<li><strong>YouTube:</strong> pide a los creadores que indiquen el contenido alterado o sintético realista, y también usa C2PA, por ejemplo para mostrar «grabado con una cámara».</li>
<li><strong>X y otras:</strong> sus normas de etiquetado cambian a menudo; muchas se basan en lo que declara el creador, en los metadatos o en su propia detección.</li>
</ul>

<h2>Revisa y limpia tu archivo antes de publicar</h2>
<ol>
<li>Abre <a href="/es/#images">IA Cleaner → Imágenes</a> (o <a href="/es/#video">Vídeo</a> para MP4/MOV).</li>
<li>Arrastra exactamente el archivo que ibas a subir.</li>
<li>Busca <em>C2PA / Content Credentials</em>, <em>XMP</em> con <code>DigitalSourceType</code> y el recuadro <em>Lo que el original revela</em>.</li>
<li>Descarga la copia limpia y sube esa.</li>
</ol>

<h2>Lo que esto no cambia</h2>
<ul>
<li>Una etiqueta que hayas puesto tú, o que la red añada por su propia detección o por la configuración de tu cuenta.</li>
<li>Las marcas de agua invisibles en los píxeles (como SynthID) o los logos visibles.</li>
<li>Tus obligaciones: la mayoría de redes exigen indicar el contenido realista generado con IA. Quitar metadatos sirve para tu privacidad y para evitar etiquetas injustas (por ejemplo, cuando un pequeño retoque con IA marca una foto real como «IA»), no para ocultar contenido sintético.</li>
</ul>
'''},
 },
 {
  'id': 'watermark',
  'en': {
   'slug': 'remove-ai-watermark',
   'title': 'AI watermarks: what can be removed and what can’t (C2PA, SynthID, ChatGPT text)',
   'seo_title': 'Can You Remove an AI Watermark? C2PA vs SynthID vs ChatGPT Text, Explained',
   'desc': '“AI watermark” can mean three very different things: metadata like C2PA, invisible watermarks like SynthID, and visible logos. Here is which ones exist in images, video and text, and which ones a metadata cleaner can remove.',
   'lead': 'People say “AI watermark” for three different things. Only one of them is metadata. Here is an honest breakdown of what ChatGPT, Gemini, Firefly and others add, and what can and can’t be removed.',
   'cta': 'images', 'mins': 6,
   'body': '''
<h2>1. Metadata “watermarks” (removable)</h2>
<p><strong>C2PA Content Credentials</strong>, XMP and IPTC fields are records stored <em>next to</em> the image or video data. ChatGPT, Adobe Firefly, Microsoft tools and others write them to say a file was AI-generated. They are what most social networks read to show AI labels, and they can be removed without touching a single pixel — that is exactly what <a href="/#images">IA Cleaner</a> does.</p>

<h2>2. Invisible watermarks (not removable here)</h2>
<p><strong>SynthID</strong> (Google: Gemini, Imagen, Veo) and similar systems hide a signal in the pixels, audio or word choices themselves. It survives screenshots, cropping and compression and is detected only by the provider’s own tools. It is not metadata, so no metadata cleaner — including IA Cleaner — can see or remove it. Tools that claim to remove it do so by altering the content itself.</p>

<h2>3. Visible marks (not removable here)</h2>
<p>Logos or icons drawn into the image, like the mark Samsung adds to Galaxy AI edits. They are part of the picture. IA Cleaner does not edit pixels.</p>

<h2>What about ChatGPT text?</h2>
<p>There is no visible watermark in ChatGPT text. What people find are <strong>invisible Unicode characters</strong>, citation markers like <code>oaicite</code> and <code>utm_source=chatgpt.com</code> links that come along when you copy. Those are easy to detect and remove — see <a href="/guides/chatgpt-hidden-characters/">ChatGPT hidden characters</a> or paste your text in <a href="/">IA Cleaner → Text</a>. Statistical watermarks in word choice, if a provider uses them, can’t be removed by cleaning characters.</p>

<h2>Quick summary</h2>
<ul>
<li><strong>C2PA, XMP, IPTC, PNG prompts:</strong> removable, losslessly.</li>
<li><strong>Hidden characters in text:</strong> removable.</li>
<li><strong>SynthID and other invisible watermarks:</strong> not removable with a metadata tool.</li>
<li><strong>Visible logos:</strong> not removable with a metadata tool.</li>
</ul>
<p>Use this for privacy and to avoid wrong labels, and disclose AI use where it is required.</p>
'''},
  'es': {
   'slug': 'quitar-marca-de-agua-ia',
   'title': 'Marcas de agua de IA: qué se puede quitar y qué no (C2PA, SynthID, texto de ChatGPT)',
   'seo_title': '¿Se puede quitar la marca de agua de IA? C2PA, SynthID y texto de ChatGPT explicados',
   'desc': '«Marca de agua de IA» puede ser tres cosas muy distintas: metadatos como C2PA, marcas invisibles como SynthID y logos visibles. Te explicamos cuáles hay en imágenes, vídeos y textos, y cuáles se pueden quitar con un limpiador de metadatos.',
   'lead': 'Se llama «marca de agua de IA» a tres cosas distintas, y solo una son metadatos. Este es un resumen honesto de lo que añaden ChatGPT, Gemini, Firefly y otras herramientas, y de lo que se puede y no se puede quitar.',
   'cta': 'images', 'mins': 6,
   'body': '''
<h2>1. «Marcas» en los metadatos (se pueden quitar)</h2>
<p>Las <strong>Content Credentials (C2PA)</strong> y los campos XMP e IPTC son registros guardados <em>junto a</em> los datos de la imagen o el vídeo. ChatGPT, Adobe Firefly, las herramientas de Microsoft y otras los escriben para indicar que un archivo se generó con IA. Son lo que leen la mayoría de redes para mostrar etiquetas de IA, y se pueden quitar sin tocar ni un píxel: es justo lo que hace <a href="/es/#images">IA Cleaner</a>.</p>

<h2>2. Marcas de agua invisibles (aquí no se pueden quitar)</h2>
<p><strong>SynthID</strong> (Google: Gemini, Imagen, Veo) y sistemas parecidos esconden una señal en los propios píxeles, en el audio o en la elección de palabras. Sobrevive a capturas, recortes y compresión, y solo la detectan las herramientas del propio proveedor. No son metadatos, así que ningún limpiador de metadatos, tampoco IA Cleaner, puede verla ni quitarla. Las herramientas que dicen eliminarla lo hacen alterando el propio contenido.</p>

<h2>3. Marcas visibles (aquí no se pueden quitar)</h2>
<p>Logos o iconos dibujados en la imagen, como la marca que añade Samsung a las ediciones con Galaxy AI. Forman parte de la imagen. IA Cleaner no edita píxeles.</p>

<h2>¿Y el texto de ChatGPT?</h2>
<p>El texto de ChatGPT no lleva una marca de agua visible. Lo que la gente encuentra son <strong>caracteres Unicode invisibles</strong>, marcas de cita como <code>oaicite</code> y enlaces con <code>utm_source=chatgpt.com</code> que vienen al copiar. Eso se detecta y se quita fácilmente: mira <a href="/es/guias/caracteres-ocultos-chatgpt/">caracteres ocultos de ChatGPT</a> o pega tu texto en <a href="/es/">IA Cleaner → Texto</a>. Las marcas estadísticas en la elección de palabras, si un proveedor las usa, no se quitan limpiando caracteres.</p>

<h2>Resumen rápido</h2>
<ul>
<li><strong>C2PA, XMP, IPTC, prompts en PNG:</strong> se pueden quitar, sin pérdida.</li>
<li><strong>Caracteres ocultos en el texto:</strong> se pueden quitar.</li>
<li><strong>SynthID y otras marcas invisibles:</strong> no se quitan con una herramienta de metadatos.</li>
<li><strong>Logos visibles:</strong> no se quitan con una herramienta de metadatos.</li>
</ul>
<p>Úsalo para tu privacidad y para evitar etiquetas injustas, e indica el uso de IA donde sea obligatorio.</p>
'''},
 },
 {
  'id': 'whatsapp',
  'en': {
   'slug': 'whatsapp-photo-metadata',
   'title': 'Does WhatsApp remove photo metadata? What gets sent and how to be sure',
   'seo_title': 'Does WhatsApp Remove Photo Metadata (GPS, EXIF)? Photo vs Document Explained',
   'desc': 'WhatsApp usually strips most metadata when you send a photo, but not when you send it as a document. Here is what is kept in each case and how to clean a photo before sending it.',
   'lead': 'It depends on how you send it. As a normal photo, WhatsApp recompresses the image and drops most metadata. As a document, it sends the original file untouched — GPS location included. Here is how to be sure.',
   'cta': 'images', 'mins': 4,
   'body': '''
<h2>Sent as a photo</h2>
<p>When you send an image the usual way (gallery or camera), WhatsApp makes a new, compressed copy. That copy normally loses most EXIF data, including the GPS location and the camera model, and any C2PA Content Credentials. Quality is reduced too, even with the HD option.</p>

<h2>Sent as a document</h2>
<p>When you attach the image as a <strong>document</strong> to keep full quality, WhatsApp sends the original file byte for byte. Everything inside it travels too: GPS location, phone model, dates, editing apps and AI metadata.</p>

<h2>Other apps work differently</h2>
<ul>
<li><strong>Telegram:</strong> “photo” is compressed; “file” sends the original with all its metadata.</li>
<li><strong>Email, cloud links and AirDrop:</strong> usually send the original file.</li>
<li><strong>Social networks:</strong> most strip metadata from the public copy, but read it first when you upload.</li>
</ul>

<h2>Clean the photo before sending it</h2>
<ol>
<li>Open <a href="/#images">iacleaner.com → Images</a> in your phone’s browser.</li>
<li>Pick the photo, check what it contains, and tap <strong>Download clean image</strong>.</li>
<li>Send the clean copy, as a photo or as a document — full quality, no metadata.</li>
</ol>
<p>Nothing is uploaded: the photo is cleaned on your phone.</p>

<h2>Can you see the metadata of a photo you received?</h2>
<p>If it came as a normal WhatsApp photo, there is usually little left besides basic size information. If it came as a document, drop it into IA Cleaner to see everything it contains.</p>
'''},
  'es': {
   'slug': 'metadatos-fotos-whatsapp',
   'title': '¿WhatsApp borra los metadatos de las fotos? Qué se envía y cómo asegurarte',
   'seo_title': '¿WhatsApp borra los metadatos de las fotos (GPS, EXIF)? Foto o documento',
   'desc': 'WhatsApp suele quitar casi todos los metadatos al enviar una foto, pero no si la envías como documento. Te explicamos qué se conserva en cada caso y cómo limpiar una foto antes de enviarla.',
   'lead': 'Depende de cómo la envíes. Como foto normal, WhatsApp vuelve a comprimir la imagen y quita casi todos los metadatos. Como documento, envía el archivo original sin tocar, con la ubicación GPS incluida. Así puedes asegurarte.',
   'cta': 'images', 'mins': 4,
   'body': '''
<h2>Enviada como foto</h2>
<p>Cuando envías una imagen de la forma habitual (galería o cámara), WhatsApp crea una copia nueva y comprimida. Esa copia normalmente pierde casi todos los datos EXIF, incluidas la ubicación GPS y el modelo de cámara, y las Content Credentials (C2PA). También baja la calidad, incluso con la opción HD.</p>

<h2>Enviada como documento</h2>
<p>Cuando adjuntas la imagen como <strong>documento</strong> para mantener la calidad, WhatsApp envía el archivo original byte a byte. Todo lo que lleva dentro viaja también: ubicación GPS, modelo del móvil, fechas, apps de edición y metadatos de IA.</p>

<h2>Otras apps funcionan distinto</h2>
<ul>
<li><strong>Telegram:</strong> «foto» se comprime; «archivo» envía el original con todos sus metadatos.</li>
<li><strong>Correo, enlaces de la nube y AirDrop:</strong> suelen enviar el archivo original.</li>
<li><strong>Redes sociales:</strong> la mayoría quitan los metadatos de la copia pública, pero los leen antes al subirla.</li>
</ul>

<h2>Limpia la foto antes de enviarla</h2>
<ol>
<li>Abre <a href="/es/#images">iacleaner.com → Imágenes</a> en el navegador del móvil.</li>
<li>Elige la foto, mira lo que contiene y toca <strong>Descargar imagen limpia</strong>.</li>
<li>Envía la copia limpia, como foto o como documento: máxima calidad y sin metadatos.</li>
</ol>
<p>No se sube nada: la foto se limpia en tu móvil.</p>

<h2>¿Se pueden ver los metadatos de una foto que te han enviado?</h2>
<p>Si llegó como foto normal de WhatsApp, normalmente queda poco más que el tamaño. Si llegó como documento, arrástrala a IA Cleaner para ver todo lo que contiene.</p>
'''},
 },
 {
  'id': 'viewer',
  'en': {
   'slug': 'view-metadata-online',
   'title': 'How to view the metadata of a photo, PDF or video online',
   'seo_title': 'View Metadata Online: Photo (EXIF, GPS), PDF & Video Metadata Viewer — Free',
   'desc': 'See every metadata block in a JPG, PNG, WebP, PDF, Word file or MP4: EXIF, GPS, XMP, C2PA Content Credentials, author and AI tags. Free, in your browser, nothing uploaded.',
   'lead': 'Want to know what a file says about you before sharing it? IA Cleaner works as a metadata viewer: drop any photo, document or video and it lists everything hidden inside — and you decide whether to download a clean copy.',
   'cta': 'images', 'mins': 3,
   'body': '''
<h2>What you will see</h2>
<ul>
<li><strong>Photos (JPG, PNG, WebP):</strong> EXIF (camera, dates, GPS), XMP, IPTC, comments, embedded prompts and C2PA Content Credentials.</li>
<li><strong>Videos (MP4, MOV):</strong> location, device, XMP and Content Credentials.</li>
<li><strong>PDF:</strong> title, author, creator, producer, dates and XMP.</li>
<li><strong>Word, Excel, PowerPoint, OpenDocument:</strong> author, last modified by, company, application, template and editing time.</li>
<li><strong>What the original reveals:</strong> a summary of the tool, author or account, AI use and edit history found in Content Credentials and XMP.</li>
</ul>

<h2>How to use it</h2>
<ol>
<li>Open the right tab: <a href="/#images">Images</a>, <a href="/#video">Video</a> or <a href="/#documents">Documents</a>.</li>
<li>Drop the file. It is read in your browser — nothing is uploaded.</li>
<li>Read the report. Entries related to AI are marked <strong>AI</strong>.</li>
<li>If you only wanted to look, you are done. If you want to share the file without that data, click the download button for a clean copy.</li>
</ol>

<h2>Why “no metadata” can be meaningful</h2>
<p>Screenshots and files downloaded from social networks or messaging apps usually arrive without metadata. An empty report doesn’t tell you who made a file — it tells you the information has already been removed somewhere along the way. See <a href="/guides/check-if-image-is-ai-metadata/">how to tell if an image was made with AI</a>.</p>
'''},
  'es': {
   'slug': 'ver-metadatos-online',
   'title': 'Cómo ver los metadatos de una foto, un PDF o un vídeo online',
   'seo_title': 'Ver metadatos online gratis: fotos (EXIF, GPS), PDF, Word y vídeo',
   'desc': 'Mira todos los metadatos de un JPG, PNG, WebP, PDF, Word o MP4: EXIF, GPS, XMP, Content Credentials (C2PA), autor y etiquetas de IA. Gratis, en tu navegador y sin subir nada.',
   'lead': '¿Quieres saber qué dice un archivo de ti antes de compartirlo? IA Cleaner funciona como visor de metadatos: arrastra cualquier foto, documento o vídeo y te muestra todo lo que lleva escondido. Luego decides si descargas una copia limpia.',
   'cta': 'images', 'mins': 3,
   'body': '''
<h2>Qué vas a ver</h2>
<ul>
<li><strong>Fotos (JPG, PNG, WebP):</strong> EXIF (cámara, fechas, GPS), XMP, IPTC, comentarios, prompts incrustados y Content Credentials (C2PA).</li>
<li><strong>Vídeos (MP4, MOV):</strong> ubicación, dispositivo, XMP y Content Credentials.</li>
<li><strong>PDF:</strong> título, autor, creador, productor, fechas y XMP.</li>
<li><strong>Word, Excel, PowerPoint, OpenDocument:</strong> autor, última modificación por, empresa, aplicación, plantilla y tiempo de edición.</li>
<li><strong>Lo que el original revela:</strong> un resumen de la herramienta, el autor o la cuenta, el uso de IA y el historial de ediciones que haya en las Content Credentials y el XMP.</li>
</ul>

<h2>Cómo usarlo</h2>
<ol>
<li>Abre la pestaña adecuada: <a href="/es/#images">Imágenes</a>, <a href="/es/#video">Vídeo</a> o <a href="/es/#documents">Documentos</a>.</li>
<li>Arrastra el archivo. Se lee en tu navegador: no se sube nada.</li>
<li>Lee el informe. Las entradas relacionadas con IA aparecen marcadas con <strong>IA</strong>.</li>
<li>Si solo querías mirar, ya está. Si quieres compartir el archivo sin esos datos, pulsa el botón de descarga para obtener una copia limpia.</li>
</ol>

<h2>Por qué «sin metadatos» también dice algo</h2>
<p>Las capturas de pantalla y los archivos descargados de redes sociales o apps de mensajería suelen llegar sin metadatos. Un informe vacío no te dice quién hizo un archivo: te dice que esa información ya se eliminó por el camino. Mira <a href="/es/guias/saber-si-imagen-es-ia-metadatos/">cómo saber si una imagen está hecha con IA</a>.</p>
'''},
 },
]

CSS = '''
:root{--bg:#f5f7fa;--surface:#fff;--surface-2:#f0f3f7;--ink:#24344b;--muted:#6c7a8e;--faint:#9aa6b6;--line:#e2e7ee;--brand:#3f5a7d;--brand-2:#5a78a0;--brand-soft:#e7edf5;--shadow:0 1px 2px rgba(36,52,75,.04),0 8px 28px rgba(36,52,75,.06)}
*{box-sizing:border-box}
body{margin:0;background:radial-gradient(1200px 500px at 50% -180px,#e3eaf3 0%,transparent 70%),var(--bg);color:var(--ink);font:16px/1.7 Inter,system-ui,-apple-system,"Segoe UI",Roboto,sans-serif;-webkit-font-smoothing:antialiased}
a{color:var(--brand-2)}
code{font-family:ui-monospace,Consolas,monospace;font-size:.88em;background:var(--surface-2);padding:1px 6px;border-radius:5px;word-break:break-word}
kbd{font-family:inherit;font-size:.82em;background:var(--surface);border:1px solid var(--line);border-bottom-width:2px;border-radius:5px;padding:1px 6px}
.top{max-width:1040px;margin:0 auto;padding:22px 24px;display:flex;align-items:center;justify-content:space-between}
.brand{display:flex;align-items:center;gap:10px;text-decoration:none;color:var(--ink);font-weight:700;font-size:18px}
.brand img{width:38px;height:38px;object-fit:contain;mix-blend-mode:multiply}
.brand b{color:var(--brand-2)}
.top-right{display:flex;align-items:center;gap:18px}
.top-right>a{color:var(--muted);text-decoration:none;font-size:14px;font-weight:500}
.lang{display:flex;background:var(--surface);border:1px solid var(--line);border-radius:10px;padding:3px;box-shadow:var(--shadow)}
.lang a{font-size:12px;font-weight:700;letter-spacing:.04em;color:var(--muted);padding:5px 10px;border-radius:7px;text-decoration:none}
.lang a[aria-current=page]{background:var(--brand);color:#fff}
main{max-width:740px;margin:0 auto;padding:20px 24px 40px}
.crumbs{font-size:13px;color:var(--faint);margin-bottom:14px}
.crumbs a{color:var(--muted);text-decoration:none}
h1{font-size:clamp(28px,4.5vw,40px);line-height:1.18;letter-spacing:-.03em;margin:0 0 14px}
.lead{font-size:18px;color:var(--muted);margin:0 0 10px}
.meta{font-size:13px;color:var(--faint);margin-bottom:26px}
article h2{font-size:23px;letter-spacing:-.02em;margin:36px 0 10px}
article li{margin:6px 0}
.cta{display:flex;align-items:center;justify-content:space-between;gap:16px;flex-wrap:wrap;background:var(--surface);border:1px solid var(--line);border-radius:18px;padding:18px 22px;box-shadow:var(--shadow);margin:28px 0}
.cta img{width:46px;height:46px;mix-blend-mode:multiply}
.cta div{flex:1;min-width:200px}
.cta strong{display:block;font-size:16px}
.cta span{color:var(--muted);font-size:14px}
.btn{display:inline-block;background:var(--brand);color:#fff;text-decoration:none;font-weight:600;font-size:14px;padding:11px 20px;border-radius:11px;box-shadow:0 4px 14px rgba(63,90,125,.22)}
.btn:hover{background:#3d5577}
.cards{display:grid;gap:12px;margin-top:14px}
.card{display:block;background:var(--surface);border:1px solid var(--line);border-radius:16px;padding:18px 20px;text-decoration:none;color:var(--ink);box-shadow:var(--shadow);transition:.2s}
.card:hover{border-color:var(--brand-2);transform:translateY(-2px)}
.card strong{display:block;font-size:17px;margin-bottom:4px}
.card span{color:var(--muted);font-size:14px}
footer{text-align:center;color:var(--faint);font-size:12.5px;padding:24px 24px 40px}
'''

FONT = ('<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>'
        '<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">')

def e(s): return html.escape(s, quote=True)

def page(lang, url, alt, title, desc, body, ld):
    t = T[lang]
    other = 'es' if lang == 'en' else 'en'
    alts = ''.join(f'<link rel="alternate" hreflang="{l}" href="{SITE}{u}">' for l, u in alt.items())
    alts += f'<link rel="alternate" hreflang="x-default" href="{SITE}{alt["en"]}">'
    return f'''<!DOCTYPE html>
<!-- Generated by tools/build_guides.py. Do not edit by hand. -->
<html lang="{lang}">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{e(title)}</title>
<meta name="description" content="{e(desc)}">
<link rel="canonical" href="{SITE}{url}">
{alts}
<meta property="og:type" content="article"><meta property="og:site_name" content="IA Cleaner">
<meta property="og:url" content="{SITE}{url}"><meta property="og:title" content="{e(title)}"><meta property="og:description" content="{e(desc)}">
<meta property="og:locale" content="{t['locale']}"><meta property="og:image" content="{SITE}/logo.webp"><meta name="twitter:card" content="summary">
<meta name="theme-color" content="#3f5a7d">
<link rel="icon" href="/logo-96.webp" type="image/webp">
{FONT}
<script type="application/ld+json">{json.dumps(ld, ensure_ascii=False)}</script>
<style>{CSS}</style>
</head>
<body>
<div class="top">
  <a class="brand" href="{t['home']}"><img src="/logo-96.webp" width="38" height="38" alt=""><span>IA <b>Cleaner</b></span></a>
  <div class="top-right">
    <a href="{t['guides']}">{t['guides_name']}</a>
    <nav class="lang" aria-label="Language"><a href="{alt['en']}" hreflang="en" lang="en" data-lang="en"{' aria-current="page"' if lang == 'en' else ''}>EN</a><a href="{alt['es']}" hreflang="es" lang="es" data-lang="es"{' aria-current="page"' if lang == 'es' else ''}>ES</a></nav>
  </div>
</div>
<main>
{body}
</main>
<footer>{t['footer']}</footer>
<script>document.addEventListener('click', function(e){{ var a = e.target.closest('.lang a'); if (a) try{{ localStorage.setItem('iacleaner-lang', a.dataset.lang); }}catch(_){{}} }});</script>
<!-- Cloudflare Web Analytics: cookieless, anonymous page-view counts -->
<script defer src="https://static.cloudflareinsights.com/beacon.min.js" data-cf-beacon='{{"token": "fa9ba728ece1485f8ff40f3ab5f2eb02"}}'></script>
</body>
</html>
'''

def cta(lang, kind):
    t = T[lang]
    href = t['home'] + ('#' + kind if kind in ('images', 'video', 'documents') else '')
    return (f'<div class="cta"><img src="/logo-96.webp" width="46" height="46" alt=""><div><strong>{t["cta_title"]}</strong><span>{t["cta_text"]}</span></div>'
            f'<a class="btn" href="{href}">{t["open"]}</a></div>')

def url_of(lang, g):
    return f"{T[lang]['guides']}{g[lang]['slug']}/"

def write(url, content):
    p = ROOT / url.strip('/') / 'index.html'
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(content, encoding='utf-8')

sitemap_groups = [{'en': '/', 'es': '/es/'}, {'en': '/guides/', 'es': '/es/guias/'}]

for g in GUIDES:
    alt = {l: url_of(l, g) for l in ('en', 'es')}
    sitemap_groups.append(alt)
    for lang in ('en', 'es'):
        t, c = T[lang], g[lang]
        i = GUIDES.index(g)
        others = [GUIDES[(i + k) % len(GUIDES)] for k in range(1, len(GUIDES))][:5]
        related = ''.join(f'<a class="card" href="{url_of(lang, o)}"><strong>{e(o[lang]["title"])}</strong><span>{e(o[lang]["desc"])}</span></a>'
                          for o in others)
        body = f'''<nav class="crumbs"><a href="{t['home']}">IA Cleaner</a> › <a href="{t['guides']}">{t['guides_name']}</a></nav>
<article>
<h1>{e(c['title'])}</h1>
<p class="lead">{e(c['lead'])}</p>
<div class="meta">{t['updated']} {UPDATED} · {c['mins']} {t['read']}</div>
{cta(lang, c['cta'])}
{c['body'].strip()}
{cta(lang, c['cta'])}
</article>
<h2>{t['related']}</h2>
<div class="cards">{related}</div>'''
        ld = [{'@context': 'https://schema.org', '@type': 'TechArticle', 'headline': c['title'], 'description': c['desc'],
               'inLanguage': lang, 'datePublished': UPDATED, 'dateModified': UPDATED, 'url': SITE + alt[lang],
               'image': SITE + '/logo.webp', 'author': {'@type': 'Organization', 'name': 'IA Cleaner', 'url': SITE + t['home']},
               'publisher': {'@type': 'Organization', 'name': 'IA Cleaner', 'logo': {'@type': 'ImageObject', 'url': SITE + '/logo.webp'}}},
              {'@context': 'https://schema.org', '@type': 'BreadcrumbList', 'itemListElement': [
                  {'@type': 'ListItem', 'position': 1, 'name': 'IA Cleaner', 'item': SITE + t['home']},
                  {'@type': 'ListItem', 'position': 2, 'name': t['guides_name'], 'item': SITE + t['guides']},
                  {'@type': 'ListItem', 'position': 3, 'name': c['title'], 'item': SITE + alt[lang]}]}]
        write(alt[lang], page(lang, alt[lang], alt, c['seo_title'] + ' | IA Cleaner', c['desc'], body, ld))

# Guide index pages
for lang in ('en', 'es'):
    t = T[lang]
    cards = ''.join(f'<a class="card" href="{url_of(lang, g)}"><strong>{e(g[lang]["title"])}</strong><span>{e(g[lang]["desc"])}</span></a>' for g in GUIDES)
    body = f'''<nav class="crumbs"><a href="{t['home']}">IA Cleaner</a> › {t['guides_name']}</nav>
<h1>{t['idx_h1']}</h1>
<p class="lead">{t['idx_lead']}</p>
<div class="cards">{cards}</div>
{cta(lang, 'files')}'''
    ld = {'@context': 'https://schema.org', '@type': 'CollectionPage', 'name': t['idx_h1'], 'inLanguage': lang, 'url': SITE + t['guides']}
    write(t['guides'], page(lang, t['guides'], {'en': '/guides/', 'es': '/es/guias/'}, t['idx_title'], t['idx_desc'], body, ld))

# Sitemap
rows = []
for grp in sitemap_groups:
    links = ''.join(f'\n    <xhtml:link rel="alternate" hreflang="{l}" href="{SITE}{u}"/>' for l, u in grp.items())
    links += f'\n    <xhtml:link rel="alternate" hreflang="x-default" href="{SITE}{grp["en"]}"/>'
    for u in grp.values():
        rows.append(f'  <url>\n    <loc>{SITE}{u}</loc>\n    <lastmod>{UPDATED}</lastmod>{links}\n  </url>')
(ROOT / 'sitemap.xml').write_text('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" '
                                  'xmlns:xhtml="http://www.w3.org/1999/xhtml">\n' + '\n'.join(rows) + '\n</urlset>\n', encoding='utf-8')
print(f'{len(GUIDES) * 2} guides + 2 index pages + sitemap ({len(rows)} URLs) written')
