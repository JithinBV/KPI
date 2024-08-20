import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
 
# Create data for Downtime Causes
downtime_data = {
    'Cause': ['Technical Failures', 'Maintenance', 'Power Issues', 'Human Error', 'Resource Shortages', 'Environmental Conditions'],
    'Percentage': [30, 20, 15, 15, 10, 10],
    'OEE_Impact': [30, 20, 15, 15, 10, 10],
    'OEE_Recovery': [90, 70, 60, 80, 50, 40]
}
downtime_df = pd.DataFrame(downtime_data)
 
# Create data for Maintenance Types
maintenance_data = {
    'Type': ['Preventive Maintenance', 'Predictive Maintenance', 'Reactive Maintenance', 'Condition-based Maintenance', 'Proactive Maintenance'],
    'Percentage': [25, 20, 15, 20, 20],
    'OEE_Impact': [40, 35, 25, 30, 30],
    'OEE_Recovery': [80, 75, 50, 70, 60]
}
maintenance_df = pd.DataFrame(maintenance_data)
 
# Create data for OEE Components
oee_data = {
    'Component': ['Availability', 'Performance', 'Quality'],
    'Percentage': [30, 50, 20],
    'OEE_Impact': [40, 50, 30],
    'OEE_Recovery': [85, 80, 75]
}
oee_df = pd.DataFrame(oee_data)
 
# Function to plot pie charts
def plot_pie(data, names, values, title):
    fig = px.pie(data, names=names, values=values, title=title)
    st.plotly_chart(fig)
 
# Function to plot bar charts
def plot_bar(data, x, y, title):
    fig = px.bar(data, x=x, y=y, title=title)
    st.plotly_chart(fig)
 
# Function to plot line charts
def plot_line(data, x, y, title):
    fig = px.line(data, x=x, y=y, title=title)
    st.plotly_chart(fig)
 
# Sidebar Navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio("Select a Page", ['Home', 'Downtime Causes', 'Maintenance Types', 'OEE Components'])
 
# Main Dashboard Title
st.title("Manufacturing Dashboard")
st.markdown("This dashboard provides an overview of downtime causes, maintenance types, their impact on OEE, and how maintenance can recover OEE.")
 
# Home Page Overview
if page == 'Home':
    st.header("Overview of Downtime Causes, Maintenance Types, and OEE")
    st.subheader("Downtime Causes")
    plot_pie(downtime_df, 'Cause', 'Percentage', 'Downtime Causes Distribution')
    st.subheader("Maintenance Types")
    plot_pie(maintenance_df, 'Type', 'Percentage', 'Maintenance Types Distribution')
    st.subheader("OEE Components")
    plot_pie(oee_df, 'Component', 'Percentage', 'OEE Components Distribution')
 
