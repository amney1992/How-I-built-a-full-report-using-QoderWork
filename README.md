# Q1 2024 Sales Analysis Dashboard

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue)](https://www.python.org/)
[![Pandas](https://img.shields.io/badge/Pandas-1.3%2B-orange)](https://pandas.pydata.org/)
[![React](https://img.shields.io/badge/React-18%2B-61DAFB)](https://reactjs.org/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

A comprehensive sales data analysis project featuring Python-based data processing and an interactive React dashboard for visualizing Q1 2024 sales performance.

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Project Structure](#project-structure)
- [Installation](#installation)
- [Usage](#usage)
- [Data Analysis](#data-analysis)
- [Dashboard](#dashboard)
- [Key Insights](#key-insights)
- [Technologies Used](#technologies-used)
- [Contributing](#contributing)
- [License](#license)

## Overview

This project provides a complete sales analysis solution for Q1 2024 (January-March) including:

- **Data Generation**: Realistic sample sales data with 5,000+ records
- **Data Processing**: Python-based cleaning, transformation, and analysis
- **Visualizations**: 8+ charts covering trends, categories, regions, and customers
- **Interactive Dashboard**: React-based web application with tabbed navigation
- **Business Insights**: Actionable recommendations based on data analysis

### Key Metrics Summary

| Metric | Value |
|--------|-------|
| Total Revenue | $4,070,016.31 |
| Total Orders | 5,000 |
| Unique Customers | 1,180 |
| Average Order Value | $814.00 |
| Customer Lifetime Value | $3,449.17 |
| Repeat Customer Rate | 94.07% |

## Features

### Data Analysis
- Monthly sales trend analysis with growth calculations
- Product category performance breakdown
- Regional sales comparison across 4 regions
- Customer segmentation (VIP, High Value, Medium Value, Low Value, New)
- Purchase frequency and behavior analysis
- Key Performance Indicators (KPIs) calculation

### Dashboard
- **6 Navigation Tabs**: Overview, Trends, Categories, Regions, Customers, Insights
- **Interactive Charts**: Bar charts, pie charts, line charts with hover tooltips
- **KPI Cards**: Visual summary of key metrics with gradient styling
- **Data Tables**: Formatted tables with currency and number formatting
- **Responsive Design**: Works on desktop and mobile devices

### Visualizations

All charts are generated automatically and saved to the `outputs/` folder:

| Chart | File | Description |
|-------|------|-------------|
| Monthly Revenue | `chart_monthly_revenue.png` | Bar chart comparing Jan-Mar revenue |
| Daily Revenue | `chart_daily_revenue.png` | Line chart showing daily trends across Q1 |
| Category Distribution | `chart_category_distribution.png` | Pie chart of revenue by product category |
| Category Revenue | `chart_category_revenue.png` | Horizontal bar chart of category performance |
| Regional Performance | `chart_regional_performance.png` | Side-by-side regional comparison |
| Customer Segments | `chart_customer_segments.png` | Bar chart of customer distribution |
| Order Distribution | `chart_order_distribution.png` | Histogram of order values with mean/median |
| Orders vs AOV | `chart_monthly_orders_aov.png` | Combo chart showing orders and average order value |

![Monthly Revenue](outputs/chart_monthly_revenue.png)
*Monthly revenue comparison showing March as the strongest month*

## Project Structure

```
sales-analysis-dashboard/
├── data/
│   └── sales_data_q1_2024.csv          # Sample sales dataset (5,000 records)
├── scripts/
│   ├── generate_sample_data.py         # Data generation script
│   └── sales_analysis_report.py        # Main analysis script
├── dashboard/
│   └── index.html                      # React dashboard (single file)
├── outputs/
│   ├── chart_monthly_revenue.png       # Monthly revenue bar chart
│   ├── chart_daily_revenue.png         # Daily revenue trend line chart
│   ├── chart_category_distribution.png # Product category pie chart
│   ├── chart_category_revenue.png      # Category revenue horizontal bar chart
│   ├── chart_regional_performance.png  # Regional comparison charts
│   ├── chart_customer_segments.png     # Customer segment distribution
│   ├── chart_order_distribution.png    # Order value histogram
│   ├── chart_monthly_orders_aov.png    # Orders vs AOV combo chart
│   └── sales_analysis_report_q1_2024.html  # Static HTML report
├── README.md                           # This file
└── requirements.txt                    # Python dependencies
```

## Installation

### Prerequisites
- Python 3.8 or higher
- pip package manager
- Modern web browser (Chrome, Firefox, Safari, Edge)

### Python Dependencies

```bash
pip install pandas numpy matplotlib seaborn
```

Or install from requirements.txt:

```bash
pip install -r requirements.txt
```

### Dashboard

The dashboard is a self-contained HTML file with no build step required. Simply open `dashboard/index.html` in your browser.

## Usage

### 1. Generate Sample Data

```bash
python scripts/generate_sample_data.py
```

This creates `data/sales_data_q1_2024.csv` with 5,000 realistic sales records.

### 2. Run Analysis

```bash
python scripts/sales_analysis_report.py
```

This will:
- Load and clean the sales data
- Calculate KPIs and metrics
- Generate 8 visualization charts (saved to `outputs/`):
  - `chart_monthly_revenue.png`
  - `chart_daily_revenue.png`
  - `chart_category_distribution.png`
  - `chart_category_revenue.png`
  - `chart_regional_performance.png`
  - `chart_customer_segments.png`
  - `chart_order_distribution.png`
  - `chart_monthly_orders_aov.png`
- Create an HTML report (`outputs/sales_analysis_report_q1_2024.html`)

### 3. View Dashboard

Open `dashboard/index.html` in your web browser:

```bash
# macOS
open dashboard/index.html

# Linux
xdg-open dashboard/index.html

# Windows
start dashboard/index.html
```

Or serve it locally:

```bash
cd dashboard
python -m http.server 8000
# Then visit http://localhost:8000
```

## Data Analysis

### Data Schema

| Column | Type | Description |
|--------|------|-------------|
| order_id | string | Unique order identifier |
| order_date | date | Date of purchase |
| order_month | int | Month (1-3) |
| customer_id | string | Unique customer identifier |
| region | string | Geographic region (North, South, East, West) |
| product_category | string | Product category (7 categories) |
| product_name | string | Specific product name |
| quantity | int | Units purchased |
| unit_price | float | Price per unit |
| total_amount | float | Gross order amount |
| discount | float | Discount applied |
| final_amount | float | Net order amount |

### Analysis Workflow

1. **Data Loading**: Import CSV and validate structure
2. **Data Cleaning**: Check for missing values, duplicates, outliers
3. **KPI Calculation**: Compute revenue, orders, AOV, CLV metrics
4. **Trend Analysis**: Monthly aggregation and growth calculations
5. **Category Analysis**: Revenue breakdown by product category
6. **Regional Analysis**: Performance comparison across regions
7. **Customer Analysis**: Segmentation and behavior analysis
8. **Visualization**: Generate charts and export to HTML

## Dashboard

### Navigation

The dashboard is organized into 6 tabs:

#### Overview
- 4 KPI cards (Revenue, Orders, Customers, AOV)
- Additional metrics table
- Quick charts for monthly revenue and category distribution

#### Monthly Trends
- Monthly performance summary table
- Revenue vs Orders comparison chart
- Average Order Value trend line chart
- **Static Chart**: `chart_monthly_revenue.png`, `chart_monthly_orders_aov.png`

#### Categories
- Revenue distribution pie chart
- Category revenue bar chart
- Detailed category performance table
- **Static Charts**: `chart_category_distribution.png`, `chart_category_revenue.png`

#### Regions
- Revenue by region bar chart
- Market share pie chart
- Regional performance metrics table
- **Static Chart**: `chart_regional_performance.png`

#### Customers
- Customer segment distribution
- Revenue by segment analysis
- Detailed segment metrics table
- **Static Charts**: `chart_customer_segments.png`, `chart_order_distribution.png`

#### Insights
- Key findings cards with icons
- Business recommendations
- Strategic action items

### Static Report

For a standalone HTML report with all charts embedded, open:
```
outputs/sales_analysis_report_q1_2024.html
```

This report includes:
- All KPIs and metrics
- All 8 generated charts
- Data tables
- Business insights and recommendations
- Professional styling

### Customization

To use your own data:

1. Replace `data/sales_data_q1_2024.csv` with your dataset
2. Update the column names in `sales_analysis_report.py` if needed
3. Re-run the analysis script
4. Update the data object in `dashboard/index.html` (lines 30-90)

## Generated Charts Gallery

### Monthly Performance
| Monthly Revenue | Daily Revenue Trend |
|-----------------|---------------------|
| ![Monthly](outputs/chart_monthly_revenue.png) | ![Daily](outputs/chart_daily_revenue.png) |
| Revenue comparison across Q1 months | Daily revenue fluctuations throughout the quarter |

### Product Categories
| Category Distribution | Category Revenue |
|-----------------------|------------------|
| ![Distribution](outputs/chart_category_distribution.png) | ![Revenue](outputs/chart_category_revenue.png) |
| Pie chart showing market share by category | Horizontal bar chart of revenue by category |

### Regional & Customer Analysis
| Regional Performance | Customer Segments |
|----------------------|-------------------|
| ![Regional](outputs/chart_regional_performance.png) | ![Segments](outputs/chart_customer_segments.png) |
| Side-by-side revenue and market share | Customer distribution by value segment |

### Order Analysis
| Order Distribution | Orders vs AOV |
|--------------------|---------------|
| ![Distribution](outputs/chart_order_distribution.png) | ![OrdersAOV](outputs/chart_monthly_orders_aov.png) |
| Histogram of order values | Monthly orders and average order value trend |

## Key Insights

### Top Findings

1. **Best Performing Month**: March generated $1.40M in revenue (5.5% growth from February)
   - *See: `chart_monthly_revenue.png`*

2. **Top Product Category**: Electronics dominates with $2.56M (63% of total revenue)
   - *See: `chart_category_distribution.png`, `chart_category_revenue.png`*

3. **Leading Region**: East region contributed $1.26M with the highest AOV of $946.66
   - *See: `chart_regional_performance.png`*

4. **VIP Customer Impact**: 118 VIP customers generated $1.24M, averaging $10,467 per customer
   - *See: `chart_customer_segments.png`*

5. **Customer Loyalty**: 94.07% repeat customer rate indicates strong retention
   - *See: `chart_order_distribution.png` for purchase patterns*

### Business Recommendations

1. **Focus on High-Value Categories**: Expand Electronics and Home & Garden product variety
2. **Optimize Regional Strategies**: Apply East/North tactics to South/West regions
3. **Nurture VIP Customers**: Implement loyalty programs and exclusive offers
4. **Increase Purchase Frequency**: Use email marketing to drive repeat purchases
5. **Monitor Seasonal Trends**: Optimize inventory and staffing based on patterns
6. **Review Discount Strategy**: Evaluate if strategic discounts could drive volume

## Technologies Used

### Data Analysis
- **Python 3.8+**: Core programming language
- **Pandas**: Data manipulation and analysis
- **NumPy**: Numerical computing
- **Matplotlib**: Static visualizations
- **Seaborn**: Statistical data visualization

### Dashboard
- **React 18**: UI library
- **Tailwind CSS**: Utility-first CSS framework
- **Recharts**: Composable charting library
- **Babel**: JavaScript compiler (in-browser)

### Development
- **Git**: Version control
- **GitHub**: Repository hosting

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

### Development Setup

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

### Areas for Contribution

- **Additional Visualizations**: New chart types or interactive features
- **Data Export**: Add export to Excel/CSV functionality
- **Dashboard UI**: Improve styling, add dark mode
- **Documentation**: Expand README with more examples
- **Bug Fixes**: Report issues or submit fixes

### Adding New Charts

To add a new visualization:

1. Add chart generation code to `sales_analysis_report.py`:
```python
# Example: New chart
fig, ax = plt.subplots(figsize=(10, 6))
# ... chart code ...
plt.savefig(f"{output_dir}/chart_new_visualization.png")
```

2. Reference the chart in this README:
```markdown
![New Chart](outputs/chart_new_visualization.png)
*Description of the new chart*
```

3. Update the dashboard (`dashboard/index.html`) to include the new chart data

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Sample data generated for demonstration purposes
- Charts powered by [Recharts](https://recharts.org/)
- Styling with [Tailwind CSS](https://tailwindcss.com/)

## Contact

For questions or feedback, please open an issue on GitHub.

---

**Note**: This project uses sample data for demonstration. Replace with your actual sales data for production use.
