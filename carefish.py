import streamlit as st
from streamlit_carousel import carousel
from st_ant_carousel import st_ant_carousel


st.set_page_config(
    page_title="Το λαβράκι του Αμβρακικού",
    page_icon="🐟",
    initial_sidebar_state="collapsed"
)

lnk = '<link rel="stylesheet" href="https://use.fontawesome.com/releases/v5.12.1/css/all.css" crossorigin="anonymous">'
def metrics_customize(red,green,blue,iconname,sline,i):

    htmlstr = f"""<p style='background-color: rgb({red},{green},{blue}, 0.75); 
                        color: rgb(0,0,0, 0.75); 
                        font-size: 18px; 
                        border-radius: 7px; 
                        padding-left: 12px; 
                        padding-top: 18px; 
                        padding-bottom: 18px; 
                        line-height:25px;'>
                        <i class='{iconname} fa-xs'></i> <strong>{i}</strong>
                        </style><BR><span style='font-size: 15px; 
                        margin-top: 0;'>{sline}</style></span></p>"""
    return htmlstr

def metrics_customize_bullets(red, green, blue, iconname, bullets, title):
    bullet_html = "".join([
        f"<li style='margin-bottom: 10px;'>{b}</li>"
        for b in bullets
    ])

    htmlstr = f"""
        <div style='background-color: rgba({red},{green},{blue}, 0.75);
                    color: rgba(0,0,0, 0.85);
                    font-size: 25px;
                    border-radius: 7px;
                    padding: 18px 12px;
                    line-height: 28px;'>

            <i class='{iconname} fa-xs'></i>
            <strong>{title}</strong>

            <ul style='font-size: 22px;
                       margin-top: 15px;
                       margin-left: 25px;
                       padding-left: 10px;
                       list-style-type: disc;'>
                {bullet_html}
            </ul>

        </div>
        """
    return htmlstr


st.markdown("""
<style>
.hero-wrapper {
    background: linear-gradient(135deg, #e8f1ff 0%, #f9fbff 100%);
    padding: 40px 20px 50px 20px;
    border-radius: 16px;
    margin-bottom: 25px;
    box-shadow: 0 6px 20px rgba(0,0,0,0.08);
}

.hero-card {
    background: #ffffff;
    padding: 28px;
    border-radius: 14px;
    box-shadow: 0 4px 12px rgba(0,0,0,0.05);
    border: 1px solid rgba(0,0,0,0.05);
}

.hero-title {
    font-size: 32px;
    font-weight: 700;
    color: #1a3c6e;
    margin-bottom: 12px;
}

.hero-sub {
    font-size: 18px;
    color: #425b78;
    margin-bottom: 20px;
}
</style>
""", unsafe_allow_html=True)

# --------- HERO ---------


left, right = st.columns([1, 1.2], vertical_alignment="center")

with left:
    st.image(
        "https://raw.githubusercontent.com/sotiristiga/euroleague/main/python%20code/download.jpg",
        caption="Άποψη από τον Αμβρακικό",
        use_container_width=True
    )

with right:
    st.markdown('<div class="hero-title">Το λαβράκι του Αμβρακικού</div>', unsafe_allow_html=True)
    st.markdown('<div class="hero-sub">Το ψάρι σου σε 60’’</div>', unsafe_allow_html=True)
    st.write("""
        Το λαβράκι του Αμβρακικού έχει μια ιστορία που συνδέεται άμεσα με τον ίδιο τον κόλπο:
        μια ημι‑κλειστή θαλάσσια λεκάνη, με ιδιαίτερα νερά και μοναδική οικολογία που επηρεάζει
        άμεσα την ποιότητα των ψαριών.
    """)
    st.markdown('</div>', unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)




TITLE_COLOR = "#1A3C6E"   # σκούρο μπλε για τίτλους
TEXT_COLOR  = "#2B2B2B"   # ουδέτερο για σώμα κειμένου
PADDING     = "20px 24px"
TITLE_SIZE  = "24px"
BODY_SIZE   = "16px"
LINE_BODY   = "1.55"
LINE_LIST   = "1.45"
SPACING_SM  = "6px"   # spacing bullets
SPACING_MD  = "12px"  # spacing

