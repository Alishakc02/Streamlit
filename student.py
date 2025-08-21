import streamlit as st 
import pandas as pd
st.header("Student's performance evaluation")
import streamlit as st
import pandas as pd
import numpy as np


# Page configuration
st.set_page_config(
    page_title="Student Performance Dashboard",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Load sample data (in a real app, you'd load from CSV/database)
@st.cache_data
def load_data():
    data = {
        'Student_ID': range(1, 101),
        'Name': [f'Student {i}' for i in range(1, 101)],
        'Math_Score': np.random.randint(40, 100, 100),
        'Science_Score': np.random.randint(45, 98, 100),
        'English_Score': np.random.randint(50, 97, 100),
        'Attendance': np.random.randint(70, 100, 100),
        'Class': np.random.choice(['A', 'B', 'C'], 100),
        'Gender': np.random.choice(['Male', 'Female'], 100)
    }
    return pd.DataFrame(data)

df = load_data()

# Calculate additional metrics
df['Average_Score'] = df[['Math_Score', 'Science_Score', 'English_Score']].mean(axis=1).round(1)
df['Performance_Category'] = pd.cut(df['Average_Score'], 
                                   bins=[0, 60, 80, 100],
                                   labels=['Needs Improvement', 'Satisfactory', 'Excellent'])

# Sidebar filters
st.sidebar.header("📌 Filters")
selected_class = st.sidebar.multiselect(
    "Select Class", 
    options=df['Class'].unique(),
    default=df['Class'].unique()
)

selected_performance = st.sidebar.multiselect(
    "Performance Category",
    options=df['Performance_Category'].unique(),
    default=df['Performance_Category'].unique()
)

score_range = st.sidebar.slider(
    "Select Average Score Range",
    min_value=0, max_value=100,
    value=(30, 100)
)

# Filter data based on selections
filtered_df = df[
    (df['Class'].isin(selected_class)) & 
    (df['Performance_Category'].isin(selected_performance)) &
    (df['Average_Score'] >= score_range[0]) & 
    (df['Average_Score'] <= score_range[1])
]

# Main dashboard
st.title("🎓 Student Performance Evaluation Dashboard")
st.markdown("Analyze student performance across different subjects and metrics")

# Key metrics
st.subheader("📊 Key Metrics")
col1, col2, col3, col4 = st.columns(4)
col1.metric("Total Students", len(filtered_df))
col2.metric("Avg Math Score", f"{filtered_df['Math_Score'].mean():.1f}")
col3.metric("Avg Science Score", f"{filtered_df['Science_Score'].mean():.1f}")
col4.metric("Avg English Score", f"{filtered_df['English_Score'].mean():.1f}")

# Tabs for different views
tab1, tab2, tab3, tab4 = st.tabs(["📈 Overview", "📋 Student Data", "📊 Subject Analysis", "📅 Attendance"])

with tab1:
    st.subheader("Performance Distribution")
    
    col1, col2 = st.columns(2)
    
    with col1:
        # Performance category pie chart
        fig1 = px.pie(filtered_df, names='Performance_Category', 
                      title='Performance Category Distribution')
        st.plotly_chart(fig1, use_container_width=True)
    
    with col2:
        # Average score histogram
        fig2 = px.histogram(filtered_df, x='Average_Score', 
                           nbins=20, title='Average Score Distribution')
        st.plotly_chart(fig2, use_container_width=True)
    
    # Class-wise comparison
    st.subheader("Class-wise Comparison")
    fig3 = px.box(filtered_df, x='Class', y='Average_Score', 
                 color='Class', title='Class Performance Comparison')
    st.plotly_chart(fig3, use_container_width=True)

with tab2:
    st.subheader("Student Performance Data")
    st.dataframe(filtered_df.sort_values('Average_Score', ascending=False), 
                use_container_width=True)

with tab3:
    st.subheader("Subject-wise Analysis")
    
    col1, col2 = st.columns(2)
    
    with col1:
        # Subject comparison
        subject_df = filtered_df.melt(id_vars=['Student_ID', 'Name'], 
                                    value_vars=['Math_Score', 'Science_Score', 'English_Score'],
                                    var_name='Subject', value_name='Score')
        fig4 = px.box(subject_df, x='Subject', y='Score', 
                     title='Subject Score Distributions')
        st.plotly_chart(fig4, use_container_width=True)
    
    with col2:
        # Subject correlation
        fig5 = px.scatter_matrix(filtered_df,
                                dimensions=['Math_Score', 'Science_Score', 'English_Score'],
                                color='Performance_Category',
                                title='Subject Score Correlations')
        st.plotly_chart(fig5, use_container_width=True)

with tab4:
    st.subheader("Attendance Analysis")
    
    col1, col2 = st.columns(2)
    
    with col1:
        # Attendance vs Performance
        fig6 = px.scatter(filtered_df, x='Attendance', y='Average_Score',
                         color='Performance_Category',
                         title='Attendance vs Performance',
                         trendline="lowess")
        st.plotly_chart(fig6, use_container_width=True)
    
    with col2:
        # Class attendance
        fig7 = px.box(filtered_df, x='Class', y='Attendance',
                     title='Class Attendance Comparison')
        st.plotly_chart(fig7, use_container_width=True)

# Download button
st.sidebar.markdown("---")
st.sidebar.download_button(
    label="📥 Download Filtered Data",
    data=filtered_df.to_csv(index=False).encode('utf-8'),
    file_name='student_performance.csv',
    mime='text/csv'
)