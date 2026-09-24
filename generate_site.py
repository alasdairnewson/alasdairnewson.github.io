#!/usr/bin/env python3
"""Generate static HTML pages for alasdairnewson.github.io"""
from pathlib import Path

ROOT = Path(__file__).resolve().parent

NAV_ITEMS = [
    ("About Me", "/", None),
    ("Curriculum Vitae", "/cv/", None),
    ("PhD thesis and HDR", "/phd-thesis/", None),
    ("Publications", "/publications/", None),
    (
        "Research",
        "/research/",
        [
            ("Background Estimation", "/research/background-estimation/"),
            ("Biological Tracking", "/research/biological-tracking/"),
            ("Film Grain Rendering", "/research/film-grain/"),
            ("Image Editing & Autoencoders", "/research/image-editing/"),
            ("Image Inpainting", "/research/image-inpainting/"),
            ("Radar Tracking", "/research/radar-tracking/"),
            ("Video Inpainting", "/research/video-inpainting/"),
        ],
    ),
    ("Software and codes", "/software/", None),
    ("Teaching", "/teaching/", None),
    ("Misc", "/misc/", None),
]


def nav_html(active: str) -> str:
    parts = ['<ul class="nav-list" id="site-nav">']
    for label, href, children in NAV_ITEMS:
        current = ' aria-current="page"' if active == href else ""
        if children:
            parts.append('<li class="has-dropdown">')
            parts.append(f'<a href="{href}"{current}>{label}</a>')
            parts.append('<ul class="dropdown">')
            for clabel, chref in children:
                ccur = ' aria-current="page"' if active == chref else ""
                parts.append(f'<li><a href="{chref}"{ccur}>{clabel}</a></li>')
            parts.append("</ul></li>")
        else:
            parts.append(f'<li><a href="{href}"{current}>{label}</a></li>')
    parts.append("</ul>")
    return "\n".join(parts)


def page(title: str, active: str, body: str, description: str = "", body_class: str = "") -> str:
    desc = description or f"{title} — Alasdair Newson, Full Professor, Université Paris Cité"
    body_attr = f' class="{body_class}"' if body_class else ""
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <meta name="description" content="{desc}">
  <title>{title} — Alasdair Newson</title>
  <link rel="stylesheet" href="/css/style.css">
</head>
<body{body_attr}>
  <header class="site-header">
    <div class="nav-inner">
      <a class="brand" href="/">Alasdair Newson</a>
      <button class="nav-toggle" type="button" aria-expanded="false" aria-controls="site-nav">Menu</button>
      {nav_html(active)}
    </div>
  </header>
  <main>
{body}
  </main>
  <footer class="site-footer">
    <div class="wrap">
      <span>&copy; Alasdair Newson</span>
      <span>
        <a href="https://github.com/alasdairnewson">GitHub</a>
      </span>
    </div>
  </footer>
  <script src="/js/main.js"></script>
</body>
</html>
"""


def write(rel: str, html: str) -> None:
    path = ROOT / rel
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(html, encoding="utf-8")
    print("wrote", rel)


# ——— About / Home ———
ABOUT_BODY = """
    <section class="hero wrap">
      <h1>Alasdair Newson</h1>
      <p class="subtitle">Full Professor, MAP5 lab, Université Paris Cité</p>
    </section>

    <section class="about-band">
      <div class="wrap">
        <div class="about-panel">
          <h2>About me</h2>
          <div class="about-grid">
            <div class="about-text">
              <p>
                I completed my PhD in image and video processing in March 2014 under the supervision
                of Andrés Almansa, Yann Gousseau and Patrick Pérez, with Technicolor and Télécom Paris.
                My research interests include image and video inpainting and restoration, statistical
                methods in image processing, film restoration, variational methods, and motion estimation.
                I spent one year as a Postdoc researcher with the team of Guillermo Sapiro, after which
                I spent one year at Paris Descartes (Paris, France) with Julie Delon and Bruno Galerne.
                From 2018–2023 I was assistant professor with Télécom Paris.
              </p>
              <p>
                I am currently Full Professor at Université Paris Cité, in the Mathematics for Imaging
                team in the MAP5 lab, where I am working on deep learning for image processing.
              </p>
            </div>
            <div class="portrait-wrap">
              <picture>
                <img class="portrait" src="/assets/images/alasdair_portrait.jpg" alt="Portrait of Alasdair Newson"
                     onerror="this.style.display='none'; this.nextElementSibling.style.display='flex';">
                <div class="portrait portrait-placeholder" style="display:none" aria-hidden="true">
                  Add <strong>alasdair_portrait.jpg</strong><br>to assets/images/
                </div>
              </picture>
            </div>
          </div>
        </div>
      </div>
    </section>

    <div class="wrap page" style="padding-top:0">
      <section class="section">
        <div class="contact-block">
          <div><strong>Professional address:</strong> MAP5, Université Paris Cité</div>
          <div><strong>Contact:</strong> anewson &#39;at&#39; isir.upmc.fr</div>
        </div>
      </section>

      <section class="section">
        <div class="section-label">News</div>
        <h2>Recent updates</h2>
        <ul class="news-list">
          <li>
            Paper &ldquo;AURA: AUdio-dRiven streaming Avatar&rdquo;, with Nathaniel Cohen, Nicolas Dufour,
            Amélie Royer and Patrick Pérez, was accepted to <em>BMVC 2026</em>.
            <span class="links"><a href="https://nathanielcohen3.github.io/aura_website/">Project page</a></span>
          </li>
          <li>
            Paper &ldquo;Stochastic Orthogonal Regularization for Deep Projective Priors&rdquo;, with Ali Joundi
            and Yann Traonmilin, was accepted to <em>SIAM Journal on Imaging Sciences</em>.
            <span class="links"><a href="https://arxiv.org/abs/2505.13078">Preprint</a></span>
          </li>
          <li>
            Paper &ldquo;FlowID: Enhancing Forensic Identification with Latent Flow-Matching Models&rdquo;,
            with Jules Ripoll, David Bertoin and Charles Dossal, was accepted to
            <em>IJCAI 2026</em> (AI and Social Good Track).
            <span class="links"><a href="https://jrpll.github.io/flowid/">Project page</a></span>
          </li>
          <li>
            Paper &ldquo;Learning to Steer: Input-dependent Steering for Multimodal LLMs&rdquo;, with
            Jayneel Parekh, Pegah Khayatan, Mustafa Shukor, Arnaud Dapogny and Matthieu Cord,
            was accepted to <em>NeurIPS 2025</em>.
            <span class="links"><a href="https://arxiv.org/abs/2508.12815">Preprint</a></span>
          </li>
        </ul>
      </section>

      <section class="section">
        <div class="section-label">Group</div>
        <h2>PhD students and postdocs</h2>
        <ul class="people-list people-list-vertical">
          <li><a href="https://nathanielcohen3.github.io/">Nathaniel Cohen</a> (since 2026)</li>
          <li>Antoine Crosnier (since 2026)</li>
          <li><a href="https://pegah-kh.github.io/">Pegah Khayatan</a> (since 2025)</li>
          <li>Kimia Sadreddini (PhD student since 2025)</li>
          <li>Ali Joundi (PhD student since 2023)</li>
          <li>Jules Ripoll (PhD student since 2023)</li>
        </ul>

        <h3>Former PhD students and postdocs</h3>
        <ul class="people-list people-list-vertical">
          <li><a href="https://research.pasteur.fr/en/member/raphael-reme/">Raphael Reme</a></li>
          <li><a href="https://perso.telecom-paristech.fr/glesne/">Gwilherm Lesné</a></li>
          <li><a href="https://perso.telecom-paristech.fr/nicherel/">Nicolas Cherel</a></li>
          <li>Chi-Hieu Pham (now Maître de Conférences, Université de Bretagne Occidentale)</li>
          <li><a href="https://arthurouaknine.github.io/">Arthur Ouaknine</a> (now postdoc, MILA)</li>
          <li><a href="https://xu-yao.github.io/">Xu Yao</a> (now research scientist, Zoox)</li>
        </ul>
      </section>

      <section class="section">
        <div class="section-label">Network</div>
        <h2>Collaborators</h2>
        <p>I have had the great pleasure to collaborate with the following people:</p>
        <ul class="people-list">
          <li><a href="http://perso.telecom-paristech.fr/~almansa/HomePage/">Andrés Almansa</a></li>
          <li><a href="https://perso.telecom-paristech.fr/angelini/">Elsa Angelini</a></li>
          <li><a href="https://cord.isir.upmc.fr/">Matthieu Cord</a></li>
          <li><a href="https://delon.wp.mines-telecom.fr/">Julie Delon</a></li>
          <li><a href="https://www.lirmm.fr/~nfaraj/">Noura Faraj</a></li>
          <li><a href="http://www.math-info.univ-paris5.fr/~bgalerne/">Bruno Galerne</a></li>
          <li><a href="http://perso.telecom-paristech.fr/~gousseau/">Yann Gousseau</a></li>
          <li><a href="https://people.irisa.fr/Pierre.Hellier/">Pierre Hellier</a></li>
          <li><a href="https://perso.telecom-paristech.fr/ladjal/">Saïd Ladjal</a></li>
          <li><a href="https://research.pasteur.fr/fr/member/thibault-lagache/">Thibault Lagache</a></li>
          <li><a href="http://www.technicolor.com/en/patrick-perez">Patrick Pérez</a></li>
          <li><a href="http://www.cs.umd.edu/~qiu/">Qiang Qiu</a></li>
          <li><a href="http://www.ee.duke.edu/faculty/guillermo-sapiro">Guillermo Sapiro</a></li>
          <li><a href="http://cims.nyu.edu/~pablo/">Pablo Sprechmann</a></li>
          <li><a href="https://www.intel.com/content/www/us/en/research/researchers/mariano-tepper.html">Mariano Tepper</a></li>
          <li><a href="https://yanntraonmilin.perso.math.cnrs.fr/">Yann Traonmilin</a></li>
          <li><a href="https://perso.telecom-paristech.fr/tupin/">Florence Tupin</a></li>
        </ul>
      </section>
    </div>