# Detailed Downtime Causes Pages
if page == 'Downtime Causes':
    st.header("Downtime Causes and OEE Impact")
    cause = st.selectbox("Select Downtime Cause", downtime_df['Cause'])
 
    if cause == 'Technical Failures':
        st.subheader("Technical Failures")
        st.markdown("""
        **How It’s Maintained:**
        - Regular diagnostics and monitoring of equipment.
        - Scheduled hardware replacements and upgrades.
        - Use of predictive maintenance tools to identify issues before they occur.
        
        **How to Improve:**
        - Implement advanced monitoring systems with real-time alerts.
        - Adopt AI-driven predictive maintenance to anticipate failures.
        - Increase redundancy for critical components.
        
        **OEE Impact:**
        - **Current Impact:** Technical failures decrease the Availability component of OEE due to unexpected downtime.
        - **OEE Recovery:** Implementing predictive maintenance can recover up to 80-90% of lost OEE due to technical failures.
        """)
        st.subheader("Visualizations")
        plot_bar(downtime_df[downtime_df['Cause'] == cause], 'Cause', 'OEE_Impact', 'Impact of Technical Failures on OEE')
        plot_line(downtime_df[downtime_df['Cause'] == cause], 'Cause', 'OEE_Recovery', 'OEE Recovery through Maintenance')
 
    elif cause == 'Maintenance':
        st.subheader("Maintenance")
        st.markdown("""
        **How It’s Maintained:**
        - Scheduled maintenance routines based on manufacturer recommendations.
        - Use of checklists and maintenance logs.
        
        **How to Improve:**
        - Transition to condition-based maintenance (CBM) instead of time-based.
        - Implement a Computerized Maintenance Management System (CMMS) for better tracking.
        
        **OEE Impact:**
        - **Current Impact:** Inadequate maintenance can lower the Performance and Availability components of OEE.
        - **OEE Recovery:** Condition-based maintenance can improve OEE by up to 70%.
        """)
        st.subheader("Visualizations")
        plot_bar(downtime_df[downtime_df['Cause'] == cause], 'Cause', 'OEE_Impact', 'Impact of Maintenance on OEE')
        plot_line(downtime_df[downtime_df['Cause'] == cause], 'Cause', 'OEE_Recovery', 'OEE Recovery through Maintenance')
 
    elif cause == 'Power Issues':
        st.subheader("Power Issues")
        st.markdown("""
        **How It’s Maintained:**
        - Regular testing of backup power systems (generators, UPS).
        - Installation of power surge protection.
        
        **How to Improve:**
        - Invest in more reliable and redundant power sources.
        - Implement power monitoring and energy management systems.
        
        **OEE Impact:**
        - **Current Impact:** Power issues can significantly reduce Availability, impacting OEE.
        - **OEE Recovery:** Reliable power solutions can recover up to 60% of lost OEE.
        """)
        st.subheader("Visualizations")
        plot_bar(downtime_df[downtime_df['Cause'] == cause], 'Cause', 'OEE_Impact', 'Impact of Power Issues on OEE')
        plot_line(downtime_df[downtime_df['Cause'] == cause], 'Cause', 'OEE_Recovery', 'OEE Recovery through Maintenance')
 
    elif cause == 'Human Error':
        st.subheader("Human Error")
        st.markdown("""
        **How It’s Maintained:**
        - Training programs and regular refreshers for operators.
        - Implementation of standard operating procedures (SOPs).
        
        **How to Improve:**
        - Increase automation where feasible to reduce human intervention.
        - Implement error-proofing (poka-yoke) techniques.
        
        **OEE Impact:**
        - **Current Impact:** Human errors can reduce both Performance and Quality, affecting OEE.
        - **OEE Recovery:** Training and automation can recover up to 80% of lost OEE.
        """)
        st.subheader("Visualizations")
        plot_bar(downtime_df[downtime_df['Cause'] == cause], 'Cause', 'OEE_Impact', 'Impact of Human Error on OEE')
        plot_line(downtime_df[downtime_df['Cause'] == cause], 'Cause', 'OEE_Recovery', 'OEE Recovery through Maintenance')
 
    elif cause == 'Resource Shortages':
        st.subheader("Resource Shortages")
        st.markdown("""
        **How It’s Maintained:**
        - Just-in-time inventory management.
        - Supplier reliability monitoring.
        
        **How to Improve:**
        - Develop stronger supplier relationships and diversify suppliers.
        - Implement buffer stocks for critical materials.
        
        **OEE Impact:**
        - **Current Impact:** Resource shortages primarily impact Performance, leading to OEE reduction.
        - **OEE Recovery:** Buffer stocks and reliable suppliers can recover up to 50% of lost OEE.
        """)
        st.subheader("Visualizations")
        plot_bar(downtime_df[downtime_df['Cause'] == cause], 'Cause', 'OEE_Impact', 'Impact of Resource Shortages on OEE')
        plot_line(downtime_df[downtime_df['Cause'] == cause], 'Cause', 'OEE_Recovery', 'OEE Recovery through Maintenance')
 
    elif cause == 'Environmental Conditions':
        st.subheader("Environmental Conditions")
        st.markdown("""
        **How It’s Maintained:**
        - Installation of environmental controls (HVAC, dust filtration).
        - Regular monitoring of operating environment conditions.
        
        **How to Improve:**
        - Upgrade to more robust environmental control systems.
        - Implement real-time environmental monitoring with automated adjustments.
        
        **OEE Impact:**
        - **Current Impact:** Environmental conditions can affect all three components of OEE (Availability, Performance, Quality).
        - **OEE Recovery:** Improved environmental controls can recover up to 40% of lost OEE.
        """)
        st.subheader("Visualizations")
        plot_bar(downtime_df[downtime_df['Cause'] == cause], 'Cause', 'OEE_Impact', 'Impact of Environmental Conditions on OEE')
        plot_line(downtime_df[downtime_df['Cause'] == cause], 'Cause', 'OEE_Recovery', 'OEE Recovery through Maintenance')
 
