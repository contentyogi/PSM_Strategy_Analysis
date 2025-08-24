# 18_display_results_streamlit.py

import streamlit as st
import pandas as pd
import os
import glob # For finding image files

# Define base directory for results
results_dir = r'C:\Users\Aarthi\Desktop\anupam\PSM\results_v2'
plots_dir = os.path.join(results_dir, 'plots')

st.set_page_config(layout="wide") # Use wide layout

st.title("📈 Price Surprise Momentum Strategy Analysis (v2 - Peak Return Logic)")
st.write("This application presents the results of the re-evaluated 'Price Surprise Momentum' strategy with the new 'Peak 5-Day Forward Return' exit logic. The stocks have been tiered based on their overall average peak return and consistency scores, and their recent performance is also integrated.")

# --- Load and Display Final Report ---
final_report_path = os.path.join(results_dir, 'strategy_final_report_v2.csv')
if os.path.exists(final_report_path):
    st.header("1. Final Strategy Report (Tiered Stocks)")
    st.write("This table contains the comprehensive report of all re-analyzed stocks, including their assigned tiers.")
    df_final_report = pd.read_csv(final_report_path)
    st.dataframe(df_final_report)
else:
    st.warning(f"Final report CSV not found at: {final_report_path}")

# --- Load and Display Tier Yearly Performance ---
tier_yearly_performance_path = os.path.join(results_dir, 'tier_yearly_performance.csv')
if os.path.exists(tier_yearly_performance_path):
    st.header("2. Tier Performance Over Time")
    st.write("This table shows the average peak return for each tier, broken down by year, to analyze year-over-year consistency.")
    df_tier_yearly_performance = pd.read_csv(tier_yearly_performance_path, index_col='year')
    st.dataframe(df_tier_yearly_performance)
else:
    st.warning(f"Tier yearly performance CSV not found at: {tier_yearly_performance_path}")

# --- Load and Display Recent Performance Summary ---
recent_performance_summary_path = os.path.join(results_dir, 'tier_recent_performance_summary.csv')
if os.path.exists(recent_performance_summary_path):
    st.header("3. Recent Performance Summary by Tier (Last Year)")
    st.write("Descriptive statistics for 'Last Year's Average Peak Return' grouped by each tier, highlighting recent trends.")
    df_recent_performance_summary = pd.read_csv(recent_performance_summary_path, index_col='new_tier')
    st.dataframe(df_recent_performance_summary)
else:
    st.warning(f"Recent performance summary CSV not found at: {recent_performance_summary_path}")

# --- Display Visualizations ---
st.header("4. Visualizations")
st.write("Graphical representations to understand the tiering logic and recent performance distributions.")

if os.path.exists(plots_dir):
    plot_files = glob.glob(os.path.join(plots_dir, '*.png'))
    if plot_files:
        # Sort plots for consistent order
        plot_files.sort()
        for plot_path in plot_files:
            plot_name = os.path.basename(plot_path).replace('.png', '').replace('_', ' ').title()
            st.subheader(f"Plot: {plot_name}")
            st.image(plot_path, use_column_width=True)
    else:
        st.warning(f"No PNG plot files found in {plots_dir}.")
else:
    st.warning(f"Plots directory not found at: {plots_dir}")

st.markdown("---")
st.info("Analysis prepared by Gemini AI Assistant based on your project handoff.")