"""

# ——— CV ———
CV_BODY = """
    <div class="wrap page">
      <header class="page-header">
        <div class="section-label">Curriculum Vitae</div>
        <h1>Curriculum Vitae</h1>
        <p class="lead">Full Professor, MAP5 lab, Université Paris Cité · British &amp; French</p>
      </header>

      <section class="section panel">
        <p><strong>Email:</strong> anewson &#39;at&#39; isir.upmc.fr</p>
        <p><a href="/assets/pdfs/cv_newson_english.pdf">Download CV (PDF)</a></p>
      </section>

      <section class="section">
        <h2>Professional experience</h2>
        <ul class="timeline">
          <li>
            <span class="when">Sept. 2026 – present</span>
            <span class="what">Full Professor</span>
            <div class="where">Université Paris Cité (MAP5)</div>
          </li>
          <li>
            <span class="when">Sept. 2023 – August 2026</span>
            <span class="what">Lecturer</span>
            <div class="where">Sorbonne Université (ISIR lab)</div>
          </li>
          <li>
            <span class="when">June 2018 – August 2023</span>
            <span class="what">Assistant Professor</span>
            <div class="where">Télécom Paris (LTCI lab)</div>
          </li>
          <li>
            <span class="when">Jan. 2017 – May 2018</span>
            <span class="what">Postdoc</span>
            <div class="where">Télécom Paris — Stochastic models for film grain synthesis</div>
          </li>
          <li>
            <span class="when">Sept. 2015 – Dec. 2016</span>
            <span class="what">Postdoc</span>
            <div class="where">Université Paris Descartes — Stochastic models for film grain synthesis</div>
          </li>
          <li>
            <span class="when">May 2014 – June 2015</span>
            <span class="what">Postdoc</span>
            <div class="where">Duke University — Background/foreground estimation in videos</div>
          </li>
          <li>
            <span class="when">Feb. 2010 – August 2010</span>
            <span class="what">Internship</span>
            <div class="where">Technicolor R&amp;I, Cesson-Sévigné — Logo removal algorithm &amp; GPU parallelisation</div>
          </li>
        </ul>
      </section>

      <section class="section">
        <h2>Education</h2>
        <ul class="timeline">
          <li>
            <span class="when">Feb. 2024</span>
            <span class="what">HDR, Institut Polytechnique de Paris</span>
            <div class="where">&ldquo;On Several Mathematical and Data-Driven Models for Image and Video Editing, Synthesis and Analysis&rdquo;</div>
          </li>
          <li>
            <span class="when">Jan. 2011 – March 2014</span>
            <span class="what">PhD in image processing</span>
            <div class="where">Technicolor &amp; Télécom ParisTech — &ldquo;On Video Completion: Line Scratch Detection and Video Inpainting in Complex Scenes&rdquo;</div>
          </li>
          <li>
            <span class="when">Sept. 2005 – July 2010</span>
            <span class="what">Engineering diploma (Master&rsquo;s), Computer Science</span>
            <div class="where">Université de Technologie de Compiègne — Real-time and embedded systems</div>
          </li>
          <li>
            <span class="when">June 2005</span>
            <span class="what">French Baccalauréat (scientific section, mention bien)</span>
            <div class="where">Lycée International de Saint-Germain-en-Laye</div>
          </li>
        </ul>
      </section>

      <section class="section">
        <h2>Academic exchanges</h2>
        <ul class="timeline">
          <li>
            <span class="when">Feb. 2009 – July 2009</span>
            <span class="what">Technische Universität Berlin, Germany</span>
            <div class="where">Six-month exchange, electronics and computer science</div>
          </li>
          <li>
            <span class="when">Feb. 2007 – July 2007</span>
            <span class="what">Fachhochschule Karlsruhe, Germany</span>
            <div class="where">Six-month exchange</div>
          </li>
        </ul>
      </section>

      <section class="section">
        <h2>Languages &amp; skills</h2>
        <div class="panel">
          <p><strong>Languages:</strong> Bilingual English–French; German (fluent); Spanish (beginner); Japanese (beginner).</p>
          <p><strong>Research domains:</strong> Image and video processing, computer vision, inpainting, statistical methods, variational methods.</p>
          <p><strong>Computing:</strong> C, C++, Matlab, Scilab, Ada, Python, VHDL, assembler, SQL, UML, Pascal, LaTeX, Excel, Word, PowerPoint.</p>
          <p><strong>Intercultural experience:</strong> Having lived in Great Britain, Canada, France, Germany and the United States, I enjoy discovering and adapting to new cultures and situations.</p>
        </div>
      </section>

      <section class="section">
        <h2>Awards and distinctions</h2>
        <ul>
          <li>ANR Jeunes Chercheurs Jeunes Chercheuses grant (starting October 2021)</li>
          <li>Google best student paper award, CVMP 2013 (&ldquo;Towards fast, generic video inpainting&rdquo;)</li>
        </ul>
      </section>
    </div>
"""

# ——— PhD / HDR ———
PHD_BODY = """
    <div class="wrap page">
      <header class="page-header">
        <div class="section-label">Theses</div>
        <h1>PhD thesis and HDR</h1>
        <p class="lead">Habilitation and doctoral dissertation.</p>
      </header>

      <section class="section panel">
        <h3>Habilitation à Diriger des Recherches (2023 / 2024)</h3>
        <p class="pub-title">On Several Mathematical and Data-Driven Models for Image and Video Editing, Synthesis and Analysis</p>
        <p class="pub-authors">Alasdair Newson · Institut Polytechnique de Paris</p>
        <p class="download-list"><a href="https://hal.science/tel-04198797v1" target="_blank" rel="noopener">Manuscript on HAL</a></p>
      </section>

      <section class="section panel">
        <h3>PhD thesis (2014)</h3>
        <p class="pub-title">On Video Completion: Line Scratch Detection in Films and Video Inpainting of Complex Scenes</p>
        <p class="pub-authors">Alasdair Newson · Technicolor &amp; Télécom ParisTech</p>
        <p class="download-list">
          <a href="https://drive.google.com/file/d/12VBOSJxyWhwxKF-oQ11yrG-214xxwvaT/view?usp=sharing" target="_blank" rel="noopener">Manuscript (PDF)</a>
        </p>
      </section>
    </div>
