import html
from datetime import date, datetime, timedelta, timezone
from pathlib import Path

import pandas as pd
import streamlit as st

BASE_DIR = Path(__file__).parent

# ===========================================================================
# Content: profile, links, bio, background, education, interests, milestones, skills, projects
# ===========================================================================

PROFILE = {
    "name": "Vonn Vincent S. Caballero",
    "section": "CSIT349-F2",
    "program": "BSCS",
    "year_level": "3rd Year",
    "birthdate": date(2005, 4, 11),  
    "email": "vonnvincentcaballero@gmail.com",
    "phone": "09153405200",
    "page_icon": "👋",
    "photo_path": "images/profile.png",
    "photo_caption": "Vonn Vincent S. Caballero",
}

# >>> EDIT: replace the urls. "icon" is a slug from https://simpleicons.org
LINKS = [
    {"label": "Facebook", "icon": "facebook", "url": "https://www.facebook.com/vonnvincentcaballero"},
    {"label": "GitHub", "icon": "github", "url": "https://github.com/vnnvncnt3"},
    {"label": "LeetCode", "icon": "leetcode", "url": "https://leetcode.com/u/OyHM2NmTGV/"},
]

BIO = (
    "**Vonn**, **Bo**, or **Vong** is just an ordinary "
    "person who loves sleeping, eating, reading, watching, playing, running, walking, "
    "daydreaming, dancing, wrestling, and overthinking. At first impression, he may not "
    "seem approachable because of his intimidating gaze and a sense of awkwardness, but "
    "he is actually just your homie. Though he does not talk much, he would rather "
    "listen to your side stories."
)

BACKGROUND = (
    "Hello people from the world, I am Vonn Vincent S. Caballero. My middle name, "
    "Samoramos, is my mother's maiden name. It is my grandfather's last name, and he "
    "originated from Negros Oriental. When my mother married my father, her last name "
    "became Caballero and Samoramos became her middle name. I was born on {birthdate}, "
    "and I have existed on earth for {days} days (as of {today}). I am currently "
    "studying at Cebu Institute of Technology – University as a Computer Science student."
)

EDUCATION_TIMELINE = [
    {"Level": "Elementary", "School": "St. Thomas Aquinas School – Montessori (Bulacao)",
     "Years": "2011 – 2018",},
    {"Level": "Junior High School", "School": "Pardo National High School",
     "Years": "2018 – 2022",},
    {"Level": "Senior High School (STEM)", "School": "Cebu Institute of Technology – University",
     "Years": "2022 – 2024",},
    {"Level": "College (BSCS)", "School": "Cebu Institute of Technology – University",
     "Years": "2024 – present",},
]

EDUCATION_STORY = (
    "Back when I was in elementary school, I studied at a private school, St. Thomas "
    "Aquinas School – Montessori in Bulacao. There are actually two branches of the "
    "school: the main branch in Lawaan, Talisay City, which is very far from my place, "
    "and the Bulacao branch. I wasn't anything special to begin with, and I considered "
    "myself a late bloomer since there weren't any competitions or opportunities that I "
    "could have participated in at the school. That would not have been the case in the "
    "main branch, since it has many more sections compared to the Bulacao branch, which "
    "only had two. That's why I decided that when I graduated from elementary, I wanted "
    "to transfer somewhere I could harness my skills. I even planned to try the Science "
    "High School in Talisay City, but I wasn't able to meet the grade standard since it "
    "was the first time in my life I experienced academic burnout, and it affected my "
    "performance and grades. To step up, I made the decision to go to Pardo National "
    "High School. During my junior high school days, I was very lucky to experience "
    "becoming a star section. However, I had a hard time keeping up with them since I "
    "had little understanding of how the system worked. There was one time that I had a "
    "good score on an examination, but the grade I was given was too low. I had a hard "
    "time adapting to a completely different environment, since we were trained to speak "
    "English inside the campus during my elementary days, and having a conversation with "
    "them was like oil and water. Despite feeling like a burden to my classmates, I tried "
    "my best to work hard and surpass my limits so that I could also stand my ground with "
    "them. Although that didn't last long due to the pandemic. I'd say this was a "
    "difficult period for me, when I withdrew from the people around me, including my "
    "family and teachers who tried to approach me. In the end, though, I was able to "
    "reflect and understand myself better than before. As soon as the pandemic was almost "
    "lifted, it was time for me to move up to senior high school. I was planning to stay "
    "and have a redemption arc in this school, but I was unable to meet the grade "
    "requirements to get into STEM. So I decided to enroll at Cebu Institute of "
    "Technology – University to study STEM, officially becoming a Teknoy :/"
)