# Detailed Maintenance Types Pages
if page == 'Maintenance Types':
    st.header("Maintenance Types and OEE Impact")
    maintenance_type = st.selectbox("Select Maintenance Type", maintenance_df['Type'])
 
    if maintenance_type == 'Preventive Maintenance':
        st.subheader("Preventive Maintenance")
        st.markdown("""
        **How It Helps Uptime:**
        - Reduces unexpected downtime by addressing potential issues before they occur.
        - Ensures consistent machine performance and extends equipment lifespan.
        
        **Potential Issues if Not Performed:**
        - Increased risk of unexpected failures.
        - Higher long-term maintenance costs due to major breakdowns.
        
        **OEE Impact:**
        - **Current Impact:** Preventive maintenance increases Availability and Performance, leading to higher OEE.
        - **OEE Recovery:** Proper implementation can recover up to 80% of OEE losses caused by lack of maintenance.
        """)
        st.subheader("Visualizations")
        plot_bar(maintenance_df[maintenance_df['Type'] == maintenance_type], 'Type', 'OEE_Impact', 'Impact of Preventive Maintenance on OEE')
        plot_line(maintenance_df[maintenance_df['Type'] == maintenance_type], 'Type', 'OEE_Recovery', 'OEE Recovery through Preventive Maintenance')
 
    elif maintenance_type == 'Predictive Maintenance':
        st.subheader("Predictive Maintenance")
        st.markdown("""
        **How It Helps Uptime:**
        - Uses data-driven insights to predict and prevent failures before they happen.
        - Optimizes maintenance schedules based on actual equipment condition.
        
        **Potential Issues if Not Performed:**
        - Missed opportunities to prevent failures, leading to unexpected downtime.
        - Inefficient maintenance practices and increased costs.
        
        **OEE Impact:**
        - **Current Impact:** Predictive maintenance enhances all three components of OEE (Availability, Performance, Quality).
        - **OEE Recovery:** Can recover up to 75% of OEE losses by preventing unexpected failures.
        """)
        st.subheader("Visualizations")
        plot_bar(maintenance_df[maintenance_df['Type'] == maintenance_type], 'Type', 'OEE_Impact', 'Impact of Predictive Maintenance on OEE')
        plot_line(maintenance_df[maintenance_df['Type'] == maintenance_type], 'Type', 'OEE_Recovery', 'OEE Recovery through Predictive Maintenance')
 
    elif maintenance_type == 'Reactive Maintenance':
        st.subheader("Reactive Maintenance")
        st.markdown("""
        **How It Helps Uptime:**
        - Necessary for restoring operation after an unexpected failure.
        - Focuses on getting equipment back online quickly.
        
        **Potential Issues if Overused:**
        - Increased downtime and higher repair costs.
        - Reduced equipment lifespan due to lack of preventive care.
        
        **OEE Impact:**
        - **Current Impact:** Reactive maintenance often reduces OEE by decreasing Availability and Performance.
        - **OEE Recovery:** Limited potential to recover OEE, but essential for immediate failure response.
        """)
        st.subheader("Visualizations")
        plot_bar(maintenance_df[maintenance_df['Type'] == maintenance_type], 'Type', 'OEE_Impact', 'Impact of Reactive Maintenance on OEE')
        plot_line(maintenance_df[maintenance_df['Type'] == maintenance_type], 'Type', 'OEE_Recovery', 'OEE Recovery through Reactive Maintenance')
 
    elif maintenance_type == 'Condition-based Maintenance':
        st.subheader("Condition-based Maintenance")
        st.markdown("""
        **How It Helps Uptime:**
        - Tailors maintenance schedules based on real-time equipment condition.
        - Reduces unnecessary maintenance and focuses on actual needs.
        
        **Potential Issues if Not Performed:**
        - Risk of over-maintenance or under-maintenance leading to unexpected failures.
        - Increased maintenance costs due to inefficiencies.
        
        **OEE Impact:**
        - **Current Impact:** Improves OEE by optimizing both Availability and Performance.
        - **OEE Recovery:** Can recover up to 70% of OEE losses by preventing unnecessary downtime.
        """)
        st.subheader("Visualizations")
        plot_bar(maintenance_df[maintenance_df['Type'] == maintenance_type], 'Type', 'OEE_Impact', 'Impact of Condition-based Maintenance on OEE')
        plot_line(maintenance_df[maintenance_df['Type'] == maintenance_type], 'Type', 'OEE_Recovery', 'OEE Recovery through Condition-based Maintenance')
 
    elif maintenance_type == 'Proactive Maintenance':
        st.subheader("Proactive Maintenance")
        st.markdown("""
        **How It Helps Uptime:**
        - Focuses on identifying and addressing root causes of equipment failure.
        - Implements design improvements and procedural changes to prevent future issues.
        
        **Potential Issues if Not Performed:**
        - Persistent problems leading to recurring downtime.
        - Higher costs due to frequent repairs and replacements.
        
        **OEE Impact:**
        - **Current Impact:** Proactive maintenance enhances all OEE components by eliminating root causes of downtime.
        - **OEE Recovery:** Can recover up to 60% of OEE losses by addressing systemic issues.
        """)
        st.subheader("Visualizations")
        plot_bar(maintenance_df[maintenance_df['Type'] == maintenance_type], 'Type', 'OEE_Impact', 'Impact of Proactive Maintenance on OEE')
        plot_line(maintenance_df[maintenance_df['Type'] == maintenance_type], 'Type', 'OEE_Recovery', 'OEE Recovery through Proactive Maintenance')
 