"""

# ——— Publications (condensed but complete by year) ———
PUBLICATIONS = [
    ("2025", [
        ("Neural Film Grain Rendering", "G. Lesné, Y. Gousseau, S. Ladjal, A. Newson", "Eurographics 2025",
         [("Code", "https://gwilherm-lesne.github.io/"), ("Paper", "https://hal.science/hal-04667141")]),
        ("Infusion: Internal Diffusion for Video Inpainting", "N. Cherel, A. Almansa, Y. Gousseau, A. Newson", "Eurographics 2025",
         [("Paper", "https://arxiv.org/abs/2311.01090"), ("Code", "https://github.com/ncherel/infusion"), ("Project", "https://infusion.telecom-paris.fr/")]),
        ("Restyling Unsupervised Concept Based Interpretable Networks with Generative Models", "J. Parekh, Q. Bouniot, P. Mozharovskyi, A. Newson, F. d'Alché-Buc", "ICLR 2025",
         [("Paper", "https://arxiv.org/abs/2407.01331")]),
        ("Learning to Steer: Input-dependent Steering for Multimodal LLMs", "J. Parekh, P. Khayatan, M. Shukor, A. Dapogny, A. Newson, M. Cord", "NeurIPS 2025",
         [("Preprint", "https://arxiv.org/abs/2508.12815")]),
    ]),
    ("2024", [
        ("A Concept-Based Explainability Framework for Large Multimodal Models", "J. Parekh, P. Khayatan, M. Shukor, A. Newson, M. Cord", "NeurIPS 2024",
         [("Paper", "https://arxiv.org/abs/2406.08074")]),
        ("Particle tracking in biological images with optical-flow enhanced Kalman filtering", "R. Reme, A. Newson, E. Angelini, J.C. Olivo-Marin, T. Lagache", "ISBI 2024",
         [("Paper", "https://pasteur.hal.science/pasteur-04626732/file/Kalman_and_optical_flow_filtering-1.pdf")]),
        ("Diffusion-Based Image Inpainting with Internal Learning", "N. Cherel, A. Almansa, Y. Gousseau, A. Newson", "EUSIPCO 2024",
         [("Paper", "https://arxiv.org/abs/2406.04206")]),
        ("Patch-based stochastic attention for image editing", "N. Cherel, A. Almansa, Y. Gousseau, A. Newson", "CVIU 2024",
         [("Paper", "https://arxiv.org/abs/2202.03163"), ("Code", "https://github.com/ncherel/psal")]),
    ]),
    ("2023", [
        ("A Compact and Semantic Latent Space for Disentangled and Controllable Image Editing", "G. Lesné, Y. Gousseau, S. Ladjal, A. Newson", "CVMP 2023",
         [("Paper", "https://arxiv.org/abs/2312.08256"), ("Code", "https://github.com/Gwilherm-LESNE/Disentangler")]),
        ("Tracking Intermittent Particles with Self-Learned Visual Features", "R. Reme, V. Piriou, A. Hanson, R. Yuste, A. Newson, E. Angelini, J.-C. Olivo-Marin, T. Lagache", "ISBI 2023",
         [("Paper", "https://hal.science/pasteur-04270849")]),
        ("Disentangled latent representations of images with atomic autoencoders", "A. Newson, Y. Traonmilin", "SAMPTA 2023",
         [("Paper", "https://hal.science/hal-03962759/file/atomic_autoencoders_hal2.pdf")]),
        ("Infusion: Internal Diffusion for Video Inpainting", "N. Cherel, A. Almansa, Y. Gousseau, A. Newson", "Preprint 2023",
         [("Preprint", "https://arxiv.org/abs/2311.01090")]),
    ]),
    ("2022", [
        ("Feature-style Encoder for Style-Based GAN Inversion", "X. Yao, A. Newson, Y. Gousseau, P. Hellier", "ECCV 2022",
         [("Paper", "https://arxiv.org/abs/2202.02183")]),
        ("A Patch-based Approach for Diverse and High-Fidelity Single Image Generation", "N. Cherel, A. Almansa, Y. Gousseau, A. Newson", "ICIP 2022",
         [("Paper", "https://hal.science/hal-03822204/"), ("Code", "https://github.com/ncherel/psin")]),
        ("PCA-AE: Principal Component Analysis Autoencoder for Organising the Latent Space of Generative Networks", "C.-H. Pham, S. Ladjal, A. Newson", "JMIV 2022",
         [("Paper", "https://hal.archives-ouvertes.fr/hal-03713275/")]),
    ]),
    ("2021", [
        ("A Latent Transformer for Disentangled Face Editing in Images and Videos", "X. Yao, A. Newson, Y. Gousseau, P. Hellier", "ICCV 2021",
         [("Paper", "https://openaccess.thecvf.com/content/ICCV2021/papers/Yao_A_Latent_Transformer_for_Disentangled_Face_Editing_in_Images_and_ICCV_2021_paper.pdf"),
          ("Code", "https://github.com/InterDigitalInc/latent-transformer")]),
        ("Multi-view Radar Semantic Segmentation", "A. Ouaknine, A. Newson, F. Tupin, P. Pérez, J. Rebut", "ICCV 2021",
         [("Paper", "https://openaccess.thecvf.com/content/ICCV2021/papers/Ouaknine_Multi-View_Radar_Semantic_Segmentation_ICCV_2021_paper.pdf"),
          ("Code", "https://github.com/valeoai/MVRSS")]),
        ("Learning Non-Linear Disentangled Editing For StyleGAN", "X. Yao, A. Newson, Y. Gousseau, P. Hellier", "ICIP 2021",
         [("Paper", "https://xu-yao.github.io/files/2021ICIP_Disentanglement_final_version.pdf")]),
    ]),
    ("2020", [
        ("High Resolution Face Age Editing", "X. Yao, G. Puy, A. Newson, Y. Gousseau, P. Hellier", "ICPR 2020",
         [("Paper", "https://arxiv.org/abs/2005.04410"), ("Code", "https://github.com/InterDigitalInc/HRFAE")]),
        ("CARRADA Dataset: Camera and Automotive Radar with Range-Angle-Doppler Annotations", "A. Ouaknine, A. Newson, J. Rebut, F. Tupin, P. Pérez", "ICPR 2020",
         [("Paper", "https://arxiv.org/abs/2005.01456")]),
        ("Un Modèle Aléatoire pour le Grain Photographique", "J. Delon, A. Newson", "Images des mathématiques, 2020",
         [("Paper", "http://images.math.cnrs.fr/Un-modele-aleatoire-pour-le-grain-photographique")]),
    ]),
    ("2019", [
        ("Processing Simple Geometric Attributes with Autoencoders", "A. Newson, A. Almansa, Y. Gousseau, S. Ladjal", "JMIV 2019",
         [("Paper", "https://hal.archives-ouvertes.fr/hal-02271281/document")]),
        ("A PCA-like Autoencoder", "S. Ladjal, A. Newson, C.-H. Pham", "arXiv:1904.01277",
         [("Preprint", "https://arxiv.org/abs/1904.01277")]),
    ]),
    ("2018", [
        ("Taking Apart Autoencoders: How do They Encode Geometric Shapes?", "A. Newson, A. Almansa, S. Ladjal, Y. Gousseau", "HAL preprint",
         [("Paper", "https://hal.archives-ouvertes.fr/hal-01676326/document")]),
    ]),
    ("2017", [
        ("Realistic Film Grain Rendering", "A. Newson, N. Faraj, J. Delon, B. Galerne", "IPOL 2017",
         [("Project", "http://www.ipol.im/pub/art/2017/192/")]),
        ("Non-Local Patch-Based Image Inpainting", "A. Newson, A. Almansa, Y. Gousseau, P. Pérez", "IPOL 2017",
         [("Project", "http://www.ipol.im/pub/art/2017/189/")]),
        ("Analysis of a Physically Realistic Film Grain Model, and a Gaussian Film Grain Synthesis Algorithm", "A. Newson, N. Faraj, J. Delon, B. Galerne", "SSVM 2017",
         [("Paper", "https://hal.archives-ouvertes.fr/hal-01494123/en")]),
        ("A Stochastic Film Grain Model for Resolution-Independent Rendering", "A. Newson, J. Delon, B. Galerne", "Computer Graphics Forum, 2017",
         [("Project", "http://www.ipol.im/pub/art/2017/192/")]),
    ]),
    ("2015", [
        ("Low-Rank Spatio-Temporal Video Segmentation", "A. Newson, M. Tepper, G. Sapiro", "BMVC 2015", []),
        ("Multi-temporal Foreground Detection in Videos", "M. Tepper, A. Newson, P. Sprechmann, G. Sapiro", "ICIP 2015",
         [("Project", "http://www.marianotepper.com.ar/multitemporal")]),
    ]),
    ("2014", [
        ("Video inpainting of complex scenes", "A. Newson, A. Almansa, M. Fradet, Y. Gousseau, P. Pérez", "SIAM Journal on Imaging Sciences, 2014",
         [("Paper", "http://perso.telecom-paristech.fr/~gousseau/video_inpainting/Video_inpainting_complex_scenes.pdf"),
          ("Project", "http://perso.telecom-paristech.fr/~gousseau/video_inpainting/"),
          ("Code", "http://perso.telecom-paristech.fr/~gousseau/video_inpainting/Video_inpainting_code_newson.tar.gz")]),
        ("Robust automatic line scratch detection in films", "A. Newson, A. Almansa, Y. Gousseau, P. Pérez", "IEEE Transactions on Image Processing, 2014",
         [("Project", "http://perso.telecom-paristech.fr/~gousseau/scratches/")]),
    ]),
    ("2013", [
        ("Towards fast, generic video inpainting", "A. Newson, A. Almansa, M. Fradet, Y. Gousseau, P. Pérez", "CVMP 2013",
         [("Project", "http://perso.telecom-paristech.fr/~gousseau/videoinpainting_cvmp")], True),
        ("Temporal filtering of line scratch detections in degraded films", "A. Newson, A. Almansa, Y. Gousseau, P. Pérez", "ICIP 2013",
         [("Project", "http://perso.telecom-paristech.fr/~gousseau/scratchfiltering")]),
        ("Vers un inpainting vidéo automatique, rapide et générique", "A. Newson, M. Fradet, P. Pérez, A. Almansa, Y. Gousseau", "GRETSI 2013",
         [("Paper", "http://perso.telecom-paristech.fr/~newson/Fast_video_inpainting_gretsi_complet.pdf")]),
    ]),
    ("2012", [
        ("Adaptive line scratch detection in degraded films", "A. Newson, P. Pérez, A. Almansa, Y. Gousseau", "CVMP 2012",
         [("Project", "http://perso.telecom-paristech.fr/~gousseau/scratch_detection")]),
    ]),
]


def pubs_html() -> str:
    blocks = []
    for year, items in PUBLICATIONS:
        pubs = []
        for item in items:
            title, authors, venue, links = item[0], item[1], item[2], item[3]
            award = item[4] if len(item) > 4 else False
            badge = ' <span class="badge">Best student paper</span>' if award else ""
            link_html = " · ".join(f'<a href="{h}">{t}</a>' for t, h in links if h and h != "#")
            missing = [t for t, h in links if h == "#"]
            if missing:
                extra = " · ".join(f'<span style="color:var(--muted)">{t}</span>' for t in missing)
                link_html = (link_html + " · " + extra) if link_html else extra
            if not link_html:
                link_html = ""
            pubs.append(f"""
        <article class="pub">
          <div class="pub-title">{title}{badge}</div>
          <div class="pub-authors">{authors}</div>
          <div class="pub-venue">{venue}</div>
          <div class="pub-links">{link_html}</div>
        </article>""")
        blocks.append(f'<section class="year-block"><h3>{year}</h3>{"".join(pubs)}</section>')
    return "\n".join(blocks)


PUBS_BODY = f"""
    <div class="wrap page">
      <header class="page-header">
        <div class="section-label">Bibliography</div>
        <h1>Publications</h1>
        <p class="lead">Journal and conference papers, with links to papers, code and project pages where available.</p>
      </header>
      {pubs_html()}
      <section class="section">
        <h2>Theses</h2>
        <article class="pub">
          <div class="pub-title">On Several Mathematical and Data-Driven Models for Image and Video Editing, Synthesis and Analysis</div>
          <div class="pub-authors">A. Newson, 2023/2024 — HDR</div>
          <div class="pub-links"><a href="/phd-thesis/">Details</a></div>
        </article>
        <article class="pub">
          <div class="pub-title">On Video Completion: Line Scratch Detection in Films and Video Inpainting of Complex Scenes</div>
          <div class="pub-authors">A. Newson, 2014 — PhD</div>
          <div class="pub-links"><a href="/phd-thesis/">Details</a></div>
        </article>
      </section>
    </div>
