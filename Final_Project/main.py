
import streamlit as st
from langchain_community.document_loaders.web_base import WebBaseLoader


from chains import Chain
from portfolio import Portfolio
from utils import clean_text


def create_streamlit_app(llm, portfolio, clean_text):
    # Page configuration
    st.set_page_config(page_title="Cold Mail Generator", page_icon="📧", layout="wide")

    # Sidebar
    with st.sidebar:
        st.header("📄 About")
        st.markdown("""
        This app generates **cold emails** tailored to job postings.  
        Simply paste a job URL and receive a well-crafted email based on your portfolio.
        """)
        st.markdown("---")
        st.markdown("🔗 **Powered by:** LLM")
        github_username = "Faisalece18"
        st.markdown("👤 **Developer**")
        st.markdown(f"""
            <div style="display: flex; align-items: center; margin-top: 10px;">
                <a href="https://github.com/{github_username}" target="_blank" style="text-decoration: none; color: inherit;">
                  <img src="https://github.com/{github_username}.png" width="40" 
                  style="border-radius: 50%; margin-right: 10px; border: 1px solid #ccc;">
                  <span style="font-size: 16px; font-weight: 500;">{github_username}</span>
                </a>
            </div>
            """, unsafe_allow_html=True)


    # Title and description
    st.title("📧 Cold Mail Generator")
    st.markdown("Generate personalized cold emails using job descriptions and your own experience.")

    # Input section
    with st.container():
        st.subheader("🔗 Enter Job Posting URL")
        url_input = st.text_input(
            label="Job URL",
            placeholder="e.g. https://jobs.bdjobs.com/jobdetails.asp?id=1366243&fcatId=8&ln=1",
            help="Paste the job posting URL from LinkedIn, Bdjobs, etc."
        )
        submit_button = st.button("🚀 Generate Email")

    # Processing logic
    if submit_button:
        if not url_input.strip():
            st.warning("Please enter a job posting URL before generating an email.")
            return

        try:
            with st.spinner("🔍 Analyzing job post and generating email..."):
                loader = WebBaseLoader([url_input])
                page_content = loader.load().pop().page_content
                cleaned_data = clean_text(page_content)

                portfolio.load_portfolio()
                jobs = llm.extract_jobs(cleaned_data)

                if not jobs:
                    st.warning("No job descriptions were found on the provided page.")
                    return

                for idx, job in enumerate(jobs, start=1):
                    skills = job.get('skills', [])
                    links = portfolio.query_links(skills)
                    email = llm.write_mail(job, links)

                    with st.expander(f"✉️ Here is the Email", expanded=True):
                        st.code(email, language='markdown')
                        st.download_button(
                            label="📥 Download Email",
                            data=email,
                            file_name=f"cold_email_{idx}.txt",
                            mime="text/plain"
                        )
        except Exception as e:
            st.error("❌ An error occurred while processing the URL.")
            st.exception(e)

# Entry point
if __name__ == "__main__":
    chain = Chain()
    portfolio = Portfolio()
    create_streamlit_app(chain, portfolio, clean_text)



