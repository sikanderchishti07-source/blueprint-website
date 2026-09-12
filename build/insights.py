# Insights section for the home page — built from content/blog/*.md
# so it stays current on its own as the owner publishes.

ICONS = {
    'Quarries & Mining': 'fa-mountain',
    'Inspections': 'fa-clipboard-check',
    'Renewals': 'fa-rotate',
    'Permitting': 'fa-stamp',
    'Waste Permits': 'fa-recycle',
    'Monitoring': 'fa-tower-broadcast',
    'Reporting': 'fa-file-lines',
    'Marine': 'fa-water',
}


def insights(posts, limit=4):
    posts = posts[:limit]
    n_total = str(len(posts)).zfill(2)

    cards = "".join(f"""
      <a href="blog-{p['slug']}.html" class="icard scroll-reveal">
        <span class="icard-img">
          <img src="{p['image']}" alt="" loading="lazy" />
          <span class="icard-n">{str(i).zfill(2)} / {n_total}</span>
          <span class="icard-ic"><i class="fas {ICONS.get(p['category'], 'fa-leaf')}"></i></span>
        </span>
        <span class="icard-body">
          <span class="icard-cat">{p['category']}</span>
          <h3>{p['title']}</h3>
          <p>{p['summary']}</p>
          <span class="icard-more">Read more <i class="fas fa-arrow-right"></i></span>
        </span>
      </a>""" for i, p in enumerate(posts, 1))

    return f"""
<!-- INSIGHTS -->
<section class="isec" id="insights">
  <div class="iwrap">

    <div class="ihead scroll-reveal">
      <div>
        <div class="ikick">INSIGHTS</div>
        <h2>Practical guidance on Saudi<br>environmental <em>regulation</em></h2>
        <p>What the rules actually require, written for the people who have to comply
           with them &mdash; permit categories, reporting deadlines, inspection findings
           and what to do about them.</p>
        <a href="blog.html" class="ibtn"><span class="circ"><i class="fas fa-arrow-right"></i></span><span>Read all articles</span></a>
      </div>
      <div class="ipanel">
        <img src="assets/img/cover-1-1920.webp" alt="" loading="lazy" />
        <span class="ipanel-tint"></span>
        <span class="ipanel-tag">WRITTEN BY PRACTITIONERS<br>NOT BY MARKETERS</span>
      </div>
    </div>

    <div class="itrack">{cards}</div>

    <div class="ifoot scroll-reveal">
      <div class="itag">Updated as the regulations change</div>
      <a href="blog.html" class="ibtn2-link">All articles <i class="fas fa-arrow-right"></i></a>
    </div>

  </div>
</section>
"""