INTERESTS = {
    "Roblox": [
        "Playing hard-tier obbies such as Juke's Tower of Hell and Flood Escape 2.",
        "Building and creating maps for the game.",
        "Creating content videos about me overcoming obby challenges.",
        "Speedrunning and racing with players around the world.",
    ],
    "Mobile Legends": [
        "The roles I currently play are mid, EXP, and gold lane.",
        "I usually play solo queue, and matchmaking always picks me for EXP lane.",
        "I keep watching MPL tournaments and the watch parties of Wise and OhmyV33nus "
        "to keep up with meta changes and the pick-or-ban strategies to use.",
        "Last season, I kept using Balmond to rank up, but this season I keep using Edith "
        "to counter those pabebe duos who love using utility heroes such as Angela, "
        "Floryn, and Rafaela.",
    ],
    "Manhwa": [
        "I love reading manhwa, especially shoujo, and isekai slop stories.",
        "I usually read ongoing series, but I also read on other platforms such as MangaFire.",
        "I love reading manhwa because of the art style, the story, and the character development.",
        "Some of my favorite manhwa are 'Got Dropped into a Ghost Story, Still Gotta Work', 'Villainess Are Destined to Die', and 'Return of the Mountain Hua Sect'.",
    ],
    "Anime": [
        "I love watching anime and I usually enjoyed shounen and isekai genres.",
        "I usually watch reaction videos such as CawCawTv on his Twitch for a commentary and reactions to the anime.",
        "I have been watching anime ever since I was  in elementary school, it started when I was watching Pokemon and BeyBlade series.",
        "My favorite anime are 'Classroom of the Elite', 'Jojo Bizarre Adventure', and 'One Piece'.",
    ],    
}

MILESTONES = [
    ("4.9 million", "total views on my content videos"),
    ("Mythical Immortal", "rank reached in Mobile Legends, Season 40"),
    ("DAA & DSA", "passed under Sir Jay Vince Serato"),
    ("Perfect score", "on the Java Certification"),
]

SKILL_SCALE_NOTE = "Self-rated, 0 to 100."

TECH_SKILLS = [ 
    ("C", "Programming languages", 75),
    ("C++", "Programming languages", 78),
    ("C#", "Programming languages", 70),
    ("Java", "Programming languages", 85),
    ("Python", "Programming languages", 70),
    ("SQL Databases", "Data and AI", 80),
    ("Data Analytics", "Data and AI", 73),
    ("Machine Learning", "Data and AI", 61),
    ("Blazor", "Web", 55),
    ("Web Development", "Web", 90),
    ("Algorithm Solving", "Problem solving", 30),
]

SOFT_SKILLS = [
    ("Communication", "Interpersonal", 80),
    ("Teamwork", "Interpersonal", 80),
    ("Critical Thinking", "Thinking", 70),
    ("Problem Solving", "Thinking", 76),
    ("Adaptability", "Self-management", 90),
    ("Time Management", "Self-management", 60),
    ("Leadership", "Interpersonal", 60),
    ("Creativity", "Thinking", 95),
    ("Work Ethic", "Self-management", 95),
]