"""

# ——— Research hub ———
RESEARCH_BODY = """
    <div class="wrap page">
      <header class="page-header">
        <div class="section-label">Topics</div>
        <h1>Research</h1>
        <p class="lead">I have worked on, or am working on, the following topics.</p>
      </header>
      <div class="card-grid">
        <a class="card" href="/research/image-inpainting/">
          <h3>Image Inpainting</h3>
          <p>Filling occlusions with patch-based and diffusion methods.</p>
          <span class="arrow">Explore →</span>
        </a>
        <a class="card" href="/research/video-inpainting/">
          <h3>Video Inpainting</h3>
          <p>Patch-based and diffusion approaches for complex video scenes.</p>
          <span class="arrow">Explore →</span>
        </a>
        <a class="card" href="/research/image-editing/">
          <h3>Image Editing &amp; Autoencoders</h3>
          <p>Generative models and structured latent spaces for editing.</p>
          <span class="arrow">Explore →</span>
        </a>
        <a class="card" href="/research/background-estimation/">
          <h3>Background Estimation</h3>
          <p>Low-rank and robust methods for video foreground/background.</p>
          <span class="arrow">Explore →</span>
        </a>
        <a class="card" href="/research/radar-tracking/">
          <h3>Radar Tracking</h3>
          <p>Semantic segmentation and detection in automotive radar.</p>
          <span class="arrow">Explore →</span>
        </a>
        <a class="card" href="/research/biological-tracking/">
          <h3>Biological Tracking</h3>
          <p>Neuron tracking in biological microscopy imagery.</p>
          <span class="arrow">Explore →</span>
        </a>
        <a class="card" href="/research/film-grain/">
          <h3>Film Grain Rendering</h3>
          <p>Stochastic and neural synthesis of analog film grain.</p>
          <span class="arrow">Explore →</span>
        </a>
      </div>
      <p style="margin-top:2rem;color:var(--muted)">Also related: old film restoration (line scratch detection).</p>
    </div>
"""


def research_page(title: str, kicker: str, content: str) -> str:
    return f"""
    <div class="wrap page">
      <header class="page-header">
        <div class="section-label"><a href="/research/">Research</a> / {kicker}</div>
        <h1>{title}</h1>
      </header>
      {content}
    </div>