content = [
    # 1) Πού μεγάλωσε
    {
        "style": {"color": "black"},
        "content": f"""
            <div style='padding: {PADDING};'>
                <div style="font-size: {TITLE_SIZE}; font-weight: 700; color: {TITLE_COLOR}; margin-bottom: {SPACING_MD};">
                    Πού μεγάλωσε το λαβράκι του Αμβρακικού;
                </div>
                <div style="font-size: {BODY_SIZE}; color: {TEXT_COLOR}; line-height: {LINE_BODY};">
                    Το λαβράκι αναπτύχθηκε σε μια λεκάνη περίπου 405 km², με μέσο βάθος 26 μέτρα
                    και μέγιστο τα 60–65 μέτρα. Τα νερά του κόλπου ανανεώνονται αργά, επειδή η είσοδος
                    προς το Ιόνιο είναι στενή και σχετικά ρηχή (600 μ. πλάτος, 5–15 μ. βάθος).
                    Αυτό δημιουργεί ένα ήρεμο και παραγωγικό υδάτινο περιβάλλον.
                </div>
            </div>
        """
    },

    # 2) Διατροφή
    {
        "style": {"color": "black"},
        "content": f"""
            <div style='padding: {PADDING};'>
                <div style="font-size: {TITLE_SIZE}; font-weight: 700; color: {TITLE_COLOR}; margin-bottom: {SPACING_MD};">
                    Ποια είναι η διατροφή του;
                </div>
                <div style="font-size: {BODY_SIZE}; color: {TEXT_COLOR}; line-height: {LINE_BODY};">
                    Το λαβράκι είναι σαρκοφάγο και η διατροφή του αλλάζει ανάλογα με το στάδιο ζωής και το περιβάλλον.
                    Τρέφεται κυρίως με μικρά ψάρια και θαλάσσιους οργανισμούς (π.χ. καρκινοειδή), προσαρμόζοντας την
                    επιλογή τροφής ανά εποχή και διαθεσιμότητα.
                </div>
            </div>
        """
    },

    # 3) Τι είναι ευζωία
    {
        "style": {"color": "black"},
        "content": f"""
            <div style='padding: {PADDING};'>
                <div style="font-size: {TITLE_SIZE}; font-weight: 700; color: {TITLE_COLOR}; margin-bottom: {SPACING_MD};">
                    Τι είναι η «ευζωία»;
                </div>
                <div style="font-size: {BODY_SIZE}; color: {TEXT_COLOR}; line-height: {LINE_BODY};">
                    Η ευζωία είναι η συνολική ποιότητα ζωής ενός ζώου. Σημαίνει ότι ζει σε συνθήκες που του
                    επιτρέπουν να είναι υγιές, να νιώθει ασφάλεια, να μην βιώνει φόβο ή στρες και να εκδηλώνει
                    τη φυσική του συμπεριφορά σε όλο τον κύκλο ζωής του.
                </div>
            </div>
        """
    },

    # 4) Τι ελέγχεται στην ευζωία (bullets)

    {
        "style": {"color": "black"},
        "content": f"""
            <div style='padding: {PADDING}; min-height: 280px;"'>
            <div style="font-size: {TITLE_SIZE}; font-weight: 700; color: {TITLE_COLOR}; margin-bottom: {SPACING_MD};">
                Τι ελέγχεται στην «ευζωία»;
            </div>

            <ul style="font-size: {BODY_SIZE}; color: {TEXT_COLOR}; padding-left: 22px; line-height: {LINE_LIST}; margin: 0;">
                <li style="margin-bottom: {SPACING_SM};">Υγεία, φυσική κατάσταση και διατροφή</li>
                <li style="margin-bottom: {SPACING_SM};">Ποιότητα νερού και περιβάλλον διαβίωσης</li>
                <li style="margin-bottom: {SPACING_SM};">Χειρισμός και μεταφορά</li>
                <li style="margin-bottom: {SPACING_SM};">Συμπεριφορά και προστασία από φόβο/στρες</li>          </ul>

        </div>

        """
    },


    # 5) Γιατί να σε νοιάζει
    {
        "style": {"color": "black"},
        "content": f"""
            <div style='padding: {PADDING};'>
                <div style="font-size: {TITLE_SIZE}; font-weight: 700; color: {TITLE_COLOR}; margin-bottom: {SPACING_MD};">
                    Γιατί να σε νοιάζει η «ευζωία» των ψαριών;
                </div>
                <div style="font-size: {BODY_SIZE}; color: {TEXT_COLOR}; line-height: {LINE_BODY};">
                    Γιατί επηρεάζει άμεσα την υγεία και την ποιότητα του ζώου, άρα και την ασφάλεια και αξιοπιστία
                    του τελικού προϊόντος που φτάνει στον άνθρωπο. Η καλή ευζωία σημαίνει καλύτερα πρότυπα παραγωγής
                    και υψηλότερη ποιότητα για όλους.
                </div>
            </div>
        """
    },
]