# Detailed OEE Components Pages
if page == 'OEE Components':
    st.header("OEE Components and Their Impact")
    oee_component = st.selectbox("Select OEE Component", oee_df['Component'])
 
    if oee_component == 'Availability':
        st.subheader("Availability")
        st.markdown("""
        **How It’s Affected:**
        - Downtime due to technical failures, maintenance, or other interruptions reduces Availability.
        
        **How to Improve:**
        - Implement reliable maintenance practices.
        - Minimize unplanned downtime through predictive and preventive measures.
        
        **Impact on OEE:**
        - **Current Impact:** Low Availability directly reduces OEE by decreasing operational time.
        - **OEE Recovery:** Improving Availability can recover up to 85% of OEE.
        """)
        st.subheader("Visualizations")
        plot_bar(oee_df[oee_df['Component'] == oee_component], 'Component', 'OEE_Impact', 'Impact of Availability on OEE')
        plot_line(oee_df[oee_df['Component'] == oee_component], 'Component', 'OEE_Recovery', 'OEE Recovery through Improved Availability')
 
    elif oee_component == 'Performance':
        st.subheader("Performance")
        st.markdown("""
        **How It’s Affected:**
        - Speed losses, small stops, and slow cycles reduce Performance.
        
        **How to Improve:**
        - Optimize processes and reduce inefficiencies.
        - Ensure machines are operating at optimal speeds.
        
        **Impact on OEE:**
        - **Current Impact:** Poor Performance reduces OEE by lowering the rate of production.
        - **OEE Recovery:** Improving Performance can recover up to 80% of OEE.
        """)
        st.subheader("Visualizations")
        plot_bar(oee_df[oee_df['Component'] == oee_component], 'Component', 'OEE_Impact', 'Impact of Performance on OEE')
        plot_line(oee_df[oee_df['Component'] == oee_component], 'Component', 'OEE_Recovery', 'OEE Recovery through Improved Performance')
 
    elif oee_component == 'Quality':
        st.subheader("Quality")
        st.markdown("""
        **How It’s Affected:**
        - Defects and rework reduce the Quality component of OEE.
        
        **How to Improve:**
        - Implement strict quality control measures.
        - Train operators to reduce human error and ensure consistency.
        
        **Impact on OEE:**
        - **Current Impact:** Poor Quality reduces OEE by decreasing the percentage of good parts produced.
        - **OEE Recovery:** Improving Quality can recover up to 75% of OEE.
        """)
        st.subheader("Visualizations")
        plot_bar(oee_df[oee_df['Component'] == oee_component], 'Component', 'OEE_Impact', 'Impact of Quality on OEE')
        plot_line(oee_df[oee_df['Component'] == oee_component], 'Component', 'OEE_Recovery', 'OEE Recovery through Improved Quality')
 