"""


BG_BODY = research_page(
    "Background Estimation in Videos",
    "Background estimation",
    """
      <section class="section">
        <p>
          Background estimation is a fundamental task of computer vision. Indeed, in problems such as
          tracking or object recognition in videos, a good background estimation is usually a
          prerequisite. This is because these subsequent tasks are much easier if we know where to
          look for interesting objects, in particular if we know where the foreground is (when we
          track objects, we are generally interested in foreground objects).
        </p>
      </section>

      <section class="section">
        <h2>Publications in this research area</h2>
        <ul>
          <li>
            <em>Low-Rank Spatio-Temporal Video Segmentation</em>,
            A. Newson, M. Tepper, G. Sapiro, BMVC 2015
          </li>
          <li>
            <em>Multi-temporal Foreground Detection in Videos</em>,
            M. Tepper, A. Newson, P. Sprechmann, G. Sapiro, ICIP 2015 —
            <a href="http://www.marianotepper.com.ar/multitemporal">Project webpage</a>
          </li>
        </ul>
      </section>

      <section class="section">
        <p>
          Here is an example of background/foreground estimation (thanks to
          <a href="http://dev.ipol.im/~jlezama/">Jose Lezama</a> for appearing in this video):
        </p>
        <figure class="figure figure-row">
          <div>
            <img src="/assets/images/background_estimation/background_input.png" alt="Input frame from a video">
            <figcaption>Input image (one frame of a video)</figcaption>
          </div>
          <div>
            <img src="/assets/images/background_estimation/background_output.png" alt="Estimated background">
            <figcaption>Estimated background</figcaption>
          </div>
        </figure>
      </section>

      <section class="section panel">
        <h3>Robust Principal Component Analysis (RPCA)</h3>
        <p>
          Candès et al. introduced an approach which is widely known as Robust Principal Component
          Analysis <a href="https://dl.acm.org/doi/10.1145/1970392.1970395">[1]</a> (even if other
          works had previously proposed robustified PCAs
          <a href="https://ieeexplore.ieee.org/document/937541">[2]</a>), which could be used for
          tasks such as background estimation. The central idea of this work is to robustify
          traditional Principal Component Analysis, a data analysis method which is very popular, but
          can break down in the presence of outliers. This is done by decomposing an input matrix
          (the video, in our case) into the sum of a low-rank and a sparse component. More precisely,
          we solve the following convex optimisation problem:
        </p>
        <p style="text-align:center; margin:1.25rem 0; font-size:1.05rem;">
          min<sub>L,S</sub>
          &nbsp;‖X − L − S‖<sub>F</sub><sup>2</sup>
          + λ<sub>*</sub> ‖L‖<sub>*</sub>
          + λ<sub>1</sub> ‖S‖<sub>1</sub>
        </p>
        <p>
          where <em>X</em> is the input matrix (our video), <em>L</em> is the low-rank background
          component and <em>S</em> is the sparse foreground component. The norms ‖·‖<sub>F</sub>,
          ‖·‖<sub>*</sub> and ‖·‖<sub>1</sub> correspond to the Frobenius matrix norm, the nuclear
          norm and the ℓ<sub>1</sub> norm, respectively. The two parameters λ<sub>*</sub> and
          λ<sub>1</sub> are tuning parameters.
        </p>
      </section>
    """,
)

BIO_BODY = research_page(
    "Biological Tracking",
    "Biological tracking",
    """
      <section class="section">
        <p>
          The goal of this project, which is the PhD work of
          <a href="https://github.com/raphaelreme">Raphael Reme</a>, in collaboration between
          Télécom Paris (Elsa Angelini, Alasdair Newson) and Institut Pasteur (Thibault Lagache,
          Jean-Christophe Olivo-Marin), is to detect and track the neurons of the hydra (a microscopic
          aquatic animal) when they light up when in contact with a certain substance. An example of
          this data:
        </p>
        <figure class="figure figure-compact">
          <img src="/assets/images/biological_tracking/biological_tracking.gif"
               alt="Example biological tracking of hydra neurons">
          <figcaption>Example biological tracking data</figcaption>
        </figure>
        <p>
          Codes for this work:
          <a href="https://github.com/raphaelreme">Raphael Reme</a>
        </p>
      </section>
    """,
)

FILM_BODY = research_page(
    "Film Grain Rendering",
    "Film grain",
    """
      <section class="section">
        <p>
          Film grain is the visual texture due to silver halide crystals in analog film emulsions.
          Synthesising it in digital images is desirable for artistic and compression purposes.
        </p>
      </section>
      <section class="section panel">
        <h3>Neural Film Grain Rendering</h3>
        <p>
          PhD work of <a href="https://perso.telecom-paristech.fr/glesne/">Gwilherm Lesné</a> at Télécom Paris
          (Yann Gousseau, Saïd Ladjal, Alasdair Newson): deep neural networks for analog film grain synthesis.
        </p>
        <figure class="figure">
          <img src="/assets/images/film_grain_rendering/film_grain_rendering.png"
               alt="Neural film grain rendering: original landscape (left) and with synthesised grain (right)">
          <figcaption>Neural film grain rendering — original (left) and with synthesised grain (right)</figcaption>
        </figure>
      </section>
      <section class="section panel">
        <h3>A Stochastic Film Grain Model for Resolution-Independent Rendering</h3>
        <p>
          Postdoc work at Université Paris Descartes with Julie Delon and Bruno Galerne: a physically
          realistic stochastic model for film grain synthesis.
        </p>
        <figure class="figure">
          <img src="/assets/images/film_grain_rendering/louvre.png"
               alt="Louvre courtyard with synthesised film grain">
          <figcaption>Stochastic film grain rendering — Louvre courtyard</figcaption>
        </figure>
        <figure class="figure">
          <img src="/assets/images/film_grain_rendering/cary_grant.jpg" alt="Cary Grant portrait with film grain">
          <figcaption>Cary Grant</figcaption>
        </figure>
        <figure class="figure">
          <img src="/assets/images/film_grain_rendering/rose.jpg" alt="Rose with film grain">
          <figcaption>Rose</figcaption>
        </figure>
        <figure class="figure">
          <img src="/assets/images/film_grain_rendering/ship.jpg" alt="Ship with film grain">
          <figcaption>Ship</figcaption>
        </figure>
        <figure class="figure">
          <img src="/assets/images/film_grain_rendering/vintage_car.jpg" alt="Vintage car with film grain">
          <figcaption>Vintage car</figcaption>
        </figure>
        <figure class="figure">
          <img src="/assets/images/film_grain_rendering/wizard_of_oz.jpg" alt="Wizard of Oz still with film grain">
          <figcaption>Wizard of Oz</figcaption>
        </figure>
        <ul>
          <li>A. Newson, J. Delon, B. Galerne — <em>Computer Graphics Forum</em> 36(8): 684–699 (2017)</li>
          <li>A. Newson, N. Faraj, B. Galerne, J. Delon — <em>IPOL</em> 7: 165–183 (2017)</li>
        </ul>
        <p>
          Software: GPU and CPU (IPOL demo) versions — see
          <a href="/software/">Software and codes</a>.
        </p>
      </section>
    """,
)

EDIT_BODY = research_page(
    "Image Editing and Autoencoders",
    "Image editing",
    """
      <section class="section">
        <p>
          Image editing is the process of modifying the visual, often times semantic, content of an
          image. An example is to remove or add glasses to an image of a face. This is useful mostly
          for artistic purposes (advertising, film post-production). These algorithms often use
          generative models or Autoencoders. Here are some of the works I have carried out on this
          subject.
        </p>
      </section>

      <section class="section panel">
        <h3>Image editing using Generative Models</h3>
        <p>
          Here is a link to the work of
          <a href="https://perso.telecom-paristech.fr/glesne/">Gwilherm Lesné</a>, my former PhD
          student, at Télécom Paris (Saïd Ladjal, Yann Gousseau, Alasdair Newson), on image editing
          using GANs and diffusion models:
        </p>
        <ul>
          <li><a href="https://perso.telecom-paristech.fr/glesne/">Gwilherm Lesné</a></li>
        </ul>
        <p>
          Here is a list of publications linked to the work of
          <a href="https://xu-yao.github.io/">Xu Yao</a>, my former PhD student, in collaboration
          between InterDigital (Pierre Hellier) and Télécom Paris (Yann Gousseau, Alasdair Newson),
          on image editing with GANs:
        </p>
        <ul>
          <li>
            Feature-style Encoder for Style-Based GAN Inversion,
            X. Yao, A. Newson, Y. Gousseau, P. Hellier, ECCV 2022 —
            <a href="https://arxiv.org/abs/2202.02183">Paper</a>
          </li>
          <li>
            A Latent Transformer for Disentangled Face Editing in Images and Videos,
            X. Yao, A. Newson, Y. Gousseau, P. Hellier, ICCV 2021 —
            <a href="https://openaccess.thecvf.com/content/ICCV2021/papers/Yao_A_Latent_Transformer_for_Disentangled_Face_Editing_in_Images_and_ICCV_2021_paper.pdf">Paper</a>,
            <a href="https://github.com/InterDigitalInc/latent-transformer">Code</a>
          </li>
          <li>
            Learning Non-Linear Disentangled Editing For StyleGAN,
            X. Yao, A. Newson, Y. Gousseau, P. Hellier, ICIP 2021 —
            <a href="https://xu-yao.github.io/files/2021ICIP_Disentanglement_final_version.pdf">Paper</a>
          </li>
          <li>
            High Resolution Face Age Editing,
            X. Yao, G. Puy, A. Newson, Y. Gousseau, P. Hellier, ICPR 2020 —
            <a href="https://arxiv.org/abs/2005.04410">Paper</a>,
            <a href="https://github.com/InterDigitalInc/HRFAE">Code</a>
          </li>
        </ul>
      </section>

      <section class="section panel">
        <h3>A short description of autoencoders</h3>
        <p>
          Autoencoders are (often deep) neural networks which project to and from a latent space
          which is of smaller dimensionality than the input data domain.
        </p>
        <figure class="figure">
          <img src="/assets/images/autoencoders/autoencoder.png" alt="Illustration of an autoencoder: encoder, latent space, and decoder">
          <figcaption>Illustration of an autoencoder</figcaption>
        </figure>
        <p>
          The main idea behind this is to use the compact and powerful latent space to understand,
          analyse and manipulate the input data in a much more high-level manner than in the data
          space. In the following projects, we try to study these architectures in detail in simple
          cases (images of shapes) and we propose new architectures and loss functions to create
          latent spaces with useful properties. More precisely, we are interested in the following
          questions:
        </p>
        <ul>
          <li>
            How can we build autoencoders with latent spaces with useful structural properties
            (independence of components, organisation of attributes in latent space)?
          </li>
          <li>
            Can we describe the precise mechanisms which allow autoencoders to encode and decode
            simple images?
          </li>
          <li>How to use autoencoder or GAN-type networks to carry out image editing</li>
        </ul>
      </section>

      <section class="section panel">
        <h3>Principal Component Analysis Autoencoder</h3>
        <p>
          <strong>PCAAE: Principal Component Analysis Autoencoder for organising the latent space of
          generative networks</strong>
        </p>
        <p>
          This is the work of Chi-Hieu Pham (postdoc), supervised by Saïd Ladjal, Alasdair Newson.
          The goal is to create an autoencoder which mimics the behaviour of a PCA, which can then
          be used for image editing. Here is an example of such editing:
        </p>
        <figure class="figure">
          <img src="/assets/images/autoencoders/pca_ae.png" alt="PCA-AE editing examples: hair colour and head pose control">
          <figcaption>PCA-AE editing — (a) hair colour controlling, (b) head pose controlling</figcaption>
        </figure>
        <p>
          The paper can be found here:
          <a href="https://arxiv.org/abs/2006.07827">Paper</a>
        </p>
      </section>

      <section class="section panel">
        <h3>Processing Simple Geometric Attributes with Autoencoders</h3>
        <p>
          Alasdair Newson, Andrés Almansa, Yann Gousseau, Saïd Ladjal<br>
          <em>Journal of Mathematical Imaging and Vision</em>, 2020 —
          <a href="https://hal.archives-ouvertes.fr/hal-02271281v1">Paper</a>
        </p>
        <h4>Abstract</h4>
        <p>
          Image synthesis is a core problem in modern deep learning, and many recent architectures
          such as autoencoders and Generative Adversarial networks produce spectacular results on
          highly complex data, such as images of faces or landscapes. While these results open up a
          wide range of new, advanced synthesis applications, there is also a severe lack of
          theoretical understanding of how these networks work. This results in a wide range of
          practical problems, such as difficulties in training, the tendency to sample images with
          little or no variability, and generalisation problems. In this paper, we propose to
          analyse the ability of the simplest generative network, the autoencoder, to encode and
          decode two simple geometric attributes: size and position. We believe that, in order to
          understand more complicated tasks, it is necessary to first understand how these networks
          process simple attributes. For the first property, we analyse the case of images of
          centred disks with variable radii. We explain how the autoencoder projects these images
          to and from a latent space of smallest possible dimension, a scalar. In particular, we
          describe both the encoding process and a closed-form solution to the decoding training
          problem in a network without biases, and show that during training, the network indeed
          finds this solution. We then investigate the best regularisation approaches which yield
          networks that generalise well. For the second property, position, we look at the encoding
          and decoding of Dirac delta functions, also known as &ldquo;one-hot&rdquo; vectors. We
          describe a hand-crafted filter that achieves encoding perfectly, and show that the network
          naturally finds this filter during training. We also show experimentally that the decoding
          can be achieved if the dataset is sampled in an appropriate manner. We hope that the
          insights given here will provide better understanding of the precise mechanisms used by
          generative networks, and will ultimately contribute to producing more robust and
          generalisable networks.
        </p>
      </section>
    """,
)

IMG_INP_BODY = research_page(
    "Image Inpainting",
    "Image inpainting",
    """
      <section class="section">
        <p>
          Image inpainting fills a hole (occlusion) in an image — for example to remove an unwanted
          object or restore a degraded region. It is used in personal editing and professional
          restoration (including films).
        </p>
        <figure class="figure figure-row">
          <div>
            <img src="/assets/images/image_inpainting/image_inpainting_in.png" alt="Input image with occlusion">
            <figcaption>Input image</figcaption>
          </div>
          <div>
            <img src="/assets/images/image_inpainting/image_inpainting_out.png" alt="Inpainted result">
            <figcaption>Inpainted image</figcaption>
          </div>
        </figure>
      </section>
      <section class="section panel">
        <h3>Diffusion-Based Image Inpainting with Internal Learning</h3>
        <p>
          Work of Nicolas Cherel (Télécom Paris / Université Paris Cité with Andrés Almansa &amp; Yann Gousseau) —
          EUSIPCO 2024. See <a href="https://perso.telecom-paristech.fr/nicherel/">Nicolas Cherel</a>.
        </p>
      </section>
      <section class="section panel">
        <h3>Non-Local Patch-Based Image Inpainting</h3>
        <p>
          Part of my PhD work (2014), later published in IPOL 2017 with an online demo and source code.
        </p>
      </section>
    """,
)

RADAR_BODY = research_page(
    "Radar Tracking",
    "Radar tracking",
    """
      <section class="section">
        <p>
          PhD work of <a href="https://arthurouaknine.github.io/">Arthur Ouaknine</a>, in collaboration between
          Télécom Paris (Alasdair Newson, Florence Tupin) and Valeo AI (Julien Rebut, Patrick Pérez):
          detecting pedestrians, cyclists and vehicles in Range–Doppler radar signals.
        </p>
        <figure class="figure">
          <img src="/assets/images/radar/radar_tracking.png" alt="Radar tracking illustration">
        </figure>
        <ul>
          <li>Multi-view Radar Semantic Segmentation — ICCV 2021</li>
          <li>CARRADA Dataset — ICPR 2020</li>
        </ul>
      </section>
    """,
)

VID_INP_BODY = research_page(
    "Video Inpainting",
    "Video inpainting",
    """
      <section class="section panel">
        <h3>Diffusion-based Video Inpainting</h3>
        <p>
          The goal of this project, which is the PhD work of
          <a href="https://ncherel.github.io/">Nicolas Cherel</a>, in collaboration between
          Télécom Paris (Yann Gousseau, Alasdair Newson) and Université Paris Cité (Andrés Almansa),
          is to use diffusion models for video inpainting. It concerns the following publications:
        </p>
        <ul>
          <li>
            <em>Infusion: Internal Diffusion for Video Inpainting</em>,
            N. Cherel, A. Almansa, Y. Gousseau, A. Newson, 2024 —
            <a href="https://arxiv.org/abs/2311.01090">Preprint</a> ·
            <a href="https://infusion.telecom-paris.fr/">Project</a> ·
            <a href="https://github.com/ncherel/infusion">Code</a>
          </li>
          <li>
            <em>Diffusion-Based Image Inpainting with Internal Learning</em>,
            N. Cherel, A. Almansa, Y. Gousseau, A. Newson, EUSIPCO 2024 —
            <a href="https://arxiv.org/abs/2406.04206">Paper</a>
          </li>
        </ul>
        <p>
          For more information, see the webpage of
          <a href="https://ncherel.github.io/">Nicolas Cherel</a>.
        </p>
      </section>

      <section class="section panel">
        <h3>Patch-based Video Inpainting</h3>
        <p>
          This was part of my PhD work, in collaboration between Technicolor
          (Matthieu Fradet, Patrick Pérez) and Télécom ParisTech (Andrés Almansa, Yann Gousseau).
          The goal is to use a patch-based approach to video inpainting. Here is an example of such
          an inpainting:
        </p>
        <figure class="figure figure-row">
          <div>
            <img src="/assets/images/video_inpainting/video_inpainting_in.png" alt="Input video frame with occlusion">
            <figcaption>Input frame</figcaption>
          </div>
          <div>
            <img src="/assets/images/video_inpainting/video_inpainting_out.png" alt="Inpainted video frame">
            <figcaption>Inpainted frame</figcaption>
          </div>
        </figure>

        <h3>Abstract</h3>
        <p>
          We propose an automatic video inpainting algorithm which relies on the optimisation of a
          global, patch-based functional. Our algorithm is able to deal with a variety of challenging
          situations which naturally arise in video inpainting, such as the correct reconstruction of
          dynamic textures, multiple moving objects and moving background. Furthermore, we achieve
          this in an order of magnitude less execution time with respect to the state-of-the-art.
          We are also able to achieve good quality results on high definition videos. Finally, we
          provide specific algorithmic details to make implementation of our algorithm as easy as
          possible. The resulting algorithm requires no segmentation or manual input other than the
          definition of the inpainting mask, and can deal with a wider variety of situations than is
          handled by previous work.
        </p>
        <p>
          Original project webpage:
          <a href="http://perso.telecom-paristech.fr/~gousseau/video_inpainting/">Project webpage</a>
        </p>

        <h3>Citing this work</h3>
        <p>If you wish to use our work or code, please cite the following paper:</p>
        <p>
          <strong>Video Inpainting of Complex Scenes</strong><br>
          Alasdair Newson, Andrés Almansa, Matthieu Fradet, Yann Gousseau, Patrick Pérez<br>
          <em>SIAM Journal on Imaging Sciences</em> 2014 7:4, 1993–2019
        </p>
        <p class="download-list">
          <a href="http://perso.telecom-paristech.fr/~gousseau/video_inpainting/Video_inpainting_complex_scenes.pdf">Download paper</a>
          ·
          <a href="https://perso.telecom-paristech.fr/gousseau/video_inpainting/">Video Inpainting of Complex Scenes</a>
        </p>
      </section>

      <section class="section">
        <h2>Video inpainting examples</h2>

        <div class="panel">
          <h3>Input video — Fontaine, Châtelet</h3>
          <p>Input video:</p>
          <div class="video-embed">
            <iframe src="https://www.youtube.com/embed/hnwo-HlzGE8" title="Fontaine Châtelet — input" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen loading="lazy"></iframe>
          </div>
          <ul>
            <li><a href="https://drive.google.com/file/d/0B34L9p-ehVeTNDdUX3Q4ZnNNbXc/view?usp=sharing">Download the input video</a></li>
            <li><a href="https://drive.google.com/file/d/0B34L9p-ehVeTV1hyMFp5bkJ2RkU/view?usp=sharing">Download the occlusion mask (AVI)</a></li>
            <li><a href="https://drive.google.com/file/d/0B34L9p-ehVeTVEUxdVE1VVJ0OGs/view?usp=sharing">Occlusion mask (.mat)</a></li>
          </ul>
          <p>Our inpainting result (slowed down by a factor of two for visualisation):</p>
          <div class="video-embed">
            <iframe src="https://www.youtube.com/embed/yyPm-PW6W7Y" title="Fontaine Châtelet — result" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen loading="lazy"></iframe>
          </div>
          <p><a href="https://drive.google.com/file/d/0B34L9p-ehVeTVEEwOV9pVEpjN3c/view?usp=sharing">Download our inpainting result</a></p>
        </div>

        <div class="panel">
          <h3>Input video — Les Loulous</h3>
          <p>Input video:</p>
          <div class="video-embed">
            <iframe src="https://www.youtube.com/embed/no4sOApQPV4" title="Les Loulous — input" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen loading="lazy"></iframe>
          </div>
          <ul>
            <li><a href="https://drive.google.com/file/d/0B34L9p-ehVeTMUhVUnQ2WGFSM2s/view?usp=sharing">Download the video</a></li>
            <li><a href="https://drive.google.com/file/d/0B34L9p-ehVeTV1hyMFp5bkJ2RkU/view?usp=sharing">Occlusion mask (AVI)</a></li>
            <li><a href="https://drive.google.com/file/d/0B34L9p-ehVeTQmlrbXFGVTlMZkk/view?usp=sharing">Occlusion mask (.mat)</a></li>
          </ul>
          <p>Our inpainting result (slowed down by a factor of two for visualisation):</p>
          <div class="video-embed">
            <iframe src="https://www.youtube.com/embed/2N0omfghhIc" title="Les Loulous — result" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen loading="lazy"></iframe>
          </div>
          <p><a href="https://drive.google.com/file/d/0B34L9p-ehVeTczJCUVR1blpiRlk/view?usp=sharing">Download inpainting result</a></p>
        </div>

        <div class="panel">
          <h3>Input video — Young Jaws</h3>
          <p>Input video:</p>
          <div class="video-embed">
            <iframe src="https://www.youtube.com/embed/cZfrtu9cwjw" title="Young Jaws — input" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen loading="lazy"></iframe>
          </div>
          <ul>
            <li><a href="https://drive.google.com/file/d/0B34L9p-ehVeTZm9za3QtYTVzRkE/view?usp=sharing">Young Jaws input</a></li>
            <li><a href="https://drive.google.com/file/d/0B34L9p-ehVeTZDAycEVLRy1iS1U/view?usp=sharing">Occlusion (AVI)</a></li>
            <li><a href="https://drive.google.com/file/d/0B34L9p-ehVeTbFFSOXZud0dmTHM/view?usp=sharing">Occlusion (.mat)</a></li>
          </ul>
          <p>Our result (slowed down by a factor of two for visualisation):</p>
          <div class="video-embed">
            <iframe src="https://www.youtube.com/embed/dgrw7PlR9Gc" title="Young Jaws — result" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen loading="lazy"></iframe>
          </div>
          <p><a href="https://drive.google.com/file/d/0B34L9p-ehVeTaUQwS093NGp5M1E/view?usp=sharing">Download inpainting result</a></p>
        </div>

        <div class="panel">
          <h3>Input video — Museum</h3>
          <p>
            This example is from the work of Miguel Granados et al.:
            <em>How not to be seen: Object removal from videos of crowded scenes</em>,
            M. Granados, K. Kim, J. Tompkin, O. Grau, J. Kautz and C. Theobalt,
            Computer Graphics Forum (EUROGRAPHICS), 2012.
          </p>
          <p>
            To download the input and masks of this work, see
            <a href="http://gvv.mpi-inf.mpg.de/projects/vidinp/">How Not to be Seen — Miguel Granados</a>.
          </p>
          <p>Comparison with Granados et al. (their result above, ours below):</p>
          <div class="video-embed">
            <iframe src="https://www.youtube.com/embed/znQxjpnL1WI" title="Museum — comparison with Granados et al." allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen loading="lazy"></iframe>
          </div>
          <p><a href="https://drive.google.com/file/d/0B34L9p-ehVeTajN3Q2JsRjR5TjA/view?usp=sharing">Museum, our result</a></p>
        </div>

        <div class="panel">
          <h3>Input video — Duo</h3>
          <p>
            This example is also from Granados et al. (EUROGRAPHICS 2012).
            Comparison (their result above, ours below):
          </p>
          <div class="video-embed">
            <iframe src="https://www.youtube.com/embed/MtflFvj8coQ" title="Duo — comparison with Granados et al." allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen loading="lazy"></iframe>
          </div>
          <p><a href="https://drive.google.com/file/d/0B34L9p-ehVeTaEJEWW1Vd0lxU3M/view?usp=sharing">Duo, our result</a></p>
        </div>
      </section>
    """,
)

# ——— Software ———
SOFTWARE_BODY = """
    <div class="wrap page">
      <header class="page-header">
        <div class="section-label">Code</div>
        <h1>Software and codes</h1>
        <p class="lead">Open implementations and demos related to my research.</p>
      </header>

      <section class="section panel">
        <h3>Image editing</h3>
        <p>Code for Gwilherm Lesné&rsquo;s work on disentangled image editing (CVMP 2023): see
          <a href="https://perso.telecom-paristech.fr/glesne/">Gwilherm Lesné</a>.</p>
      </section>

      <section class="section panel">
        <h3>Video inpainting</h3>
        <ul>
          <li>Diffusion-based video inpainting (Nicolas Cherel, 2024) —
            <a href="https://perso.telecom-paristech.fr/nicherel/">project page</a></li>
          <li>Video Inpainting of Complex Scenes —
            <a href="https://perso.telecom-paristech.fr/gousseau/video_inpainting/">Project &amp; code</a></li>
        </ul>
      </section>

      <section class="section panel">
        <h3>Image inpainting</h3>
        <ul>
          <li>Diffusion-based image inpainting (Nicolas Cherel, EUSIPCO 2024) —
            <a href="https://perso.telecom-paristech.fr/nicherel/">project page</a></li>
          <li>Non-local patch-based image inpainting (IPOL 2017) — online demo &amp; source on IPOL</li>
        </ul>
      </section>

      <section class="section panel">
        <h3>Film grain rendering</h3>
        <ul>
          <li>Neural film grain (Gwilherm Lesné) —
            <a href="https://perso.telecom-paristech.fr/glesne/">project page</a></li>
          <li>Stochastic film grain (IPOL 2017) — demo &amp; CPU code on IPOL</li>
          <li>GPU version —
            <a href="/assets/pdfs/film-grain-gpu.zip">Download</a>
            <span style="color:var(--muted)">(add archive)</span></li>
        </ul>
      </section>
    </div>