PROJECTS = [
    {"title": "TugmaSycan", "role": "SQL Database, & Web Developer",
     "tools": ["Python", "HTML", "CSS", "JavaScript", "Supabase", "draw.io",],
     "outcome": "TugmaSycan reads resumes the way a thorough reviewer would — if that reviewer never got tired, never skimmed, and could check every candidate against the exact same criteria. Built for recruiters, student organization leaders, and project managers who need to screen high volumes of applicants without losing track of why each one ranks where they do.", "link": "https://github.com/vnnvncnt3/TugmaSycan.git"},
    {"title": "CivicGuard", "role": "Backend Developer",
     "tools": ["Java 24", "JavaFX", "JavaFXML", "MariaDB", "CSS(JavaFX)", "JDBC", "Leaflet.js", "Maven", "XAMPP",],
     "outcome": "CivicGuard is a JavaFX desktop application built to bring order and transparency to disaster response operations in Cebu City. It replaces error-prone, paper-based workflows with a single shared MariaDB database that LGU staff, barangay officials, and the public all draw from in real time. ", "link": "https://github.com/kworuu/CivicGuard.git"},
    {"title": "Vestige", "role": "Frontend Developer",
     "tools": ["Blazor", "Tailwind CSS", "HTML", "C#", "JavaScript",],
     "outcome": "Front-end project for a walking-tour company: a Blazor Web App (.NET 8, Interactive Server) styled with Tailwind CSS 3. Three pages: Home, Our Story and Reviews.", "link": "https://github.com/vnnvncnt3/Vestige.git"},
]

FEEDBACK_TITLE = "What do you think of my portfolio?"

SECTIONS = [  
    ("About me", "about"),
    ("Autobiography", "autobiography"),
    ("Skills", "skills"),
    ("Projects", "projects"),
    ("Feedback", "feedback"),
]


# ===========================================================================
# Main function: sets up the page, sidebar, and all sections
# ===========================================================================

