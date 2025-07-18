import streamlit as st
from datetime import datetime
import os
import time

# Import your crew class
from src.social_activity_of_a_person.crew import SocialActivityOfAPerson

# Enhanced page config
st.set_page_config(
    page_title="Candidate Profile Analyzer",
    page_icon="🔍",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for better styling
st.markdown("""
<style>
    /* Main container styling */
    .main {
        padding: 1rem 2rem;
    }
    
    /* Header styling */
    .header-container {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 2rem;
        border-radius: 15px;
        margin-bottom: 2rem;
        box-shadow: 0 10px 30px rgba(0,0,0,0.1);
    }
    
    .header-title {
        color: white;
        font-size: 2.5rem;
        font-weight: 700;
        margin: 0;
        text-align: center;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
    }
    
    .header-subtitle {
        color: rgba(255,255,255,0.9);
        font-size: 1.2rem;
        text-align: center;
        margin-top: 0.5rem;
        font-weight: 300;
    }
    
    /* Sidebar styling */
    .sidebar .sidebar-content {
        background: linear-gradient(180deg, #f8f9fa 0%, #e9ecef 100%);
    }
    
    /* Input container */
    .input-container {
        background: white;
        padding: 1.5rem;
        border-radius: 10px;
        box-shadow: 0 5px 15px rgba(0,0,0,0.08);
        margin-bottom: 1rem;
    }
    
    /* Button styling */
    .stButton > button {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        border: none;
        padding: 0.75rem 2rem;
        border-radius: 25px;
        font-weight: 600;
        font-size: 1rem;
        transition: all 0.3s ease;
        width: 100%;
        box-shadow: 0 5px 15px rgba(102, 126, 234, 0.4);
    }
    
    .stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 8px 25px rgba(102, 126, 234, 0.6);
    }
    
    /* Results container */
    .results-container {
        background: white;
        padding: 2rem;
        border-radius: 15px;
        box-shadow: 0 10px 30px rgba(0,0,0,0.1);
        margin-bottom: 2rem;
    }
    
    /* Result card styling */
    .result-card {
        background: linear-gradient(135deg, #f8f9fa 0%, #ffffff 100%);
        padding: 1.5rem;
        border-radius: 10px;
        margin-bottom: 1.5rem;
        border-left: 4px solid #667eea;
        box-shadow: 0 3px 10px rgba(0,0,0,0.05);
        transition: transform 0.3s ease;
    }
    
    .result-card:hover {
        transform: translateY(-3px);
        box-shadow: 0 8px 25px rgba(0,0,0,0.1);
    }
    
    .result-title {
        color: #2c3e50;
        font-size: 1.3rem;
        font-weight: 600;
        margin-bottom: 1rem;
        display: flex;
        align-items: center;
        gap: 0.5rem;
    }
    
    /* Progress bar styling */
    .progress-container {
        background: white;
        padding: 2rem;
        border-radius: 15px;
        box-shadow: 0 10px 30px rgba(0,0,0,0.1);
        text-align: center;
    }
    
    .progress-text {
        color: #667eea;
        font-size: 1.1rem;
        font-weight: 500;
        margin-bottom: 1rem;
    }
    
    /* Status indicators */
    .status-success {
        color: #27ae60;
        background: #d5f4e6;
        padding: 0.5rem 1rem;
        border-radius: 20px;
        font-weight: 600;
    }
    
    .status-warning {
        color: #f39c12;
        background: #fef9e7;
        padding: 0.5rem 1rem;
        border-radius: 20px;
        font-weight: 600;
    }
    
    .status-error {
        color: #e74c3c;
        background: #fadbd8;
        padding: 0.5rem 1rem;
        border-radius: 20px;
        font-weight: 600;
    }
    
    /* Animation keyframes */
    @keyframes fadeIn {
        from { opacity: 0; transform: translateY(20px); }
        to { opacity: 1; transform: translateY(0); }
    }
    
    .fade-in {
        animation: fadeIn 0.6s ease-out;
    }
    
    /* Responsive design */
    @media (max-width: 768px) {
        .header-title {
            font-size: 2rem;
        }
        .header-subtitle {
            font-size: 1rem;
        }
        .main {
            padding: 1rem;
        }
    }
</style>
""", unsafe_allow_html=True)

# Header section
st.markdown("""
<div class="header-container fade-in">
    <h1 class="header-title">🔍 Candidate Profile Analyzer</h1>
    <p class="header-subtitle">AI-Powered Due Diligence Through Digital Footprint Analysis</p>
</div>
""", unsafe_allow_html=True)

# Main content area
col1, col2 = st.columns([1, 3])

# Enhanced sidebar
with col1:
    st.markdown("""
    <div class="input-container">
        <h3 style="color: #2c3e50; margin-bottom: 1rem;">📝 Candidate Information</h3>
    </div>
    """, unsafe_allow_html=True)
    
    # Input fields with better styling
    person = st.text_input(
        "👤 Full Name",
        value="Om Anand",
        placeholder="Enter candidate's full name",
        help="The complete name of the person you want to analyze"
    )
    
    company = st.text_input(
        "🏢 Company / Institute",
        value="IIT Bhilai",
        placeholder="Current or previous organization",
        help="The organization they're associated with"
    )
    
    location = st.text_input(
        "📍 Location",
        value="Bihar",
        placeholder="City, State or Country",
        help="Geographic location for better search results"
    )
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # API Configuration Section
    st.markdown("""
    <div class="input-container">
        <h3 style="color: #2c3e50; margin-bottom: 1rem;">🔑 API Configuration</h3>
    </div>
    """, unsafe_allow_html=True)
    
    # Gemini API Key
    gemini_key = st.text_input(
        "🤖 Gemini API Key",
        type="password",
        value=st.session_state.get("GEMINI_API_KEY", ""),
        placeholder="Enter your Gemini API key",
        help="Enter your Google Gemini API key for AI analysis"
    )
    
    # Serper API Key
    serper_key = st.text_input(
        "🔍 Serper API Key",
        type="password",
        value=st.session_state.get("SERPER_API_KEY", ""),
        placeholder="Enter your Serper API key",
        help="Enter your Serper API key for web search capabilities"
    )
    
    # Save Settings Button
    if st.button("💾 Save API Settings", key="save_settings"):
        updated = False
        
        if gemini_key:
            st.session_state["GEMINI_API_KEY"] = gemini_key
            os.environ["GEMINI_API_KEY"] = gemini_key
            updated = True
        
        if serper_key:
            st.session_state["SERPER_API_KEY"] = serper_key
            os.environ["SERPER_API_KEY"] = serper_key
            updated = True
        
        if updated:
            st.success("✅ API settings saved successfully!")
        else:
            st.warning("⚠️ Please enter at least one API key to save.")
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Enhanced run button
    run_button = st.button("🚀 Start Analysis", key="run_analysis")
    
    if run_button:
        # Validation
        if not person.strip():
            st.error("Please enter a valid name")
            st.stop()
        
        # API key validation
        if not gemini_key and not st.session_state.get("GEMINI_API_KEY"):
            st.error("Please enter Gemini API key before starting analysis")
            st.stop()
        
        if not serper_key and not st.session_state.get("SERPER_API_KEY"):
            st.error("Please enter Serper API key before starting analysis")
            st.stop()
    
    # Information box
    st.markdown("""
    <div style="background: #e8f4f8; padding: 1rem; border-radius: 10px; margin-top: 1rem;">
        <h4 style="color: #2c3e50; margin: 0 0 0.5rem 0;">ℹ️ What we analyze:</h4>
        <ul style="color: #34495e; margin: 0; padding-left: 1.2rem;">
            <li>Professional background</li>
            <li>Online reputation</li>
            <li>Social media presence</li>
            <li>Behavioral patterns</li>
            <li>Cultural fit indicators</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

# Main results area
with col2:
    if run_button:
        # Progress section
        st.markdown("""
        <div class="progress-container fade-in">
            <div class="progress-text">🔄 Running comprehensive analysis...</div>
            <p style="color: #7f8c8d;">This may take a few minutes. Please wait while we gather and analyze data.</p>
        </div>
        """, unsafe_allow_html=True)
        
        # Progress bar
        progress_bar = st.progress(0)
        status_text = st.empty()
        
        # Simulate progress updates
        progress_steps = [
            (20, "🔍 Searching online profiles..."),
            (40, "📊 Analyzing professional data..."),
            (60, "🔍 Checking reputation indicators..."),
            (80, "🧠 Processing behavioral patterns..."),
            (90, "📝 Generating comprehensive report..."),
            (100, "✅ Analysis complete!")
        ]
        
        inputs = {
            "person": person,
            "company": company,
            "location": location,
            "current_year": str(datetime.now().year)
        }

        try:
            # Simulate progress while running the crew
            for i, (progress, text) in enumerate(progress_steps[:-1]):
                progress_bar.progress(progress)
                status_text.text(text)
                time.sleep(0.5)  # Small delay for UX
            
            # Run the actual Crew
            SocialActivityOfAPerson().crew().kickoff(inputs=inputs)
            
            # Complete progress
            progress_bar.progress(100)
            status_text.text("✅ Analysis complete!")
            
            # Success message
            st.markdown("""
            <div class="status-success fade-in" style="text-align: center; margin: 2rem 0;">
                ✅ Analysis completed successfully!
            </div>
            """, unsafe_allow_html=True)

            # Results section
            st.markdown("""
            <div class="results-container fade-in">
                <h2 style="color: #2c3e50; margin-bottom: 2rem;">📊 Analysis Results</h2>
            </div>
            """, unsafe_allow_html=True)

            # Enhanced result files display
            result_files = {
                "📌 Research Summary": {
                    "file": "research_task.md",
                    "description": "Overview of online presence and key findings",
                    "icon": "📌"
                },
                "💼 Professional Background": {
                    "file": "professional_background.md",
                    "description": "Career history and professional achievements",
                    "icon": "💼"
                },
                "🚨 Reputation Check": {
                    "file": "reputation_check.md",
                    "description": "Public perception and reputation analysis",
                    "icon": "🚨"
                },
                "🧠 Behavior & Pattern Analysis": {
                    "file": "analysis_task.md",
                    "description": "Behavioral insights and pattern recognition",
                    "icon": "🧠"
                },
                "👥 Cultural Fit Evaluation": {
                    "file": "cultural_fit.md",
                    "description": "Assessment of organizational culture alignment",
                    "icon": "👥"
                },
                "📘 Final Life Story": {
                    "file": "life_story.md",
                    "description": "Comprehensive narrative profile",
                    "icon": "📘"
                }
            }

            # Display results in enhanced cards
            for title, details in result_files.items():
                path = os.path.join(os.getcwd(), details["file"])
                if os.path.exists(path):
                    with open(path, "r", encoding="utf-8") as f:
                        content = f.read()
                    
                    # Create expandable result card
                    with st.expander(f"{details['icon']} {title.replace(details['icon'] + ' ', '')}", expanded=False):
                        st.markdown(f"*{details['description']}*")
                        st.markdown("---")
                        st.markdown(content, unsafe_allow_html=True)
                        
                        # Download button for each section
                        st.download_button(
                            label=f"📥 Download {title.split(' ', 1)[1]}",
                            data=content,
                            file_name=f"{person.replace(' ', '_').lower()}_{details['file']}",
                            mime="text/markdown",
                            key=f"download_{details['file']}"
                        )
                else:
                    st.markdown(f"""
                    <div class="status-warning">
                        ⚠️ {details['file']} not found
                    </div>
                    """, unsafe_allow_html=True)

            # Final download section
            if os.path.exists(os.path.join(os.getcwd(), "life_story.md")):
                st.markdown("---")
                st.markdown("""
                <div style="text-align: center; padding: 2rem;">
                    <h3 style="color: #2c3e50;">📄 Complete Report</h3>
                    <p style="color: #7f8c8d;">Download the comprehensive analysis report</p>
                </div>
                """, unsafe_allow_html=True)
                
                with open(os.path.join(os.getcwd(), "life_story.md"), "r", encoding="utf-8") as f:
                    final_content = f.read()
                
                col_dl1, col_dl2, col_dl3 = st.columns([1, 2, 1])
                with col_dl2:
                    st.download_button(
                        label="📥 Download Complete Life Story Report",
                        data=final_content,
                        file_name=f"{person.replace(' ', '_').lower()}_complete_analysis.md",
                        mime="text/markdown",
                        key="download_complete"
                    )

        except Exception as e:
            st.markdown(f"""
            <div class="status-error fade-in">
                ❌ Error occurred: {str(e)}
            </div>
            """, unsafe_allow_html=True)
            
            # Error details in expander
            with st.expander("🔍 Error Details", expanded=False):
                st.code(str(e), language="python")
                st.markdown("**Troubleshooting Tips:**")
                st.markdown("- Check internet connectivity")
                st.markdown("- Verify API keys are properly configured")
                st.markdown("- Ensure the person's name is spelled correctly")
                st.markdown("- Try with a different name or location")
    
    else:
        # Welcome message when not running
        st.markdown("""
        <div class="results-container fade-in">
            <div style="text-align: center; padding: 3rem 1rem;">
                <h3 style="color: #2c3e50; margin-bottom: 1rem;">Welcome to Candidate Profile Analyzer</h3>
                <p style="color: #7f8c8d; font-size: 1.1rem; line-height: 1.6;">
                    Enter candidate information in the sidebar and click <strong>"Start Analysis"</strong> 
                    to begin comprehensive due diligence through AI-powered digital footprint analysis.
                </p>
                <div style="margin-top: 2rem;">
                    <div style="display: inline-block; background: #e8f4f8; padding: 1rem 2rem; border-radius: 10px;">
                        <p style="color: #2c3e50; margin: 0; font-weight: 500;">
                            🔒 <strong>Privacy First:</strong> We only analyze publicly available information
                        </p>
                    </div>
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)

# Footer
st.markdown("---")
st.markdown("""
<div style="text-align: center; padding: 1rem; color: #7f8c8d;">
    <p>🔍 Powered by AI | Built with Streamlit | © 2025 Candidate Profile Analyzer</p>
</div>
""", unsafe_allow_html=True)