"""

# ——— Teaching ———
TEACHING_BODY = """
    <div class="wrap page">
      <header class="page-header">
        <div class="section-label">Courses</div>
        <h1>Teaching</h1>
        <p class="lead">Current and previous teaching activities.</p>
      </header>

      <section class="section">
        <h2>Current teaching</h2>
        <div class="panel">
          <h3>Université Paris Cité</h3>
          <ul>
            <li>Programmation —
              <a href="/assets/pdfs/teaching/programmation-tp.pdf">Sujet de TP</a> ·
              <a href="/assets/pdfs/teaching/programmation-mini-projets.pdf">Mini-projets</a> ·
              <a href="/assets/pdfs/teaching/programmation-qcm-2024-2025.pdf">QCM 2024–2025</a>
            </li>
          </ul>
        </div>
        <div class="panel">
          <h3>Sorbonne Université</h3>
          <ul><li>RDFIA</li></ul>
        </div>
        <div class="panel">
          <h3>Master MVA (ENS Paris-Saclay)</h3>
          <ul><li>Deep Learning for Image Restoration and Synthesis (DELIREs)</li></ul>
        </div>
        <div class="panel">
          <h3>Master Data Sciences (Polytechnique)</h3>
          <ul>
            <li>Deep Learning 2 —
              <a href="/assets/pdfs/teaching/slides-generative-models.pdf">Slides (generative models)</a>
            </li>
          </ul>
        </div>
      </section>

      <section class="section">
        <h2>Previous teaching</h2>
        <div class="panel">
          <h3>Sorbonne Université</h3>
          <ul>
            <li>Sciences des Données par l&rsquo;Exemple (lectures, TD, TP)</li>
            <li>DALAS: Data science, Learning and Applications</li>
          </ul>
        </div>
        <div class="panel">
          <h3>Master Data Sciences (Polytechnique)</h3>
          <ul>
            <li>Deep Learning 1</li>
            <li>Introduction to Computer Vision</li>
          </ul>
        </div>
        <div class="panel">
          <h3>Télécom Paris</h3>
          <ul>
            <li>IMA 205 — Apprentissage pour l&rsquo;image et la reconnaissance d&rsquo;objets</li>
            <li>IMA 206 — Réseaux génératifs, méthodes par patches, photographie computationnelle</li>
            <li>SI101 — Outils et applications pour le signal, les images et le son</li>
            <li>Lab supervision in &ldquo;Apprentissage Avancé&rdquo; (Data Scientist course)</li>
          </ul>
        </div>
        <div class="panel">
          <h3>Université Paris Descartes</h3>
          <ul>
            <li>TD/TP — Probabilités et Statistiques pour l&rsquo;Informatique (L2 Informatique)</li>
            <li>TD — Introduction aux Statistiques (L2 Mathématiques)</li>
          </ul>
        </div>
        <div class="panel">
          <h3>ESIEA</h3>
          <ul><li>Linear algebra (travaux dirigés)</li></ul>
        </div>
      </section>
    </div>