carousel_style = {
    "background-color": "white",
    "border-radius": "14px",
    "box-shadow": "0px 4px 18px rgba(0, 0, 0, 0.08)",
    "padding": "6px 12px",
    "border": "1px solid rgba(0,0,0,0.06)",
    'customCss': '\n        .ant-carousel .slick-dots li button {\n            background-color: #1b61ef !important;\n        }\n        .ant-carousel .slick-dots li.slick-active button {\n            background-color: #1b871b !important;\n        }\n    '
    }



st_ant_carousel(
    content,
    carousel_style=carousel_style,
    autoplay=False,
    dotPosition="top",
    dots=True,
    vertical=False,
    adaptiveHeight=True  # ώστε να προσαρμόζεται στο περιεχόμενο κάθε slide
)








st.markdown("""
<style>
/* Γενικό στυλ για primary buttons */
.stButton > button[kind="primary"] {
    background-color: #1f6feb !important;
    border-color: #1b61d1 !important;
    color: #ffffff !important;
}
.stButton > button[kind="primary"]:hover {
    background-color: #195cc7 !important;
}

/* Optional: λίγο style και για secondary */
.stButton > button[kind="secondary"] {
    background-color: #eaf2ff !important;
    color: #1f6feb !important;
    border: 1px solid #cfe1ff !important;
}
.stButton > button[kind="secondary"]:hover {
    background-color: #dceaff !important;
}
</style>
""", unsafe_allow_html=True)
st.markdown(
    f"""
<style>
.centered-title {{
    text-align: center;
    font-size: 0.5em;
    font-weight: bold;
}}
.box1 {{
    border-bottom: 2px solid #6fc98a;   /* green border */
    border-radius: 12px;         /* rounded corners */
    padding: 20px;               /* inner spacing */
    background-color: #f9f9f9;   /* light background */
    box-shadow: 2px 2px 8px rgba(0,0,0,0.1); /* soft shadow */
}}
</style>
<div class="centered-title box1">Γνωρίζετε τι είναι η ευζωία;</div>
""",
    unsafe_allow_html=True,
)

if "answer1" not in st.session_state:
    st.session_state.answer1 = None


def choose_yes():
    st.session_state.answer1 = "Ναι"


def choose_no():
    st.session_state.answer1 = "Όχι"



yes_type1 = "primary" if st.session_state.answer1 == "Ναι" else "secondary"
no_type1  = "primary" if st.session_state.answer1 == "Όχι" else "secondary"

st.write(" ")
col1, col2 = st.columns(2)

with col1:
    st.button("Ναι", key="yes_btn1", type=yes_type1, use_container_width=True, on_click=choose_yes)

with col2:
    st.button("Όχι", key="no_btn1",  type=no_type1,  use_container_width=True, on_click=choose_no)


if st.session_state.answer1 == "Ναι":
    st.success("Μπράβο! Χαίρομαι που γνωρίζεις ήδη για την ευζωία των ψαριών.")
elif st.session_state.answer1 == "Όχι":
    st.warning("##### ℹ️ Τι είναι η ευζωία;")
    st.write("""
    Η **ευζωία** σημαίνει ότι ένα ζώο ζει σε συνθήκες που του επιτρέπουν:
    - να είναι **υγιές**
    - να νιώθει **ασφάλεια**
    - να μην βιώνει **φόβο ή στρες**
    - και να εκδηλώνει τη **φυσική του συμπεριφορά**

    Με απλά λόγια, είναι η **ποιότητα ζωής** του ζώου σε όλο τον κύκλο του.
    """)

st.markdown(
    f"""
<style>
.centered-title {{
    text-align: center;
    font-size: 0.5em;
    font-weight: bold;
}}
.box2 {{
    border-bottom: 2px solid #b3cf59;   /* green border */
    border-radius: 12px;         /* rounded corners */
    padding: 20px;               /* inner spacing */
    background-color: #f9f9f9;   /* light background */
    box-shadow: 2px 2px 8px rgba(0,0,0,0.1); /* soft shadow */
}}
</style>
<div class="centered-title box2">Η ποιότητα του νερού επηρεάζει την ευζωία;</div>
""",
    unsafe_allow_html=True,
)


if "answer2" not in st.session_state:
    st.session_state.answer2 = None


def choose_yes():
    st.session_state.answer2 = "Ναι"


def choose_no():
    st.session_state.answer2 = "Όχι"



yes_type2 = "primary" if st.session_state.answer2 == "Ναι" else "secondary"
no_type2  = "primary" if st.session_state.answer2 == "Όχι" else "secondary"
st.write(" ")

