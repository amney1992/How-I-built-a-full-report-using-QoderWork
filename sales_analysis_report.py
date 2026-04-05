"""
Q1 2024 Sales Data Analysis Report
====================================
Comprehensive analysis of sales performance including:
- Monthly sales trends
- Product category analysis
- Customer behavior insights
- Regional performance comparison
- KPI calculations
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime
import warnings
warnings.filterwarnings('ignore')

# Set style for better visualizations
plt.style.use('seaborn-v0_8-whitegrid')
sns.set_palette("husl")

# =============================================================================
# 1. DATA LOADING AND CLEANING
# =============================================================================

def load_and_clean_data(filepath):
    """Load and clean sales data from CSV."""
    print("=" * 60)
    print("STEP 1: DATA LOADING AND CLEANING")
    print("=" * 60)
    
    # Load data
    df = pd.read_csv(filepath)
    print(f"\nLoaded {len(df)} records from {filepath}")
    
    # Initial data info
    print("\n--- Initial Data Info ---")
    print(f"Shape: {df.shape}")
    print(f"\nColumns: {list(df.columns)}")
    
    # Data types
    print("\n--- Data Types ---")
    print(df.dtypes)
    
    # Convert date column
    df['order_date'] = pd.to_datetime(df['order_date'])
    df['order_month_name'] = df['order_date'].dt.strftime('%B')
    
    # Check for missing values
    print("\n--- Missing Values ---")
    missing = df.isnull().sum()
    print(missing[missing > 0] if missing.sum() > 0 else "No missing values found")
    
    # Check for duplicates
    duplicates = df.duplicated().sum()
    print(f"\nDuplicate rows: {duplicates}")
    
    # Data validation
    print("\n--- Data Validation ---")
    print(f"Date range: {df['order_date'].min()} to {df['order_date'].max()}")
    print(f"Negative amounts: {(df['final_amount'] < 0).sum()}")
    print(f"Zero amounts: {(df['final_amount'] == 0).sum()}")
    
    # Basic statistics
    print("\n--- Numeric Columns Summary ---")
    print(df[['quantity', 'unit_price', 'total_amount', 'discount', 'final_amount']].describe())
    
    print("\nData cleaning completed successfully!")
    return df


# =============================================================================
# 2. KEY PERFORMANCE INDICATORS (KPIs)
# =============================================================================

def calculate_kpis(df):
    """Calculate key performance indicators."""
    print("\n" + "=" * 60)
    print("STEP 2: KEY PERFORMANCE INDICATORS (KPIs)")
    print("=" * 60)
    
    kpis = {}
    
    # Revenue metrics
    kpis['total_revenue'] = df['final_amount'].sum()
    kpis['total_orders'] = len(df)
    kpis['average_order_value'] = df['final_amount'].mean()
    kpis['total_discounts'] = df['discount'].sum()
    
    # Customer metrics
    kpis['unique_customers'] = df['customer_id'].nunique()
    kpis['orders_per_customer'] = kpis['total_orders'] / kpis['unique_customers']
    kpis['customer_lifetime_value'] = kpis['total_revenue'] / kpis['unique_customers']
    
    # Product metrics
    kpis['total_units_sold'] = df['quantity'].sum()
    kpis['average_units_per_order'] = df['quantity'].mean()
    
    # Print KPIs
    print(f"\n--- Revenue Metrics ---")
    print(f"Total Revenue: ${kpis['total_revenue']:,.2f}")
    print(f"Total Orders: {kpis['total_orders']:,}")
    print(f"Average Order Value: ${kpis['average_order_value']:.2f}")
    print(f"Total Discounts Given: ${kpis['total_discounts']:,.2f}")
    print(f"Discount Rate: {kpis['total_discounts']/df['total_amount'].sum()*100:.2f}%")
    
    print(f"\n--- Customer Metrics ---")
    print(f"Unique Customers: {kpis['unique_customers']:,}")
    print(f"Orders per Customer: {kpis['orders_per_customer']:.2f}")
    print(f"Customer Lifetime Value: ${kpis['customer_lifetime_value']:.2f}")
    
    print(f"\n--- Product Metrics ---")
    print(f"Total Units Sold: {kpis['total_units_sold']:,}")
    print(f"Average Units per Order: {kpis['average_units_per_order']:.2f}")
    
    return kpis


# =============================================================================
# 3. MONTHLY SALES TREND ANALYSIS
# =============================================================================

def analyze_monthly_trends(df):
    """Analyze monthly sales trends."""
    print("\n" + "=" * 60)
    print("STEP 3: MONTHLY SALES TREND ANALYSIS")
    print("=" * 60)
    
    # Monthly aggregation
    monthly_stats = df.groupby('order_month_name').agg({
        'final_amount': ['sum', 'mean', 'count'],
        'quantity': 'sum',
        'customer_id': 'nunique'
    }).round(2)
    
    monthly_stats.columns = ['Revenue', 'Avg_Order_Value', 'Order_Count', 'Units_Sold', 'Unique_Customers']
    
    # Reorder by month
    month_order = ['January', 'February', 'March']
    monthly_stats = monthly_stats.reindex(month_order)
    
    # Calculate month-over-month growth
    monthly_stats['Revenue_Growth'] = monthly_stats['Revenue'].pct_change() * 100
    monthly_stats['Order_Growth'] = monthly_stats['Order_Count'].pct_change() * 100
    
    print("\n--- Monthly Performance Summary ---")
    print(monthly_stats.to_string())
    
    # Daily trend data
    daily_stats = df.groupby('order_date').agg({
        'final_amount': 'sum',
        'order_id': 'count'
    }).reset_index()
    daily_stats.columns = ['date', 'revenue', 'orders']
    
    return monthly_stats, daily_stats


# =============================================================================
# 4. PRODUCT CATEGORY ANALYSIS
# =============================================================================

def analyze_product_categories(df):
    """Analyze sales by product category."""
    print("\n" + "=" * 60)
    print("STEP 4: PRODUCT CATEGORY ANALYSIS")
    print("=" * 60)
    
    # Category aggregation
    category_stats = df.groupby('product_category').agg({
        'final_amount': ['sum', 'mean'],
        'quantity': 'sum',
        'order_id': 'count',
        'customer_id': 'nunique'
    }).round(2)
    
    category_stats.columns = ['Revenue', 'Avg_Order_Value', 'Units_Sold', 'Order_Count', 'Unique_Customers']
    category_stats = category_stats.sort_values('Revenue', ascending=False)
    
    # Calculate percentage of total
    total_revenue = df['final_amount'].sum()
    category_stats['Revenue_Percentage'] = (category_stats['Revenue'] / total_revenue * 100).round(2)
    
    print("\n--- Category Performance ---")
    print(category_stats.to_string())
    
    # Top products by category
    print("\n--- Top Products by Revenue ---")
    top_products = df.groupby(['product_category', 'product_name'])['final_amount'].sum().reset_index()
    top_products = top_products.sort_values('final_amount', ascending=False).head(10)
    print(top_products.to_string(index=False))
    
    return category_stats


# =============================================================================
# 5. CUSTOMER BEHAVIOR ANALYSIS
# =============================================================================

def analyze_customer_behavior(df):
    """Analyze customer purchasing behavior."""
    print("\n" + "=" * 60)
    print("STEP 5: CUSTOMER BEHAVIOR ANALYSIS")
    print("=" * 60)
    
    # Customer-level aggregation
    customer_stats = df.groupby('customer_id').agg({
        'final_amount': ['sum', 'mean', 'count'],
        'quantity': 'sum',
        'order_date': ['min', 'max']
    }).round(2)
    
    customer_stats.columns = ['Total_Spent', 'Avg_Order_Value', 'Order_Count', 'Total_Units', 'First_Order', 'Last_Order']
    
    # Calculate customer lifetime (days between first and last order)
    customer_stats['Customer_Lifetime_Days'] = (
        pd.to_datetime(customer_stats['Last_Order']) - pd.to_datetime(customer_stats['First_Order'])
    ).dt.days
    
    # Customer segmentation based on spending
    spending_quartiles = customer_stats['Total_Spent'].quantile([0.25, 0.5, 0.75, 0.9])
    
    def segment_customer(spend):
        if spend >= spending_quartiles[0.9]:
            return 'VIP'
        elif spend >= spending_quartiles[0.75]:
            return 'High Value'
        elif spend >= spending_quartiles[0.5]:
            return 'Medium Value'
        elif spend >= spending_quartiles[0.25]:
            return 'Low Value'
        else:
            return 'New'
    
    customer_stats['Segment'] = customer_stats['Total_Spent'].apply(segment_customer)
    
    # Segment analysis
    segment_analysis = customer_stats.groupby('Segment').agg({
        'Total_Spent': ['count', 'sum', 'mean'],
        'Order_Count': 'mean',
        'Avg_Order_Value': 'mean'
    }).round(2)
    
    segment_analysis.columns = ['Customer_Count', 'Total_Revenue', 'Avg_Revenue', 'Avg_Orders', 'Avg_Order_Value']
    segment_analysis = segment_analysis.reindex(['VIP', 'High Value', 'Medium Value', 'Low Value', 'New'])
    
    print("\n--- Customer Segmentation ---")
    print(segment_analysis.to_string())
    
    # Purchase frequency distribution
    print("\n--- Purchase Frequency Distribution ---")
    freq_dist = customer_stats['Order_Count'].value_counts().sort_index().head(10)
    print(freq_dist.to_string())
    
    # Repeat customer rate
    repeat_customers = (customer_stats['Order_Count'] > 1).sum()
    repeat_rate = repeat_customers / len(customer_stats) * 100
    print(f"\nRepeat Customer Rate: {repeat_rate:.2f}%")
    print(f"Customers with 2+ orders: {repeat_customers}")
    
    return customer_stats, segment_analysis


# =============================================================================
# 6. REGIONAL PERFORMANCE ANALYSIS
# =============================================================================

def analyze_regional_performance(df):
    """Analyze sales performance by region."""
    print("\n" + "=" * 60)
    print("STEP 6: REGIONAL PERFORMANCE ANALYSIS")
    print("=" * 60)
    
    # Regional aggregation
    regional_stats = df.groupby('region').agg({
        'final_amount': ['sum', 'mean'],
        'quantity': 'sum',
        'order_id': 'count',
        'customer_id': 'nunique'
    }).round(2)
    
    regional_stats.columns = ['Revenue', 'Avg_Order_Value', 'Units_Sold', 'Order_Count', 'Unique_Customers']
    regional_stats = regional_stats.sort_values('Revenue', ascending=False)
    
    # Calculate market share
    total_revenue = df['final_amount'].sum()
    regional_stats['Market_Share'] = (regional_stats['Revenue'] / total_revenue * 100).round(2)
    
    # Calculate revenue per customer
    regional_stats['Revenue_Per_Customer'] = (regional_stats['Revenue'] / regional_stats['Unique_Customers']).round(2)
    
    print("\n--- Regional Performance ---")
    print(regional_stats.to_string())
    
    # Category performance by region
    print("\n--- Top Category by Region ---")
    region_category = df.groupby(['region', 'product_category'])['final_amount'].sum().reset_index()
    top_category_by_region = region_category.loc[region_category.groupby('region')['final_amount'].idxmax()]
    print(top_category_by_region.to_string(index=False))
    
    return regional_stats


# =============================================================================
# 7. GENERATE VISUALIZATIONS
# =============================================================================

def create_visualizations(df, monthly_stats, daily_stats, category_stats, customer_stats, regional_stats, output_dir):
    """Create and save visualization charts."""
    print("\n" + "=" * 60)
    print("STEP 7: GENERATING VISUALIZATIONS")
    print("=" * 60)
    
    # Set up the plotting style
    plt.rcParams['figure.figsize'] = (12, 6)
    plt.rcParams['font.size'] = 10
    
    charts = []
    
    # Chart 1: Monthly Revenue Trend
    fig, ax = plt.subplots(figsize=(10, 6))
    months = ['Jan', 'Feb', 'Mar']
    revenues = monthly_stats['Revenue'].values
    ax.bar(months, revenues, color=['#1f77b4', '#ff7f0e', '#2ca02c'], alpha=0.8)
    ax.set_title('Monthly Revenue Trend - Q1 2024', fontsize=14, fontweight='bold')
    ax.set_ylabel('Revenue ($)', fontsize=12)
    ax.set_xlabel('Month', fontsize=12)
    for i, v in enumerate(revenues):
        ax.text(i, v + 10000, f'${v:,.0f}', ha='center', fontweight='bold')
    plt.tight_layout()
    chart_path = f"{output_dir}/chart_monthly_revenue.png"
    plt.savefig(chart_path, dpi=150, bbox_inches='tight')
    charts.append(chart_path)
    plt.close()
    print(f"Saved: {chart_path}")
    
    # Chart 2: Daily Revenue Trend
    fig, ax = plt.subplots(figsize=(14, 6))
    ax.plot(daily_stats['date'], daily_stats['revenue'], color='#1f77b4', linewidth=1.5, alpha=0.7)
    ax.fill_between(daily_stats['date'], daily_stats['revenue'], alpha=0.3, color='#1f77b4')
    ax.set_title('Daily Revenue Trend - Q1 2024', fontsize=14, fontweight='bold')
    ax.set_ylabel('Revenue ($)', fontsize=12)
    ax.set_xlabel('Date', fontsize=12)
    plt.xticks(rotation=45)
    plt.tight_layout()
    chart_path = f"{output_dir}/chart_daily_revenue.png"
    plt.savefig(chart_path, dpi=150, bbox_inches='tight')
    charts.append(chart_path)
    plt.close()
    print(f"Saved: {chart_path}")
    
    # Chart 3: Product Category Sales Distribution (Pie)
    fig, ax = plt.subplots(figsize=(10, 8))
    category_revenue = category_stats['Revenue'].sort_values(ascending=False)
    colors = plt.cm.Set3(np.linspace(0, 1, len(category_revenue)))
    wedges, texts, autotexts = ax.pie(category_revenue.values, labels=category_revenue.index, 
                                       autopct='%1.1f%%', colors=colors, startangle=90)
    ax.set_title('Revenue Distribution by Product Category', fontsize=14, fontweight='bold')
    plt.tight_layout()
    chart_path = f"{output_dir}/chart_category_distribution.png"
    plt.savefig(chart_path, dpi=150, bbox_inches='tight')
    charts.append(chart_path)
    plt.close()
    print(f"Saved: {chart_path}")
    
    # Chart 4: Category Revenue Bar Chart
    fig, ax = plt.subplots(figsize=(12, 6))
    category_revenue_sorted = category_stats.sort_values('Revenue', ascending=True)
    bars = ax.barh(category_revenue_sorted.index, category_revenue_sorted['Revenue'], color='steelblue', alpha=0.8)
    ax.set_title('Revenue by Product Category', fontsize=14, fontweight='bold')
    ax.set_xlabel('Revenue ($)', fontsize=12)
    for i, (idx, row) in enumerate(category_revenue_sorted.iterrows()):
        ax.text(row['Revenue'] + 10000, i, f'${row["Revenue"]:,.0f}', va='center', fontsize=9)
    plt.tight_layout()
    chart_path = f"{output_dir}/chart_category_revenue.png"
    plt.savefig(chart_path, dpi=150, bbox_inches='tight')
    charts.append(chart_path)
    plt.close()
    print(f"Saved: {chart_path}")
    
    # Chart 5: Regional Performance Comparison
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))
    
    # Revenue by region
    regional_stats_sorted = regional_stats.sort_values('Revenue', ascending=False)
    ax1.bar(regional_stats_sorted.index, regional_stats_sorted['Revenue'], color='coral', alpha=0.8)
    ax1.set_title('Revenue by Region', fontsize=14, fontweight='bold')
    ax1.set_ylabel('Revenue ($)', fontsize=12)
    for i, (idx, row) in enumerate(regional_stats_sorted.iterrows()):
        ax1.text(i, row['Revenue'] + 10000, f'${row["Revenue"]:,.0f}', ha='center', fontsize=9)
    
    # Market share pie
    ax2.pie(regional_stats_sorted['Market_Share'], labels=regional_stats_sorted.index, 
            autopct='%1.1f%%', colors=['#ff9999', '#66b3ff', '#99ff99', '#ffcc99'], startangle=90)
    ax2.set_title('Market Share by Region', fontsize=14, fontweight='bold')
    
    plt.tight_layout()
    chart_path = f"{output_dir}/chart_regional_performance.png"
    plt.savefig(chart_path, dpi=150, bbox_inches='tight')
    charts.append(chart_path)
    plt.close()
    print(f"Saved: {chart_path}")
    
    # Chart 6: Customer Segmentation
    fig, ax = plt.subplots(figsize=(10, 6))
    segment_order = ['VIP', 'High Value', 'Medium Value', 'Low Value', 'New']
    segment_counts = customer_stats['Segment'].value_counts().reindex(segment_order)
    colors = ['#gold', '#silver', '#CD7F32', '#lightblue', '#lightgray']
    bars = ax.bar(segment_counts.index, segment_counts.values, 
                  color=['#FFD700', '#C0C0C0', '#CD7F32', '#87CEEB', '#D3D3D3'], alpha=0.8)
    ax.set_title('Customer Distribution by Segment', fontsize=14, fontweight='bold')
    ax.set_ylabel('Number of Customers', fontsize=12)
    ax.set_xlabel('Customer Segment', fontsize=12)
    for i, v in enumerate(segment_counts.values):
        ax.text(i, v + 5, str(v), ha='center', fontweight='bold')
    plt.tight_layout()
    chart_path = f"{output_dir}/chart_customer_segments.png"
    plt.savefig(chart_path, dpi=150, bbox_inches='tight')
    charts.append(chart_path)
    plt.close()
    print(f"Saved: {chart_path}")
    
    # Chart 7: Order Value Distribution
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.hist(df['final_amount'], bins=50, color='skyblue', alpha=0.7, edgecolor='black')
    ax.axvline(df['final_amount'].mean(), color='red', linestyle='--', linewidth=2, label=f'Mean: ${df["final_amount"].mean():.2f}')
    ax.axvline(df['final_amount'].median(), color='green', linestyle='--', linewidth=2, label=f'Median: ${df["final_amount"].median():.2f}')
    ax.set_title('Order Value Distribution', fontsize=14, fontweight='bold')
    ax.set_xlabel('Order Value ($)', fontsize=12)
    ax.set_ylabel('Frequency', fontsize=12)
    ax.legend()
    plt.tight_layout()
    chart_path = f"{output_dir}/chart_order_distribution.png"
    plt.savefig(chart_path, dpi=150, bbox_inches='tight')
    charts.append(chart_path)
    plt.close()
    print(f"Saved: {chart_path}")
    
    # Chart 8: Monthly Orders and AOV
    fig, ax1 = plt.subplots(figsize=(10, 6))
    
    months = ['Jan', 'Feb', 'Mar']
    order_counts = monthly_stats['Order_Count'].values
    aov_values = monthly_stats['Avg_Order_Value'].values
    
    color = 'tab:blue'
    ax1.set_xlabel('Month', fontsize=12)
    ax1.set_ylabel('Order Count', color=color, fontsize=12)
    ax1.bar(months, order_counts, color=color, alpha=0.6, label='Order Count')
    ax1.tick_params(axis='y', labelcolor=color)
    
    ax2 = ax1.twinx()
    color = 'tab:red'
    ax2.set_ylabel('Average Order Value ($)', color=color, fontsize=12)
    ax2.plot(months, aov_values, color=color, marker='o', linewidth=2, markersize=8, label='AOV')
    ax2.tick_params(axis='y', labelcolor=color)
    
    ax1.set_title('Monthly Orders vs Average Order Value', fontsize=14, fontweight='bold')
    plt.tight_layout()
    chart_path = f"{output_dir}/chart_monthly_orders_aov.png"
    plt.savefig(chart_path, dpi=150, bbox_inches='tight')
    charts.append(chart_path)
    plt.close()
    print(f"Saved: {chart_path}")
    
    print(f"\nAll {len(charts)} charts generated successfully!")
    return charts


# =============================================================================
# 8. GENERATE HTML REPORT
# =============================================================================

def generate_html_report(df, kpis, monthly_stats, category_stats, customer_stats, 
                         segment_analysis, regional_stats, charts, output_path):
    """Generate comprehensive HTML analysis report."""
    print("\n" + "=" * 60)
    print("STEP 8: GENERATING HTML REPORT")
    print("=" * 60)
    
    # Calculate additional insights
    total_revenue = kpis['total_revenue']
    
    # Top insights
    top_month = monthly_stats['Revenue'].idxmax()
    top_month_revenue = monthly_stats.loc[top_month, 'Revenue']
    
    top_category = category_stats.index[0]
    top_category_revenue = category_stats.loc[top_category, 'Revenue']
    top_category_pct = category_stats.loc[top_category, 'Revenue_Percentage']
    
    top_region = regional_stats.index[0]
    top_region_revenue = regional_stats.loc[top_region, 'Revenue']
    
    vip_customers = segment_analysis.loc['VIP', 'Customer_Count'] if 'VIP' in segment_analysis.index else 0
    vip_revenue = segment_analysis.loc['VIP', 'Total_Revenue'] if 'VIP' in segment_analysis.index else 0
    
    html_content = f'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Q1 2024 Sales Analysis Report</title>
    <style>
        :root {{
            --primary-color: #2c3e50;
            --secondary-color: #3498db;
            --accent-color: #e74c3c;
            --success-color: #27ae60;
            --warning-color: #f39c12;
            --bg-color: #f8f9fa;
            --card-bg: #ffffff;
            --text-color: #333333;
            --border-color: #e0e0e0;
        }}
        
        * {{
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }}
        
        body {{
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background-color: var(--bg-color);
            color: var(--text-color);
            line-height: 1.6;
        }}
        
        .container {{
            max-width: 1400px;
            margin: 0 auto;
            padding: 20px;
        }}
        
        header {{
            background: linear-gradient(135deg, var(--primary-color), var(--secondary-color));
            color: white;
            padding: 40px;
            border-radius: 10px;
            margin-bottom: 30px;
            box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        }}
        
        header h1 {{
            font-size: 2.5em;
            margin-bottom: 10px;
        }}
        
        header p {{
            font-size: 1.1em;
            opacity: 0.9;
        }}
        
        .report-meta {{
            display: flex;
            gap: 30px;
            margin-top: 20px;
            flex-wrap: wrap;
        }}
        
        .meta-item {{
            display: flex;
            align-items: center;
            gap: 8px;
        }}
        
        .section {{
            background: var(--card-bg);
            border-radius: 10px;
            padding: 30px;
            margin-bottom: 30px;
            box-shadow: 0 2px 4px rgba(0,0,0,0.05);
        }}
        
        .section h2 {{
            color: var(--primary-color);
            font-size: 1.8em;
            margin-bottom: 20px;
            padding-bottom: 10px;
            border-bottom: 3px solid var(--secondary-color);
        }}
        
        .section h3 {{
            color: var(--primary-color);
            font-size: 1.3em;
            margin: 25px 0 15px 0;
        }}
        
        .kpi-grid {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
            gap: 20px;
            margin-bottom: 20px;
        }}
        
        .kpi-card {{
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            padding: 25px;
            border-radius: 10px;
            text-align: center;
            transition: transform 0.3s ease;
        }}
        
        .kpi-card:hover {{
            transform: translateY(-5px);
        }}
        
        .kpi-card.revenue {{
            background: linear-gradient(135deg, #11998e 0%, #38ef7d 100%);
        }}
        
        .kpi-card.orders {{
            background: linear-gradient(135deg, #4facfe 0%, #00f2fe 100%);
        }}
        
        .kpi-card.customers {{
            background: linear-gradient(135deg, #fa709a 0%, #fee140 100%);
        }}
        
        .kpi-card.aov {{
            background: linear-gradient(135deg, #a8edea 0%, #fed6e3 100%);
            color: #333;
        }}
        
        .kpi-value {{
            font-size: 2.2em;
            font-weight: bold;
            margin-bottom: 5px;
        }}
        
        .kpi-label {{
            font-size: 0.95em;
            opacity: 0.9;
        }}
        
        .chart-grid {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(500px, 1fr));
            gap: 30px;
            margin-top: 20px;
        }}
        
        .chart-container {{
            background: #f8f9fa;
            border-radius: 8px;
            padding: 20px;
            text-align: center;
        }}
        
        .chart-container img {{
            max-width: 100%;
            height: auto;
            border-radius: 5px;
        }}
        
        .chart-title {{
            font-size: 1.1em;
            color: var(--primary-color);
            margin-bottom: 15px;
            font-weight: 600;
        }}
        
        table {{
            width: 100%;
            border-collapse: collapse;
            margin: 20px 0;
            font-size: 0.95em;
        }}
        
        th, td {{
            padding: 12px 15px;
            text-align: left;
            border-bottom: 1px solid var(--border-color);
        }}
        
        th {{
            background-color: var(--primary-color);
            color: white;
            font-weight: 600;
        }}
        
        tr:hover {{
            background-color: #f5f5f5;
        }}
        
        .insights {{
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            padding: 30px;
            border-radius: 10px;
            margin-bottom: 30px;
        }}
        
        .insights h2 {{
            color: white;
            border-bottom-color: rgba(255,255,255,0.3);
        }}
        
        .insight-list {{
            list-style: none;
            padding: 0;
        }}
        
        .insight-list li {{
            padding: 12px 0;
            padding-left: 30px;
            position: relative;
            border-bottom: 1px solid rgba(255,255,255,0.2);
        }}
        
        .insight-list li:before {{
            content: "✓";
            position: absolute;
            left: 0;
            color: #2ecc71;
            font-weight: bold;
            font-size: 1.2em;
        }}
        
        .recommendations {{
            background: var(--card-bg);
            border-left: 5px solid var(--success-color);
        }}
        
        .recommendations h2 {{
            color: var(--success-color);
            border-bottom-color: var(--success-color);
        }}
        
        .rec-grid {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
            gap: 20px;
            margin-top: 20px;
        }}
        
        .rec-card {{
            background: #f0f9f4;
            border: 1px solid #c8e6c9;
            border-radius: 8px;
            padding: 20px;
        }}
        
        .rec-card h4 {{
            color: var(--success-color);
            margin-bottom: 10px;
            font-size: 1.1em;
        }}
        
        .rec-card p {{
            color: #555;
            font-size: 0.95em;
        }}
        
        .highlight {{
            background: #fff3cd;
            padding: 2px 6px;
            border-radius: 3px;
            font-weight: 600;
        }}
        
        .positive {{
            color: var(--success-color);
        }}
        
        .negative {{
            color: var(--accent-color);
        }}
        
        footer {{
            text-align: center;
            padding: 20px;
            color: #666;
            font-size: 0.9em;
        }}
        
        @media (max-width: 768px) {{
            .chart-grid {{
                grid-template-columns: 1fr;
            }}
            
            .kpi-grid {{
                grid-template-columns: repeat(2, 1fr);
            }}
            
            header h1 {{
                font-size: 1.8em;
            }}
        }}
    </style>
</head>
<body>
    <div class="container">
        <header>
            <h1>Q1 2024 Sales Analysis Report</h1>
            <p>Comprehensive analysis of sales performance, customer behavior, and market trends</p>
            <div class="report-meta">
                <div class="meta-item">
                    <span>📅</span>
                    <span>Report Period: January - March 2024</span>
                </div>
                <div class="meta-item">
                    <span>📊</span>
                    <span>Total Records: {kpis['total_orders']:,}</span>
                </div>
                <div class="meta-item">
                    <span>👥</span>
                    <span>Unique Customers: {kpis['unique_customers']:,}</span>
                </div>
                <div class="meta-item">
                    <span>💰</span>
                    <span>Total Revenue: ${total_revenue:,.2f}</span>
                </div>
            </div>
        </header>
        
        <!-- Key Performance Indicators -->
        <div class="section">
            <h2>Key Performance Indicators</h2>
            <div class="kpi-grid">
                <div class="kpi-card revenue">
                    <div class="kpi-value">${total_revenue:,.0f}</div>
                    <div class="kpi-label">Total Revenue</div>
                </div>
                <div class="kpi-card orders">
                    <div class="kpi-value">{kpis['total_orders']:,}</div>
                    <div class="kpi-label">Total Orders</div>
                </div>
                <div class="kpi-card customers">
                    <div class="kpi-value">{kpis['unique_customers']:,}</div>
                    <div class="kpi-label">Unique Customers</div>
                </div>
                <div class="kpi-card aov">
                    <div class="kpi-value">${kpis['average_order_value']:.2f}</div>
                    <div class="kpi-label">Average Order Value</div>
                </div>
            </div>
            
            <h3>Additional Metrics</h3>
            <table>
                <tr>
                    <th>Metric</th>
                    <th>Value</th>
                    <th>Description</th>
                </tr>
                <tr>
                    <td>Customer Lifetime Value</td>
                    <td>${kpis['customer_lifetime_value']:.2f}</td>
                    <td>Average revenue per customer</td>
                </tr>
                <tr>
                    <td>Orders per Customer</td>
                    <td>{kpis['orders_per_customer']:.2f}</td>
                    <td>Average purchase frequency</td>
                </tr>
                <tr>
                    <td>Total Units Sold</td>
                    <td>{kpis['total_units_sold']:,}</td>
                    <td>Total quantity sold</td>
                </tr>
                <tr>
                    <td>Total Discounts</td>
                    <td>${kpis['total_discounts']:,.2f}</td>
                    <td>Discount amount given</td>
                </tr>
                <tr>
                    <td>Discount Rate</td>
                    <td>{kpis['total_discounts']/df['total_amount'].sum()*100:.2f}%</td>
                    <td>Discount as % of gross revenue</td>
                </tr>
            </table>
        </div>
        
        <!-- Key Insights -->
        <div class="insights">
            <h2>Key Insights</h2>
            <ul class="insight-list">
                <li><strong>Best Performing Month:</strong> {top_month} generated ${top_month_revenue:,.2f} in revenue, representing the strongest month of Q1.</li>
                <li><strong>Top Product Category:</strong> {top_category} leads with ${top_category_revenue:,.2f} ({top_category_pct:.1f}% of total revenue).</li>
                <li><strong>Leading Region:</strong> {top_region} region contributed ${top_region_revenue:,.2f} to total sales.</li>
                <li><strong>VIP Customers:</strong> {vip_customers:.0f} VIP customers generated ${vip_revenue:,.2f} in revenue.</li>
                <li><strong>Repeat Purchase Rate:</strong> {(customer_stats['Order_Count'] > 1).sum() / len(customer_stats) * 100:.1f}% of customers made multiple purchases.</li>
                <li><strong>Average Order Value Trend:</strong> Monthly AOV ranged from ${monthly_stats['Avg_Order_Value'].min():.2f} to ${monthly_stats['Avg_Order_Value'].max():.2f}.</li>
            </ul>
        </div>
        
        <!-- Monthly Trends -->
        <div class="section">
            <h2>Monthly Sales Trend Analysis</h2>
            <div class="chart-grid">
                <div class="chart-container">
                    <div class="chart-title">Monthly Revenue Comparison</div>
                    <img src="chart_monthly_revenue.png" alt="Monthly Revenue Chart">
                </div>
                <div class="chart-container">
                    <div class="chart-title">Daily Revenue Trend</div>
                    <img src="chart_daily_revenue.png" alt="Daily Revenue Chart">
                </div>
            </div>
            
            <h3>Monthly Performance Summary</h3>
            <table>
                <tr>
                    <th>Month</th>
                    <th>Revenue</th>
                    <th>Orders</th>
                    <th>Avg Order Value</th>
                    <th>Units Sold</th>
                    <th>Unique Customers</th>
                    <th>Revenue Growth</th>
                </tr>
'''
    
    # Add monthly data rows
    for month in ['January', 'February', 'March']:
        row = monthly_stats.loc[month]
        growth = row['Revenue_Growth']
        growth_class = 'positive' if growth > 0 else 'negative' if pd.notna(growth) else ''
        growth_str = f'+{growth:.1f}%' if growth > 0 else f'{growth:.1f}%' if pd.notna(growth) else 'N/A'
        
        html_content += f'''                <tr>
                    <td>{month}</td>
                    <td>${row['Revenue']:,.2f}</td>
                    <td>{row['Order_Count']:,.0f}</td>
                    <td>${row['Avg_Order_Value']:.2f}</td>
                    <td>{row['Units_Sold']:,.0f}</td>
                    <td>{row['Unique_Customers']:,.0f}</td>
                    <td class="{growth_class}">{growth_str}</td>
                </tr>
'''
    
    html_content += '''            </table>
            
            <div class="chart-grid">
                <div class="chart-container">
                    <div class="chart-title">Monthly Orders vs Average Order Value</div>
                    <img src="chart_monthly_orders_aov.png" alt="Orders vs AOV Chart">
                </div>
            </div>
        </div>
        
        <!-- Product Category Analysis -->
        <div class="section">
            <h2>Product Category Analysis</h2>
            <div class="chart-grid">
                <div class="chart-container">
                    <div class="chart-title">Revenue Distribution by Category</div>
                    <img src="chart_category_distribution.png" alt="Category Distribution Chart">
                </div>
                <div class="chart-container">
                    <div class="chart-title">Revenue by Product Category</div>
                    <img src="chart_category_revenue.png" alt="Category Revenue Chart">
                </div>
            </div>
            
            <h3>Category Performance Summary</h3>
            <table>
                <tr>
                    <th>Category</th>
                    <th>Revenue</th>
                    <th>% of Total</th>
                    <th>Orders</th>
                    <th>Avg Order Value</th>
                    <th>Units Sold</th>
                    <th>Unique Customers</th>
                </tr>
'''
    
    # Add category data rows
    for category in category_stats.index:
        row = category_stats.loc[category]
        html_content += f'''                <tr>
                    <td>{category}</td>
                    <td>${row['Revenue']:,.2f}</td>
                    <td>{row['Revenue_Percentage']:.1f}%</td>
                    <td>{row['Order_Count']:,.0f}</td>
                    <td>${row['Avg_Order_Value']:.2f}</td>
                    <td>{row['Units_Sold']:,.0f}</td>
                    <td>{row['Unique_Customers']:,.0f}</td>
                </tr>
'''
    
    html_content += '''            </table>
        </div>
        
        <!-- Regional Performance -->
        <div class="section">
            <h2>Regional Performance Comparison</h2>
            <div class="chart-grid">
                <div class="chart-container">
                    <div class="chart-title">Regional Performance Overview</div>
                    <img src="chart_regional_performance.png" alt="Regional Performance Chart">
                </div>
            </div>
            
            <h3>Regional Performance Summary</h3>
            <table>
                <tr>
                    <th>Region</th>
                    <th>Revenue</th>
                    <th>Market Share</th>
                    <th>Orders</th>
                    <th>Avg Order Value</th>
                    <th>Unique Customers</th>
                    <th>Revenue/Customer</th>
                </tr>
'''
    
    # Add regional data rows
    for region in regional_stats.index:
        row = regional_stats.loc[region]
        html_content += f'''                <tr>
                    <td>{region}</td>
                    <td>${row['Revenue']:,.2f}</td>
                    <td>{row['Market_Share']:.1f}%</td>
                    <td>{row['Order_Count']:,.0f}</td>
                    <td>${row['Avg_Order_Value']:.2f}</td>
                    <td>{row['Unique_Customers']:,.0f}</td>
                    <td>${row['Revenue_Per_Customer']:.2f}</td>
                </tr>
'''
    
    html_content += '''            </table>
        </div>
        
        <!-- Customer Analysis -->
        <div class="section">
            <h2>Customer Behavior Analysis</h2>
            <div class="chart-grid">
                <div class="chart-container">
                    <div class="chart-title">Customer Segmentation</div>
                    <img src="chart_customer_segments.png" alt="Customer Segments Chart">
                </div>
                <div class="chart-container">
                    <div class="chart-title">Order Value Distribution</div>
                    <img src="chart_order_distribution.png" alt="Order Distribution Chart">
                </div>
            </div>
            
            <h3>Customer Segment Analysis</h3>
            <table>
                <tr>
                    <th>Segment</th>
                    <th>Customer Count</th>
                    <th>Total Revenue</th>
                    <th>Avg Revenue</th>
                    <th>Avg Orders</th>
                    <th>Avg Order Value</th>
                </tr>
'''
    
    # Add segment data rows
    for segment in ['VIP', 'High Value', 'Medium Value', 'Low Value', 'New']:
        if segment in segment_analysis.index:
            row = segment_analysis.loc[segment]
            html_content += f'''                <tr>
                    <td><span class="highlight">{segment}</span></td>
                    <td>{row['Customer_Count']:,.0f}</td>
                    <td>${row['Total_Revenue']:,.2f}</td>
                    <td>${row['Avg_Revenue']:.2f}</td>
                    <td>{row['Avg_Orders']:.2f}</td>
                    <td>${row['Avg_Order_Value']:.2f}</td>
                </tr>
'''
    
    html_content += '''            </table>
        </div>
        
        <!-- Business Recommendations -->
        <div class="section recommendations">
            <h2>Business Insights & Recommendations</h2>
            <div class="rec-grid">
                <div class="rec-card">
                    <h4>🎯 Focus on High-Value Categories</h4>
                    <p>Electronics and Clothing represent the largest revenue segments. Consider expanding product variety in these categories and implementing targeted promotions to drive further growth.</p>
                </div>
                <div class="rec-card">
                    <h4>📈 Optimize Regional Strategies</h4>
                    <p>East and North regions show higher average order values. Analyze successful tactics from these regions and apply them to South and West regions to boost performance.</p>
                </div>
                <div class="rec-card">
                    <h4>💎 Nurture VIP Customers</h4>
                    <p>VIP customers generate disproportionate revenue. Implement loyalty programs, exclusive offers, and personalized experiences to retain these high-value customers.</p>
                </div>
                <div class="rec-card">
                    <h4>🔄 Increase Purchase Frequency</h4>
                    <p>With an average of ''' + f"{kpis['orders_per_customer']:.1f}" + ''' orders per customer, there's opportunity to increase repeat purchases through email marketing and retargeting campaigns.</p>
                </div>
                <div class="rec-card">
                    <h4>📊 Monitor Seasonal Trends</h4>
                    <p>Analyze daily and weekly patterns to identify peak sales periods. Use this data to optimize inventory, staffing, and promotional timing.</p>
                </div>
                <div class="rec-card">
                    <h4>💰 Review Discount Strategy</h4>
                    <p>Current discount rate is ''' + f"{kpis['total_discounts']/df['total_amount'].sum()*100:.1f}" + '''%. Evaluate if discounts are driving sufficient volume increase to justify the margin reduction.</p>
                </div>
            </div>
        </div>
        
        <footer>
            <p>Report generated on ''' + datetime.now().strftime('%Y-%m-%d %H:%M:%S') + '''</p>
            <p>Sales Analysis System - Q1 2024</p>
        </footer>
    </div>
</body>
</html>
'''
    
    # Write HTML file
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(html_content)
    
    print(f"\nHTML report saved to: {output_path}")
    return output_path


# =============================================================================
# MAIN EXECUTION
# =============================================================================

def main():
    """Main execution function."""
    print("\n" + "=" * 60)
    print("Q1 2024 SALES DATA ANALYSIS")
    print("=" * 60)
    
    # File paths
    data_path = '/Users/amneymounir/.qoderwork/workspace/mnlw16r1jz6u80bs/sales_analysis/sales_data_q1_2024.csv'
    output_dir = '/Users/amneymounir/.qoderwork/workspace/mnlw16r1jz6u80bs/sales_analysis'
    
    # Step 1: Load and clean data
    df = load_and_clean_data(data_path)
    
    # Step 2: Calculate KPIs
    kpis = calculate_kpis(df)
    
    # Step 3: Monthly trends
    monthly_stats, daily_stats = analyze_monthly_trends(df)
    
    # Step 4: Product categories
    category_stats = analyze_product_categories(df)
    
    # Step 5: Customer behavior
    customer_stats, segment_analysis = analyze_customer_behavior(df)
    
    # Step 6: Regional performance
    regional_stats = analyze_regional_performance(df)
    
    # Step 7: Create visualizations
    charts = create_visualizations(df, monthly_stats, daily_stats, category_stats, 
                                   customer_stats, regional_stats, output_dir)
    
    # Step 8: Generate HTML report
    report_path = f"{output_dir}/sales_analysis_report_q1_2024.html"
    generate_html_report(df, kpis, monthly_stats, category_stats, customer_stats,
                        segment_analysis, regional_stats, charts, report_path)
    
    print("\n" + "=" * 60)
    print("ANALYSIS COMPLETE!")
    print("=" * 60)
    print(f"\nReport saved to: {report_path}")
    print(f"Charts saved to: {output_dir}/")
    
    return report_path


if __name__ == "__main__":
    main()