"""

# ——— Misc ———
MISC_BODY = """
    <div class="wrap page">
      <header class="page-header">
        <div class="section-label">Odds and ends</div>
        <h1>Misc</h1>
      </header>

      <section class="section">
        <blockquote class="poem">
          <p>An iamb&rsquo;s not an iamb</p>
          <p>A trochee&rsquo;s a trochee</p>
          <p>A spondee is not a spondee</p>
        </blockquote>
        <p class="poem-prompt">Can you figure out what is interesting about this poem? :)</p>
      </section>
    </div>
"""


def main() -> None:
    write("index.html", page("About Me", "/", ABOUT_BODY, "Alasdair Newson — Full Professor, MAP5, Université Paris Cité", body_class="home"))
    write("cv/index.html", page("Curriculum Vitae", "/cv/", CV_BODY))
    write("phd-thesis/index.html", page("PhD thesis and HDR", "/phd-thesis/", PHD_BODY))
    write("publications/index.html", page("Publications", "/publications/", PUBS_BODY))
    write("research/index.html", page("Research", "/research/", RESEARCH_BODY))
    write("research/background-estimation/index.html", page("Background Estimation", "/research/background-estimation/", BG_BODY))
    write("research/biological-tracking/index.html", page("Biological Tracking", "/research/biological-tracking/", BIO_BODY))
    write("research/film-grain/index.html", page("Film Grain Rendering", "/research/film-grain/", FILM_BODY))
    write("research/image-editing/index.html", page("Image Editing", "/research/image-editing/", EDIT_BODY))
    write("research/image-inpainting/index.html", page("Image Inpainting", "/research/image-inpainting/", IMG_INP_BODY))
    write("research/radar-tracking/index.html", page("Radar Tracking", "/research/radar-tracking/", RADAR_BODY))
    write("research/video-inpainting/index.html", page("Video Inpainting", "/research/video-inpainting/", VID_INP_BODY))
    write("software/index.html", page("Software and codes", "/software/", SOFTWARE_BODY))
    write("teaching/index.html", page("Teaching", "/teaching/", TEACHING_BODY))
    write("misc/index.html", page("Misc", "/misc/", MISC_BODY))

    assets_readme = """# Assets to add

Place the following files so the site can display them:

## Images (`assets/images/`)
- `portrait.jpg` — your photo (used on the About page)
- Research figures (optional but recommended):
  - `research/bg-input.jpg`, `research/bg-estimate.jpg`
  - `research/biological-tracking.jpg` (or `.gif` / `.mp4` in `assets/videos/`)
  - `research/film-grain-neural.jpg`, `research/film-grain-stochastic.jpg`
  - `research/pca-ae-editing.jpg`
  - `research/inpainting-input.jpg`, `research/inpainting-result.jpg`
  - `research/radar-tracking.jpg`
  - `research/video-inpaint-input.jpg`, `research/video-inpaint-result.jpg`

## PDFs (`assets/pdfs/`)
- `cv.pdf` — optional downloadable CV
- PhD / HDR manuscripts are linked externally (Google Drive / HAL), not stored in this repo
- Teaching materials under `assets/pdfs/teaching/` (see Teaching page links)
- Code archives (`.zip`) linked from Software / research pages

After copying files, update any placeholder `#` paper links on the Publications page with the real URLs from your Google Site.
"""
    write("assets/README.md", assets_readme)
    print("done")


if __name__ == "__main__":
    main()