def main():
    P = PROFILE

    # Page setup 
    st.set_page_config(
        page_title=f"{P['name']} | Portfolio",
        page_icon=P["page_icon"],
        layout="wide",
    )
    inject_css()

    # Session state: reviews live here while the visitor's session is open
    st.session_state.setdefault("reviews", [])

    today = today_ph()
    days_alive = (today - P["birthdate"]).days

    # Sidebar: name, section, jump links, and social icons
    with st.sidebar:
        st.subheader(P["name"])
        st.caption(f"Section: {P['section']}")
        st.markdown("**Jump to**")
        st.markdown("\n".join(f"- [{label}](#{anchor})" for label, anchor in SECTIONS))
        st.divider()
        st.markdown(icon_links_html(), unsafe_allow_html=True)

    # Title and basic info (name, program, year level, section)
    st.title(P["name"])
    st.write(f"Program & Year: {P['program']} - {P['year_level']}")
    st.write(f"Section: {P['section']}")

    # About Me (photo + bio + metrics + contact info + social icons)
    st.header("About me", anchor="about", divider="orange")
    col_photo, col_info = st.columns([1, 2], gap="large")
    with col_photo:
        show_photo()
    with col_info:
        st.markdown(BIO)
        m1, m2, m3 = st.columns(3)
        m1.metric("Program", P["program"])
        m2.metric("Year level", P["year_level"])
        m3.metric("Days on earth", f"{days_alive:,}")
        st.markdown(
            f" [{P['email']}](mailto:{P['email']})  \n"
            f" [{P['phone']}](tel:{P['phone']})"
        )
        st.markdown(icon_links_html(34), unsafe_allow_html=True)

    # Autobiography (background, education, interests, milestones)
    st.header("Autobiography", anchor="autobiography", divider="orange")

    st.subheader("Background")
    st.markdown(
        BACKGROUND.format(
            days=f"{days_alive:,}",
            birthdate=long_date(P["birthdate"]),
            today=long_date(today),
        )
    )

    st.subheader("Education")
    st.table(pd.DataFrame(EDUCATION_TIMELINE).set_index("Level"))
    st.markdown(EDUCATION_STORY)  # always fully visible, no expander

    st.subheader("Interests")
    tabs = st.tabs(list(INTERESTS.keys()))
    for tab, points in zip(tabs, INTERESTS.values()):
        with tab:
            st.markdown("\n".join(f"- {point}" for point in points))

    st.subheader("Milestones")
    st.markdown(milestone_cards_html(), unsafe_allow_html=True)

    # Skills (tech and soft, with filters, chart, table, and CSV download)
    st.header("Skills", anchor="skills", divider="orange")
    skills_df = load_skills(TECH_SKILLS, SOFT_SKILLS)

    st.markdown(
        "**Tech:** " + ", ".join(s for s, _, _ in TECH_SKILLS) + ".  \n"
        "**Soft:** " + ", ".join(s for s, _, _ in SOFT_SKILLS) + "."
    )

    ctrl_col, chart_col = st.columns([1, 2], gap="large")
    with ctrl_col:
        kind = st.radio("Skill type", ["Tech skills", "Soft skills"], horizontal=True)
        of_kind = skills_df[skills_df["Type"] == kind]
        category = st.selectbox("Category", ["All"] + sorted(of_kind["Category"].unique()))
        min_level = st.slider("Show skills rated at least", 0, 100, 0, step=5)
        show_table = st.checkbox("Show data table", value=False)
        st.caption(SKILL_SCALE_NOTE)

    shown = of_kind if category == "All" else of_kind[of_kind["Category"] == category]
    shown = shown[shown["Level"] >= min_level]

    with chart_col:
        if shown.empty:
            st.info("No skills match these filters. Lower the minimum rating or pick another category.")
        else:
            st.vega_lite_chart(
                shown,
                {
                    "mark": {"type": "bar", "color": "#D4A24C"},
                    "height": {"step": 30},
                    "padding": {"left": 12, "right": 12, "top": 5, "bottom": 5},
                    "encoding": {
                        "x": {"field": "Level", "type": "quantitative",
                              "scale": {"domain": [0, 100]}},
                        "y": {"field": "Skill", "type": "nominal", "sort": "-x",
                              "title": None,
                              "axis": {"labelLimit": 300, "labelOverlap": False,
                                       "minExtent": 150, "labelPadding": 8}},
                    },
                },
                width="stretch",
            )

        if show_table and not shown.empty:
            st.table(shown[["Skill", "Category", "Level"]].set_index("Skill"))

    st.download_button(
        "Download these skills (CSV)",
        data=shown.to_csv(index=False).encode("utf-8"),
        file_name="skills.csv",
        mime="text/csv",
        disabled=shown.empty,
    )

    # Projects (title, role, tools, outcome, and link to GitHub or live site)
    st.header("Projects", anchor="projects", divider="orange")
    project_cols = st.columns(len(PROJECTS), gap="medium")
    for col, project in zip(project_cols, PROJECTS):
        with col.container(border=True):
            st.subheader(project["title"])
            st.markdown(f"**My role:** {project['role']}")
            st.markdown("**Tools:** " + " ".join(f"`{t}`" for t in project["tools"]))
            st.markdown(f"**Outcome:** {project['outcome']}")
            if project["link"]:
                st.link_button("Open project", project["link"])
            else:
                st.button("Link coming soon", key=f"nolink_{project['title']}", disabled=True)

    # Feedback (form for visitors to submit reviews, plus a list of reviews)
    st.header("Feedback", anchor="feedback", divider="orange")
    form_col, review_col = st.columns(2, gap="large")

    with form_col:
        st.subheader(FEEDBACK_TITLE)
        with st.form("feedback_form"):
            name = st.text_input("Your name (optional)")
            st.write("Overall rating")
            stars_picked = st.feedback("stars")  # None until clicked, else 0-4
            liked = st.multiselect(
                "Which sections did you like?", [label for label, _ in SECTIONS[:-1]]
            )
            comment = st.text_area("Your feedback", placeholder="Write a short comment here.")
            share = st.checkbox("Show my review in the list", value=True)
            submitted = st.form_submit_button("Send feedback")

        if submitted:
            if stars_picked is None:
                st.error("Please pick a star rating before sending.")
            elif not comment.strip():
                st.error("Please write a short comment before sending.")
            else:
                who = name.strip() or "Anonymous"
                if share:
                    st.session_state.reviews.insert(0, {
                        "name": who,
                        "rating": stars_picked + 1,
                        "liked": liked,
                        "comment": comment.strip(),
                    })
                st.success(f"Thanks, {who}! Your feedback was sent.")
                st.toast("Feedback sent", icon="✅")

    with review_col:
        st.subheader("Reviews")
        reviews = st.session_state.reviews
        if reviews:
            avg = sum(r["rating"] for r in reviews) / len(reviews)
            a, b = st.columns(2)
            a.metric("Reviews", len(reviews))
            b.metric("Average rating", star_text(int(avg + 0.5)), help=f"{avg:.1f} out of 5")
            for r in reviews:
                with st.container(border=True):
                    st.markdown(f"**{r['name']}**  \n:orange[{star_text(r['rating'])}]")
                    st.markdown(r["comment"])
                    if r["liked"]:
                        st.caption("Liked: " + ", ".join(r["liked"]))
            if st.button("Clear reviews"):
                st.session_state.reviews = []
                st.rerun()
            st.caption("Reviews are kept only while this page is open.")
        else:
            st.info("No reviews yet. Send the first one with the form.")

    st.divider()
    st.caption(f"{P['name']} | {P['section']}")