col1, col2 = st.columns(2)


with col1:
    st.button("Ναι", key="yes_btn2", type=yes_type2, use_container_width=True, on_click=choose_yes)

with col2:
    st.button("Όχι", key="no_btn2",  type=no_type2,  use_container_width=True, on_click=choose_no)

if st.session_state.answer2 == "Ναι":
    st.success("Σωστά! Το νερό είναι κρίσιμο για την υγεία και την ευζωία των ψαριών.")
elif st.session_state.answer2 == "Όχι":
    st.warning("##### ℹ️ Πληροφορίες για το νερό")
    st.write("""
    Η ποιότητα του νερού επηρεάζει άμεσα:
    - την υγεία των ψαριών  
    - την ανάπτυξή τους  
    - τα επίπεδα στρες  
    - και το ανοσοποιητικό τους

    Σωστή οξυγόνωση, pH και θερμοκρασία = καλή ευζωία.
    """)

st.markdown(
    f"""
<style>
.centered-title {{
    text-align: center;
    font-size: 1.5em;
    font-weight: bold;
}}
.box3 {{
    border-bottom: 2px solid #f68bdd;   /* green border */
    border-radius: 12px;         /* rounded corners */
    padding: 20px;               /* inner spacing */
    background-color: #f9f9f9;   /* light background */
    box-shadow: 2px 2px 8px rgba(0,0,0,0.1); /* soft shadow */
}}
</style>
<div class="centered-title box3">Το στρες επηρεάζει την ποιότητα των ψαριών;</div>
""",
    unsafe_allow_html=True,
)


if "answer3" not in st.session_state:
    st.session_state.answer3 = None
def choose_yes():
    st.session_state.answer3 = "Ναι"


def choose_no():
    st.session_state.answer3 = "Όχι"



yes_type3 = "primary" if st.session_state.answer3 == "Ναι" else "secondary"
no_type3  = "primary" if st.session_state.answer3 == "Όχι" else "secondary"
st.write(" ")

col1, col2 = st.columns(2)

with col1:
    st.button("Ναι", key="yes_btn3", type=yes_type3, use_container_width=True, on_click=choose_yes)

with col2:
    st.button("Όχι", key="no_btn3",  type=no_type3,  use_container_width=True, on_click=choose_no)


if st.session_state.answer3 == "Ναι":
    st.success("Σωστά! Το στρες είναι μεγάλος παράγοντας στην ποιότητα των ψαριών.")
elif st.session_state.answer3 == "Όχι":
    st.warning("##### ℹ️ Τι προκαλεί το στρες στα ψάρια;")
    st.write("""
    Το στρες προκαλείται από:
    - υπερπυκνότητα  
    - θόρυβο ή απότομη διαχείριση  
    - κακή ποιότητα νερού  

    Αποτελέσματα στρες:
    - μειωμένη υγεία  
    - ευάλωτο ανοσοποιητικό  
    - χειρότερη τελική ποιότητα προϊόντος  
    """)

st.write(" ")
st.write("##### Θα μας βοηθούσες πολύ συμμετέχοντας σε μια μικρή έρευνα για το πώς οι άνθρωποι βλέπουν την ευζωία των ψαριών.Αν θέλεις, πάτησε τον παρακάτω σύνδεσμο!")
s1,s2,s3=st.columns(3)



st.markdown("""
<style>

/* 1) Νέες εκδόσεις Streamlit */
div[data-testid="stLinkButton"] > a {
    background-color: #4646b3 !important;
    color: white !important;
    padding: 10px 24px !important;
    border-radius: 8px !important;
    text-decoration: none !important;
    font-weight: 600 !important;
    display: inline-block !important;
    border: none !important;
}

/* 2) Παλαιότερες εκδόσεις Streamlit */
.stLinkButton > a {
    background-color: #4646b3 !important;
    color: white !important;
    padding: 10px 24px !important;
    border-radius: 8px !important;
    text-decoration: none !important;
    font-weight: 600 !important;
    display: inline-block !important;
    border: none !important;
}

/* Hover effect */
div[data-testid="stLinkButton"] > a:hover,
.stLinkButton > a:hover {
    background-color: #4646b3 !important;
}

</style>
""", unsafe_allow_html=True)


with s2:

    st.markdown('<div class="custom-link-btn">', unsafe_allow_html=True)
    st.link_button(
                    "Συμμετοχή στην έρευνα",
                    "https://www.prorataonlinesurveys.gr/243537?lang=el",
                    type="primary"
                )
    st.markdown('</div>', unsafe_allow_html=True)