# ===========================================================================
# Helper functions: CSS, HTML, stars, dates, icons, and data loading
# ===========================================================================

def inject_css():
    """Global styling: clean links (no underline) and the milestone cards."""
    st.markdown(
        """
<style>
/* Links: no underline, no default link color */
a, a:hover, a:focus, a:visited, a:active,
[data-testid="stMarkdownContainer"] a,
[data-testid="stSidebar"] a,
[data-testid="stHeaderActionElements"] a {
    text-decoration: none !important;
}
[data-testid="stMarkdownContainer"] a,
[data-testid="stSidebar"] a {
    color: inherit !important;
}
[data-testid="stMarkdownContainer"] a:hover,
[data-testid="stSidebar"] a:hover {
    color: #D4A24C !important;
}

/* Milestone cards: one grid, identical padding and gaps, centered text */
.milestones {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(240px, 1fr));
    gap: 1rem;
    margin: 0;
    padding: 0;
}
.milestone-card {
    box-sizing: border-box;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    gap: 0.5rem;
    margin: 0;
    padding: 1.5rem 1rem;
    min-height: 9rem;
    text-align: center;
    background: #1E2128;
    border: 1px solid rgba(236, 232, 225, 0.15);
    border-radius: 12px;
}
.milestone-title {
    margin: 0;
    padding: 0;
    font-size: 1.9rem;
    font-weight: 700;
    line-height: 1.2;
    color: #D4A24C;
}
.milestone-desc {
    margin: 0;
    padding: 0;
    font-size: 0.95rem;
    line-height: 1.4;
    color: rgba(236, 232, 225, 0.75);
}
</style>
""",
        unsafe_allow_html=True,
    )


def milestone_cards_html():
    """Builds the milestone cards (title large on top, description beneath)."""
    cards = "".join(
        f'<div class="milestone-card">'
        f'<p class="milestone-title">{html.escape(title)}</p>'
        f'<p class="milestone-desc">{html.escape(desc)}</p>'
        f"</div>"
        for title, desc in MILESTONES
    )
    return f'<div class="milestones">{cards}</div>'


def star_text(score, out_of=5):
    """Filled and empty stars for a score, e.g. 4 -> ★★★★☆."""
    score = max(0, min(out_of, int(score)))
    return "★" * score + "☆" * (out_of - score)


def today_ph():
    """Today's date in the Philippines (UTC+8), so the age counter is correct
    even when the app runs on a cloud server in another time zone."""
    return datetime.now(timezone(timedelta(hours=8))).date()


def long_date(d):
    """April 11, 2005 (no leading zero, works on every OS)."""
    return f"{d.strftime('%B')} {d.day}, {d.year}"


def icon_links_html(size=30):
    """Clickable icons that open the links listed in LINKS."""
    parts = []
    for link in LINKS:
        parts.append(
            f'<a href="{link["url"]}" target="_blank" title="{link["label"]}" '
            f'style="margin-right:14px;">'
            f'<img src="https://cdn.simpleicons.org/{link["icon"]}/ffffff" '
            f'alt="{link["label"]}" width="{size}" height="{size}"></a>'
        )
    return "".join(parts)


@st.cache_data  # the cache key now includes the skill lists, so edits refresh it
def load_skills(tech_skills, soft_skills):
    rows = []
    for kind, items in (("Tech skills", tech_skills), ("Soft skills", soft_skills)):
        for skill, category, level in items:
            rows.append({"Type": kind, "Category": category, "Skill": skill, "Level": level})
    return pd.DataFrame(rows)


def show_photo():
    photo = BASE_DIR / PROFILE["photo_path"]
    if photo.exists():
        st.image(str(photo), caption=PROFILE["photo_caption"], width="stretch")
    else:
        with st.container(border=True):
            st.markdown("### 📷 Photo placeholder")
            st.caption(f"Add your photo at `{PROFILE['photo_path']}` to replace this stand-in.")


main()